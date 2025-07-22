numberLargest = int(input("Enter Largest number : "))
numberSmallest = int(input("Enter Smallest number : "))

while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberLargest
    numberLargest = numberStore

print("HFC is  : ",numberLargest)