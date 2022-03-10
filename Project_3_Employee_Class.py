# Project 3 - Employee Management System
# Author - Prince Soin
# Student ID - u3229940

class EmployeeEntry:
    def __init__(self, id, name, department, job_title):
        self.__id = id
        self.__name = name
        self.__department = department
        self.__job_title = job_title

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    def __str__(self):
        return ("Name: " + self.__name + '\n'
                ", ID Number: " + str(self.__id) + '\n'
                ", Department: " + self.__department + '\n'
                ", Job Title: " + self.__job_title)


class ShiftEmployee(EmployeeEntry):
    def __init__(self, id, name, department, job_title, shift_number, hourly_pay):
        super().__init__(name, id, department, job_title)
        self.__id = id
        self.__name = name
        self.__department = department
        self.__job_title = job_title
        self.__shift_number = shift_number
        self.__hourly_pay = hourly_pay

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_pay(self, hourly_pay):
        self.__hourly_pay = hourly_pay

    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_pay(self):
        return self.__hourly_pay

    def __str__(self):
        return ("Name: " + self.__name + '\n'
                ", ID Number: " + str(self.__id) + '\n'
                ", Department: " + self.__department + '\n'
                ", Job Title: " + self.__job_title + '\n'
                ", Shift: " + self.__shift_number + '\n'
                ", Hourly Pay: " + self.__hourly_pay)


class Contractor(EmployeeEntry):
    def __init__(self, id, name, department, job_title, contract_end_date, australian_business_number, contract_salary):
        super().__init__(id, name, department, job_title)
        self.__id = id
        self.__name = name
        self.__department = department
        self.__job_title = job_title
        self.__contract_end_date = contract_end_date
        self.__australian_business_number = australian_business_number
        self.__contract_salary = contract_salary

    def set_contract_end_date(self, contract_end_date):
        self.__contract_end_date = contract_end_date

    def set_australian_business_number(self, australian_business_number):
        self.__australian_business_number = australian_business_number

    def set_contract_salary(self, contract_salary):
        self.__contract_salary = contract_salary

    def get_contract_end_date(self):
        return self.__contract_end_date

    def get_australian_business_number(self):
        return self.__australian_business_number

    def get_contract_salary(self):
        return self.__contract_salary

    def __str__(self):
        return ("Name: " + self.__name + '\n'
                ", ID Number: " + str(self.__id) + '\n'
                ", Department: " + self.__department + '\n'
                ", Job Title: " + self.__job_title + '\n'
                ", Contract End Date: " + self.__contract_end_date + '\n'
                ", Australian Business Number: " + self.__australian_business_number + '\n'
                ", Contract Salary: " + self.__contract_salary)

