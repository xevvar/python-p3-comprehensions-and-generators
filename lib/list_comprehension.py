#!/usr/bin/env python3

def return_evens(num_list):
    pass
    even_numbers = [num for num in num_list if (num % 2 == 0)]
    return even_numbers


def make_exclamation(sentence_list):
    pass
    new_sentence = [sentence + '!' for sentence in sentence_list]
    return new_sentence