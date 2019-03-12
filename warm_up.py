import pulp

points = [
    (1, 3),
    (2, 5),
    (3, 7),
    (5, 11),
    (7, 14),
    (8, 15),
    (10, 19)
]
z = pulp.LpVariable("z", 0, None)
a = pulp.LpVariable("a")
b = pulp.LpVariable("b")
prob = pulp.LpProblem("best_fit", pulp.LpMinimize)
prob += z, "obj"
for point in points:
    prob += point[0]*a+b-point[1] <= z
    prob += point[0]*a+b-point[1] >= -z
status = prob.solve()

# Print the status of the solved LP
print("Status:", pulp.LpStatus[prob.status])

# Print the value of the variables at the optimum
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Print the value of the objective
print("objective=", pulp.value(prob.objective))
