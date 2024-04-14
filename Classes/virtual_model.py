class Data:
    def __init__(self, info: list):
        self.info = info

    def __getitem__(self, index):
        return self.info[index]


lessons = Data(["lesson0", 'lesson1', 'lesson2'])


class People:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Student(People):
    def __init__(self, name: str, age: int, knowledge: list):
        super().__init__(name, age)
        self.knowledge = knowledge

    def new_knowledge(self, info: str):
        self.knowledge.append(info)
        return self.knowledge


class Teacher(People):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    @staticmethod
    def teach(lesson_index: str, students: list[Student]):
        for item in students:
            item.new_knowledge(lesson_index)


lesson = Data(['class', 'object', 'inheritance', 'polymorphism', 'encapsulation'])
marIvanna = Teacher("maria", 40)
vasy = Student("vasy", 14, [])
pety = Student("pety", 14, [])
marIvanna.teach(lesson[2], [vasy, pety])  # учить обоих знанию lesson[2]
marIvanna.teach(lesson[0], [pety])  # учить pety знанию lesson[0]
print(vasy.knowledge)  # вывод: ['inheritance']
print(pety.knowledge)  # вывод: ['inheritance', 'class']
