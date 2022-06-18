from parent_interface import ParentInterface


class ParentClass(ParentInterface):
    def get_first_name(self, fullname):
        return fullname.split(" ")[0]

    def hey(self, fullname):
        print(f"Hello {self.get_first_name(fullname)}")
