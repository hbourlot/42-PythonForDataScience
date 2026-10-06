import sqlalchemy as db
from sqlalchemy import text, TIMESTAMP, String, BIGINT, Numeric, INTEGER, UUID
from sqlalchemy.orm import Session
from pathlib import Path


def read_password(path: str) -> str:
    """Read the database password from a file.

    Args:
        path (str): Path to the file that contains the password.

    Returns:
        str: The password, without surrounding whitespace.
    """
    with open(path) as f:
        return f.read().strip()


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
        f"postgresql+psycopg://{user}:{password}@{host}:{port}/{database}"
    )

    with engine.connect():
        print("\033[32mEngine created successfully.\033[0m\n")

    return engine


def table_exists(engine: db.Engine, table: str) -> bool:
    """Check if tables already exist.

    Args:
        engine (db.Engine): Engine object.
        table (str): table name.

    Returns:
        bool: Return True if a table with this name exists in the database.
    """
    return db.inspect(engine).has_table(table_name=table)


def is_empty(engine: db.Engine, table: db.Table) -> bool:
    """_summary_

    Args:
        engine (db.Engine): _description_
        table (db.Table): _description_

    Returns:
        bool: _description_
    """
    with engine.connect() as conn:
        return conn.execute(db.select(table).limit(1)).first() is None


def count_rows(engine: db.Engine, table: db.Table) -> int | None:
    """Return True if the table has no rows."""
    with engine.connect() as conn:
        return conn.execute(db.select(db.func.count()).select_from(table)).scalar()


def get_data_tables(engine: db.Engine) -> list[db.Table]:
    """Reflect the existing data_202* tables from the database.

    Args:
        engine (db.Engine): Engine connected to the database

    Returns:
        list[db.Table]: The monthly tables, sorted by name.
    """

    metadata = db.MetaData()
    metadata.reflect(bind=engine, only=lambda name, _: name.startswith("data_202"))

    return [metadata.tables[name] for name in sorted(metadata.tables)]


def merge_tables(engine: db.Engine, merged: db.Table, tables: list[db.Table]) -> None:
    """Insert the rows of all the given tables into the merged table.

    The work is done inside PostgreSQL (INSERT ... SELECT ... UNION ALL),
    so no row goes through Python.

    Args:
        engine (db.Engine): Engine connected to the database.
        merged (db.Table): Destination table, it must already exist.
        tables (list[db.Table]): Source tables, with the same columns.
    """
    query = db.union_all(*[db.select(t) for t in tables])

    with Session(engine) as session:
        session.execute(merged.insert().from_select(merged.columns.keys(), query))
        session.commit()


def create_table(metadata: db.MetaData, name: str, **columns) -> db.Table:
    """Define a table in the metadata, using keyword arguments as columns.

    Args:
        metadata (db.MetaData): Metadata where the table is registered.
        name (str): Name of the table.
        **columns: column_name=column_type pairs, in column order.

    Returns:
        db.Table: The table that was defined (not created in Postgres yet).
    """
    cols = [db.Column(k, v) for k, v in columns.items()]
    table = db.Table(name, metadata, *cols)

    print(f"Table '\033[32m{name}\033[0m' created successfully.")

    return table


def main() -> None:
    """Join all the data_202* tables into a table called customers."""

    database = "piscineds"
    user = "hbourlot"
    password = read_password("./db_password.txt")
    port = "4242"
    host = "localhost"

    engine = get_engine(database, user, password, port, host)

    sources = get_data_tables(engine)
    if not sources:
        print("No data_202* tables found. Load the first (automatic_table).")
        return

    columns = {c.name: c.type for c in sources[0].columns}

    metadata = db.MetaData()
    merged = create_table(metadata, "customers", **columns)

    already_filled = table_exists(engine, merged.name) and not is_empty(engine, merged)

    metadata.create_all(engine)

    if already_filled:
        print(f"'{merged.name}' already has data, skipping the merge.")
        return

    print(f"Merging {len(sources)} tables: {[t.name for t in sources]} ")
    merge_tables(engine, merged, sources)
    print(f"'{merged.name}' now has {count_rows(engine, merged)} rows.")


if __name__ == "__main__":

    try:
        main()
    except Exception as e:
        print("Error -> ", e)
        raise
