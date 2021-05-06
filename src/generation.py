import random


def generate_parent():
    parent = [random.choice(['B', 'b']), random.choice(['B', 'b']),
              random.choice(['G', 'g']), random.choice(['G', 'g'])]
    return "".join(sorted(parent[0:2]) + sorted(parent[2:]))


def generate_brown():
    parent = ['B', random.choice(['B', 'b']), 'g', 'g']
    return "".join(parent)


def generate_green():
    parent = [random.choice(['B', 'b']), random.choice(['B', 'b']),
              'G', random.choice(['G', 'g'])]
    return "".join(sorted(parent[0:2]) + parent[2:])


def generate_blue():
    return 'bbgg'
