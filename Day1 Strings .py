# Basic of Python Programming 

#Strings

a="My cast is Khan" # a.casefold() function will convert all the string into lower letter
print(a.casefold())
print("String function count")
print(a.count("a")) # return the number of specific characters in the string
print("String function find")
print(a.find("a")) # return the index position of the specific character , if the character isn't present then it will return -1
print("String function index")
print(a.index("st")) # return the index position of the character  , if not found it will raise a valueError .
print("String function isalnum")
print("khan2".isalnum()) # It will return True if there is any integer in the string , return False is all the character are letter
print("String function isalpha()")
print("Haseen".isalpha()) # Return True if all the character are only letter , Return False if there is any space ,special character or  digit in the string
print("String function isascii()")
print(a.isascii()) # return True if all the characters have ascii value . empty string have also ascii value 
print("String function casefold ")
print(a.casefold()) # convert the string into lower case 
print("String function isdecimal ")
print("4".isdecimal()) # it will return True if the number is integer , and return False if the number is floating  point,negative number will also return False
print("String function isdigit ")
print("9".isdigit()) # it will return True if the number is integer , and return False if the number is floating  point,negative number will also return False
print("-4".isnumeric()) # it will return True if the number is integer , and return False if the number is floating  point,negative number will also return False
print("String function split")
print("My,Name,is,Khan".split(",")) # it will convert a string into a list 
print("String join function ")
print("".join(["1","2","3","4","5","6"])) # join function is a reverse of a split function, it will convert list into a string
print("String function removeprefix")
print("rereading".removeprefix("re")) # this function is used to remove prefix of the string , you have to pass the prefix is as arguement
print("String function removesuffix")
print("usefull".removesuffix("full")) # it is the reverse of the removprefix function , it will remove the suffix of the string
print("String function swapcase")
print("My name is Khan".swapcase()) # it will convert the upper case letter into lower and vice versa,
print("String function strip ")
print("*****My name is Haseen####?????#".strip("*?#")) # it will remove the inappropriate spaces , special words or anything else , you will have to pass as arguement which you need to remove, by default it can remove only spaces,
print("Similar function lstrip and rstrip") # it will remove from left side only , and Right side only ,
print("""khan is brand 
      kpk is a provience 
      bannu is a disrict """.splitlines())
print("String function len ()")
print(len("My name is Haseen Ullah Khan "))