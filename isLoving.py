class Person:
    def __init__(self, name, sex, age, attractiveness, personality, residence):
        self.name = name
        self.sex = sex
        self.age = age
        self.attractiveness = attractiveness
        self.personality = personality
        self.residence = residence

    def isMarried(self):
        return self.age >= 40 and self.attractiveness >= 50

    def isHot(self):
        return self.attractiveness >= 70

    def isSafe(self):
        if self.personality == 'violent':
            return False
        return self.personality in ['Cute', 'Nice']

    def isNear(self):
        return self.residence in ['경기', '서울', '창원']

    @staticmethod
    def isloving(person1, person2):
        yes = 0

        if abs(person1.age - person2.age) <= 7:
            yes += 1
        if person1.sex != person2.sex:
            yes += 1
        if person1.isMarried() or person2.isMarried():
            return False
        if person2.isHot():
            yes += 1
        if person1.isNear() and person2.isNear():
            yes += 1
        if not person2.isHot() or not person2.isSafe():
            return False

        return yes >= 3  

JW = Person('KimJaewoo', 'male', 24, 100, 'Nice', '경기')
YR = Person('HongYerim', 'female', 24, 80, 'Cute', '경기')

if Person.isloving(JW, YR) and Person.isloving(YR, JW):
    print(YR.name, "and", JW.name, "love each other!")
    print("They are in Love.")
else:
    print(YR.name, "and", JW.name, "are not in love.")
