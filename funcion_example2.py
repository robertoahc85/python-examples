def log_message():
   print('Hello World')
 
log_message()


#The function body is only executed when the function is being called, which is why, in the following example, the updated value of num is printed:
num = 0
def log_message():
   print(num)
   
num = 1
log_message()

# Why all this, you may ask? One reason is that you can call a function as often as you want. Let's try it:
def log_message():
   print('Hello World')
 
log_message()
log_message()

# What will be the output?
def func():
	print(2)
 
func()

# What will be the output?
def func():
	print(2)
 
func()

# The value specified after the return keyword is passed back to the caller of the function and can then be used for further operations:
def func():
   return 5
 
result = func()
print(result)

# Here, the print() function that follows the return statement is not executed:
def func():
  return 5
  print('I am not printed!')
 
print(func())