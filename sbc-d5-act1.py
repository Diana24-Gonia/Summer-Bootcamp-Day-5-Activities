corrupt = []

corrupt.append(int(input("Enter number 1: ")))
corrupt.append(int(input("Enter number 2: ")))
corrupt.append(int(input("Enter number 3: ")))
corrupt.append(int(input("Enter number 4: ")))
corrupt.append(int(input("Enter number 3: ")))

print("Display User Numbers:", corrupt)

act =""

if act == "naa":
    corrupt.pop(0)
    print("Result sa queue boss: ", corrupt)

elif act == "wala": 
    corrupt.pop()
    print("Result sa stack boss: ", corrupt)
    corrupt.append(int(input("Enter add number: ")))
    corrupt.append(int(input("Enter add number: ")))
    print("insert add number result: ", corrupt)

else:
    print("Invalid input. kung dili Naa or Wala.")
