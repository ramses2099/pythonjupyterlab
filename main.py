from fastapi import FastAPI

app = FastAPI()

data = [{
    "id": 1,
    "name": "Lidsoupcont Rp12dn",
    "price": "$83.37"
}, {
    "id": 2,
    "name": "Beef - Diced",
    "price": "$82.96"
}, {
    "id": 3,
    "name": "Crab - Meat",
    "price": "$82.05"
}, {
    "id": 4,
    "name": "True - Vue Containers",
    "price": "$76.19"
}, {
    "id": 5,
    "name": "Juice - Apple 284ml",
    "price": "$94.43"
}, {
    "id": 6,
    "name": "Green Scrubbie Pad H.duty",
    "price": "$71.56"
}]


@app.get("/")
def home():
    return data


@app.get("/about")
def about():
    return {"Data": "About"}


@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    elem = {}
    for l in data:
        if(l['id'] == item_id):
            elem = l
    return elem


if __name__ == "__main__":
    for l in data:
        print(l['id'])
