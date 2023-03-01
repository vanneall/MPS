import topsis
import saw
import edas


criteria = ["Совместимость", "Юзабилити", "Надежность", "Защищенность", "Сопровождаемость", "Мобильность", "Стоимость"]

criteriaWeight = [0.1, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2]

suppliers = ["Spotify", "Яндекс музыка", "ВК музыка", "Зайцев.нет", "Deezer", "SoundCloud", "Apple Music"]

matrix = [
    [0.8, 0.7, 0.6, 0.6, 0.8, 0.9, 0.6],  # Совместимость
    [0.93, 0.8, 0.78, 0.6, 0.88, 0.85, 0.7],  # Юзабилити
    [0.9, 0.8, 0.8, 0.4, 0.6, 0.8, 0.6],  # Надежность
    [0.8, 0.69, 0.73, 0.4, 0.75, 0.8, 0.76],  # Защищенность
    [0.98, 0.89, 0.76, 0.64, 0.76, 0.78, 0.6],  # Сопровождаемость
    [0.9, 0.9, 0.7, 0.7, 0.9, 0.9, 0.5],  # Мобильность
    [0.169, 0.5, 0.159, 0.169, 0.169, 0.169, 0.169]  # Стоимость
]

choice = int(input("1. TOPSIS\n2. SAW\n3. EDAS\n>>> "))
if choice == 1:
    matrixWithCriteriaWeight = topsis.createMatrixWithCriteriaWeight(criteria, suppliers, matrix, criteriaWeight)
    positive, negative = topsis.findPositiveAndNegativeDecision(matrixWithCriteriaWeight, criteria)
    plus, minus = topsis.findDistance(positive, negative, matrixWithCriteriaWeight, suppliers, criteria)
    P = topsis.getResult(plus, minus)
    for i in suppliers:
        print(i, end=" | ")
    print()
    for i in P:
        print(f'{i:.5}', end=" | ")
elif choice == 2:
    matrixWithCriteriaWeight = saw.createMatrixWithCriteriaWeight(criteria, suppliers, matrix, criteriaWeight)
    P = saw.getRating(criteria, suppliers, matrixWithCriteriaWeight)
    for i in suppliers:
        print(i, end=" | ")
    print()
    for i in P:
        print(f'{i:.5}', end=" | ")
elif choice == 3:
    avrgScore = edas.getAvarageScoreFromCriteria(matrix)
    newMatrix = edas.getPositiveMatrix(matrix, avrgScore, criteriaWeight)
    for i in newMatrix:
        for j in i:
            print(j, end=" ")
        print()