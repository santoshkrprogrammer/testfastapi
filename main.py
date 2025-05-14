from fastapi import FastAPI
from mangum import Mangum
import os
app = FastAPI()
handler = Mangum(app)
import requests
import socket
# import pymssql



@app.get("/data")
async def root():

    return  {"database":{
         "hosts":["webserver1"],
         "vars":{
             "ansible_ssh_pass":"root",
             "ansible_ssh_host": "3.80.201.74"
         }
     }
     }

@app.get("/api2")
async def root():
    return {"message": "This is a second api"}

@app.get("/api3")
async def root():
    print('This is api3')
    return {"message": "This is a third api for testing vnet with vpn access"}

@app.get("/api4")
async def root():
    return {"message": "This is a fourth api for testing vnet with vpn access"}

@app.get("/checksecret")
async def root():
    return {"message": f"testsecret={os.environ['testsecret']}"}

@app.get("/demosecret")
async def root():
    return {"message": f"demosecret={os.environ['demosecret']}"}

@app.get("/demo")
async def root():
    return {"message": f"This is demo api"}

@app.get("/demo2")
async def root():
    return {"message": f"This is demo2 api"}
# Function to check connectivity to a specific VM
def check_connectivity(ip: str, port: int):
    try:
        # Create a socket object
        sock = socket.create_connection((ip, port), timeout=5)
        sock.close()
        return f"Successfully connected to {ip}:{port}"
    except (socket.timeout, socket.error) as e:
        return f"Failed to connect to {ip}:{port} - {str(e)}"

# FastAPI route to check VM connectivity
@app.get("/check-connectivity/{ip}/{port}")
def check_connectivity_route(ip: str, port: int):
    result = check_connectivity(ip, port)
    return {"result": result}

# @app.get("/db-connect")
# def db_connect():
#     try:
#         conn = pymssql.connect(server="10.0.18.5", user="Prod-LC-Connector", password="c@UkKuProd", database="CELF")
#         cursor = conn.cursor()
#         cursor.execute ("SELECT * from dbo.XLImport")
#         rows = cursor.fetchall()  # Fetch all rows
#         print('Test api')
#         # Convert rows to a list of dictionaries for JSON compatibility
#         columns = [column[0] for column in cursor.description]  # Get column names
#         results = [dict(zip(columns, row)) for row in rows]  # Map column names to row values

#         cursor.close()
#         conn.close()
#         return {"success":results}
#     except Exception as e:
#         print("\nERROR: Unable to connect to the server.",e)
#         return {"error":"error in db connection"}