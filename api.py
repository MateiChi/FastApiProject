from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional
import json

app = FastAPI()

with open("Inventory.json") as f:
     Inventory = json.load(f)

class Item(BaseModel):
    Brand: str
    Price: str
    Taste: Optional[str]

class UpdateItem(BaseModel):
    Brand: Optional[str] = None
    Price: Optional[str] = None
    Taste: Optional[str] = None
          
@app.get("/")
def home():
    return {'data': 'test'}

@app.get("/get-item/{item_id}")
def inv(item_id: str = Path(..., description="The id of the item you want to preview")):
    return Inventory.get(item_id)

@app.get("/get-by-brand")
def inv1(name: str = None):
    for id_item in Inventory:
        if Inventory[id_item]['Brand'] == name:
            return Inventory[id_item]
    return 'Item not found'

@app.post("/create-item/{item_id}")
def create_item(item_id: str, item: Item):
    if item_id in Inventory:
        return {"Error": "Item ID already exists."}
    Inventory[item_id] = item.dict()
    with open("Inventory.json", 'w') as f:
        json.dump(Inventory, f, indent=4)
    return Inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: str, item: UpdateItem):
    if item_id not in Inventory:
        return {"Error": "Item ID doesn't exist."}
    if item.Brand is not None:
        Inventory[item_id]["Brand"] = item.Brand
    if item.Price is not None:
        Inventory[item_id]["Price"] = item.Price
    if item.Taste is not None:
        Inventory[item_id]["Taste"] = item.Taste 
    with open("Inventory.json", 'w') as f:
        json.dump(Inventory, f, indent=4)
    return Inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: str):
    if item_id not in Inventory:
        return {"Error": "Id does not exist."}
    del Inventory[item_id]
    with open("Inventory.json", 'w') as f:
        json.dump(Inventory, f, indent=4)
    return {"Success": "Item deleted!"}
