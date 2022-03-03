class Math:
    var = 20

    @staticmethod #declaring static method()
    def add5(x):
        return x+5

    @staticmethod #declaring static method()
    def add10(x):
        return x+10

    @classmethod #declaring class method(cls)
    def vadd10(cls):
        return cls.var+10

    def pr():
        print("run")

print(Math.add10(5))
Math.pr()

print(Math.var)
Math.var = Math.vadd10()
print(Math.var)