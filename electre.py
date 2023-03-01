def createSetOfSuperiority(matrix: list, supplierCount: int):
    setOfCriteria = list()
    for i in range(supplierCount):
        setOfCriteria.append(createMatrixOfCriteria(i, matrix))
    return setOfCriteria


def createMatrixOfCriteria(originalSupplierIndex: int, allSuppliersCriteria: list):
    res = list()
    for crit in range(len(allSuppliersCriteria)):
        res.append([])
        for company in range(len(allSuppliersCriteria[crit])):
            if company == originalSupplierIndex:
                continue
            elif allSuppliersCriteria[crit][originalSupplierIndex] > allSuppliersCriteria[crit][company]:
                res[crit].append(1)
            elif allSuppliersCriteria[crit][originalSupplierIndex] < allSuppliersCriteria[crit][company]:
                res[crit].append(-1)
            else:
                res[crit].append(0)
    return res


def createSumOfWeightsOfCriteria(matrix: list, supplier: list, criteriaWeight: list):
    positiveSet = list()
    negativeSet = list()
    equalSet = list()
    for i in range(len(supplier)):
        positiveSet.append(createMatrixOfTheWeightsOfCriteria(matrix, criteriaWeight, 1, i))
        negativeSet.append(createMatrixOfTheWeightsOfCriteria(matrix, criteriaWeight, -1, i))
        equalSet.append(createMatrixOfTheWeightsOfCriteria(matrix, criteriaWeight, 0, i))
    return positiveSet, negativeSet, equalSet


def createMatrixOfTheWeightsOfCriteria(matrix: list, criteria: list, typeMatrix: int, supplierIndex: int):
    set = list()
    if typeMatrix == 1:
        for i in range(len(matrix[supplierIndex])):
            sum = 0
            for j in range(len(matrix[supplierIndex][i])):
                if matrix[supplierIndex][i][j] == 1:
                    sum += criteria[j]
            set.append(sum)
    elif typeMatrix == -1:
        for i in range(len(matrix[supplierIndex])):
            sum = 0
            for j in range(len(matrix[supplierIndex][i])):
                if matrix[supplierIndex][i][j] == -1:
                    sum += criteria[j]
            set.append(sum)
    else:
        for i in range(len(matrix[supplierIndex])):
            sum = 0
            for j in range(len(matrix[supplierIndex][i])):
                if matrix[supplierIndex][i][j] == 0:
                    sum += criteria[j]
            set.append(sum)
    return set