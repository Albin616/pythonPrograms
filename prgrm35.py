class Time:
 def __init__(self, hour, minute, second):
  self.__hour = hour
  self.__minute = minute
  self.__second = second
 def __add__(self, other):
  sec = self.__second + other.__second
  minute = self.__minute + other.__minute + sec // 60
  hour = self.__hour + other.__hour + minute // 60
  sec = sec % 60
  minute = minute % 60
  return Time(hour, minute, sec)
 def display(self):
  print(self.__hour, ":", self.__minute, ":", self.__second)
t1 = Time(2, 45, 50)
t2 = Time(1, 30, 30)
t3 = t1 + t2
print("First Time:")
t1.display()

print("Second Time:")
t2.display()

print("Sum of Two Times:")
t3.display()