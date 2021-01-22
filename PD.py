class PD:
    def __init__(self, goal, dt, p=1, d=1):
        self.p = p
        self.d = d
        self.goal = goal
        self.dt = dt
        
        self.prev_output = 0

    def next(self, output):
        error = self.goal - output
        d_output = output - self.prev_output

        new_output = self.p*error - self.d*(d_output/self.dt)

        self.prev_output = new_output

        return new_output
