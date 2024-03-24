from typing import Union
import mongoDB
from fastapi import FastAPI

app = FastAPI()


@app.get("/readDB")
def read_mongoDB():
    return mongoDB.readDB()


@app.post("/addBiscs2DB/{val}")
def add_bisc_2_mongo(val: bool):
    return mongoDB.addBiscs2DB(val=val)

@app.delete("/remBisc4mDB")
def rem_Bisc_4m_DB():
    return mongoDB.remBisc4mDB()