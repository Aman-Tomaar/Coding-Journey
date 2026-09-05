# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives you getter, setter, and deleter methods


class Rectangle:
    def __init__(self, height, width):
        self._height = height  #  '_' if used to show that this is something not to be used in code publicaly
        self._width = width

    @property  # getter
    def height(self):
        return f"{self._height:.2f}cm"

    @property  # getter
    def width(self):
        return f"{self._width:.2f}cm"

    @height.setter  # setter
    def height(self, new_height):
        if new_height <= 0:
            print(f"Height should be grater then 0")
        else:
            self._height = new_height

    @width.setter  # setter
    def width(self, new_width):
        if new_width < 0:
            print(f"Height should be grater then 0")
        else:
            self._width = new_width

    @height.deleter  # delete
    def height(self):
        del self._height
        print("Height has been Succesfully Deleated")

    @width.deleter  # delete
    def width(self):
        del self._width
        print("Width has been Succesfully Deleated")


rectangle = Rectangle(3, 5)

rectangle.height = 0  # changing value of height to 4 from 3

print(f"Height: {rectangle.height}")
print(f"Width: {rectangle.width}")

del rectangle.width
# print(f"Width: {rectangle.width}") => if we try to search for it after deleating it , we will get an error
