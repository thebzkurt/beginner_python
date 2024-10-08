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
            process = input("Please enter the action you want to perform.\nAdd to do (1)\nDelete to do (2)\nExit (3)\nEnter(1/2/3): ")

            if process == "1":
                valueX = input("Enter your to-do items: ")
                self.Add(valueX)
                print(self.todo_list)
            elif process == "2":
                valueX = input("Enter the to-do item to delete: ")
                while valueX not in self.todo_list:
                    print(f"\nYour list = {self.todo_list}")
                    valueX = input("Item not found, try again: ")
                self.Delete(valueX)
            elif process == "3":
                print("Exiting...")
                break
            else:
                print("Invalid input, please try again.")

if __name__ == "__main__":
    deneme = list_management()
    deneme.main()
    