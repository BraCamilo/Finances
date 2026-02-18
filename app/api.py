from fastapi import FastAPI, HTTPException
from .models import MovimientoUpdate, create_tables, add_movimientos, get_movimientos, balance_total
from pydantic import BaseModel

class Item(BaseModel):
    nombre: str
    descripcion: str


app = FastAPI(title="Api finanzas")


create_tables()

@app.put("/movimientos/{id}")
def actualizar_movimiento(id: int, movimiento: MovimientoUpdate):
    # 1. buscar registro existente
    registro = db.buscar_por_id(id)

    if not registro:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")

    # 2. actualizar datos
    registro.fecha = movimiento.fecha
    registro.tipo = movimiento.tipo
    registro.categoria = movimiento.categoria
    registro.monto = movimiento.monto
    registro.descripcion = movimiento.descripcion

    # 3. guardar cambios
    db.guardar(registro)

    return {"mensaje": "actualizado", "item": registro}

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

#Actualizar movimientos

