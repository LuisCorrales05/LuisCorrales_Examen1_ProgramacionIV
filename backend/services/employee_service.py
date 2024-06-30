from model.employee import Employee

class EmployeeService:
    def __init__(self):
        self.employees = {}
        self.next_employee_id = 1

    def create_employee(self, name, email, number):
        employee_id = self.next_employee_id
        self.next_employee_id += 1
        employee = Employee(employee_id, name, email, number)
        self.employees[employee_id] = employee
        return employee
    
    def get_employee(self, employee_id):
        return self.employees.get(employee_id)
    
    def update_employee(self, employee_id, name, email, number):
        if employee_id in self.employees:
            employee = self.employees[employee_id]
            employee.name = name
            employee.email = email
            employee.number = number
            return employee
        
    def delete_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            return True
        return False
    
    def get_all_employees(self):
        return [employee.serialize() for employee in self.employees.values()]