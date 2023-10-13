import random

class Human:
  # wird bei jedem neuen Objekt erneut ausgeführt
  def __init__(self, name: str, age: int, height: float):
    self.name = name
    self.age = age
    self.height = height

  # wenn man ein Objekt print()
  def __str__(self):
    return f"Name: {self.name} | Age: {self.age} | Height: {self.height}cm"

  # private funktion die nur in der Klasse selbst aufgerufen werden kann
  def __get_age(self):
    return self.age

  def height_in_meter(self):
    return self.height / 100

  def predict_lifespan(self):
    lifespan = random.randint(self.__get_age()+1, 100)
    return f"{self.age} - {lifespan}"


human_1 = Human('Peter', 34, 179.34)
print(human_1.predict_lifespan())