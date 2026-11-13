
import timeit

sizes = [1000, 10000, 100000, 1000000]

for n in sizes:
    data = list(range(n))

    tiempo = timeit.timeit(
        lambda: data[n // 2],
        number=100000
    )

    print(f"N = {n}, tiempo = {tiempo:.6f} s")
