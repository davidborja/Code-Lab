from parent_class import ParentClass
from child_decorator import ChildDecorator

if __name__ == "__main__":

    a = ParentClass()
    b = ChildDecorator(a)
    c = ChildDecorator(a, 14)

    a.hey("Alfredo Topete Escamilla")

    b.hey("Alfredo Topete Escamilla")

    c.hey("Alfredo Topete Escamilla")
