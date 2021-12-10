from constants import *


class QuestionNumber:
    def __init__(self, quantity):
        self.quantity = quantity
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


class ExamTime:
    def __init__(self, rules):
        self.fuzzyValues = {
            TIME_LONG: 0,
            TIME_MEDIUM: 0,
            TIME_SHORT: 0,
            TIME_VERY_SHORT: 0
        }
        for rule in rules:
            self.fuzzyValues[rule['examTimeType']] += rule['weight']

    def memberFunction(self, x, ranges):
        if(self.type == TIME_VERY_SHORT):
            if(ranges == [5, 20]):
                return 4/3 - x/15
        if(self.type == TIME_SHORT):
            if(ranges == [15, 30]):
                return x/15 - 1
            if(ranges == [30, 40]):
                return 4 - x/10
        if(self.type == TIME_MEDIUM):
            if(ranges == [30, 45]):
                return x/15 - 2
            if(ranges == [45, 60]):
                return 4 - x/15
        if(self.type == TIME_LONG):
            if(ranges == [45, 75]):
                return x/30 - 3/2
        return "Type or ranges not allowed"


class FuzzyRules:
    def __init__(self, decisionTable, questionNumber, questionDifficulty):
        self.rules = self.__setRules(
            decisionTable, questionNumber, questionDifficulty)

    def __setRules(self, decisionTable, questionNumber, questionDifficulty):
        rules = []
        for key in decisionTable:
            for element in decisionTable[key]:
                questiondifficultyType = element[0]
                questionNumberType = element[1]
                weight = min(
                    questionDifficulty.fuzzyValues[questiondifficultyType], questionNumber.fuzzyValues[questionNumberType])
                rules.append({
                    'examTimeType': key,
                    'questiondifficultyType': questiondifficultyType,
                    'questionNumberType': questionNumberType,
                    'weight': weight
                })
        return rules
