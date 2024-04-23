from fastapi import FastAPI, Path

app=FastAPI()

inventory={1:{"Brand":"milbona",
              "price": 4.50,
              "taste":"delicious"
               },
            2:{"Brand":"milka",
               "price":3.20,
               "taste":"mid"}
          }
@app.get("/")
def home():
    return {'data':'test'}

@app.get("/get-item/{item_id}")
def inv(item_id: int = Path( description="The id of the item you want to preview")):
    return inventory[item_id]

@app.get("/get-by-brand")
def inv1(name:str = None):
    for id_item in inventory:
        if inventory[id_item]["Brand"] == name:
            return inventory[id_item]
    return 'Item not found'






