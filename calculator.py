
#list 
work_list = ["+","-","x","/",]
ask_list = ["c", "f"]

#velues
ts_value = 0


nmbr_1 = int(input("first transaction number = "))
while True:
    process = input("Choose one of the operations to be done = ( + , - , x , / ) : ")
    if process in work_list:
        break
    else:
        print("Invalid operation. Please try again.")

def process_control(nmbr_1, nmbr_2, process, ):
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
            return "Error: Division by zero!"
    else:
        return "Error: Invalid operation!"


nmbr_2 = int(input("second transaction number = "))
ts_value = process_control(nmbr_1, nmbr_2, process)
print("********************************")
print(f"Result = {ts_value}")

def process_control2(ts_value, nmbr_3, process, ):
    if process == "+":
        return ts_value + nmbr_3
    elif process == "-":
        return ts_value - nmbr_3
    elif process == "x":
        return ts_value * nmbr_3
    elif process == "/":
        if nmbr_3 != 0:
            return ts_value / nmbr_3
        else:
            return "Error: Division by zero!"
    else:
        return "Error: Invalid operation!"

while True:
    ask = input("\nContiun(c) or Finish(f) = ")
    if ask in ask_list:
        if ask.lower() == "c":
            while True:
                process = input("\nChoose one of the operations to be done = ( + , - , x , / ) : ")
                if process in work_list:
                    break
                else:
                    print("Invalid operation. Please try again.")
            nmbr_3 = int(input("next transaction number = "))
            ts_value = process_control2(ts_value, nmbr_3, process,)
            print("********************************")
            print(f"Result = {ts_value}")
        elif ask.lower() == "f":
            print("********************************")
            print(f"Finish result = {ts_value}")
            print("********************************")
            break
    else:
        print("Invalid operation. Please try again.")




    









