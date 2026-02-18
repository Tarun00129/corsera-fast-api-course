from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()


@app.get("/shipment")
def get_shipment():
    return {
        "shipment_id": 123,
        "content": "Cricket Bat",
        "destination": "Modinagar",
        "source": "Delhi",
        "status": "Out for Delivery",
    }


@app.get("/scalar", include_in_schema=False)
def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Shipment API",
    )
