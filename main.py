from constants import DECISION_TABLE, TIME_LONG
from exam import (ExamTime, FuzzyRules, QuestionDifficulty,QuestionNumber)

questionNumber = QuestionNumber(50)
questionDifficulty = QuestionDifficulty([0.2,0.3,0.3,0.2])
fuzzyRules = FuzzyRules(DECISION_TABLE,questionNumber,questionDifficulty)

# print(questionNumber.fuzzyValues)
# print(questionDifficulty.fuzzyValues)
# for rule in fuzzyRules.rules:
#     print(rule)
# print(min(questionDifficulty.fuzzyValues['DIFFICULTY_HARD'], questionNumber.fuzzyValues['NUMBER_LARGE']))

examTime = ExamTime(fuzzyRules.rules)
print(examTime.fuzzyValues)