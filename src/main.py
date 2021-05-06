import sys
from typing import Callable
from .punnett import simulate
from .gene_stats import phenotype_ratio, genotype_ratio


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


def main_input():
    choices = {'T': True, 'F': False}
    colors = ['Brown', 'Green', 'Blue', 'Any']
    print('Enter -1 to exit')

    no_of_children = input_value('Number of children to generate: ',
                                 (lambda x: x > 0))
    parent1 = input_parameter('Eye color of parent 1 (Brown/Green/Blue/Any): ',
                              colors)
    parent2 = input_parameter('Eye color of parent 2 (Brown/Green/Blue/Any): ',
                              colors)
    show_g_ratio = input_parameter('Show genotype ratio (T/F)? ',
                                   list(choices))
    show_p_ratio = input_parameter('Show phenotype ratio (T/F)? ',
                                   list(choices))

    return (no_of_children, parent1, parent2,
            choices[show_g_ratio], choices[show_p_ratio])


def main():
    no_of_children, p1, p2, show_gr, show_pr = main_input()
    children = simulate(no_of_children, p1, p2)
    if (show_gr):
        print(genotype_ratio(children))
    if (show_pr):
        print(phenotype_ratio(children))
