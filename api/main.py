from fastapi import FastAPI
from mangum import Mangum
import os


import requests
import socket
# import pymssql

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "This is home page"}


@app.get("/data")
async def data():

    return  {"database":{
         "hosts":["webserver1"],
         "vars":{
             "ansible_ssh_pass":"root",
             "ansible_ssh_host": "3.80.201.74"
         }
     }
     }

@app.get("/api2")
async def api2():
    return {"message": "This is a second api"}

@app.get("/api3")
async def api3():
    print('This is api3')
    return {"message": "This is a third api for testing vnet with vpn access"}


@app.get("/api4")
async def api4():
    print('This is api4')
    return {"message": "This is a fourth api for testing vnet with vpn access"}

@app.get("/pom")
async def pom():
    print('This is api4')
    return {"message": "This is a new pom test"}




handler = Mangum(app)