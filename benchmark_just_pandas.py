import pandas as pd
import time
import os
import psutil
from scripts import clean_quantity
from pathlib import Path
import pandas as pd
import timeit

# Define the file path
filepath = Path("data/orders.csv")


def print_usage():
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / (1024 * 1024)  # MB
    cpu = process.cpu_percent(interval=1)
    print(f"[Resource] Memory: {mem:.2f} MB, CPU: {cpu:.2f}%")


def run_normal():
    # Read the CSV file into a DataFrame
    start = time.time()
    print("[Step] Reading CSV...")

    df = pd.read_csv(filepath)
    print_usage()

    df = clean_quantity(df)
    print_usage()

    end = time.time()
    print(f"[Benchmark] Total time: {end - start:.2f} seconds")



def run_with_chunking():
    chunk_size = 100_000  # rows per chunk
    print("[Step] Reading CSV in chunk of 100000 rows...")
    for chunk in pd.read_csv(filepath, chunksize=chunk_size):
        print_usage()
        chunk = clean_quantity(chunk)
        print_usage()



normal_execution_time = timeit.timeit(
    stmt=run_normal,
    number=1
)


# chunk_execution_time = timeit.timeit(
#     stmt=run_with_chunking,
#     number=1
# )

print(
    f"Total time: {normal_execution_time: .4f} seconds"
)
# print(
#     f"Total time: {chunk_execution_time: .4f} seconds"
# )