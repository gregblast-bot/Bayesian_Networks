# This is for INFSCI 2440 in Spring 2026
# Please add comments along with your code
# Task 2: Build Bayesian Network probability distribution from data 

import numpy as np

'''
Get the Conditional Probability Table for P(b | c,d)

Returns:
    p_b_cd (np.array): The filled Conditional Probability Table for P(b | c,d)
'''
def get_p_b_cd():
    # you need to implement this method.
    p_b_cd = np.zeros((3,3,2), dtype = int)
    return set_p_b_cd(p_b_cd)

'''
Set the Conditional Probability Table for P(b | c,d)

Args:
    p_b_cd (np.array): The empty Conditional Probability Table for P(b | c,d)

Returns:
    p_b_cd (np.array): The filled Conditional Probability Table for P(b | c,d)
'''
def set_p_b_cd(p_b_cd):
    # Extract relevant probabilities from file
    _, _, p_b, p_c, p_d, _ = extract(data_add)

    # Convert lists to np.arrays for efficiency
    p_b = np.array(p_b, dtype = int)
    p_c = np.array(p_c, dtype = int)
    p_d = np.array(p_d, dtype = int)

    # Fill the Conditional Probability Table for P(b | c,d)
    for c in range(3):
        for d in range(2):
            # In this case, the probability of the event is the frequency of its occurence
            # P(b | c,d) = P(b, c, d) / P(c, d) = count(b, c, d) / count(c, d)
            for b in range(3):
                p_bcd = 0
                p_cd = 0
                for i in range(len(p_b)):
                    if p_c[i] == (c+1) and p_d[i] == (d+1):
                        p_cd += 1
                        if p_b[i] == (b+1):
                            p_bcd += 1
                p_b_cd[b][c][d] = int(round((p_bcd / p_cd) * 100)) if p_cd > 0 else 0

    return p_b_cd

'''
Get the Conditional Probability Table for P(a | b,e)

Returns:
    p_a_be (np.array): The filled Conditional Probability Table for P(a | b,e)
'''
def get_p_a_be():
    # you need to implement this method.
    p_a_be = np.zeros((2,3,2),dtype = int)
    return set_p_a_be(p_a_be)

'''
Set the Conditional Probability Table for P(a | b,e)

Args:
    p_a_be (np.array): The empty Conditional Probability Table for P(a | b,e)

Returns:
    p_a_be (np.array): The filled Conditional Probability Table for P(a | b,e)
'''
def set_p_a_be(p_a_be):
    # Extract relevant probabilities from file
    _, p_a, p_b, _, _, p_e = extract(data_add)

    # Convert relevant lists to np.arrays for efficiency
    p_a = np.array(p_a, dtype = int)
    p_b = np.array(p_b, dtype = int)
    p_e = np.array(p_e, dtype = int)

    # Fill the Conditional Probability Table for P(a | b,e)
    for b in range(3):
        for e in range(2):
            for a in range(2):
                p_abe = 0
                p_be = 0
                # In this case, the probability of the event is the frequency of its occurence
                # P(a | b,e) = P(a, b, e) / P(b, e) = count(a, b, e) / count(b, e)
                for i in range(len(p_a)):
                    if p_b[i] == (b+1) and p_e[i] == (e+1):
                        p_be += 1
                        if p_a[i] == (a+1):
                            p_abe += 1
                p_a_be[a][b][e] = int(round((p_abe / p_be) * 100)) if p_be > 0 else 0
    
    return p_a_be

'''
Extract the probabilities from the data file

Args:
    data_add (file object): The file object containing probabilities of the Bayesian Network

Returns:
    sample_id (list): The index of the sample
    p_a (list): The probabilities of node a Bayesian Network
    p_b (list): The probabilities of node b Bayesian Network
    p_c (list): The probabilities of node c Bayesian Network
    p_d (list): The probabilities of node d Bayesian Network
    p_e (list): The probabilities of node e Bayesian Network
'''
def extract(data_add):
    # Open file containing probabilities
    with open(data_add, 'r') as file:
        sample_id, p_a, p_b, p_c, p_d, p_e = parse_file(file)

    return sample_id, p_a, p_b, p_c, p_d, p_e

'''
Parse the data file to collect the Bayesian Network probabilities

Args:
    file (file object): The file object containing probabilities of the Bayesian Network

Returns:
    sample_id (list): The index of the sample
    p_a (list): The probabilities of node a Bayesian Network
    p_b (list): The probabilities of node b Bayesian Network
    p_c (list): The probabilities of node c Bayesian Network
    p_d (list): The probabilities of node d Bayesian Network
    p_e (list): The probabilities of node e Bayesian Network
'''
def parse_file(file):
    # Use local lists to clear the data every time this method is called
    sample_id, p_a, p_b, p_c, p_d, p_e = [], [], [], [], [], []

    # For each line in the file (except the header), extract probabilities of all nodes
    next(file)
    for line in file:
        parts = line.strip().split('\t')
        sample_id.append(parts[0])
        p_a.append(parts[1])
        p_b.append(parts[2])
        p_c.append(parts[3])
        p_d.append(parts[4])
        p_e.append(parts[5])

    return sample_id, p_a, p_b, p_c, p_d, p_e


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

