class Lecture:
    def __init__(self,title):
        self.title = title
    def print_info(self):
        print(f" 정상호출: 이 강의는 {self.title} 입니다")

    def no_self_method():
        print("이메세지는 객체로 호출하면 볼 수 없습니다")

my_lec = Lecture("파이썬 기초")
my_lec.print_info()

# my_lec.no_self_method()

Lecture.no_self_method()