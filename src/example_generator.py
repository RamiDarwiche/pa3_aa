import random
import string
import time

def generate():
    k = int(input("Enter the number of characters in the alphabet(k: k <= 26): "))
    if k > 26:
        print("Error: k must be less than or equal to 26")
        return
    string_a_length = int(input("Enter the length of string A: "))
    string_b_length = int(input("Enter the length of string B: "))

    alphabet = {}
    a = []
    b = []
    while len(alphabet) < k:
        alphabet[random.choice(string.ascii_lowercase)] = random.randint(1, 25)

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

    with open(f"./examples/example_k{k}_a{string_a_length}_b{string_b_length}_{time.time()}.in", "w") as f:
        f.write(f"{k}\n")
        for char, value in alphabet.items():
            f.write(f"{char} {value}\n")
        f.write(f"{a}\n")
        f.write(f"{b}\n")

    print(f"Example generated and saved to ./examples/example_k{k}_a{string_a_length}_b{string_b_length}_{time.time()}.in")

if __name__ == "__main__":
    generate()