

class A:
    x = 10
    y = 50

    # def plus1(self, a: int, b: int) -> int:
    #     return a * b

    def __init__(self, a: float):
        self.a = a


    # @classmethod
    # def sub(cls):
    #     return cls.x * cls.y
    @classmethod
    def sub(cls):
        return cls(666)

print(A.sub().__dict__)



print(A.sub)
print(A.sub())
