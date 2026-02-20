class Student:
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa

std = Student("철수",4.0)
print(f"변경 전 : {std.name}, 학점 : {std.gpa}")

std.gpa =9.999

print(f"변경 후 : {std.name}, 학점 : {std.gpa}")


class Student:
    def __init__(self,name,gpa):
        self.__name = name
        self.__gpa = gpa
    @property
    def name(self):
        return self.__name
    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self,value):
        if value < 0.0 or value > 4.5:
            print(f"오류 : 학점은 0.0 ~ 4.5 사이여야 합니다. 입력값 {value}")
            return
        self.__gpa = value
        print(f"학점이 {value}로 안전하게 수정되었습니다")
    @name.setter
    def name(self,value):
         self.__name = value
        

std = Student("영희" , 3.5)

print(f"학생 이름: {std.name}")
print(f"학생 성적: {std.gpa}")

std.gpa = 4.0
print(f"학생 성적: {std.gpa} ")

std.name ="동욱"
print(std.name)