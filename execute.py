from scripts import clean_quantity
import timeit
from pathlib import Path
import pandas as pd

# Define the file path
filepath = Path("data/orders.csv")

def run_normal():
    # Read the CSV file into a DataFrame
    df = pd.read_csv(filepath)
    df = clean_quantity(df)
    print(
        df[["quantity", "cleaned_quantity"]]
    )


def run_with_chunking():
    chunk_size = 100_000  # rows per chunk
    for chunk in pd.read_csv(filepath, chunksize=chunk_size):
        chunk = clean_quantity(chunk)
        print(
            chunk[["quantity", "cleaned_quantity"]]
        )



def run_with_multiprocessing():
    pass



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