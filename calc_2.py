class Calculator:
    def __init__(self):
        self.work_list = ["+", "-", "x", "/"]
        self.ask_list = ["c", "f"]
        self.ts_value = 0

    def get_number(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_process(self):
        while True:
            process = input("Choose one of the operations to be done ( + , - , x , / ) : ")
            if process in self.work_list:
                return process
            else:
                print("Invalid operation. Please try again.")

    def calculate(self, nmbr_1, nmbr_2, process):
        if process == "+":
            return nmbr_1 + nmbr_2
        elif process == "-":
            return nmbr_1 - nmbr_2
        elif process == "x":
            return nmbr_1 * nmbr_2
        elif process == "/":
            if nmbr_2 != 0:
                return nmbr_1 / nmbr_2
            else:
                print("Error: Division by zero!")
                return None

    def main(self):
        nmbr_1 = self.get_number("First transaction number = ")
        process = self.get_process()
        nmbr_2 = self.get_number("Second transaction number = ")
        self.ts_value = self.calculate(nmbr_1, nmbr_2, process)
        if self.ts_value is not None:
            print("********************************")
            print(f"Result = {self.ts_value}")

        while True:
            ask = input("\nContinue (c) or Finish (f) = ").lower()
            if ask in self.ask_list:
                if ask == "c":
                    process = self.get_process()
                    nmbr_3 = self.get_number("Next transaction number = ")
                    self.ts_value = self.calculate(self.ts_value, nmbr_3, process)
                    if self.ts_value is not None:
                        print("********************************")
                        print(f"Result = {self.ts_value}")
                elif ask == "f":
                    print("********************************")
                    print(f"Final result = {self.ts_value}")
                    print("********************************")
                    break
            else:
                print("Invalid input. Please try again.")

if __name__ == "__main__":
    calc = Calculator()
    calc.main()