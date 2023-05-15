from art import logo

print(logo)



def add(n1, n2):
  return n1 + n2 
def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2 

def divide(n1, n2):
  return n1 / n2 
## Adding function to a dictionnary 
operators = {
            "+": add, 
            "-": substract, 
            "*": multiply, 
            "/": divide
           }

def caculator():
  
  num1 = float(input("What's the first numbers?: "))
  continue_operation = True
  #print all operation in screen
  for operator in operators: 
    print(operator)
  
  #select the operation
  while continue_operation:   
    operation = input("select your operation from the line above ")
    
    num2 = float(input("What's the second number?: "))
    
    # use operation as key to select function in dictionary
    caculation_function = operators[operation]
    
    answer = caculation_function(num1, num2)
    
    print(f"{num1} {operation} {num2} = {answer}")
  
    another_calculation = input(f"Type 'y' to continue calculation with {answer} or type 'r' to restart, or e to exit ").lower()

    print(another_calculation)
    if another_calculation == 'r':
      caculator()
    elif another_calculation == 'y':
      num1 = answer
    else: 
      continue_operation = False
  
    

caculator()