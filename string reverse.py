string = input('Enter the string: ')  #take input from user

def reverse(string):
    reverse= ''
    for character in string:
        reverse= character+reverse

    return reverse


reversed_string= reverse(string)  #reverse of given string
print('Reversed String is: ', reversed_string)  #result
