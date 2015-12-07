def simple_function_without_arguments_or_return_value():
    print("Hello, world")
   
simple_function_without_arguments_or_return_value()

def function_with_arguments(print_this):
    print(print_this)
    
function_with_arguments("Hello 2")

def function_with_return_value():
    return "Hello 3"
    
print(function_with_return_value())

def function_with_arguments_and_return(x):
    return x * 2
    
print("4 * 2 is %d" % function_with_arguments_and_return(4))

def convert_to_usd(price):
    return price * 1.67

price = 9
price = convert_to_usd(price)
print(price)
