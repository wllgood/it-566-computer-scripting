def list_demo():
    number_list = [1,'today','tomorrow',2,3,4,5]
    print(f'First element of number_list is: ' + str(number_list[0]))
    
    list_2 = [0] * 10
    list_2[0] = 1
    list_2[1] = 2
    list_2[9] = 10
    list_2.append(11) #add 11 to the list

    print(list_2)

    for n in list_2:
        print(f' {n} ', end='')
    
    print()

    list_2[10] = 12 #access the newly added element

    for n in list_2:
        print(f' {n} ', end='')

    for n in number_list:
        print(f' {n} ', end='')
    
    number_list[0] = "Hello, World!"

    for n in number_list:
        print(f' {n} ', end='')

    first_name = 'Winnie'

    for c in first_name:
        print(c, end='')

    print()

    number_list.extend(list_2)

    for n in list_2:
        print(f' {n} ', end='')
    
    for i in range(16):
        print(f' {i+1}, ', end='')
    
    print()

    for n in number_list[:]:
        print(f' {n} ', end='')
    
    print()

    for n in number_list[6:12]: #print a certain range within a list
        print(f' {n} ', end='')
    
    win = 'winnie' #print each character in a string separately

    for c in win:
        print(f' {c} ', end='')
    
    print()

    
