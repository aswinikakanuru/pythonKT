#STRINGS
#Strings Are Immutable
#String methods are len(),upper(),lower(),capitalize(),title(),strip(),lstrip(),
# rstrip(),replace(),split(),join(),find(),count(),startswith(),endswith(),
# isalpha(),isdigit(),isalnum()
name="Prasad"
print(name)
print(type(name))
print(name[2])

#String slicing -> string[start:end]
name = " i am aswini "
print(name[2:5])
print(name[:3])
print(name[2:])
print(name[::-1])#[::-1] is a common way to reverse a string.
print(len(name))
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.strip())
print(name.lstrip())
print(name.rstrip())
print(name.replace("santhosh","aswini"))
print(name.split())
#print(name.join())
print(name.count("i"))
print(name.startswith("a"))
print(name.endswith("i"))

#isalpha() Checks whether all characters are alphabetic.
names="santhosh"
print(names.isalpha())

#isdigit() Checks whether all characters are alphabetic.
num="12345"
print(num.isdigit())

#isalnum()Checks whether the string contains only letters and numbers.
value = "Aswini123"

print(value.isalnum())



