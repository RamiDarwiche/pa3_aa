from typing import Dict

def main():
    K: int = int(input())
    x: Dict[str, int] = {}
    for i in range(K):
        input_str = input().split()
        x[input_str[0]] = int(input_str[1])

    A: str = input()
    B: str = input()

    print(f"K: {K}\nx: {x}\nA: {A}\nB: {B}")
    solve(K, x, A, B)

def solve(K: int, x: Dict[str, int], A: str, B: str) -> (int, str):
    dp = [[]]
    pass

if __name__ == "__main__":
    main()
