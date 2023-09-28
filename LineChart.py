import matplotlib.pyplot as plt 

student_details = [
    {'name': 'John', 'maths': 80, 'science': 70},
    {'name': 'Sarah', 'maths': 90, 'science': 65}, 
    {'name': 'David', 'maths': 75, 'science': 80},
    {'name': 'Anna', 'maths': 85, 'science': 75}
]

math_scores = []
science_scores = []

for detail in student_details:
    math_scores.append(detail['maths'])
    science_scores.append(detail['science'])

plt.plot(math_scores, label='Math Scores')
plt.plot(science_scores, label='Science Scores')

plt.title('Student Subject Scores')  
plt.xlabel('Students')
plt.ylabel('Scores')

plt.legend()

plt.show()