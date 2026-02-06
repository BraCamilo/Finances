from models import create_tables, add_movimientos, get_movimientos, balance_total

def balance():
    # Llamamos a la función y desempaquetamos los valores
    ing, gas, bal = balance_total()

    print("--- RESUMEN FINANCIERO ---")
    print(f"Total Ingresos: ${ing:,.2f}")
    print(f"Total Gastos:   ${gas:,.2f}")
    print(f"--------------------------")
    print(f"Balance Neto:   ${bal:,.2f}")

if __name__ == "__main__":
    create_tables()
    print("Base de datos creada correctamente.")

    add_movimientos(
        fecha="2024-06-01",
        tipo="gasto",
        categoria="comida",
        monto=20000,
        descripcion="Snasck en el almuerzo"
    )
    print("Movimiento agregado correctamente.")

    movimientos = get_movimientos()
    for m in movimientos:
        print(m)

    balance()



    

