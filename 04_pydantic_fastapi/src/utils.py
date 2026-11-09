from pathlib import Path
import duckdb

DATA_PATH = Path(__file__).parent / "data"

DATA_PATH.mkdir(exist_ok=True)


def query_duckdb(sql_code: str, parameters=None):
    with duckdb.connect(DATA_PATH/"movies.duckdb") as conn:
        # parameters to avoid sql injections
        cursor = conn.execute(sql_code, parameters=parameters)

        # strip, make lowercase
        # if its starts with select, from , desc , pragna
        # return df
        # else none
        if sql_code.strip().casefold().startswith(("select", "from", "desc", "pragna")):
            return cursor.df()
