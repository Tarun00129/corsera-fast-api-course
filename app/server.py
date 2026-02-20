from typing import Any, Callable

routes: dict[str, Callable[[Any], Any]] = {}


def route(path: str):
    def register_route(func):
        routes[path] = func
        return func

    return register_route


@route("/shipment")
def get_shipment():
    return {
        "shipment_id": 123,
        "content": "Cricket Bat",
        "destination": "Modinagar",
        "source": "Delhi",
        "status": "Out for Delivery",
    }


request: str = ""

while request != "exit":
    request = input("Enter your request: ")
    if request in routes:
        response = routes[request]()
        print("-" * 10)
        print(response)
        print("-" * 10)
    else:
        print("Request Not Found 404")
