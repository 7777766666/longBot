

class A:
    x = 10
    y = 50

    def plus1(self, a: int, b: int) -> int:
        return a * b

    @classmethod
    def sub(cls):
        return cls.x * cls.y



print(A.sub)
print(A.sub())
