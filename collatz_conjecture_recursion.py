#imports the code from collatz_lib to be used here
from collatz_conjecture_lib import colCon

class recursion():
    def __init__(self):
        self.n_start = int(input("what number do you want to start the loop from?: "))
        self.n_end = 1+int(input("what number do you want to end the loop at?: "))

    def run(self):
        #runs all values from n_start and self terminates when reaching n_end
        endSequenceCheck = True

        while self.n_start != self.n_end:
            output = colCon().run_iteration(self.n_start)
            
            endSequenceCheck = True
            for i in range(3):
                if output[-(i+1)] == 4 or 2 or 1:
                    pass
                else:
                    endSequenceCheck = False

            print(f"value: {output[0]} | output: {output} | status: {endSequenceCheck}")
            self.n_start += 1


if __name__ == "__main__":
    recursion = recursion()
    recursion.run()
