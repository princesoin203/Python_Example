# Project 3 - Employee Management System
# Author - Prince Soin
# Student ID - u3229940
import sys
import pickle
sys.path.append(".")
from Project_3_Employee_Class import EmployeeEntry
from Project_3_Employee_Class import ShiftEmployee
from Project_3_Employee_Class import Contractor


def user_input_value(user_input):
    num = -1
    while True:
        try:
            num = int(input(user_input))
            break
        except ValueError:
            print("Error: Enter an integer, try again...")
    return num


# Lookup an employee
def lookup(dictionary):
    # Look up the ID number if it is in the dictionary
    id = user_input_value('Enter the employee ID number: ')
    if id in dictionary:
        print(dictionary.get(id))
    else:
        print("That ID number was not found.")
    display_menu = True
    return display_menu


def add(dictionary):
    id = user_input_value('Enter employee ID number: ')
    name = input('Enter the name of the employee: ')
    department = input('Enter the employee department: ')
    job_title = input('Enter the employee job title: ')

    entry = EmployeeEntry(id, name, department, job_title)
    dictionary[id] = entry
    print('Employee added')

    display_menu = True
    return display_menu


def add_s(dictionary):
    id = user_input_value('Enter employee ID number: ')
    name = input('Enter the name of the employee: ')
    department = input('Enter the employee department: ')
    job_title = input('Enter the employee job title: ')
    shift_number = input('Enter the employee shift number')
    hourly_pay = input('Enter the employee hourly pay rate')

    entry = ShiftEmployee(id, name, department, job_title, shift_number, hourly_pay)
    dictionary[id] = entry
    if shift_number == '1':
        entry.set_shift_number('Day')
    elif shift_number == '2':
        entry.set_shift_number('Night')
    print('Shift Employee added')

    display_menu = True
    return display_menu


def add_c(dictionary):
    id = user_input_value('Enter employee ID number: ')
    name = input('Enter the name of the employee: ')
    department = input('Enter the employee department: ')
    job_title = input('Enter the employee job title: ')
    contract_end_date = input('Enter the employee contract end date')
    australian_business_number = input('Enter the employee australian business number')
    contract_salary = input('Enter the employee contract salary')

    entry = Contractor(id, name, department, job_title, contract_end_date, australian_business_number, contract_salary)
    dictionary[id] = entry
    print('Contractor Employee added')

    display_menu = True
    return display_menu


def change(dictionary):
    #Change employee details
    id = user_input_value('Enter the employee ID number: ')
    if id in dictionary:
        name = input('Enter the new name of the employee: ')
        department = input('Enter the new employee department: ')
        job_title = input('Enter the new employee job title: ')
        update = EmployeeEntry(id, name, department, job_title)
        dictionary[id] = update
        print('Employee updated')
    else:
        print("That ID number was not found.")
    display_menu = True
    return display_menu


def remove(dictionary):
    id = user_input_value('Enter the employee ID number: ')
    if id in dictionary:
        del dictionary[id]
        print("Employee removed")
    else:
        print("That ID number was not found.")
    display_menu = True
    return display_menu


def save_quit(dictionary):
    output_file = open('employee_data.dat', 'wb')
    pickle.dump(dictionary, output_file)
    output_file.close()

    display_menu = False
    return display_menu


def main():
    try:
        input_file = open('employee_data.dat', 'rb')
        employee_dictionary = pickle.load(input_file)
        input_file.close()

    except FileNotFoundError:
        employee_dictionary = {}

    display_menu = True
    while display_menu:
        print('\n Employee Management System\n')
        print('\t1. Lookup an employee')
        print('\t2. Add a new employee')
        print('\t3. Add a new Shift employee')
        print('\t4. Add a new Contractor employee')
        print('\t5. Change existing employee')
        print('\t6. Delete existing employee')
        print('\t7. Save and Quit\n')

        option_choice = user_input_value('Enter an option to continue: ')

        options = {
            1: lookup,
            2: add,
            3: add_s,
            4: add_c,
            5: change,
            6: remove,
            7: save_quit,
        }
        display_menu = options[option_choice](employee_dictionary)

main()
