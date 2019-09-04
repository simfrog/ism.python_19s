class Dog:
    def ear(self):
        return '귀를 쫑긋한다.'
    def mouth(self):
        return '멍멍 짖는다.'
    def foot(self):
        return '뒹군다.'
d=Dog()
move=input("입력:")
if move=="ears":
    d.ear()
if move=="mouth":
    d.mouth()
if move=="foot":
    d.foot()