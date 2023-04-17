class triathlon():
    def __init__(self, first_name, last_name, swim, cycle, run):
        self.first_name = first_name
        self.last_name = last_name
        self.swim_time = swim
        self.cycle_time = cycle
        self.run_time = run
        self.total_time = self.run_time + self.cycle_time + self.swim_time
    def info(self):
        print(self.first_name +'·'+ self.last_name +'.', 'swim:', self.swim_time, 'cycle:', self.cycle_time, 'run:'
              , self.swim_time, 'total:', self.total_time)

a = triathlon('Robert', 'Young', 15, 33, 10)
a.info()
