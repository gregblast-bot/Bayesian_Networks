# This is for INFSCI 2440 in Spring 2026
# Please add comments along with your code
# Task 1.b: Prediction inference on HMM

import Filtering as filter

'''
Compute the posterior distribution over the future state,
given all evidence to date.

Args:
    evidence_data_add (file object): The file object containing evidence
    prior (list): Prior distribution on the initial states
    end_day (int): The day to end prediction on

Returns:
    x_prob_rain (float): The probability of rain
'''
def prediction(evidence_data_add, prior, start_day, end_day):
    # you need to implement this method.
    x_prob_rain = []
    # x_prob_sunny[i] = 1 - x_prob_rain[i]

    # Transition model
    prob_rain_given_rain   = 0.7
    prob_rain_given_sunny  = 0.3
    #prob_sunny_given_rain = 0.3
    #prob_sunny_given_sunny = 0.7

    # Filter over all observed days
    filtered = filter.filtering(evidence_data_add, prior, start_day-1)

    # filtered[-1] = P(r_100 | u_{1:100}) = P(r_(t+k) |u_{1:t})
    prob_rain  = filtered[-1]         
    prob_sunny = 1.0 - prob_rain      

    # Loop from the given start day to the given end day
    # P(R_(t+k+1) | u_{1:t}) = r_(t+k) * P(R_(t+k+1) | r_(t+k)) * P(r_(t+k) | u_{1:t})
    # (Equation 15.6 from Artificial Intelligence, A Modern Approach, Third Edition)
    for i in range(start_day, end_day + 1):
        # Prediction step from t to t+1
        # P(R_(t+1)) = sum_(r_t)(P(R_(t+1) | r_t) * P(r_t))
        predicted_rain  = (prob_rain_given_rain  * prob_rain) + (prob_rain_given_sunny * prob_sunny)
        predicted_sunny = 1.0 - predicted_rain

        # Update probabilities
        prob_rain  = predicted_rain
        prob_sunny = predicted_sunny

        x_prob_rain.append(prob_rain)

    return x_prob_rain




# following lines are main function:
evidence_data_add = "data//assign2_umbrella.txt"
start_day = 101
end_day = 150
# the prior distribution on the initial state, P(X0). 50% rainy, and 50% sunny on day 0.
prior = [0.5, 0.5]

x_prob_rain=prediction(evidence_data_add, prior, start_day, end_day)
for i in range(start_day, end_day+1):
    print("Day " + str(i) + ": rain " + str(x_prob_rain[i-start_day]) + ", sunny " + str(1 - x_prob_rain[i-start_day]))
    # print("Day " + str(i+1) + ": rain " + str(x_prob_rain[i]) + ", sunny " + str(1 - x_prob_rain[i]))

print("*"*100)