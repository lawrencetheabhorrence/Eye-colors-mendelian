import sys
from typing import Callable


def input_parameter(prompt: str, valid_values: list[str]):
    while True:
        answer = input(prompt)
        if answer in valid_values:
            return answer
        if answer == "-1":
            sys.exit()


def input_value(prompt: str, pred: Callable[[int], bool]):
    while True:
        answer = int(input(prompt))
        if pred(answer):
            return answer
        if answer == -1:
            sys.exit()


def input():
    choices = {'T': True, 'F': False}
    colors = ['Brown', 'Green', 'Blue']
    print('Enter -1 to exit')

    children = input_value('Number of children to generate: ',
                           (lambda x: x > 0))
    parent1 = input_parameter('Eye color of parent 1 (Brown/Green/Blue): ',
                              colors)
    parent2 = input_parameter('Eye color of parent 2 (Brown/Green/Blue): ',
                              colors)
    show_g_ratio = input_parameter('Show genotype ratio (T/F)? ',
                                   list(choices))
    show_p_ratio = input_parameter('Show phenotype ratio (T/F)? ',
                                   list(choices))

    return (children, parent1, parent2,
            choices[show_g_ratio], choices[show_p_ratio])
