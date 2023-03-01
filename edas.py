def getAvarageScoreFromCriteria(criteriaMatrix: list):
    result = list()
    for criteria in criteriaMatrix:
        sum = 0
        for score in range(len(criteria)):
            sum += criteria[score]
        result.append(sum/len(criteria))
    return result


def getPositiveMatrix(criteriaMatrix: list, avrgScore: list, criteriaWeight: list):
    result = list()
    for criteria in range(len(criteriaMatrix)):
        result.append([])
        for company in range(len(criteriaMatrix[criteria])):
            result[criteria].append(max(0, criteriaMatrix[criteria][company] - avrgScore[criteria])/avrgScore[criteria] * criteriaWeight[criteria])
    return result


def getNegativeMatrix(criteriaMatrix: list, avrgScore: list, criteriaWeight: list):
    result = list()
    for criteria in range(len(criteriaMatrix)):
        result.append([])
        for company in range(len(criteriaMatrix[criteria])):
            result[criteria].append(max(0, avrgScore[criteria] - criteriaMatrix[criteria][company]) /avrgScore[criteria] * criteriaWeight[criteria])
    return result


def getResult(criteriaMatrix: list, avrgScore: list, criteriaWeight: list):
    positiveMatrix = getPositiveMatrix(criteriaMatrix, avrgScore, criteriaWeight)
    negativeMatrix = getNegativeMatrix(criteriaMatrix, avrgScore, criteriaWeight)
    result = [[]]
    for criteria in positiveMatrix:
        sum = 0
        for company in range(len(criteria)):
            sum += criteria[company]
        result[0].append(sum)
    result.append([])
    for criteria in negativeMatrix:
        sum = 0
        for company in range(len(criteria)):
            sum += criteria[company]
        result[1].append(sum)