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
    dir = Path("../examples")
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


        #i indicates the example number to indicate the order in which they were generated
        with open(f"../examples/example_n{i}_k{k}_a{string_a_length}_b{string_b_length}_{time.time()}.in", "w") as f:
            f.write(f"{k}\n")
            for char, value in alphabet.items():
                f.write(f"{char} {value}\n")
            f.write(f"{a}\n")
            f.write(f"{b}\n")

        
if __name__ == "__main__":
    custom_args = input("Would you like to use custom arguments? (y/n)")

    if custom_args.lower() == 'y':
        n = int(input("Enter the number of examples you'd like to generate"))
        while True:
            k = int(input("Enter the number of chars in desired alpahbet"))
            if k <= 26:
                break

            print("Invalid input, k must be less than 26")
        
        min_len  = int(input("Enter the minimum length of a string for comparison"))
        max_len =  int(input("Enter the maximum length of a string for comparison"))    

        maxWeight = int(input("Enter the maximum weight you want assigned to any given char in alphabet"))

    else: 
        n = 10
        k = random.randint(3,10)
        min_len = 25
        max_len = 50
        maxWeight = 15

    
    generate_n_examples(n = n, 
                        k = k, 
                        min_len= min_len, 
                        max_len= max_len,
                        maxWeight= maxWeight)
    
   
        


        



