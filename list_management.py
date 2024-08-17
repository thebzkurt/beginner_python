class list_management:
    def __init__(self):
        self.todo_list = []

    def Delete(self, value):
        if value in self.todo_list:
            self.todo_list.remove(value)
            print(f"{value} has been removed from your to-do list.")
        else:
            print(f"{value} is not in your to-do list.")


    def Add(self, value):
        self.todo_list.append(value)

    def main(self):
        while True:
            print(f"\nYour to do list = {self.todo_list}")
            self.process = input("Please enter the action you want to perform.\nAdd to do (1)\nDelete to do (2)\nExit (3)\nEnter(1/2/3): ")

            if self.process == "1":
                self.valueX = input("Enter your to-do items: ")
                self.Add(self.valueX)
                print(self.todo_list)
            elif self.process == "2":
                while True:
                    valueX = input("Enter the to-do item to delete: ")
                    print(f"\n list = {self.todo_list}")
                    if valueX in self.todo_list:
                        self.Delete(valueX)
                        break
                    else:
                        print("object not found try again")
            elif self.process == "3":
                print("Exiting...")
                break
            else:
                print("Invalid input, please try again.")

if __name__ == "__main__":
    deneme = list_management()
    deneme.main()
    