import random
from generation import generate_blue, generate_brown, \
                       generate_green, generate_parent


def punnett_pairs(parent: str):
    return [b + g for b in parent[0:2]
            for g in parent[2:]]


def crossover(pair1: str, pair2: str):
    return "".join(sorted(pair1[0] + pair2[0]) + sorted(pair1[1] + pair2[1]))


def classify(chromosome: str):
    if 'B' in chromosome:
        return "Brown"
    if 'G' in chromosome:
        return "Green"

    return "Blue"


def generate_by_color(color: str):
    if color == "Green":
        return generate_green()
    if color == "Brown":
        return generate_brown()
    if color == "Blue":
        return generate_blue
    return generate_parent()


def simulate(children: int, color1: str, color2: str):
    parent1 = generate_by_color(color1)
    parent2 = generate_by_color(color2)
    print(f"Parent 1 has {classify(parent1)} eyes: {parent1}")
    print(f"Parent 2 has {classify(parent2)} eyes: {parent2}")
    punnett_pairs1 = punnett_pairs(parent1)
    punnett_pairs2 = punnett_pairs(parent2)

    children = [crossover(random.choice(punnett_pairs1),
                          random.choice(punnett_pairs2))
                for _ in range(0, children)]

    for i, child in enumerate(children):
        print(f"Child {i+1} has {classify(child)} eyes: {child}")

    return children
