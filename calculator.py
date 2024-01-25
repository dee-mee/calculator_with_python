#this project showcases my skills after finishing python
#essentials 1 in cisco
def operations(num1=0, num2=0):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Operations include\n1.Addition,\n2.Subtraction,\n3.Multiplication,\n4.Division")
    choice = input("choose an opeartion based on its number.")
    if choice == '1' :
        print("The sum is ",num1 + num2)
    elif choice == '2':
        print("The result of Subtraction is ",num1 - num2)
    elif choice == '3':
        print("The result of the operation is ,", num1 * num2)
    elif choice == '4':
        while num1 > 1:
            try:
                print("The result of Division is ",num1 / num2)
                break
            except ZeroError:
                print("Please enter a VALUE bigger than that.")
    else:
        print("That operation is currectly not available")

operations()
