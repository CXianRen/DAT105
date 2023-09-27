### note 1
explore other performance enhancing techniques
including branch prediction and different instruction scheduling techniques.



+  Check the related sections of the simulator user guide to see what parameters are available and what each parameter refers to
[doc](https://chalmers.instructure.com/courses/25518/files/folder/Labs/Simulator%20and%20Benchmark%20reference%20documents?preview=2830295)


```shell
The default is a bimo-dal predictor with 2048 entries.
-bpred <type>
  nottaken      always predict not taken
  taken         always predict taken
  perfect       perfect predictor
  bimod         binmodal predictor, using a branch target buffer(BTB) with 2-bit        counters.
  2lev          2-level adaptive predictor.
  comb          combined predictor (bimodal and 2-level adaptive)


-bpred:bimod <size> 
    set the bimodal predictor table size to be <size> entries.

-bpred:2lev <l1size> <l2size> <hist_size> <xor>  
    <hist_size> specifies the history width,
    <xor> allows you to xor the history and the address in the second level of the predictor.

-bpred:comb <size>
    set the meta-table size of the combined pre-dictor to be <size> entries. The default is 1024.

-bpred:ras <size>
    set the return stack size to <size> (0 entries means to return stack). The default is 8 entries.

-bpred:btb <sets> <assoc>
  configure the BTB to have <sets> sets and an associativity of <assoc>. The defaults are 512 sets and an associativity of 4

-bpred:spec_update <stage>
  allow speculative updates of the branch pre-dictor in the decode or writeback stages (<stage> = [ID|WB]) The default is non-speculative updates in the commit stage.

# todo
```


### report requirement 
You must write a report that includes: A brief description of the problem
and the method you used, important assumptions (if any), simulation results and
observations, your design choices and the reason behind them. Detailed report
guidelines will be available on Canvas.


+ compare accuracy among dynamic predictors（xxx）
+ compare the CPI? and SpeedUp

# Task  
## step
+  1 run the base one
+  run perfect, binodal, two-level, and combind
+  alter RAS and BTB:
  + doubling the table size for bimodal
  + doubling of the L1 and/or L2 size of 2-level
  + doubling of the table size of combined.


# Task 2.1
+ run and check performance with different integer and multiper or divider ALU
