"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Mark Hays, Amanda Stouder,
         their colleagues and Isaac Harper.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.


import rosegraphics as rg
import math


def main():
    two_circles()
    circle_and_rectangle()
    lines()
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:


def two_circles():
    window = rg.RoseWindow()
    center_point1 = rg.Point(100, 100)
    radius1 = 15
    center_point2 = rg.Point(200, 172)
    radius2 = 25
    circle1 = rg.Circle(center_point1, radius1)
    circle2 = rg.Circle(center_point2, radius2)
    circle2.fill_color = 'red'
    circle1.attach_to(window)
    circle2.attach_to(window)
    window.render()
    window.close_on_mouse_click()
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # Done: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    window = rg.RoseWindow()
    x = 251
    y = 213
    center_point = rg.Point(x, y)
    radius = 35
    circle = rg.Circle(center_point, radius)
    circle.fill_color = 'blue'
    circle.attach_to(window)
    a = 50
    b = 87
    c = 100
    d = 300
    point1 = rg.Point(a, b)
    point2 = rg.Point(c, d)
    rectangle = rg.Rectangle(point1, point2)
    center = rectangle.get_center()
    rectangle.attach_to(window)
    window.render()
    print(circle.outline_thickness)
    print(circle.fill_color)
    print(circle.center)
    print(x)
    print(y)
    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    print(center)
    print((a + c) / 2)
    print((b + d) / 2)
    window.close_on_mouse_click()



    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # Done: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    window = rg.RoseWindow()
    a = 10
    b = 20
    c = 300
    d = 250
    point1 = rg.Point(a, b)
    point2 = rg.Point(c, d)
    point3 = rg.Point(250, 123)
    point4 = rg.Point(100, 75)
    line1 = rg.Line(point1, point2)
    line1.thickness = 15
    line2 = rg.Line(point3, point4)
    line1.attach_to(window)
    line2.attach_to(window)
    midpoint = rg.Line.get_midpoint(line1)
    print(midpoint)
    print((a + c) / 2)
    print((b + d) / 2)
    window.render()
    window.close_on_mouse_click()
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # Done: 4. Implement and test this function.


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
