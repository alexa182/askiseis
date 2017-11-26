class Square:

    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width


# define getter

    @property
    def height(self):
        print("Retriving the HEIGHT")

        return self.__height #<-- __ = protect data

    @height.setter
    def height(self, value):

        if value.isdigit():
            self.__height = value

        else:
            print("PLS ONLY ENTER A NUMBER FOR HEIGHT")




    @property
    def width(self):
        print("Retriving the WIDTH")

        return self.__width #<-- __ = protect data

    @width.setter
    def width(self, value):

        if value.isdigit():
            self.__width = value

        else:
            print("PLS ONLY ENTER A NUMBER FOR WIDTH")


    def getArea(self):
        return int(self.__width) * int(self.__height)


def main():
    aSquare = Square()

    height = input("Enter Height: ")
    width = input("Enter Width: ")

    aSquare.height = height
    aSquare.width = width

    print("Height : ", aSquare.height)
    print("Width : ", aSquare.width)

    print("The Area is :", aSquare.getArea())

main()