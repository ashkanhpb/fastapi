from fastapi import FastAPI

app = FastAPI()

names_list = [{"id":"1" , "name":"ashkan"} , {"id":"2" ,"name":"saied" } , {"id":"3" , "name":"ahmad"}]

@app.get("/")
def root():
    return {"message": "Hello World"}
@app.get("/names")
def get_names():
    return names_list

@app.get("/names/{id}")
def get_name(id: str):
    for n in names_list:
        if n["id"] == id:
            return n


