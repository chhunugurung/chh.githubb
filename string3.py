num_count = 0
upper_cont = 0
lower_count = 0
others_count = 0

input_string = input("Enter the string: ")
for char in input_string:
    if char.isnumeric():
        num_count = num_count + 1
    elif char.isupper():
        upper_cont = upper_cont + 1
    elif char.islower():
        lower_count = lower_count + 1
    else:
        others_count = others_count + 1

print("number of numbers counted is:", num_count) 
print("number of upper letter counted is:", upper_cont) 
print("number of lower letter counted is:", lower_count) 
print("number of other char counted is:", others_count)                    