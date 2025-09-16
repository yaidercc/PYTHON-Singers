# Singers Api

## Requisitos

- Python **3.8+**
- Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar el proyecto

En la raíz del proyecto, correr:

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:

-> http://127.0.0.1:8000

Documentación automática:

-> Swagger UI → http://127.0.0.1:8000/docs

-> Redoc → http://127.0.0.1:8000/redoc

## Endpoints

- Obtener todos los cantantes
GET /singers

- Obtener un cantante por ID
GET /singers/{id}

- Crear un cantante
POST /singers

JSON ejemplo:

```
{
"nombre": "The Weeknd",
"edad": 34,
"genero": "soul"
}
```

- Actualizar un cantante

PUT /singers/{id}

Body JSON ejemplo (campos opcionales):

```
{
"edad": 35
}
```

- Eliminar un cantante
DELETE /singers/{id}