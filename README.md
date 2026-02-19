💰 API de Finanzas Personales

API backend para gestionar ingresos y gastos personales, desarrollada en Python con enfoque en simplicidad, control local de datos y despliegue en infraestructura propia (self-hosted).

El proyecto permite registrar movimientos financieros, consultarlos y calcular balances, sirviendo como base para automatización personal, dashboards o integración con otras aplicaciones web.

🎯 Objetivo del proyecto

Crear un servicio backend ligero y gratuito para administrar finanzas personales sin depender de plataformas externas, con capacidad de:

Registrar ingresos y gastos

Consultar movimientos

Calcular balance financiero

Servir datos a cualquier frontend o sistema externo

Desplegarse en un servidor personal

Este proyecto nace como alternativa libre a herramientas de automatización pagas, priorizando aprendizaje técnico y control de datos.

🧱 Tecnologías utilizadas
Backend

Python 3

FastAPI → Framework moderno para crear APIs web rápidas y tipadas

Uvicorn → Servidor ASGI que ejecuta la aplicación

Base de datos

SQLite → Base de datos local embebida, sin servidor externo

Modelado de datos

Pydantic → Validación automática de datos de entrada

Arquitectura

API REST

Persistencia local

Separación por módulos (API, base de datos, modelos)


finanzas/
│
├── app/
│   ├── __init__.py
│   ├── api.py          # Endpoints FastAPI
│   ├── models.py       # Esquemas de datos y funciones DB
│   ├── database.py     # Conexión SQLite
│
├── data/
│   └── finanzas.db     # Base de datos local
│
└── requirements.txt

⚙️ Instalación
1️⃣ Clonar repositorio
git clone <repo>
cd finanzas

2️⃣ Crear entorno virtual
python -m venv venv
venv\Scripts\activate

3️⃣ Instalar dependencias
pip install fastapi uvicorn

▶️ Ejecutar el servidor
uvicorn app.api:app --reload


Servidor disponible en:

http://127.0.0.1:8000


Documentación interactiva:

http://127.0.0.1:8000/docs

🔌 Endpoints disponibles
Crear movimiento

POST /movimientos

Registra ingreso o gasto.

Campos:

fecha

tipo (ingreso | gasto)

categoria

monto

descripcion

Obtener movimientos

GET /movimientos

Devuelve todos los registros financieros.

Obtener balance total

GET /balance

Retorna:

total ingresos

total gastos

balance neto

Actualizar movimiento

PUT /movimientos/{id}

Modifica un registro existente.

Eliminar movimiento

DELETE /movimientos/{id}

Elimina un movimiento por ID.

🧠 Características técnicas

✔ Validación automática de datos
✔ Persistencia local sin servidor externo
✔ API desacoplada del frontend
✔ Documentación automática
✔ Preparado para despliegue en servidor personal
✔ Base para automatización financiera

🚀 Posibles mejoras futuras

Autenticación de usuarios

Dashboard web

Integración con hojas de cálculo

Exportación de reportes

Categorización automática

Integración con nube personal

Dockerización

Backup automático

🏠 Filosofía del proyecto

Este sistema está diseñado para ejecutarse en infraestructura propia del usuario, manteniendo privacidad de datos financieros y control total sobre la información.
