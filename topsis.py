def createMatrixWithCriteriaWeight(criteria: list, suppliers: list, matrix: list, criteriaWeight: list):
    newMatrix = list()
    for i in range(len(criteria)):
        newMatrix.append([])
        for j in range(len(suppliers)):
            newMatrix[i].append(matrix[i][j] * criteriaWeight[i])
    return newMatrix


def findPositiveAndNegativeDecision(matrixWithCriteriaWeight: list, criteria: list):
    positiveList = list()
    negativeList = list()

    for i in range(len(criteria)):
        positiveList.append(max(matrixWithCriteriaWeight[i]))
        negativeList.append(min(matrixWithCriteriaWeight[i]))
    return positiveList, negativeList


def findDistance(positive: list, negative: list, matrix: list, suppliers: list, criteria: list):
    Splus = list()
    Sminus = list()
    for criter in range(len(suppliers)):
        Splus.append(0)
        Sminus.append(0)
    for criter in range(len(criteria)):
        for company in range(len(suppliers)):
            Splus[company] += (positive[criter] - matrix[criter][company]) ** 2
            Sminus[company] += (negative[criter] - matrix[criter][company]) ** 2
    for criter in range(len(Splus)):
        Splus[criter] **= 0.5
        Sminus[criter] **= 0.5
    return Splus, Sminus


def getResult(plus: list, minus: list):
    P = list()
    for i in range(len(plus)):
        P.append(minus[i]/(plus[i] + minus[i]))
    return P