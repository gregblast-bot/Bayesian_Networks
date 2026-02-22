# This is for INFSCI 2440 in Spring 2026
# Please add comments along with your code
# Task 1.a: Filtering inference on HMM

def filtering(evidence_data_add, prior, total_day):
    # you need to implement this method.

    x_prob_rain = []
    # x_prob_sunny[i] = 1 - x_prob_rain[i]

    for i in range(100):
        x_prob_rain.append(0.0)
        
    return x_prob_rain




# following lines are main function:
evidence_data_add = "data//assign2_umbrella.txt"
total_day = 100
# the prior distribution on the initial state, P(X0). 50% rainy, and 50% sunny on day 0.
prior = [0.5, 0.5]

x_prob_rain=filtering(evidence_data_add, prior, total_day)
for i in range(100):
    print("Day " + str(i+1) + ": rain " + str(x_prob_rain[i]) + ", sunny " + str(1 - x_prob_rain[i]))

print("*"*100)