"""Test cases for 7-elevent"""

import pytest

#from seven-elevent.seven from print_7_elevent.

def test_print_7_elevent():
    """Test Cases"""
    """Project Libraly"""
from seven_elevent.test_print_7_elevent import print_7_elevent
@pytest.mark.parametrize(
        "number,expected",
        [
            (1,1),
            (2,2),
            (3,3),
            (4,4),
            (5,5),
            (6,6),
            (7,"Seven"),
            (8,8),
            (9,9),
            (10,10),
            (11,"Elevent"),
            (12,12),
            (13,13),
            (14,"Seven"),
            (21,"Seven"),
            (22,"Elevent"),
            (77,"7-Elevent"),
            (78,78),
            (154,"7-Elevent"),
            


        ]
)

def test_print_7_elevent(number,expected):
    """print 7-Elevent"""

    #Act
    result = print_7_elevent(number)

    #Assert
    assert result == expected