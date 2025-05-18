## Bench marking with Just Pandas
- size of the csv file: 300MB
- min docker memory required: 500MB, anything less than that will be killed by the Docker daemon due to memory overcommitment (OOM)


```bash
docker build -t csv-benchmark .

docker run --rm --cpus="1" --memory="800m" -v .:/app csv-benchmark
```

| No. of Cores | Memory Limit | Mem After Load (MB) | Mem After Clean (MB) | Time Taken (s) |
| ------------ | ------------ | ------------------- | -------------------- | -------------- |
| 1            | 500 MB       | 446.54              | 336.15               | 43.78          |
| 1            | 600 MB       | 580.51              | 569.45               | 41.90          |
| 1            | 700 MB       | 636.32              | 454.08               | 23.49          |
| 1            | 800 MB       | 689.16              | 777.06               | 9.29           |
| 1            | 900 MB       | 689.30              | 778.20               | 9.66           |
| 1            | 1 GB         | 689.05              | 777.99               | 9.75           |
| 1            | 2 GB         | 689.29              | 777.20               | 9.79           |
| 1            | 10 GB        | 689.54              | 778.50               | 9.51           |
| 1            | 500 MB       | 476.28              | 458.96               | 57.42          |
| 2            | 500 MB       | 470.32              | 509.94               | 51.37          |
| 4            | 500 MB       | 469.95              | 501.91               | 49.58          |


### Takeaways
    - until unless the script uses the no of cores, `multiprocessing`, adding more no of cores makes no sense
    - adding more memory other than required which is also no use

### Why 800MB RAM Helps
    - Your script peaks around ~518MB RAM usage (as seen in your 500MB test).
    - Giving it 800MB avoids memory pressure, reducing GC overhead and potential paging.
    - It ensures smooth parsing and cleaning in one go (especially with pandas loading the full DataFrame into memory).

### Why 1 CPU Core Is Sufficient
    - Task is I/O-bound initially (CSV read) and CPU-light during cleaning unless doing heavy transforms.
    - Pandas isn't inherently multithreaded — so extra cores won't drastically improve performance unless you parallelize with tools like modin, multiprocessing, or dask.



## Benchmarking with Pandas and Multiprocessing - where multiple cores are can be utilized to improve the performance



