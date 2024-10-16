# Turtle-Graphics-Drawing-with-Object-Oriented-Programming
This project demonstrates the use of Object-Oriented Programming (OOP) to create various shapes using the Python turtle module. The program defines classes such as Point, Box, BoxFilled, Circle, and CircleFilled to encapsulate behavior for drawing and filling shapes at specified coordinates. Each shape has customizable attributes like position, size, color, and fill color.

Classes:
Point: Represents a point that is drawn as a dot on the canvas.
Box: Draws a rectangular box at a specified location with given width and height.
BoxFilled: Inherits from Box and adds the ability to fill the box with a specified fill color.
Circle: Draws a circle with a specified radius and color at a given position.
CircleFilled: Inherits from Circle and adds the ability to fill the circle with a specified fill color.

Features:
OOP Structure: Each shape is encapsulated within its own class, supporting clear inheritance and method overriding.
Turtle Graphics: Utilizes Python’s built-in turtle module to visually render shapes.
Custom Colors: Allows you to specify different colors for shape outlines and fills.
Easy to Extend: The OOP design allows for easy addition of new shapes or customization of existing ones.

How to Run:
Ensure Python is installed and the turtle module is available (it’s included in Python by default).
Uncomment the test code at the bottom of the script to see different shapes drawn on the canvas.
Run the Python script to see the shapes rendered one by one using the turtle graphics window.
Example Shapes:

Draw a single point Code:
p = Point(-100, 100, "blue")
p.draw()

Draw a rectangle Code:
b = Box(100, 110, 50, 40, "red")
b.draw()

Draw a filled circle Code:

cf = CircleFilled(-100, -100, 70, "yellow", "orange")
cf.draw()

Technologies Used:
Turtle module
Object-Oriented Programming (OOP)
