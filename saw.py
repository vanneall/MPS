def createMatrixWithCriteriaWeight(criteria: list, suppliers: list, matrix: list, criteriaWeight: list):
    newMatrix = list()
    for i in range(len(criteria)):
        newMatrix.append([])
        for j in range(len(suppliers)):
            newMatrix[i].append(matrix[i][j] * criteriaWeight[i])
    return newMatrix


def getRating(criteria: list, suppliers: list, matrix: list):
    res = list()
    for company in range(len(suppliers)):
        res.append(0)
        sum = 0
        for crit in range(len(criteria)):
            res[company] += matrix[crit][company]
        res[company] *= 1 / len(criteria)
    return res
