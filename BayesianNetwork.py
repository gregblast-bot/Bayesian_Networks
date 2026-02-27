# This is for INFSCI 2440 in Spring 2026
# Please add comments along with your code
# Task 2: Build Bayesian Network probability distribution from data 

import numpy as np

p_a = []
p_b = []
p_c = []
p_d = []
p_e = []

def get_p_b_cd():
    # you need to implement this method.
    p_b_cd = np.zeros((3,3,2),dtype = np.int)
    return p_b_cd

def get_p_a_be():
    # you need to implement this method.
    p_a_be = np.zeros((2,3,2),dtype = np.int)
    return p_a_be

'''
Extract the probabilities from the data file

Args:
    data_add (file object): The file object containing probabilities of the Bayesian Network

Returns:
    p_a (list): The probabilities of node a Bayesian Network
    p_b (list): The probabilities of node b Bayesian Network
    p_c (list): The probabilities of node c Bayesian Network
    p_d (list): The probabilities of node d Bayesian Network
    p_e (list): The probabilities of node e Bayesian Network
'''
def extract(data_add):
    # Open file containing probabilities
    with open(data_add, 'r') as file:
        p_a, p_b, p_c, p_d, p_e = parse_file(file)

    return p_a, p_b, p_c, p_d, p_e

'''
Parse the data file to collect the Bayesian Network probabilities

Args:
    file (file object): The file object containing probabilities of the Bayesian Network

Returns:
    p_a (list): The probabilities of node a Bayesian Network
    p_b (list): The probabilities of node b Bayesian Network
    p_c (list): The probabilities of node c Bayesian Network
    p_d (list): The probabilities of node d Bayesian Network
    p_e (list): The probabilities of node e Bayesian Network
'''
def parse_file(file):
    # For each line in the file, extract probabilities of all nodes
    for line in file:
        parts = line.strip().split('\t')
        p_a.append(parts[1])
        p_b.append(parts[2])
        p_c.append(parts[3])
        p_d.append(parts[4])
        p_e.append(parts[5])

    return p_a, p_b, p_c, p_d, p_e


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

