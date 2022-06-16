class parenclass:
    def GetFirstName(self, fullname):
        return fullname.split(" ")[0]

    def hey(self, fullname):
        print("Hello" + self.GetFirstName(fullname))


class Child_class(parenclass):
    def __init__(self, age=None):
        self.age = age

    def hey(self, fullname):
        if self.age and self.age < 18:
            print("What's up" + self.GetFirstName(fullname) + "?")

        elif self.age and self.age > 18:
            super().hey(fullname)

        elif not self.age:
            super().hey(fullname)


if __name__ == "__main__":

    a = parenclass()

    b = Child_class()

    c = Child_class(14)

    a.hey("Alfredo Topete Escamilla")

    b.hey("Alfredo Topete Escamilla")

    c.hey("Alfredo Topete Escamilla")
