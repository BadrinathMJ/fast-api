import models, crud, schemas
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessioLocal, Base
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()


#Dependency with DB
def get_db():
    db = SessioLocal()
    try:
        yield db
    finally:
        db.close()

#Endpoints
# 1. Create an employee 
@app.post('/employees', response_model=schemas.EmployeeOut)
def creat_employees(employess:schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employees(db, employess)

# 2. get all employees
@app.get('/employees', response_model=List[schemas.EmployeeOut])
def get_employees(db:Session = Depends(get_db)):
    return crud.get_employees(db)

# 3. Get the specific employee
@app.get('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def get_employee(emp_id:int, db:Session= Depends(get_db)):
    employee = crud.get_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee not Found')
    return employee

#4. Update an employee
@app.put('/employee/{emp_id}', response_model=schemas.EmployeeOut)
def update_employee(emp_id:int, employee:schemas.EmployeeUpdate, db:Session=Depends(get_db)):
    db_employee = crud.update_employee(db, emp_id, employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail='Employee not Found')
    return db_employee

#5. Delete Employee
@app.delete('/employees/{emp_id}', response_model=dict)
def delete_employee(emp_id:int, db: Session = Depends(get_db)):
    employee = crud.delete_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee not Found')
    return {'detail':'Employee Deleted'}
