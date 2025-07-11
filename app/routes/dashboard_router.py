from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from app.database.db import SessionLocal
from sqlalchemy.orm import Session
from app.models.alerta import Alerta, order_by




router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Dependência para obter o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@router.get("/dashboard")
def exibir_dashboard(request: Request, db: Session = Depends(get_db)):
    alertas = db.query(Alerta),order_by(Alerta.data_envio.desc()).all()
    return templates.TempalateResponse("dasboard.html", {"request": request, "alertas": alertas})