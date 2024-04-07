class Circle:
    """
    Class of Circle.

    Attributes:
        all_circles (list): list of all instances of the class
        PI (int): the value of pi
        radius (float): the radius of the circle
    """

    all_circles = []
    PI = 3.1415

    def __init__(self, radius=1):
        """
        The function initializes a new class object.
        :param radius (float): the radius of the circle
        """
        self.all_circles.append(self)
        self.radius = radius

    def area(self):
        """
        The method calculates the area of a circle.
        :return: the area of the circle (float)
        """
        area_circle = Circle.PI * self.radius ** 2

        return round(area_circle, 3)

    @staticmethod
    def total_area():
        """
        The method returns the total area of all instances of the class.
        :return: the total area of the class specimens (float)
        """
        sum_area = 0
        for circle in Circle.all_circles:
            sum_area += circle.area()

        return round(sum_area, 3)

    def __str__(self):
        """
        Displaying information about a class object to users.
        """
        return f'Экземпляр класса Circle: радиус - {self.radius}, площадь - {self.area()}'

    def __repr__(self):
        """
        Displaying information about a class object in debugging mode.
        """
        return f'{self.radius}: {round(self.area(), 3)}'
