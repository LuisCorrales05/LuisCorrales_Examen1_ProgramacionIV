class Employee:
    def __init__(self, employee_id, name, email, number):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.number = number
        
    def serialize(self):
        return {
            'employee_id': self.employee_id,
            'name': self.name,
            'email': self.email,
            'number': self.number
        }