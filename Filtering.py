# This is for INFSCI 2440 in Spring 2026
# Please add comments along with your code
# Task 1.a: Filtering inference on HMM
    
'''
State estimation step. Compute the belief state (the posterior distribution
over the most recent state) given all evidence to date.

Args:
    evidence_data_add (file object): The file object containing evidence
    prior (list): Prior distribution on the initial states
    total_day (int): Total days worth of data

Returns:
    x_prob_rain (float): The probability of rain
'''
def filtering(evidence_data_add, prior, total_day):
    # you need to implement this method.
    x_prob_rain = []
    #x_prob_sunny[i] = 1 - x_prob_rain[i]

    # Transition model
    prob_rain_given_rain   = 0.7
    prob_rain_given_sunny  = 0.3
    #prob_sunny_given_rain = 0.3
    #prob_sunny_given_sunny = 0.7

    # Sensor model
    prob_umbrella_given_rain   = 0.9
    prob_umbrella_given_sunny  = 0.2
    prob_no_umbrella_given_rain   = 0.1
    prob_no_umbrella_given_sunny  = 0.8
    
    # Extract the observations and save to observations list
    observations = extract(evidence_data_add)

    # Prior distribution: [P(rain), P(sunny)]
    # P(R0)= <0.5, 0.5>
    prob_rain  = prior[0]
    prob_sunny = prior[1]

    # Loop for the total number of days given
    # α * P(u_(t+1) | R_(t+1)) * sum_(r_t)(P(R_(t+1) | r_t)P(r_t | u{1:t}))
    # (Equation 15.6 from Artificial Intelligence, A Modern Approach, Third Edition)
    for i in range(total_day):
        # Umbrella is true OR false
        umbrella = observations[i]

        # Prediction step from t to t+1
        # P(R_(t+1)) = sum_(r_t)(P(R_(t+1) | r_t) * P(r_t))
        predicted_rain  = (prob_rain_given_rain  * prob_rain) + (prob_rain_given_sunny * prob_sunny)
        predicted_sunny = 1.0 - predicted_rain

        # Update step for t
        # P(R_t | u_t) = α * P(u_t | R_t) * P(R_t)
        if umbrella:
            updated_rain  = prob_umbrella_given_rain  * predicted_rain
            updated_sunny = prob_umbrella_given_sunny * predicted_sunny
        else:
            updated_rain  = prob_no_umbrella_given_rain * predicted_rain
            updated_sunny = prob_no_umbrella_given_sunny * predicted_sunny

        # Normalize with constant α
        alpha = 1 / (updated_rain + updated_sunny)
        prob_rain  = alpha * updated_rain
        prob_sunny = alpha * updated_sunny

        x_prob_rain.append(prob_rain)
        
    return x_prob_rain

'''
Extract the evidence from the data file

Args:
    evidence_data_add (file object): The file object containing evidence

Returns:
    observations (list): The list of observations per day
'''
def extract( evidence_data_add):
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