from fastapi import FastAPI, Depends, HTTPException
from . import models, schemas, database, auth, ai_module
from sqlalchemy.orm import Session
from database import SessionLocal

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/diagnose/")
def diagnose_health(symptoms: str):
    return ai_module.diagnose_health_issues(symptoms)

@app.post("/order/")
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    medicine = db.query(models.Medicine).filter(models.Medicine.id == order.medicine_id).first()
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")
    total_price = medicine.price * order.quantity
    new_order = models.Order(user_id=order.user_id, medicine_id=order.medicine_id, quantity=order.quantity, total_price=total_price)
    db.add(new_order)
    db.commit()
    return {"message": "Order created successfully"}

@app.get("/medicines/")
def list_medicines(db: Session = Depends(get_db)):
    medicines = db.query(models.Medicine).all()
    return medicines
