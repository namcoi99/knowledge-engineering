from constants import DECISION_TABLE, TIME_LONG
from exam import (ExamTime, QuestionDifficulty, QuestionNumber)

questionNumber = QuestionNumber(50)
questionDifficulty = QuestionDifficulty([0.2, 0.3, 0.3, 0.2])
examTime = ExamTime(DECISION_TABLE, questionNumber, questionDifficulty)

print(examTime.defuzzy())


