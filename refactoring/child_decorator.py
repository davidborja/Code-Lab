from parent_interface import ParentInterface


class ChildDecorator(ParentInterface):
    def __init__(self, parent_instance, age=None):
        self.age = age
        self.wrappe = parent_instance

    def get_first_name(self, fullname):
        return self.wrappe.get_first_name(fullname)

    def hey(self, fullname):
        if self.age is not None:
            if self.age < 18:
                print(f"What's up {self.get_first_name(fullname)} ?")
            elif self.age > 18:
                self.wrappe.hey(fullname)
        else:
            self.wrappe.hey(fullname)
