import sqlalchemy as db
from pathlib import Path
import os


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
        print("\033[32mEngine created successfully.\033[0m\n")

    return engine


def create_table(metadata: db.MetaData, name: str, **columns) -> db.Table:
    """Define a SQLAlchemy table with the given columns.

    Args:
        metadata (db.MetaData): Metadata object to associate with the table.
        name (str): Name of the table.
        **columns: Column names mapped to their SQLAlchemy data types.

    Returns:
        db.Table: SQLAlchemy table definition.
    """
    cols = [db.Column(k, v) for k, v in columns.items()]

    print("\033[32mTable created successfully.\033[0m\n")

    return db.Table(name, metadata, *cols)


def load_database(engine: db.Engine, table: db.Table, csv_path: Path) -> None:
    """Load CSV data into a PostgreSQL table using COPY.

    Args:
        engine (db.Engine): SQLAlchemy database engine.
        table (db.Table): SQLAlchemy table where the data will be loaded.
        csv_path (Path): Path to the CSV file to load.
    """
    file = Path(csv_path)

    raw = engine.raw_connection()
    try:
        cur = raw.cursor()
        with open(file) as f:
            with cur.copy(f"COPY {table} FROM STDIN WITH CSV HEADER") as copy:
                while data := f.read(4242):
                    copy.write(data)
        raw.commit()
    finally:
        raw.close()


if __name__ == "__main__":
    """Run the database loading process."""
    database = "piscineds"
    user = "hbourlot"
    password = "mysecretpassword"
    port = "4242"
    host = "localhost"
    table = "items"
    path = Path("../subject/item/item.csv")

    try:
        engine = get_engine(database, user, password, port, host)

        if db.inspect(engine).has_table(table):
            with engine.connect() as conn:
                conn.execute(db.text(f"DROP TABLE IF EXISTS {table}"))
                print(f"Table '{table}' dropped.")

        metadata_obj = db.MetaData()

        new_table = create_table(
            metadata_obj,
            table,
            product_id=db.INTEGER,
            category_id=db.BIGINT,
            category_code=db.String,
            brand=db.String,
        )

        metadata_obj.create_all(engine)

        print("Loading database...")
        load_database(engine, new_table, path)
        print("\033[32mDatabase loaded.\033[0m")
    except Exception as e:
        print("Error: ", e)
