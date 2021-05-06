from typing import Any, List
from .punnett import classify


def ratio(values: List[Any]):
    uniques = set(values)
    return ':'.join([values.count(v) for v in uniques])


def phenotype_ratio(children: List[str]):
    children_color = map(classify, children)
    return ratio(children_color)


def genotype_ratio(children: List[str]):
    return ratio(children)
