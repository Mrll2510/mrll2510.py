"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    Parameters:
        student_scores (list[float]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """
    nova_lista = []
    for notas in student_scores:
        nota_arredondada = round(notas)
        nova_lista.append(nota_arredondada)

    return nova_lista

print(round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]))
        

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """

    contador = 0
    for nota in student_scores:
        if nota <=40:
            contador += 1

    return contador
        
print(count_failed_students([90, 40, 55, 70, 30, 25, 80, 95, 38, 40]))

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """

    lista = []
    for notas in student_scores:
        if notas >= threshold:
            lista.append(notas)
    return lista

print(above_threshold([90,40,55,70,30,68,70,75,83,96], 75))


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    valormin = 40
    distancia = (highest - valormin)

    valor_parte = (distancia / 4)
    lista_resultados=[
       int(40 + 1),
        int(40 + 1 +(1 * valor_parte)),
        int(40 + 1 +(2 * valor_parte)),
        int(40 + 1 +(3 * valor_parte))
    
    ]
    return lista_resultados
    
print(letter_grades(100))
print(letter_grades(88))

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """
    lista_resultados = []
    for i, nome in enumerate(student_names):
        notas = student_scores[i]
        ranking = i + 1
        lista_resultados.append(f"{ranking}. {nome}: {notas}")

    return lista_resultados
print(student_ranking([100, 99, 90, 84, 66, 53, 47], ["Joci", "Sara", "Kora", "Jan", "John", "Bern", "Fred"]))

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """
    for aluno in student_info:
        if aluno[1] == 100:
            return aluno
    return []

print(perfect_score([["Charles", 90], ["Tony", 80], ["Alex", 100]]))