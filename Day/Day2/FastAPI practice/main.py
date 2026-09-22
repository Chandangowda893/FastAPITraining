from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"page": "home"}
@app.get("/about")
def about():
    return {"page": "about","author": "chandan"}
@app.get("/health")
def health():
    return {"status": "ok"}

#post request
@app.post("/create")
def create_something():
    return {"message": "created"}

#path parameter
@app.get("/student/{usn}")
def get_student(usn):
    return {"Result":"Distinction","usn":usn}