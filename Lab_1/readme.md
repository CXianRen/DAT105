# step:
+ cp base1.txt to simhom/configs/
+ check cache setting in base1.txt (between line 100 to 135)
+ runsim_sim for the base model
+ read result from the report starting with "Stats_"

### how to run runsim_sim:
```bash
./runsim_sim . base1
```

### how to calculate $CPI_0$:

+ just set memory access lantency as 0



### what is associativity


###
cache size, associativity, block szie,

2 application,


cache config (from simple scaler ref.pdf)

+ name cache name
+ nsets : number of sets in the cache.
+ bsize : block size
+ assic : associativity of the cache (power of two)
+ repl  : replacement policy (l|f|r), l=LRU, f= FIFO, r=rando replacement
