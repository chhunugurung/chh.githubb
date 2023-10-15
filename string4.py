while True:
    input_string = input("Please enter the string or 'done' to terminate the program: ")
    if input_string.lower()== 'done':
        print("The program is terminated")
        break
    converted_string = ""

    for char in input_string:
        if char.isalpha():
            converted_string = converted_string + char.upper()
        elif char  not in  (',','.',':','!','?'):
            converted_string = converted_string + char
    print("converted string:", converted_string)           