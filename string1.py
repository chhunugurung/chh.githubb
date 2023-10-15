while True:
    string = input("please Enter two words or 'done' to terminate the program: ")
    if string == 'done':  # for terminating program.
        print("The program is terminated.")
        break

    words = string.split()

    if len(words) == 1:
        print("please enter two words again.")
    elif len(words) == 2:
        word1 , word2 = words
        if word1 < word2:
            print("The word that comes before them in lexicological order is: ", word1)
        else:
            print("The word that comes before them in lexicological order is:", word2) 
    else:
        print("invalid input, please try again")        