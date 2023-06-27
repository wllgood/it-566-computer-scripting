#def entry():
    #val = input('Enter your value: ') #input function
    #print(f'{val.upper()}') #f string, upper function

def sum_numbers():
    num = input('Enter your numbers: ')
    string_array = num.split() #split function, make input into a string array
    print (string_array)

    float_array = [0] * len(string_array) #data type = float

    i = 0
    for s in string_array:
        float_array[i] = float(s)
        i += 1
    
    print(f' {float_array} ')
    print(f' Sum = {sum(float_array)} ')

    