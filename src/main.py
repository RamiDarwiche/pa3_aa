import typer
import sys
from typing import Dict, List, Tuple, Annotated
from example_generator import generate as generate_examples

def get_input() -> Tuple[int, Dict[str, int], str, str]:
    try: 
        K: int = int(input())
        x: Dict[str, int] = {}
        for i in range(K):
            input_str = input().split()
            x[input_str[0]] = int(input_str[1])

        A: str = input()
        B: str = input()
    except Exception:
        print("Error, expected the following input format:")
        print("K\nx1 v1\nx2 v2\n...\nxK vK\nA\nB")
        sys.exit(1)
    return K, x, A, B

def get_input_from_file(file_path: str) -> Tuple[int, Dict[str, int], str, str]:
    with open(file_path, "r") as f:
        K = int(f.readline())
        x = {}
        for i in range(K):
            input_str = f.readline().split()
            x[input_str[0]] = int(input_str[1])
        A = f.readline().strip()
        B = f.readline().strip()
    return K, x, A, B


def solve(K: int, x: Dict[str, int], A: str, B: str) -> Tuple[int, str]:
    n = len(A)
    m = len(B)

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    # fill dp table ot get max value of common subseueqnce
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                v = x[A[i - 1]]
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + v)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    

    # backtrack to build valid subsequence
    i, j = n, m
    out: List[str] = []
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1] and dp[i][j] == dp[i - 1][j - 1] + x[A[i - 1]]:
            out.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1

    subseq = "".join(reversed(out))
    return dp[n][m], subseq




"""

CLI Interface functions

"""

app = typer.Typer()

@app.command()
def generate():
    generate_examples()

@app.command()
def file(
    file: Annotated[
        str, typer.Argument(help="Path to input file")
    ],
):
    K, x, A, B = get_input_from_file(file)
    value, subseq = solve(K, x, A, B)
    print(value)
    print(subseq)

@app.command("input")
def _input():
    K, x, A, B = get_input()
    value, subseq = solve(K, x, A, B)
    print(value)
    print(subseq)

if __name__ == "__main__":
    app()
    

