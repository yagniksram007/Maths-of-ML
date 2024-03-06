from scipy.optimize import minimize

# Define the utility function
def utility(x):
    return -(x[0]**0.5 * x[1]**0.5)  # We will minimize the negative of this function

# Define the budget constraint
def budget_constraint(x):
    p1, p2 = 2, 3  # Prices of the goods
    m = 100  # Consumer's income
    return m - p1*x[0] - p2*x[1]

# Initial guess
x0 = [1, 1]

# Define the constraints
cons = ({'type': 'eq', 'fun': budget_constraint})

# Solve the optimization problem
res = minimize(utility, x0, constraints=cons, method='SLSQP')

# Print the optimal quantities of the goods
print(f'Optimal quantity of good 1: {res.x[0]}')
print(f'Optimal quantity of good 2: {res.x[1]}')