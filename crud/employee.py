from fastapi import FastAPI, HTTPException
from models_val import Employee
from typing import List


employee_db: List[Employee] = []

app = FastAPI()


#1. Read all employees
@app.get('/employees', response_model=List[Employee])
def get_employees():
    return employee_db

#2. Read Specific employee
@app.get('/employees/{emp_id}', response_model=Employee)
def get_employee(emp_id:int):
    for index, employee in enumerate(employee_db):
        if employee.id == emp_id:
            return employee_db[index]
        
    raise HTTPException(status_code=404, detail='Employee Not Found')

#3. Add an Employee
@app.post('/employees')
def add_employee(new_emp: Employee):
    for employee in employee_db:
        if employee.id == new_emp.id:
            raise HTTPException(status_code=404, detail='Employee id already exists')
    employee_db.append(new_emp)
    return new_emp


#4. Update an employee
@app.put('/update_employee')
def update_employee(emp_id:int, updated_employee:Employee):
    for index, employee in enumerate(employee_db):
        if employee.id == emp_id:
            employee_db[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee Not Found")


#5. Delete Employee
@app.delete('/delete_employee/{emp_d}')
def delete_employee(emp_id:int):
    for index, employee in enumerate(employee_db):
        if employee.id == emp_id:
            del employee_db[index]
            return {'message': 'Employee deleted successfully'}
    raise HTTPException(status_code=404, detail="Employee Not Found")