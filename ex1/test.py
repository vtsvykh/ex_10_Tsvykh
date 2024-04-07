import circle


circle_1 = circle.Circle()
circle_2 = circle.Circle(2)
circle_3 = circle.Circle(3.5)

print(circle_1.area())
print(circle_2.area())
print(circle_3.area())

print(circle.Circle.total_area())
