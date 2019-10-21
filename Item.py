class Item():
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __str__(self):
        return str(self.weight) + " " + str(self.value)
