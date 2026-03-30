import random
import string
import time

from .main import solve

def generate():
    k = int(input())
    string_length = int(input())

    alphabet = {}
    a = set()
    b = set()
    while len(alphabet) < k:
        alphabet[random.choice(string.ascii_lowercase)] = random.randint(1, 25)

    while len(a) < string_length:
        a.add(random.choice(list(alphabet.keys())))
    while len(b) < string_length:
        b.add(random.choice(list(alphabet.keys())))

    a = list(a)
    b = list(b)

    random.shuffle(a)
    random.shuffle(b)

    a = "".join(a)
    b = "".join(b)

    print(alphabet)
    print(a)
    print(b)

    value, subseq = solve(k, alphabet, a, b)
    print(value)
    print(subseq)

    with open(f"./examples/example_k{k}_l{string_length}_{time.time()}.in", "w") as f:
        f.write(f"{k}\n")
        for char, value in alphabet.items():
            f.write(f"{char} {value}\n")
        f.write(f"{a}\n")
        f.write(f"{b}\n")

if __name__ == "__main__":
    generate()