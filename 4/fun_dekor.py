import time
import numpy as np


def dekor(func):
    def wew():
        print("Dekorujemy")
        return func()

    return wew


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")
        return result

    return wrapper


@dekor
def hej():
    print("Hej")


@measure_time
def my_wait():
    time.sleep(2)


@measure_time
def my_for_sum():
    suma = 0
    for i in range(15_000_000):
        suma += i
    print("Sum is:", suma)


@measure_time
def my_sum_without_for():
    total = sum(range(15_000_000))
    print("Sum is:", total)


@measure_time
def my_sum_np():
    total = np.sum(np.arange(15_000_000, dtype=np.int64))
    print("Sum is:", total)


hej()
# Hej

# po uyciu dekoratora
# Dekorujemy
# Hej
my_wait()
# Czas wykonania funkcji my_wait: 2.0007896423339844
my_for_sum()
# Sum is: 112499992500000
# Czas wykonania funkcji my_for_sum: 0.7442259788513184
my_sum_without_for()
# Sum is: 112499992500000
# Czas wykonania funkcji my_sum_without_for: 0.2953531742095947
my_sum_np()
# Sum is: 112499992500000
# Czas wykonania funkcji my_sum_np: 0.05713343620300293
