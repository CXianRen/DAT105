# step:
+ cp base1.txt to simhom/configs/
+ check cache setting in base1.txt (between line 100 to 135)
+ runsim_sim for the base model
+ read result from the report starting with "Stats_"

### how to run runsim_sim:
```bash
./runsim_sim . config/base1
```

### how to calculate $CPI_0$:

+ just set memory access lantency as 0
