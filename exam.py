from scipy.integrate import quad
from constants import *

class QuestionNumber:
    def __init__(self, quantity):
        self.quantity = quantity
        # Calculate C(y)
        self.fuzzyValues = {
            NUMBER_LARGE: self.__calcLargeValue(),
            NUMBER_MEDIUM: self.__calcMediumValue(),
            NUMBER_FEW: self.__calcFewValue(),
            NUMBER_VERY_FEW: self.__calcVeryFewValue()
        }

    def __calcVeryFewValue(self):
        x = self.quantity
        if(10 <= x <= 30):
            return 3/2 - x/20
        return 0

    def __calcFewValue(self):
        x = self.quantity
        if(10 <= x <= 30):
            return x/20 - 1/2
        if(30 <= x <= 40):
            return 4 - x/10
        return 0

    def __calcMediumValue(self):
        x = self.quantity
        if(30 <= x <= 40):
            return x/10 - 3
        if(40 <= x <= 50):
            return 5 - x/10
        return 0

    def __calcLargeValue(self):
        x = self.quantity
        if(40 <= x <= 60):
            return x/20 - 2
        return 0


class QuestionDifficulty:
    def __init__(self, distributions):
        self.fuzzyValues = {
            DIFFICULTY_HARD: distributions[0],
            DIFFICULTY_MEDIUM: distributions[1],
            DIFFICULTY_EASY: distributions[2],
            DIFFICULTY_VERY_EASY: distributions[3],
        }

class TimeIntegral:
    def __init__(self):
        self.numerators = {
            TIME_LONG: quad(self.__memberFunction, 45, 75, args=(TIME_LONG, None, NUMERATOR))[0],
            TIME_MEDIUM: quad(self.__memberFunction, 45, 60, args=(TIME_MEDIUM, UPPER_BOUND, NUMERATOR))[0] +
                         quad(self.__memberFunction, 30, 45, args=(TIME_MEDIUM, LOWER_BOUND, NUMERATOR))[0],
            TIME_SHORT: quad(self.__memberFunction, 30, 40, args=(TIME_SHORT, UPPER_BOUND, NUMERATOR))[0] +
                        quad(self.__memberFunction, 15, 30, args=(TIME_SHORT, LOWER_BOUND, NUMERATOR))[0],
            TIME_VERY_SHORT: quad(self.__memberFunction, 5, 20, args=(TIME_VERY_SHORT, None, NUMERATOR))[0]
        }
        self.denominators = {
            TIME_LONG: quad(self.__memberFunction, 45, 75, args=(TIME_LONG, None, DENOMINATOR))[0],
            TIME_MEDIUM: quad(self.__memberFunction, 45, 60, args=(TIME_MEDIUM, UPPER_BOUND, DENOMINATOR))[0] +
                         quad(self.__memberFunction, 30, 45, args=(TIME_MEDIUM, LOWER_BOUND, DENOMINATOR))[0],
            TIME_SHORT: quad(self.__memberFunction, 30, 40, args=(TIME_SHORT, UPPER_BOUND, DENOMINATOR))[0] +
                        quad(self.__memberFunction, 15, 30, args=(TIME_SHORT, LOWER_BOUND, DENOMINATOR))[0],
            TIME_VERY_SHORT: quad(self.__memberFunction, 5, 20, args=(TIME_VERY_SHORT, None, DENOMINATOR))[0]
        }
        # print(self.numerators)
        # print(self.denominators)

    def __memberFunction(self, x, timeType, bound, valueType):
        y = 0
        if(timeType == TIME_VERY_SHORT):
            y = 4/3 - x/15
        if(timeType == TIME_SHORT):
            if(bound == LOWER_BOUND):
                y = x/15 - 1
            if(bound == UPPER_BOUND):
                y = 4 - x/10
        if(timeType == TIME_MEDIUM):
            if(bound == LOWER_BOUND):
                y = x/15 - 2
            if(bound == UPPER_BOUND):
                y = 4 - x/15
        if(timeType == TIME_LONG):
            y = x/30 - 3/2
        return y if valueType == DENOMINATOR else y*x


class ExamTime:

    def __init__(self, decisionTable, questionNumber, questionDifficulty):
        self.weights = self.__weightCalculate(
            decisionTable, questionNumber, questionDifficulty)

    def __weightCalculate(self, decisionTable, questionNumber, questionDifficulty):
        weightsTable = []
        for key in decisionTable:
            for element in decisionTable[key]:
                questiondifficultyType = element[0]
                questionNumberType = element[1]
                weight = min(
                    questionDifficulty.fuzzyValues[questiondifficultyType], questionNumber.fuzzyValues[questionNumberType])
                weightsTable.append({
                    'examTimeType': key,
                    'questiondifficultyType': questiondifficultyType,
                    'questionNumberType': questionNumberType,
                    'weight': weight
                })
        weights = { TIME_LONG: 0, TIME_MEDIUM: 0, TIME_SHORT: 0, TIME_VERY_SHORT: 0 }
        for w in weightsTable:
            weights[w['examTimeType']] += w['weight']

        return weights

    def defuzzy(self):
        timeValues = TimeIntegral()
        a = b = 0
        for timeType, w in self.weights.items():
            a += timeValues.numerators[timeType] * w
            b += timeValues.denominators[timeType] * w
        return a/b
