from .database import get_connection
from pydantic import BaseModel


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movimientos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT NOT NULL,
        descripcion TEXT,
        tipo TEXT NOT NULL,
        monto REAL NOT NULL,
        Cuotas INTEGER,
        Tasa_Interes REAL,
        fecha_limite TEXT
    )
    """)
    
    # Migración: Agregar columnas a bases de datos antiguas
    for col, dtype in [("Cuotas", "INTEGER"), ("Tasa_Interes", "REAL"), ("fecha_limite", "TEXT")]:
        try:
            cursor.execute(f"ALTER TABLE movimientos ADD COLUMN {col} {dtype}")
        except Exception:
            pass

    conn.commit()
    conn.close()

def validar_tipo_movimientos(tipo):
        return tipo in ['Activo', 'Pasivo Variable', 'Pasivo Fijo']


def add_movimientos(fecha, descripcion, tipo, monto, Cuotas, Tasa_Interes, fecha_limite):
    """ if not validar_tipo_movimientos(tipo):
         print("Tipo de movimiento inválido. Debe ser 'Activo', 'Pasivo Variable' o 'Pasivo Fijo'.")
         return """
    
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO movimientos (fecha, descripcion, tipo, monto, Cuotas, Tasa_Interes, fecha_limite)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (fecha, descripcion, tipo, monto, Cuotas, Tasa_Interes, fecha_limite))
        conn.commit()
        print("Movimiento agregado con éxito.")
        return True
    except Exception as e:
        print(f"Error al insertar en la base de datos: {e}")
        raise e
    finally:
        conn.close()

def get_movimientos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM movimientos ORDER BY id DESC")
    rows = cursor.fetchall()
    
    # Obtener los nombres de las columnas
    column_names = [description[0] for description in cursor.description]

    conn.close()
    
    # Convertir cada fila en un diccionario usando los nombres de las columnas
    return [dict(zip(column_names, row)) for row in rows]

def delete_movimiento(id: int) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM movimientos WHERE id = ?", (id,))
        conn.commit()
        return cursor.rowcount > 0  # True si borró algo, False si no existía
    except Exception as e:
        print(f"Error al eliminar movimiento {id}: {e}")
        conn.rollback()  # Deshace cambios si hubo error
        return False
    finally:
        conn.close()

def balance_total():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT 
        SUM(CASE WHEN tipo = 'ingreso' THEN monto ELSE 0 END),
        SUM(CASE WHEN tipo = 'gasto' THEN monto ELSE 0 END)
    FROM movimientos
    """)
    
    # fetchone() devuelve una tupla, ej: (5000.0, 2000.0)
    ingresos, gastos = cursor.fetchone()
    
    conn.close()

    # Aseguramos que si no hay datos, nos devuelva 0 en lugar de None
    ingresos = ingresos if ingresos else 0.0
    gastos = gastos if gastos else 0.0
    balance = ingresos - gastos

    return ingresos, gastos, balance


