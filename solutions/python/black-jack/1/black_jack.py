"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    
    if card == "A":
        return 1 
    elif card == "J" or card == "Q" or card == "K":
        return 10
    else:
        return int(card)
        
print(value_of_card("K"))
print(value_of_card("4"))
print(value_of_card("A"))

    


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
 
    valor1 = value_of_card(card_one)
    valor2 = value_of_card(card_two)
    if valor1 > valor2:
        return card_one
    elif valor2 > valor1:
        return card_two
    else:
        return card_one, card_two
print (higher_card('K', '10'))
print (higher_card('4', '6'))
print (higher_card('K', 'A'))

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    
    if card_one == "A" or card_two == "A":
        return 1
    soma = value_of_card(card_one) + value_of_card(card_two)
    if soma + 11 <=21:
        return 11
    else:
        return 1

print (value_of_ace('6', 'K'))
print (value_of_ace('7', '3'))

    

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if card_one == 'A':
        if card_two in ["10", "K", "Q", "J"]:
            return True
    if card_two == 'A':
        if card_one in ["10","K", "Q", "J"]:
            return True
    return False

print (is_blackjack('A', 'K'))
print(is_blackjack('10', '9'))

    

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    valor1 = value_of_card(card_one)
    valor2 = value_of_card(card_two)
    if valor1 == valor2:
        return True
    else:
        return False
    


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    valor1 = value_of_card(card_one)
    valor2 = value_of_card(card_two)
    soma = valor1 + valor2
    if soma == 9 or soma == 10 or soma == 11:
        return True
    else:
        return False
