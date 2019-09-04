class ScoreManager:
    def __init__(self):
        self.student=0
        self.score=[]
    def add_score(self,s):
        self.score.append(s)
        self.student+=1
        return self.student
    def __ave__(self):
        return sum(self.score)/self.student


sm=ScoreManager()

print("학생성적관리 프로그램이 시작되었습니다.")
while True:
    menu=int(input("메뉴를 입력하시오."))
    if menu==1:
        while True:
            number=int(input("성적을 입력하세요. 종료하려면 -1을 입력하세요."))
            sm.add_score(number)
            if number==-1:
                break
    if menu==2:
        print("평균점수는",sm.__ave__() ,"점 입니다.")
    if menu==3:
        print("학생수는",sm.add_score(number),"명 입니다.")

'''
class ScoreManager:
    def __init__(self):
        self.scores=0
        self.students=0
    def add_score(self,s):
        self.scores+=s
        self.students+=1
        return self.students,self.scores
    def ave_score(self):
        return self.scores/self.students
    def get_students(self):
        return self.students
grade=ScoreManager()

print('학생성적관리 프로그램이 시작되었습니다.')
while True:
    menu=int(input('메뉴를 입력하시오:'))
    if menu==1:
        while True:
            score=int(input('성적을 입력하세요. 종료하려면 -1을 입력하세요:'))
            if score==-1:
                break
            grade.add_score(score)
    if menu==2:
        print('평균점수는 %f점입니다.'%grade.ave_score())
    if menu==3:
        print('학생수는 %d명 입니다.'%grade.get_students())
'''