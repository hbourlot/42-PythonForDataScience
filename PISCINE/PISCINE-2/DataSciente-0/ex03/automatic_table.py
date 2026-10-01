import sqlalchemy as db
from pathlib import Path
from getpass import getpass


# noinspection PyShadowingNames
def get_engine(
    database: str, user: str, password: str, port: str, host: str
) -> db.Engine:
    """Create and test a SQLAlchemy database engine.

    Args:
        database (str): Name of the PostgreSQL database.
        user (str): PostgreSQL username.
        password (str): PostgreSQL password.
        port (str): PostgreSQL server port.
        host (str): PostgreSQL server host.

    Returns:
        db.Engine: SQLAlchemy engine connected to the database.
    """
    engine = db.create_engine(
        f"postgresql://{user}:{password}@{host}:{port}/{database}"
    )
    with engine.connect():
        print("\033[32mEngine created successfully.\033[0m")

    return engine


def table_exists(engine: db.Engine, table_name: str) -> bool:
    """Check whether a table exists in the database.

    :param engine: SQLAlchemy database engine.
    :param table_name: Name of the table to check.
    :return: True if the table exists, otherwise False.
    """
    return db.inspect(engine).has_table(table_name)


def create_table(metadata: db.MetaData, name: str, **columns) -> db.Table:
    """
    Define a table in the metadata, using keyword arguments as columns.

    :param metadata: metadata object where the table is registered
    :param name: name of the table
    :param columns: column_name=column_type pairs, in column order
    :return: the table that was defined
    """
    cols = [db.Column(col, typ) for col, typ in columns.items()]
    return db.Table(name, metadata, *cols)


def list_tables(engine: db.Engine) -> list[str]:
    """List all tables in the database.

    Args:
        engine (db.Engine): SQLAlchemy database engine.

    Returns:
        list[str]: List of table names.
    """
    return db.inspect(engine).get_table_names()


def show_rows(engine: db.Engine, table: db.Table, limit: int = 5) -> None:
    """
    Print the first rows of a table.

    :param engine: SQLAlchemy database engine.
    :param table: SQLAlchemy table to query.
    :param limit: Maximum number of rows to display.
    """
    with engine.connect() as conn:
        for row in conn.execute(db.select(table).limit(limit)):
            print(row)


def load_database(engine: db.Engine, table: db.Table, csv_path: str) -> None:
    """Load CSV data into a PostgreSQL table.

    :param engine: SQLAlchemy engine connected to the database.
    :param table: SQLAlchemy table where the data will be loaded.
    :param csv_path: Path to the CSV file to load.
    """
    raw = engine.raw_connection()
    try:
        cur = raw.cursor()
        with open(csv_path) as f:
            with cur.copy(f"COPY {table} FROM STDIN WITH CSV HEADER") as copy:
                while data := f.read(4242):
                    copy.write(data)
        raw.commit()
    finally:
        raw.close()


def get_csv_files(path: str) -> list[Path]:
    """Get all files from a directory.

    Args:
        path (str): Path to the directory containing the CSV files.

    Returns:
        list[Path]: List of paths to the files in the directory.
    """
    folder = Path(path)
    files = []
    for file in folder.iterdir():
        if file.is_file():
            files.append(file)
    return files


# noinspection PyShadowingNames
def automatic_table(
    database: str, user: str, password: str, port: str, host: str, f_path: str
) -> None:
    """Create and load database tables from CSV files.

    Each CSV file is used to create a table named after the file.
    Existing tables with the same name are dropped before loading.

    Args:
        database (str): Name of the PostgreSQL database.
        user (str): PostgreSQL username.
        password (str): PostgreSQL password.
        port (str): PostgreSQL server port.
        host (str): PostgreSQL server host.
        f_path (str): Path to the directory containing CSV files.

    Returns:
        None: This function creates and loads the database tables.
    """
    engine = get_engine(database, user, password, port, host)

    csv_paths = get_csv_files(f_path)
    for path in csv_paths:

        file_stem = path.stem

        if table_exists(engine, file_stem):
            with engine.connect() as conn:
                conn.execute(db.text(f"DROP TABLE IF EXISTS {file_stem}"))
                print(f"Table {file_stem} dropped.")

        metadata_obj = db.MetaData()
        table = create_table(
            metadata_obj,
            file_stem,
            event_time=db.TIMESTAMP,
            event_type=db.VARCHAR(50),
            product_id=db.INTEGER,
            price=db.NUMERIC(10, 2),
            user_id=db.BIGINT,
            user_session=db.UUID,
        )

        print("Loading database...")
        load_database(engine, table, str(path))
        print("\033[32mDatabase loaded.\033[0m")

    engine.raw_connection().commit()


if __name__ == "__main__":
    data_bate = input("Database name: ")  # "piscineds"
    user = input("Username: ")  # "hbourlot"
    password = getpass("Password: ")
    # open("./db_password.txt").read().strip()
    port = input("Port: ")  # "4242"
    host = input("Host: ")  # "localhost"
    folder_csv = (
        input("CSV folder [../subject/customer]: ") or "../subject/customer"
    )  # "../subject/customer"

    try:
        automatic_table(data_bate, user, password, port, host, folder_csv)
    except Exception as e:
        print(f"Error: {e}")
