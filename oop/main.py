from person import Person
from student import Student
import json

def main():
    # Need to create an instance of Person
    
    '''p1.set_first_name('Yin')
    print(f'p1.first_name: {p1.first_name}')

    p2 = Person()
    p2.first_name = 'Rick'
    print(f'p2.first_name: {p2.first_name}')
'''
    p1 = Person('Rick', 'Warren', 'Miller')

    print(f'p1 = {p1.first_name}')


    s1 = Student('Jonathan', 'J', 'Ashford', '12345', 'Cybersecurity')
    print(f's1.first_name: {s1.first_name} Major: {s1.major}')
    print(f'{s1}')

    s2 = Student('Tony', 'R', 'Nyugen', '2345', 'Cybersecurity')
    print(f'{s2}')

    p2 = Person("Steve", "W", "Smith")


    students = [p1, s1, s2]

    for s in students:
        print(f'{s}')

    student_dictionary = {"s1": json.loads(s1.toJSON()), "s2": json.loads(s2.toJSON())}
    print(json.dumps(student_dictionary))

if __name__ == '__main__':
    main()

