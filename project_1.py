pointsPossible = 100
def calcTheGrade():
    actualScore = 100 * float(score) / float(pointsPossible)
    if actualScore >= 90:
        grade = 'A'
    elif actualScore >= 80:
        grade = 'B'
    elif actualScore >= 70:
        grade = 'C'
    elif actualScore >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print(f'{studentName} has a grade of {grade} with score {str(actualScore)}%.')

studentName = input('Enter student name: ')
try:
    score = float(input('Enter your score: '))
    if type(score) != float:
        print('Invalid score. Please enter a number.')
        score = float(input('Enter your score: '))
except ValueError: 
    print('Invalid score. Please enter a number.')
    score = float(input('Enter your score: '))
try:
    if score < 0 or score > pointsPossible:
        print('Invalid score. Please enter a score between 0 and 100.')
        score = float(input('Enter your score: '))
except ValueError: 
    print('Invalid score. Please enter a number.')
    score = float(input('Enter your score: '))
calcTheGrade()

