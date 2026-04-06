# Programming Assignment 3 : Highest Value Longest Common Sequence

Rami (UFID: 6425-8874)  
David Murillo (UFID: 7222-2427)

# Dependencies

1. Create Virtual environment:
 ```
 python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows
source venv/bin/activate   #MacOS/Linux
```

2. Install dependencies

``` 
pip install typer matplotlib 
```
# Input Format

Same as specified in assignment:

```
K
x1 v1
x2 v2
...
xK vK
A
B
```

Where:  
K - number of chars in the alphabet  
xi, vi - char and its associated integer value  
A, B - two strings to compare

Sample Input:  
```
3
a 5
b 3
c 8
abacbc
bcacab
```

# Running the Solution

(NOTE: all commands below should be run from the src/ directory)  

From an Input File:
```
python main.py file ../examples/example.in
```

From Standard Input (CLI):
```
python main.py input
```

The program will pring two lines for the output:
```
<maximum total value>
<subsequence achieving that value>
```

# Generating Examples 

Single Example:
```
python example_generator.py
```

This will prompt you to enter K, and the desired lengths for the strings A and B

Automated Multiple Examples:
```
python automated_example_generator.py
```

This will prompt you whether you want to use custom arguments, and if so you will enter:

n - number of examples to generate
k - alphabet size
min/max_len - range for string lengths
maxWeight -  a cap on the weight assigned to any given char in the given alphabet

All generated files are saved to  ../examples/ and use the following naming convention:  
```
example_n{i}_k{k}_a{len_a}_b{len_b}_{timestamp}.in
```

# Runtime Analysis

To generate and save a plot of runtime vs input size:

```
python runtime_grapher.py
```
This reads all files in ../examples/, times the solver on each, and saves a plot to ../runtime_graphs/runtime_plot.png. The x-axis is n * m (product of string lengths), which reflects the actual work done by the O(n * m) algorithm.


# Question 1: 
(Premade graph included in "runtime_graphs" folder, input examples in "examples" folder). Graph was made from the 10 existing files

# Question 2 - Recurrence: 

Let dp[i][j] be the highest value of any common subsequence of A(1 ... i) and B(1 .... j), where x[c] is the weight of the character c.

Base Cases:  
dp[0][j] = 0  
dp[i][0] = 0

When either string is empty, there is no common subsequence

Recurrence:

dp[i][j] = {
    max(dp[i-j][j], dp[i][j-1], dp[i-1][j-1]) if A[i] = B[j],
    max(dp[i-1][j], dp[i][j - 1]) if A[i] /= B[j]
}


At each cell of dp[i][j] we consider one of three options.
1. Skip A[i] (take dp[i-1][j])
2. Skip B[j] (take dp[i][j-1])
3. If the characters match,  include them in the subsequence and add x[[A[i]]] to the best value achievable from the remaining prefixes A[1...j-1] and B[1...j-1]. 

We do not include character pairs when A[i] /= B[j] as this would not be a valid common subsequence. Taking the max across all valid options ensures that we get teh highest value common subsequence of the two prefixes, and since every subproblem is solved optimally, the final answer dp[n][m] is optimal/

# Question 3 -  Big-Oh:

Pseudocode:
```
HVLCS(A, B, x):
    n = len(A) , m = len(B)

    //initialize table with 0s (dimensions of (n+1)*(m+1))
    dp[0 .. n][0 .. m] = 0

    //fill table
    for i = 1 to n
        for j = 1 to m
            if A[i] == B[j]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+x[A[i]])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    //backtrack to construct subsequence from solved subproblems
    i = n
    j = m
    output = []
    while i, j > 0:
        if A[i] == B[j] and dp[i][j] == dp[i-1][j-1] + x[A[i]]:
            add A[i] to output
            i-=1
            j-=1
        else if dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            j-=1
    
    return dp[n][m], output

```

Runtime:
The table construction has O(n*m) runtime as there are n x m cells each being filled in O(1) time. The backtracking takes at most O(n+m) steps. Thus the overall runtime is O(n*m).
