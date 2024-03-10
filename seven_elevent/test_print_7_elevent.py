"""Libraly Test Cases"""
def print_7_elevent(number):
    if number ==7:
        return "Seven"
    elif number == 11:

        return "Elevent"
    elif number % 7 == 0 and number % 11 == 0:
        return "7-Elevent"
    elif number % 7 == 0:
        return "Seven"
    elif number % 11 == 0:
        return "Elevent"
    else:
        return number
    

    