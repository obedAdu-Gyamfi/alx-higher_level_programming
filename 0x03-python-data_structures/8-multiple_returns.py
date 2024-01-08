#!/usr/bin/python3
# -----------------------------
# Function returns a tuple with the length of a string
# and its first character.
# @Obed Adu-Gyamfi
# ----------------------------

def multiple_returns(sentence):
    """ Function returns a tuple with the length of a
        string and its first character.

    Args:
        sentence

    Return:
         a tuple with the length of a string and the first char
    """
    if len(sentence) <= 0:
        return (None)
    else:
        tp = tuple(sentence)
        length = len(sentence)
        first = tp[0]

    return (length, first)
