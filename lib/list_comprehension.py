#!/usr/bin/env python3

def return_evens(num_list):
    even_nos = [num for num in num_list if num % 2 == 0]
    return even_nos
    pass


def make_exclamation(sentences):
    return [sentence + "!" for sentence in sentences]
