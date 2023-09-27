#!/bin/python3

# this python3 scipts is used for extracting key info from state report

import os
import re

app_list = ["dijkstra", "gsm-untoast", "jpeg-cjpeg", "qsort", "stringsearch-cabce"]


def get_info(file):
    ic=0    # total number of instructions committed 
    et=0    # total simulation time in cycles
    cpi=0   # cycles per instruction 
    # mpi = number of misses per instruction = number of misses / total instruction number
    mpi_il1=0   
    mpi_dl1=0
    cpi_0 = 0
    speedup = 0
    lines = open(file).readlines()
    for line in lines:
        # Instruction Count
        if line.find('sim_num_insn') == 0:
            ic = int(re.findall(r'\d+', line)[0])
            # print(ic)
        if line.find('sim_cycle') == 0:
            et = int(re.findall(r'\d+', line)[0])
            # print(et)
        if line.find('sim_CPI') == 0:
            cpi = float(re.findall(r'\d+\.\d+', line)[0])
            # print(cpi)
        if line.find('il1.misses') == 0:
            mpi_il1 = int(re.findall(r'\d+', line)[1])/ic
            # print(mpi_il1)
        if line.find('dl1.misses') == 0:
            mpi_dl1 = int(re.findall(r'\d+', line)[1])/ic
            # print(mpi_dl1)
    # get cpi 0
    lines = open(file+"_CPI0").readlines()
    for line in lines:
        if line.find('sim_CPI') == 0:
            cpi_0 = float(re.findall(r'\d+\.\d+', line)[0])
            # print(cpi_0)
    speedup = cpi/cpi_0
    # print(speedup)
    return (ic, et, cpi, mpi_il1, mpi_dl1, cpi_0, speedup)

print('Application,instruction_Count*,Execusiton_Time_in_cycles,CPI_\{base\},MPI I-L1,MPI D-L1,CPI_0,SP_\{ideal\}')
for app in app_list:
    info = get_info("./configs/Stats_base1_"+ app+".txt")
    print(app,','.join(map(str,info)),sep=',')