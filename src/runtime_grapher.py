from main import *
import matplotlib.pyplot as plt
from pathlib import Path
import time

runtimes = []
nm_values = []

examples_dir = Path(__file__).parent.parent / "examples"
output_dir = Path(__file__).parent.parent / "runtime_graphs"
#output_dir.mkdir(exist_ok=True)  


#for each file in the examples folder
for file in examples_dir.iterdir():
    #check that we are working with a file
    if file.is_file():
        
        #extract the input from the example file with the helper function
        input = get_input_from_file(file)
        n = len(input[2])
        m = len(input[3])
        start_time = time.perf_counter()
        solution = solve(K=input[0], x =input[1], A=input[2], B = input[3])
        elapsed = time.perf_counter() - start_time
        runtimes.append(elapsed)
        nm_values.append(n*m)


paired = sorted(zip(nm_values, runtimes))
nm_values, runtimes = zip(*paired)

plt.plot(nm_values, runtimes)
plt.xlabel("n*m (product of string lengths)")
plt.ylabel("Runtime (seconds)")
plt.title("Input Size vs Runtime")
plt.savefig(output_dir / "runtime_plot.png")
plt.show()
