'''
def entry():
    val = input('Enter your value: ') #input function
    print(f'{val.upper()}') #f string, upper function
'''


def sum_numbers():
    num = input('Enter your numbers separated by spaces: ')
    string_array = num.split() #split function, make input into a string array
    print (string_array)

    float_array = [0] * len(string_array) #len operate to define the length of array

    i = 0
    for s in string_array:
        float_array[i] = float(s) #change data type into float
        i += 1
    
    print(f' {float_array} ')
    print(f' Sum = {sum(float_array)} ')
    avg = sum(float_array)/len(float_array)
    print(f' Average: {avg} ')


