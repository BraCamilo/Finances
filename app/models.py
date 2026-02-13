from .database import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movimientos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT NOT NULL,
        tipo TEXT CHECK(tipo IN ('ingreso', 'gasto')),
        categoria TEXT,
        monto REAL NOT NULL,
        descripcion TEXT
    )
    """)

    conn.commit()
    conn.close()

def validar_tipo_movimientos(tipo):
        return tipo.lower() in ['ingreso', 'gasto']

def add_movimientos(fecha, tipo, categoria, monto, descripcion):
    if not validar_tipo_movimientos(tipo):
         print("Tipo de movimiento inválido. Debe ser 'ingreso' o 'gasto'.")
         return
    
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO movimientos (fecha, tipo, categoria, monto, descripcion)
        VALUES (?, ?, ?, ?, ?)
        """, (fecha, tipo.lower(), categoria, monto, descripcion))
        conn.commit()
        print("Movimiento agregado con éxito.")
    except Exception as e:
        print(f"Error al insertar en la base de datos: {e}")
    finally:
        conn.close()

def get_movimientos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM movimientos")
    rows = cursor.fetchall()

    conn.close()
    return rows

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