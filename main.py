import edas
import saw
import topsis

company = ["Spotify", "Яндекс.музыка", "ВК музыка", "Зайцев.Нет", "Deezer", "SoundCloud", "Apple Music"]
criteria = ["Совместимость", "Юзабилити", "Надежность", "Защищенность", "Сопровождаемость", "Мобильность", "Стоимость"]

matrix = [
    [0.8, 0.7, 0.6, 0.6, 0.8, 0.9, 0.6],  # Совместимость
    [0.93, 0.8, 0.78, 0.6, 0.88, 0.85, 0.7],  # Юзабилити
    [0.9, 0.8, 0.8, 0.4, 0.6, 0.8, 0.6],  # Надежность
    [0.8, 0.69, 0.73, 0.4, 0.75, 0.8, 0.76],  # Защищенность
    [0.98, 0.89, 0.76, 0.64, 0.76, 0.78, 0.6],  # Сопровождаемость
    [0.9, 0.9, 0.7, 0.7, 0.9, 0.9, 0.5],  # Мобильность
    [0.169, 0.299, 0.159, 0.169, 0.169, 0.369, 0.169]  # Стоимость для SAW и TOPSIS не менять, для EDAS вычитать из 1
]

weight_matrix = [0.1, 0.2, 0.1, 0.2, 0.1, 0.1, 0.2]

print(company)
#SAW
matrix_with_criteria_weight = saw.createMatrixWithCriteriaWeight(criteria, company, matrix, weight_matrix)
print(saw.getRating(matrix_with_criteria_weight, company, matrix))

#TOPSIS
matrix_with_criteria_weight = topsis.createMatrixWithCriteriaWeight(criteria, company, matrix, weight_matrix)
distance = topsis.findPositiveAndNegativeDecision(matrix_with_criteria_weight, criteria)
pos, neg = topsis.findPositiveAndNegativeDecision(matrix_with_criteria_weight, criteria)
print(topsis.getResult(pos, neg))

#EDAS
avg = edas.getAvarageScoreFromCriteria(matrix)
print(edas.getResult(matrix, avg, weight_matrix))
