# https://realpython.com/python-magic-methods/#getting-to-know-pythons-magic-or-special-methods
# Addition operator overloading example
class Storage(float):
    def __new__(cls, value, unit):
        instance = super().__new__(cls, value)
        instance.unit = unit
        return instance
    
    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(
                    "unsupported operand for +: "
                    f"'{type(self).__name__}'" and f"'{type(other).__name__}'"
                )

        if not self.unit == other.unit: 
            raise TypeError(
                    "unsupported operand for +: "
                    f"incompatible units: '{self.unit}' and '{other.unit}'"
                )
        
        return type(self)(super().__add__(other), self.unit)
    

# storage1 = Storage(100, "GB")
# storage2 = Storage(200, "GB")

# print(storage1 + storage2)
# print(storage2)

# # # # # # # # # # # # # # # # #
# Pipe operator overloading example
# I want to be able to pass a string from one class to the other 
# class1('4') | class2('5') = '45'
class RunnableClass(str):
    def __new__(cls, value):
        instance = super().__new__(cls, value)
        return instance

    def __or__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(
                    "unsupported operand for |: "
                    f"'{type(self).__name__}'" and f"'{type(other).__name__}'"
                )
        return type(self)(super().__add__(other))
    

class1 = RunnableClass('4')
class2 = RunnableClass('5')
print(class1 | class2)
