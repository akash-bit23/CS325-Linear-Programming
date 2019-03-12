import pulp
import math

# actual and calculated temperatures
t_actual = pulp.LpVariable("t_a")
t_calculated = pulp.LpVariable("t_c")

# difference between the temp values
z = pulp.LpVariable("z")

# constants for calculated temp
x0 = pulp.LpVariable("x0")
x1 = pulp.LpVariable("x1")
x2 = pulp.LpVariable("x2")
x3 = pulp.LpVariable("x3")
x4 = pulp.LpVariable("x4")
x5 = pulp.LpVariable("x5")

# minimize z
prob = pulp.LpProblem("best_fit",pulp.LpMinimize)
prob += z, "obj"

# compare actual readings with calculated readings
for reading in readings:
    prob += 
    (x0) + 
    (x1 * reading.day) + 
    (x2*math.cos((2*math.pi()*reading.day)/365.25)) + 
    (x3*math.sin((2*math.pi()*reading.day)/365.25)) +
    (x4*math.cos((2*math.pi()*reading.day)/(365.25*10.7))) +
    (x5*math.sin((2*math.pi()*reading.day)/(365.25*10.7))) -
    reading.temp <= z
    prob +=
    (x0) + 
    (x1 * reading.day) + 
    (x2*math.cos((2*math.pi()*reading.day)/365.25)) + 
    (x3*math.sin((2*math.pi()*reading.day)/365.25)) +
    (x4*math.cos((2*math.pi()*reading.day)/(365.25*10.7))) +
    (x5*math.sin((2*math.pi()*reading.day)/(365.25*10.7))) -
    reading.temp >= -z

# compute
status = prob.solve()

# Print the status of the solved LP
print("Status:", pulp.LpStatus[prob.status])

# Print the value of the variables at the optimum
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Print the value of the objective
print("objective=", pulp.value(prob.objective))