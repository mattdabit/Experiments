#Feedback 
import numpy as np
def stdev(player_times):
	return np.std(player_times)

def mean(player_times):
	return (sum(player_times)/len(player_times))

def rate(player_times):
	diff = [] 
	for i in range(len(player_times) -1):
		diff.append(player_times[i+1] - player_times[i])
	return diff

def round_rate(player_times):
	diff = rate(player_times)
	r_diff = []
	for num in diff:
		r_diff.append(round(num, -1))
	return r_diff