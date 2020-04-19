
FAKE_PRODUCTS = [
    {
        "id": 1,
        "title": "iPhone 11",
        "passenger_capacity": 100,
        "maximum_speed": 50,
        "in_stock": 5 
    }
]

class Storage():

    def get(self, product_id):
        return FAKE_PRODUCTS[0]

    def get_all(self):
        return FAKE_PRODUCTS
        