from fastapi import FastAPI

app= FastAPI()

@app.get ("/")
def read_root():
    return{"message":"Привет мир!"}

@app.get ("/hello")
def say_hello():
    return{"message":"Привет из /hello"}

@app.get("/hello/{name}")
def say_hello_to(name):
    return{"message":f"Привет, {name}!"}