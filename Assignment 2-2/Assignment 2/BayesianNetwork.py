# This is for INFSCI 2440 in Spring 2026
# Please add comments along with your code
# Task 2: Build Bayesian Network probability distribution from data 

import numpy as np

def get_p_b_cd():
    # you need to implement this method.
    p_b_cd = np.zeros((3,3,2),dtype = np.int)
    return p_b_cd

def get_p_a_be():
    # you need to implement this method.
    p_a_be = np.zeros((2,3,2),dtype = np.int)
    return p_a_be


# following lines are main function:
data_add = "data//assign2_BNdata.txt"

# probability distribution of b.
p_b_cd=get_p_b_cd()
for c in range(3):
    for d in range(2):
        for b in range(3):
            print("P(b=" + str(b+1) + "|c=" + str(c+1) + ",d=" + str(d+1) + ")=" + str(p_b_cd[b][c][d]))


# probability distribution of a.
p_a_be=get_p_a_be()
for b in range(3):
    for e in range(2):
        for a in range(2):
            print("P(a=" + str(a+1) + "|b=" + str(b+1) + ",e=" + str(e+1) + ")=" + str(p_a_be[a][b][e]))

