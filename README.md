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
GET /api/singers

- Obtener un cantante por ID
GET /api/singers/{id}

- Crear un cantante
POST /api/singers

- Actualizar un cantante PUT /api/singers/{id}

- Eliminar un cantante DELETE /api/singers/{id}

JSON ejemplo para crear un cantante:

```
{
"nombre": "The Weeknd",
"edad": 34,
"genero": "soul"
}
```

JSON ejemplo para actualizar un cantante (campos opcionales):

```
{
"edad": 35
}
```



