import random


def generate_parent():
    parent = [random.choice(['B', 'b']), random.choice(['B', 'b']),
              random.choice(['G', 'g']), random.choice(['G', 'g'])]
    return "".join(sorted(parent[0:2]) + sorted(parent[2:]))


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


def simulate(children: int):
    parent1, parent2 = generate_parent(), generate_parent()
    print(f"Parent 1 has {classify(parent1)} eyes: {parent1}")
    print(f"Parent 2 has {classify(parent2)} eyes: {parent2}")
    punnett_pairs1 = punnett_pairs(parent1)
    punnett_pairs2 = punnett_pairs(parent2)

    for i in range(1, children + 1):
        child = crossover(random.choice(punnett_pairs1),
                          random.choice(punnett_pairs2))
        print(f"Child {i} has {classify(child)} eyes: {child}")


def main():
    while(True):
        children = int(input("Number of children to generate (any nonpositive number/input to exit) : "))
        if not children > 0: break
        simulate(children)


main()
