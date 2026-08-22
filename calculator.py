def calculator ():
  
 print("Simple Python Calcuator")
 print("Operations:+, -, *, /, **, %")
 print("Type 'q' to quit\n")
  
 while True:
 try:
expression = input ("Enter expression (e.g. 12 + 5:").strip ()

if expression.lower() in ('q', 'quit', 'exit'):
print("Goodbye!")
break
result = eval(expression, {"__builtins__:{}},{})
print(f"Result:{result}\n")
                           
except ZeroDivisionError:
print("Error: Division by zero\n")
except Exception:
print("Invalid expression. Try again.\n")
                            
if__name__=="__main__":
calculator()
