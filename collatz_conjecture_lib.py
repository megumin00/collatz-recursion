#creates a class for collatz_recursion to use.
#same code as collatz_demo, just inside a class to be used for collatz_recursion, documentation is in collatz_demo
class colCon():
    def __init__(self):
        self.breakToggle = False
        self.breakCounter = 0
        self.n_list = []

    def run_iteration(self, n):
        while True:
            self.n_list.append(n)

            if (n % 2) == 0:
                if n == 4:
                    self.breakToggle = True
                n /= 2

            else: 
                n = 3*n+1

            n = int(n)

            if self.breakToggle == True:
                self.breakCounter += 1

            if self.breakCounter == 3:
                return self.n_list



