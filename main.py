from application import salary, people
import datetime
print(datetime.datetime.today())
print()

if __name__ == '__main__':
    print(salary.calculate_salary("300$"))
    print(people.get_employees("100 people"))
