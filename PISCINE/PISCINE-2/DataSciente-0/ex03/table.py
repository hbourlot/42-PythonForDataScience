from pathlib import Path
import psycopg


def read_password(path) -> str:
    """
    Read the database password from a file.

    :param path: path to the file that contains the password
    :return: the password, without surrounding whitespace or newline
    """
    with open(path) as f:
        return f.read().strip()


def get_connection(dbname, user, password, host, port):
    """
    Open a connection to the PostgreSQL database.

    :param dbname: name of the database
    :param user: database user
    :param password: password of the user
    :param host: address of the server
    :param port: port of the server as seen from your machine
    :return: an open connection with autocommit enabled
    """
    coon = psycopg.connect(
        dbname=dbname, user=user, password=password, host=host, port=port
    )
    coon.autocommit = True
    return coon


def create_table(cur, table):
    """
    Drop the table if it exists, then create it empty.

    :param cur: cursor used to run the SQL
    :param table: name of the table to create
    """
    cur.execute(f"DROP TABLE IF EXISTS {table}")
    cur.execute(f"""CREATE TABLE {table}(
                event_time      TIMESTAMP,
                event_type      VARCHAR(50),
                product_id      INTEGER,
                price           NUMERIC(10,2),
                user_id         BIGINT,
                user_session    UUID)""")


def load_csv(cur, table, csv_path):
    """
    Load a CSV file into an existing table.

    :param cur: cursor used to run the COPY
    :param table: name of the table to fill
    :param csv_path: path to the CSV file (its first line is the header)
    """
    with open(csv_path) as f:
        with cur.copy(f"COPY {table} FROM STDIN WITH CSV HEADER") as copy:
            while data := f.read(8192):
                copy.write(data)


def count_rows(cur, table):
    """
    Count the rows in a table.

    :param cur: cursor used to run the query
    :param table: name of the table to count
    :return: number of rows as an integer
    """
    cur.execute(f"SELECT COUNT(*) FROM {table}")
    return cur.fetchone()[0]


def main():
    """
    Create the table from the CSV file name and load the data into it.
    """
    csv_path = "../subject/customer/data_2022_oct.csv"
    table = Path(csv_path).stem
    password = read_password("./db_password.txt")

    conn = get_connection("piscineds", "hbourlot", password, "localhost", 4242)
    try:
        cur = conn.cursor()
        create_table(cur, table)
        load_csv(cur, table, csv_path)
        print(f"Table {table} created & loaded: {count_rows(cur, table)} rows")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
