str = "SaiTejaisapython programmer"
print("The original string is:",str)
reverse_string=""
count = len(str)
while count>0:
    reverse_string += str[count-1]
    count = count - 1
    print("The reversed string using a while loop:",reverse_string,)

