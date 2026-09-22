from fastapi import FastAPI
from pydantic import BaseModel
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
#path parameter with type Hint
@app.get("/candidate/{roll_no}")
def get_candidate(roll_no: int):
    return {"Result":"Distinction","roll_no":roll_no,"type": str(type(roll_no))}

# pydantic Model
class Item(BaseModel):
    name: str
    price: float
    in_stock:bool = True

@app.post("/items")
def create_item(item: Item):
    return {"received": item, "total_price": item.price * 1.18}