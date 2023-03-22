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
    for company in range(len(positiveMatrix[0])):
        sum = 0
        for criteria in range(len(positiveMatrix)):
            sum += positiveMatrix[criteria][company]
        result[0].append(sum)
    result.append([])

    for company in range(len(negativeMatrix[0])):
        sum = 0
        for criteria in range(len(negativeMatrix)):
            sum += negativeMatrix[criteria][company]
        result[1].append(sum)

    result.append([])
    for i in result[0]:
        result[2].append(i/max(result[0]))

    result.append([])
    for i in result[1]:
        result[3].append(1 - i / max(result[1]))

    result.append([])
    for i in range(len(result[2])):
        result[4].append(0.5 * (result[2][i] + result[3][i]))
    return result[4]
