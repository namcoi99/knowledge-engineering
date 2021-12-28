from constants import DECISION_TABLE, DIFFICULTY_HARD, DIFFICULTY_MEDIUM, DIFFICULTY_EASY, DIFFICULTY_VERY_EASY
from exam import (ExamTime, QuestionDifficulty, QuestionNumber)

q = 0
while q < 10 or q > 60: q = int(input("Please enter the number of questions[10-60]: "))
questionNumber = QuestionNumber(q)      # Ex: 50

lst = []
print("\nPlease enter the number of questions of the question level: ")
lst.append(int(input("{} (Example: 20): ".format(DIFFICULTY_HARD)))/q)
lst.append(int(input("{} (Example: 20): ".format(DIFFICULTY_MEDIUM)))/q)
lst.append(int(input("{} (Example: 20): ".format(DIFFICULTY_EASY)))/q)
lst.append(int(input("{} (Example: 20): ".format(DIFFICULTY_VERY_EASY)))/q)
print("\n--------------------------------------------------------")
print("The distribution of difficulty (K) is as follows: {}".format(lst))       # Ex: [0.2, 0.3, 0.3, 0.2]
questionDifficulty = QuestionDifficulty(lst)

examTime = ExamTime(DECISION_TABLE, questionNumber, questionDifficulty)

print("\nMembership function for Exam time:")
print("Uc(z) = ", end='')
for (k, v) in examTime.weights.items():
    if v > 0: print("{}*{}".format(v, k), end=' + ')

print("\n--------------------------------------------------------")
print("Result: The appropriate test time is about {} minutes.".format(round(examTime.defuzzy(), 2)))

