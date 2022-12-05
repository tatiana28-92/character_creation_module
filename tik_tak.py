class Human:
    def __init__(self, name):
        self.name = name
    def answer_question(self, question):
        self.question = question
        print ('Очень интересный вопрос! Не знаю.')

class Student(Human):   
    def ask_question(self, someone, question: str): 
        print(f'{someone.name}, {question}')
        someone.answer_question(question)
        print()       
        if someone == 'Марина': # запросите ответ на вопрос у someone
            Curator.answer_question(question)
        elif someone == 'Ира':
            Mentor.answer_question(question)
        elif someone == 'Евгений':
            CodeReviewer.answer_question(question)
        elif someone == 'Виталя':
            Human.answer_question(question)
        else:
            super().answer_question(question)

class Curator(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print ('Держись, всё получится. Хочешь видео с котиками?')      
        else:
            return super().answer_question(question)

class CodeReviewer(Human): # объявите и реализуйте классы CodeReviewer и Mentor
    def answer_question(self, question):
        if question == 'что не так с моим проектом?':
            print ('О, вопрос про проект, это я люблю.')
        elif question == 'когда каникулы?':
            return super().answer_question(question)
        else:
            return super().answer_question(question)      
        
class Mentor(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print ('Отдохни и возвращайся с вопросами по теории.')       
        elif question == 'как устроиться на работу питонистом?':
            print ('Сейчас расскажу.')
        else:
            return super().answer_question(question)
        
# следующий код менять не нужно, он работает, мы проверяли
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')