from typing import List
from punnett import classify


def ratio(values: List[str]):
    uniques = set(values)
    counts = [values.count(v) for v in uniques]
    return ':'.join(map(str, counts))


def phenotype_ratio(children: List[str]):
    children_color = list(map(classify, children))
    return ratio(children_color)


def genotype_ratio(children: List[str]):
    return ratio(children)
