# Actividad 2

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.x
- PostgreSQL
- Virtualenv (recomendado)

## Instalación y Configuración

1. **Crear y activar entorno virtual:**

```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

2. **Instalar dependencias:**

```bash
pip install flask psycopg2
```

## Endpoints de la API (Temperaturas)

| Método | Endpoint                    | Descripción                         |
| ------ | --------------------------- | ----------------------------------- |
| `GET`  | `/api/temperatures/average` | Temperatura media global.           |
| `GET`  | `/api/temperatures/max`     | Temperatura máxima registrada.      |
| `GET`  | `/api/rooms/<id>/name`      | Obtiene el nombre de la habitación. |
| `GET`  | `/api/rooms/<id>/average`   | Media histórica de una habitación.  |
| `GET`  | `/api/rooms/<id>/min-stats` | Mínima y nombre (JSON).             |

## Uso de la API

1. Inicia el servidor:

```bash
python app.py
```

2. Abre tu navegador en `http://127.0.0.1:5000/`.
3. Navega por la interfaz para gestionar tus libros o utiliza herramientas como Postman para probar la API de temperaturas.
