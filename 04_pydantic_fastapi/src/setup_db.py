from utils import query_duckdb

# in video divided but in class same script then you need to use
# __name__ == "__main__":
query_duckdb("""
    CREATE TABLE IF NOT EXISTS movies (
        title TEXT, 
        year INTEGER, 
        genre TEXT, 
        rating TINYINT, 
        summary TEXT
    ); 

""")
