import asyncio
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import Pool
from timer import timer

import random
import sqlalchemy
from datetime import date
from string import ascii_letters
import pandas as pd

df1 = pd.read_csv("hw14/5m Sales Records.csv", sep=",", encoding="utf-8")
df2 = df1.copy()
df3 = df1.copy()

@timer(1, 1)
def read1():
    with ThreadPoolExecutor(max_workers=100) as executor:
        df_read = pd.read_csv("hw14/5m Sales Records.csv", sep=",", encoding="utf-8")
        print("Reading csv with multithreading:")

@timer(1, 1)
def read2():
    with Pool() as pool:
        df_read = pd.read_csv("hw14/5m Sales Records.csv", sep=",", encoding="utf-8")
        print("Reading csv with multiprocessing:")       

async def read3():
    df_read = pd.read_csv("hw14/5m Sales Records.csv", sep=",", encoding="utf-8")

@timer(1, 1)
def func():
    asyncio.run(read3())
    print("Reading csv with asyncio:")
print("\n") 

@timer(1, 1)
def write1():
    with ThreadPoolExecutor(max_workers=100) as executor:
        df1['SOURCE_KEY'] = [''.join(random.choice(ascii_letters) for x in range(10)) for _ in range(len(df1))]
        df1['LOAD_DATE'] = date.today().strftime("%d/%m/%Y")

        def load_to_db():
            print("Loading table to db.")
            df1.to_sql('main_table_1', connection_to_db(), if_exists="append", method='multi', index=False, chunksize=1000)
            print("DONE")
        
        def connection_to_db():
            engine = sqlalchemy.create_engine("mysql://codetest:swordfish@127.0.0.1:3306/codetest", encoding="utf-8", pool_pre_ping=True)
            connection = engine.connect()
            return connection

        load_to_db()        
        print("Writing and loading with multithreading:")

@timer(1, 1)
def write2():
    with Pool() as pool:
        df2['SOURCE_KEY'] = [''.join(random.choice(ascii_letters) for x in range(10)) for _ in range(len(df2))]
        df2['LOAD_DATE'] = date.today().strftime("%d/%m/%Y")

        def load_to_db():
            print("Loading table to db.")
            df2.to_sql('main_table_2', connection_to_db(), if_exists="append", method='multi', index=False, chunksize=1000)
            print("DONE")
        
        def connection_to_db():
            engine = sqlalchemy.create_engine("mysql://codetest:swordfish@127.0.0.1:3306/codetest", encoding="utf-8", pool_pre_ping=True)
            connection = engine.connect()
            return connection

        load_to_db()          
        print("Writing and loading with multiprocessing:")     

async def write3():
    df3['SOURCE_KEY'] = [''.join(random.choice(ascii_letters) for x in range(10)) for _ in range(len(df3))]
    df3['LOAD_DATE'] = date.today().strftime("%d/%m/%Y")

    def load_to_db():
        print("Loading table to db.")
        df3.to_sql('main_table_3', connection_to_db(), if_exists="append", method='multi', index=False, chunksize=1000)
        print("DONE")
        
    def connection_to_db():
        engine = sqlalchemy.create_engine("mysql://codetest:swordfish@127.0.0.1:3306/codetest", encoding="utf-8", pool_pre_ping=True)
        connection = engine.connect()
        return connection

    load_to_db()  

@timer(1, 1)
def func():
    asyncio.run(write3())
    print("Writing and loading with asyncio:")  

