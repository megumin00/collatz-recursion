#imports the code from collatz_lib to be used here
from collatz_conjecture_lib import colCon

class recursion():
    def __init__(self):
        self.n_start = 1
        self.n_end = 100

    def run(self):
        #runs all values from n_start and self terminates when reaching n_end
        while self.n_start != self.n_end:
            output = colCon().run_iteration(self.n_start)
            
            strOutput=""
            for i in output:
                
                strOutput+=str(i)
                if i != 1:
                    strOutput+=','
                
            print(strOutput)
            self.n_start += 1


if __name__ == "__main__":
    recursion = recursion()
    recursion.run()
