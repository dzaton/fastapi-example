## Debes crear un proyecto desde 0 en Fastapi, que tenga un endpoint "/candidato", que debe ser un método POST que reciba el DNI, Nombre y Apellido, que escriba esos datos en un sqlite.

# Instalación:
Abre la terminal desde el root del proyecto y escribe:
- python -m venv env
- .\env\Scripts\activate
- pip install -r requirements.txt

# Funcionamiento:
Abre el proyecto en Visual Studio Code y dale el icono de play cuando estes posicionado en el main.py
## Endpoints
- [POST] /candidate/create: crea un candidato si no existe en la BBDD
- [GET]  /candidate/list: lista todos los candidatos

# TODO
- Añadir logger


