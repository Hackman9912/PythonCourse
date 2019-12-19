class Person:
    def __init__(self, name, diet):
        self.__name = name
        self.__diet = diet

    def set_name(self, name):
        self.__name = name

    def set_diet(self, diet):
        self.__diet = diet

    def get_name(self):
        return self.__name

    def get_diet(self):
        return self.__diet

class Student(Person):
    def __init__(self, name, diet, rank):
        super().__init__(name, diet)
        self.__rank = rank

class Instructor(Person):
    def __init__(self, name, diet, ins_type):
        super().__init__(name, diet)
        self.__ins_type = ins_type