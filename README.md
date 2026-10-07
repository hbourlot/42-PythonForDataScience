# 42 — Python for Data Science

My solutions to the 42 school **Python for Data Science** piscines: a Python
crash course followed by data engineering work on PostgreSQL.

## Layout

```
PISCINE/
├── PISCINE-1/            Python fundamentals
│   ├── Python-0-Starting   types, strings, argv, a tqdm clone, packaging
│   ├── Python-1-Array      NumPy arrays, image load / zoom / rotate / filters
│   ├── Python-2-DataTable  pandas + matplotlib on life-expectancy & population CSVs
│   ├── Python-3-OOP        abstract classes, inheritance, diamond problem, operators
│   └── Python-4-Dot        *args/**kwargs, closures, decorators, dataclasses
└── PISCINE-2/            Data science track
    ├── DataEngineer        Postgres + pgAdmin in Docker, CSV -> tables with SQLAlchemy
    └── DataWarehouse       merging customer / item tables
```

Each module has one folder per exercise (`ex00`, `ex01`, ...). The subject PDF
for the PISCINE-2 modules sits next to them as `en.subject.pdf`.

## Requirements

- Python 3.10+
- Docker (PISCINE-2 only)

```bash
pip install numpy pandas matplotlib opencv-python sqlalchemy "psycopg[binary]"
```

## Running

### PISCINE-1

Exercises are standalone scripts, run from their own folder:

```bash
cd PISCINE/PISCINE-1/Python-1-Array/ex03 && python zoom.py
```

`Python-0-Starting/ex09` is an installable package:

```bash
pip install ./PISCINE/PISCINE-1/Python-0-Starting/ex09
```

### PISCINE-2

Each exercise ships a `docker-compose.yml` that starts Postgres (port `4242`)
and pgAdmin (<http://localhost:8080>). Before starting it:

1. Create the two secret files next to the compose file (both are gitignored):
   `db_password.txt` and `pgadmin_password.txt`.
2. Edit the `/data` volume path in `docker-compose.yml` — it is an absolute
   path on my machine and must point at your folder of subject CSVs (not
   committed).

```bash
cd PISCINE/PISCINE-2/DataWarehouse/ex00 && docker compose up -d
```

Then run the table scripts, e.g. `python customers_table.py`.

| Setting  | Value       |
| -------- | ----------- |
| Database | `piscineds` |
| User     | `hbourlot`  |
| Host     | `localhost` |
| Port     | `4242`      |

## Notes

Code follows the piscine rules: flake8-clean, documented functions, no
globals. Written for learning — if you are a 42 student, use it as a
reference, not a copy source.
