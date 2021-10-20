import art

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2
  
def multiply(n1, n2):
  return n1 * n2
  
def divide(n1, n2):
  return n1 / n2

operations = {
  '+':add,
  '-':subtract,
  '*':multiply,
  '/':divide
}


def calculator():
  print(art.logo)
  num1 = float(input("Whats the first number?: "))

  for key in operations:
    print(key)

  run = True
  while run == True:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("Whats the next number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    carry_on = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or 'exit' to quit.: ")
    if carry_on == 'n':
      run = False
      calculator()
    elif carry_on == 'y':
      num1 = answer
    else: 
      return

calculator()
