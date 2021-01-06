class Conversion:
    def __init__(self, data):
        self.temp = data["main"]["temp"]

    def kel_to_cel(self):
        self.temp = round(self.temp - 273.15, 2)
