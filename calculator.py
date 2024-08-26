def calculator():
    try:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))

        operation= input("Enter the operation(+,-,*,/):")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result= num1 - num2
        elif operation == '*':
            result = num1*num2
        elif operation =='/':
            if num2!=0:
                result = num1 / num2
            else:
                return"Error: division by zero is not allowed."
        else:
            return "Invalid operation.please use +,-,*, or /."
        return f"the result of{ num1}  {operation}  {num2} is: {result}"
    except ValueError:
      return "Invalid input.please enter numeric values."
    
print(calculator())



         

