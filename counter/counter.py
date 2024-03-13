"""A singleton counter.

   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value

   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s %(funcName)8s: %(message)s")


class Counter:
    """Counter class that counts and add when increment is called"""
    __instance = None

    def __str__(self):
        return f"{self.__count}"

    def __new__(cls, *args, **kwargs):
        """Create the same instance when """
        if cls.__instance is None:
            logging.info("Create new Counter")  # for checking when create new
            cls.__instance = super().__new__(cls)
            cls.__instance.__count = 0
        return cls.__instance

    @property
    def count(self):
        """Return count value"""
        return self.__count

    def increment(self):
        """Add one to count and return the new value"""
        self.__count += 1
        return self.__count


if __name__ == '__main__':
    # should show info when create
    c = Counter()
    print(f"count value is zero: {c.count}")
    print(f"increment one time: {c.increment()}")
    print(f"count value is one: {c.count}")
    print(f"id of count object 1: {id(c)}")
    # should not show info when create and stay the same
    c2 = Counter()
    print(f"id of count object 2: {id(c2)}")
