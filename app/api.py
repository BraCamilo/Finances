from fastapi import FastAPI, HTTPException
from .models import create_tables, add_movimientos, delete_movimiento, get_movimientos, balance_total
from pydantic import BaseModel

class Item(BaseModel):
    nombre: str
    descripcion: str


app = FastAPI(title="Api finanzas Personales")


create_tables()


@app.get("/")
def home():
    return{"mensaje": "API de finanzas funcionando"}

#Ingresar movimientos
@app.post("/movimientos")
def crear_moviminetos(
    fecha: str,
    descripcion: str,
    tipo: str,
    monto: float,
    Cuotas: int = 0,
    Tasa_Interes: float = 0.0,
    fecha_limite: str = None,
):

    add_movimientos(fecha, descripcion, tipo, monto, Cuotas, Tasa_Interes, fecha_limite)
    return {"mensaje": "Movimiento creado"}

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

#Eliminar movimiento
@app.delete("/movimientos/{id}")
def eliminar_movimiento(id: int):
    eliminado = delete_movimiento(id)
    
    if eliminado:
        return {"mensaje": "Movimiento eliminado correctamente"}
    else:
        raise HTTPException(
            status_code=404,
            detail="Movimiento no encontrado"
        )



