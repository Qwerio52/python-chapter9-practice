# 9.4 学校成员管理
class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(SchoolMember):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name}（{self.age}岁）讲授 {self.subject}")


class Student(SchoolMember):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self):
        print(f"{self.name}（{self.age}岁）学习，年级：{self.grade}")


if __name__ == "__main__":
    t = Teacher("李老师", 35, "Python")
    t.teach()
    s = Student("小红", 18, "大二")
    s.study()