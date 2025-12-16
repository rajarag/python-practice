s=input("enter a string:")
output=""
for char in s:
    if char.isalpha():
        x=char
    else:
        d=int(char)
        output=output+x*d
print(output)

#second
input=input("enter the string:")
d=set(input)
print(len(d))




        