from platform import java_ver


class Lecture:
    def __init__(self,title,teacher,price):
        self.title =title
        self.teacher = teacher
        self.price = price
        #강의는 누가 듣는지
        self.student = []

    def info(self):
        print(f"[강의 정보] {self.title} (강사: {self.teacher})")

class Students:
    def __init__(self,name):
        self.name = name
        self.my_lecture = []

    def study(self):
        print(f"\n {self.name}님이 공부를 시작합니다")
        for lecture in self.my_lecture:
            print(f" - " '{lecture.title}' "복습중")

class CourseSystem:
    def register_course(self,student,lecture):
        print(f"\n[System] 수강 신청 처리중... (신청자: {student.name}, 강의 : {lecture.title}")


        student.my_lectures.append(lecture)

        lecture.students.append(student)

        print(" -> 등록이 완료되어습니다")

print("=== 1. 시스템 및 데이터 객체 생성 ===")

my_lms = CourseSystem()

python_lec = Lecture("파이썬 기초","코딩하는 기술사",50000)
java_lec = Lecture("자바의 정석","이자바",70000)

student1 = Students("철수")
student2 = Students("영희")




