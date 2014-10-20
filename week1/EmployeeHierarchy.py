class Employee:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def weeklyPay(hours):


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_wage):
        super().__init__(name)
        self.hourly_wage = hourly_wage


class SalariedEmployee(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.annual_salary = annual_salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name)
        self.salary = salary
        self.bonus = bonus


staff = []
staff.append(HourlyEmployee("Morgan, Harry", 30.0))
staff.append(SalariedEmployee("Lin, Sally", 52000.0))
staff.append(Manager("Smith, Mary", 104000.0, 50.0))
for employee in staff:
    print(employee.getName())