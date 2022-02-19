#imports the code from collatz_lib to be used here
from collatz_conjecture_lib import colCon


class recursion():
    def __init__(self):
        self.n_start = 1
        self.n_end = 1000000000

    def run(self):
        #runs all values from n_start and self terminates when reaching n_end
        highestCycleVal=0
        CycleVal=0
        val = []
        while self.n_start != self.n_end:
            endSequenceCheck = True
            output = colCon().run_iteration(self.n_start)
            
            endSequenceCheck = True
            for i in range(3):
                if output[-(i+1)] == 4 or 2 or 1:
                    pass
                else:
                    endSequenceCheck = False
            
            if len(output) > highestCycleVal:
                highestCycleVal = len(output)
                cycleVal = output[1]
                val = output
                
            self.n_start += 1
        print(f"the highest cycle value reached was {highestCycleVal}, which was in iteration {cycleVal}, holding the value of {val}")

    
if __name__ == "__main__":
    recursion = recursion()
    recursion.run()
