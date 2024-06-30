from flask import jsonify

def employee_response(employee):
    response = {
        'status': 'success',
        'employee': {
            'name': employee.name,
            'email': employee.email,
            'number': employee.number
        }
    }
    return jsonify(response)