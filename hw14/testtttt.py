from concurrent.futures import ThreadPoolExecutor
from timer import timer
import pandas as pd
import sqlalchemy


with ThreadPoolExecutor(max_workers=100) as executor:
    df = pd.read_csv("hw14/5m Sales Records.csv", sep=",", encoding="utf-8")
        
@timer(1, 1)
def read2():
    with ThreadPoolExecutor(max_workers=100) as executor:
        def load_to_db():
            print("Loading table to db.")
            df.to_sql('stage_table', connection_to_db(), if_exists="append", method='multi', index=False, chunksize=1000)
            print("DONE")
        
        def connection_to_db():
            engine = sqlalchemy.create_engine("mysql://codetest:swordfish@127.0.0.1:3306/codetest", encoding="utf-8", pool_pre_ping=True)
            connection = engine.connect()
            return connection

        load_to_db()