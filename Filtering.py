# This is for INFSCI 2440 in Spring 2026
# Please add comments along with your code
# Task 1.a: Filtering inference on HMM

def filtering(evidence_data_add, prior, total_day):
    # you need to implement this method.
    
    # Extract the observations and save to observations list
    observations = extract(evidence_data_add)

    x_prob_rain = []
    # x_prob_sunny[i] = 1 - x_prob_rain[i]

    for i in range(100):
        x_prob_rain.append(0.0)
        
    return x_prob_rain

'''
Extract the evidence from the data file

Args:
    file (file object): The file object containing evidence

Returns:
    observations (list): The list of observations per day
'''
def extract(evidence_data_add):
    # Open file containing sentences
    with open(evidence_data_add, 'r') as file:
        observations = parse_file(file)

    return observations

'''
Parse the evidence file to collect the observations

Args:
    file (file object): The file object containing evidence

Returns:
    observations (list): The list of observations per day
'''
def parse_file(file):
    observations = []
    # For each line in the file, extract truth value based on observation
    for line in file:
        parts = line.strip().split('\t')
        print(parts)
        obs = parts[1]
        observations.append(obs == 'take umbrella')

    return observations


# following lines are main function:
evidence_data_add = "data//assign2_umbrella.txt"
total_day = 100
# the prior distribution on the initial state, P(X0). 50% rainy, and 50% sunny on day 0.
prior = [0.5, 0.5]

x_prob_rain=filtering(evidence_data_add, prior, total_day)
for i in range(100):
    print("Day " + str(i+1) + ": rain " + str(x_prob_rain[i]) + ", sunny " + str(1 - x_prob_rain[i]))

print("*"*100)