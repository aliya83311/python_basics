class Road:
  def __init__(self, length, width, thickness=1):
    self._length = length
    self._width = width
    self._weight = 25
    self._thickness = thickness

  def count_weight(self):
    result = self._length*self._width*self._weight*self._thickness
    return result


Moscow_Tver = Road(1345, 10)
print(Moscow_Tver.count_weight())

Tomsk_Omsk = Road(2345, 10, 5)
print(Tomsk_Omsk.count_weight())
