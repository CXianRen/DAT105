#!/bin/python3

# this python3 scipts is used for extracting key info from state report

import os
import re
import glob

# app_list = ["dijkstra", "gsm-untoast", "jpeg-cjpeg", "qsort", "stringsearch-cabce"]

# dijkstra
base_cpi_time = 8.8859



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
    # lines = open(file+"_CPI0").readlines()
    # for line in lines:
    #     if line.find('sim_CPI') == 0:
    #         cpi_0 = float(re.findall(r'\d+\.\d+', line)[0])
    #         # print(cpi_0)
    speedup = base_cpi_time/cpi
    # print(speedup)
    return (ic, et, cpi, mpi_il1, mpi_dl1, cpi_0, speedup)

def get_size(s:str):
    return int(s.split('_')[-4].replace('S',''))

def get_associativity(s:str):
    return int(s.split('_')[-3].replace('A',''))

def get_block(s:str):
    return int(s.split('_')[-1].replace('B',''))
    

file_list =glob.glob("configs/Lab1-Task2/Stats_base1_*_S32_*B8")
file_list.sort(key=sort_by_size)
# file_list.sort()
# print(file_list)
for file in file_list:
    info = get_info(file)
    print(file.split('/')[-1], info[-1])