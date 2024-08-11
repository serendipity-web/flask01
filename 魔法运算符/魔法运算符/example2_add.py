import typing


class ShoppingCert:
    def __init__(self, items: typing.List[str]):
        self.items = items

    def __add__(self, another_cert):
        new_cart = self.items + another_cert.items
        return new_cart

    def __str__(self):
        return f"Cart{self.items}"

    def __call__(self, item):
        self.items.append(item)


carts_one = ShoppingCert(["apple", "banana"])
carts_two = ShoppingCert(["purple"])
carts_new = carts_two + carts_one
print(carts_new)
carts_one('orange')
print(carts_one)
