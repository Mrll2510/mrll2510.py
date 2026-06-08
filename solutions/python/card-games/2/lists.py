"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int):  The current round number.

    Returns:
        list: The current round number and the two that follow.
    """
    return [number, number + 1, number + 2]

print (get_rounds(27))
def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list):  The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """
    return rounds_1 + rounds_2

print(concatenate_rounds([27, 28, 29], [35, 36]))

def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds  (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """
    if number in rounds:
        return True
    else:
        return False

def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """
    soma = sum(hand)
    quantidade = len(hand)
    media = soma / quantidade
    return media

print(card_average([5, 6, 7]))

def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """
    soma = sum(hand)
    quantidade = len(hand)
    media_verdadeira = soma / quantidade

    primeira = hand[0]
    ultimo = hand[-1]
    media_extremos = (primeira + ultimo) / 2


    carta_meio = hand[len(hand)// 2]

    if media_extremos == media_verdadeira or carta_meio == media_verdadeira:
        return True
    else:
        return False

print(approx_average_is_average([1, 2, 3]))
print(approx_average_is_average([2, 3, 4, 8, 8]))
print(approx_average_is_average([1, 2, 3, 5, 9]))

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    pares = []
    impares = []

    for i in range(len(hand)):
        if i % 2 == 0:
            pares.append(hand[i])
        else:
            impares.append(hand[i])

    medias_pares = sum(pares) / len(pares)
    medias_impares = sum(impares) / len(impares)

    return medias_pares == medias_impares

print(average_even_is_average_odd([1, 2, 3]))
print(average_even_is_average_odd([1, 2, 3, 4]))

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    ultima_carta = hand[-1]

    if ultima_carta == 11:
        hand[-1] = hand[-1] * 2
        return hand
    else:
        return hand

print(maybe_double_last([5, 9, 11]))
print(maybe_double_last([5, 9, 10]))