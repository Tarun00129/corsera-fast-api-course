from fastapi import FastAPI

app = FastAPI()

@app.get("/shipment")
def get_shipment():
    return {
        "shipment_id": 123,
        "content": "Cricket Bat",
        "destination": "Modinagar",
        "source": "Delhi",
        "status": "Out for Delivery"
    }