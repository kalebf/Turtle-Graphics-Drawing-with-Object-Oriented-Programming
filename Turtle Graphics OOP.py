import turtle

class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
    
    def draw_action(self):
        turtle.dot()

class Box(Point):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, color)
        self.width = width
        self.height = height
    
    def draw_action(self):
        for _ in range(2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)

class BoxFilled(Box):
    def __init__(self, x, y, width, height, color, fillcolor):
        super().__init__(x, y, width, height, color)
        self.fillcolor = fillcolor
    
    def draw_action(self):
        turtle.begin_fill()
        super().draw_action()
        turtle.end_fill()

class Circle(Point):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, color)
        self.radius = radius
    
    def draw_action(self):
        turtle.circle(self.radius)

class CircleFilled(Circle):
    def __init__(self, x, y, radius, color, fillcolor):
        super().__init__(x, y, radius, color)
        self.fillcolor = fillcolor
    
    def draw_action(self):
        turtle.begin_fill()
        super().draw_action()
        turtle.end_fill()

# Testing the classes
'''
p = Point(-100, 100, "blue")
p.draw()

b = Box(100, 110, 50, 40, "red")
b.draw()

bf = BoxFilled(1, 2, 100, 200, "red", "blue")
bf.draw()

c = Circle(100, 0, 50, "green")
c.draw()

cf = CircleFilled(-100, -100, 70, "yellow", "orange")
cf.draw()

turtle.done()
'''
