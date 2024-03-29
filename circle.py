from __future__ import annotations
import math


class Circle:

    def __init__(self, radius):
        """Initialize a circle with given radius.
        
        :param radius: radius of the circle, may be zero.
        :raises ValueError: if radius is negative.
        >>> c1 = Circle(-1)     # test invalid create Circle object
        Traceback (most recent call last):
         ...
        ValueError: radius must be non-negative
        >>> c1 = Circle(1)      # test valid create Circle object
        >>> c1.radius
        1
        """
        if radius < 0:
            raise ValueError("radius must be non-negative")
        self.radius = radius

    def add_area(self, circle: Circle) -> Circle:
        """Return a new circle whose area equals the combined
        area of this circle and another circle.
        Since area is pi*r**2, the radii of the 3 circles
        should form a Pythagorean triple (r1^2 + r2^2 = r3^2)
        >>> c1 = Circle(3)
        >>> c2 = Circle(4)
        >>> c3 = c1.add_area(c2)    # normal case radius is two and three
        >>> c3.radius
        5.0
        >>> c4 = Circle(0)
        >>> c5 = c1.add_area(c4)    # edge case one of the radius is zero
        >>> c5.radius
        3.0
        """
        r1 = self.get_radius()
        r2 = circle.get_radius()
        # this is important, so show the operation in a rounded-box
        # on the Circle lifeline, or show it as a comment.
        r = math.hypot(r1, r2)
        # In a sequence diagram create a name for the new circle
        # so that you can show what is being returned.
        return Circle(r)

    def get_area(self) -> float:
        return math.pi*self.radius*self.radius
    
    def get_radius(self) -> float:
        return self.radius

    def __str__(self) -> str:
        return f"Circle({self.radius})"
    
    __repr__ = __str__
