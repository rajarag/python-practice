input_string=input("enter the any string:")
length=len(input_string)
print("the length of strng",length)
unique_char=set(input_string)
for char in unique_char:
    count=input_string.count(char)
    print(f"{char}:{count}")
    #f means formated strimg literals
