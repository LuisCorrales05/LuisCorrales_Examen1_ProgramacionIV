from flask import Flask, render_template, request, redirect, url_for, Blueprint, jsonify
from services.employee_service import EmployeeService

employee_blueprint = Blueprint('employee', __name__)
employee_service = EmployeeService()

@employee_blueprint.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    number = data.get('number')

    if not name or not email or not number:
        return jsonify({'status': 'error', 'message': 'Invalid input data'}), 400

    try:
        employee = employee_service.create_employee(name, email, number)
        return jsonify(employee.serialize()), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@employee_blueprint.route('/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = employee_service.get_employee(employee_id)
    if employee:
        return jsonify(employee.serialize())
    return jsonify({'status': 'error', 'message': 'Employee not found'}), 404

@employee_blueprint.route('/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.json
    name = data.get('name')
    email = data.get('email')
    number = data.get('number')

    if not name or not email or not number:
        return jsonify({'status': 'error', 'message': 'Invalid input data'}), 400
    
    employee = employee_service.update_employee(employee_id, name, email, number)
    if employee:
        return jsonify(employee.serialize())
    return jsonify({'status': 'error', 'message': 'Employee not found'}), 404

@employee_blueprint.route('/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    if employee_service.delete_employee(employee_id):
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error', 'message': 'Employee not found'}), 404

@employee_blueprint.route('/employees', methods=['GET'])
def get_employes():
    employee = employee_service.get_all_employees()
    if employee:
        return employee
    return jsonify({'status': 'error', 'message': 'Employee not found'}), 404