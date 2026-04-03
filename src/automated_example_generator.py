from main import *
import random
import string
import time
from pathlib import Path


def generate_n_examples(n : int, k : int, min_len : int, max_len : int, maxWeight):
    """
    n: number of examples to generate
    k: size of alphabet, cannot be larger than 26
    min_len : minimum length of string to be used
    max_len : maximum length of string to be used
    maxWeight : maximum weight assigned to any one letter in the examples

    """

    if k > 26:
        print("Error: k must be less than or equal to 26")
        return
    

    #remove existing files in example directory to prevent naming conflicts
    dir = Path("./examples")
    for file in dir.iterdir():
        if file.is_file():
            file.unlink()
    

    for i in range(n):

        string_a_length = random.randint(min_len, max_len)
        string_b_length = random.randint(min_len, max_len)

        alphabet = {}
        a = []
        b = []

        while len(alphabet) < k:
            if alphabet[random.choice(string.ascii_lowercase)] not in alphabet:
                alphabet[random.choice(string.ascii_lowercase)] = random.randint(1, maxWeight)

        while len(a) < string_a_length:
            a.append(random.choice(list(alphabet.keys())))
        while len(b) < string_b_length:
            b.append(random.choice(list(alphabet.keys())))

        random.shuffle(a)
        random.shuffle(b)

        a = "".join(a)
        b = "".join(b)

        print(alphabet)
        print(a)
        print(b)


        #i indicates the example number to indicate the order in which they were generated
        with open(f"./examples/example_n{i}_k{k}_a{string_a_length}_b{string_b_length}_{time.time()}.in", "w") as f:
            f.write(f"{k}\n")
            for char, value in alphabet.items():
                f.write(f"{char} {value}\n")
            f.write(f"{a}\n")
            f.write(f"{b}\n")

        


        



