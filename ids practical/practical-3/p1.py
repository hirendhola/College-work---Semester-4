# 1. List of five Indian states
states = ["Gujarat", "Rajasthan", "Andhra Pradesh", "Karnataka", "Kerala"]

# 2. List of five Indian state capitals
capitals = ["Gandhinagar", "Jaipur", "Amaravati", "Bengaluru", "Thiruvananthapuram"]

# 3. Dictionary using the state and capital lists
state_capitals = dict(zip(states, capitals))

# 4. Display the capital of Gujarat
capital = state_capitals["Gujarat"]
print(capital)  

