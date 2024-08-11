"""
add(2)(3)=5
add(1)(2)(3)(4)(5)=15
"""


class add:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"{self.num}"

    def __add__(self, num):
        return self.num + num


addTwo = add(2)
print(addTwo)
print(addTwo+5)
