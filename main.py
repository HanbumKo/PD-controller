import matplotlib.pyplot as plt

from PD import PD

# System parameters
goal_value = 5
disturbance = -0.1

# Time parameters
FPS = 60
dt = 1/FPS
total_time = 1

# PD parameters
Kp = 50
Kd = 0.01
output = 0

pd = PD(goal=goal_value, dt=dt, p=Kp, d=Kd)

goals = []
outputs = []
adjusts = []
steps = []

for i in range(total_time * FPS):
    # Get how much adjust from pd controller
    adjust = pd.next(output)

    goals.append(goal_value)
    outputs.append(output)
    adjusts.append(adjust)
    steps.append(i)

    # output from system
    output = output + adjust*dt
    output = output + disturbance*dt


plt.plot(steps, goals, label="goals")
plt.plot(steps, outputs, label="outputs")

plt.ylim((0, goal_value*2))
plt.legend()

plt.show()
