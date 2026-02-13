from fastapi import FastAPI
from .models import create_tables, add_movimientos, get_movimientos, balance_total



app = FastAPI(title="Api finanzas")
create_tables()

@app.get("/")
def home():
    return{"mensaje": "API de finanzas funcionando"}

#Ingresar movimientos
@app.post("/movimientos")
def crear_moviminetos(
    fecha: str,
    tipo: str,
    categoria:str,
    monto: float,
    descripcion: str =""
):

    add_movimientos(fecha, tipo, categoria, monto, descripcion)
    return {"mensaje: ": "Movimiento creado"}

#Ver movimientos
@app.get("/movimientos")
def listar_movimientos():
    return get_movimientos()

#Ver balance
@app.get("/balance")
def obtener_balance():
    ingresos, gastos, balance = balance_total()

    return {
        "ingresos": ingresos,
        "gastos": gastos,
        "balance": balance
    }


