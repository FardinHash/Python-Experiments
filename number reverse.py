n= int(input('Enter the number: '))  #take input from user

def reverse_num(number):
    reverse= 0
    while (number>0):
        last_digit= number%10
        reverse= reverse* 10 +last_digit
        number= number//10
    return reverse


reverse= reverse_num(n)  #reverse of given number

print('Reversed Number is: ', reverse)  #result
