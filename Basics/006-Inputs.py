#There are primaraly 2 input methods in python2

#lets define a variable
var=1234567890987654321


#1

inp=input("I can also put a prompt here. Input 'var' : ")
#is used to input an expression
#this means this can be calculated and may contain :
#   variable names
#   function calls
#   any fucking thing that you can put inside a print statement really.
print inp
#if the input above done by the user is 'var',
#then this will print out the value of var.
def sub(a,b):
    return a-b

inp=input("Input 'sub(var,1234567880887654321)' : ")
print inp
#here we make the user input a function call
#and the print statement evaluates it before printing


#2

inp=raw_input("I can also put a prompt here. Input 'var' : ")
#is used to input anything in the form of string
print inp
#if the input above done by the user is 'var',
#then this will print out the string 'var'.


inp=raw_input("Input 'sub(var,1234567880887654321)' : ")
print inp
#here we make the user input a function call
#and get nothing but disappointment

#we can also use standard type-casting functions to input other formats
this_is_a_number=int(raw_input("Give me a number, nigga, 100% nigga : "))
print this_is_a_number
