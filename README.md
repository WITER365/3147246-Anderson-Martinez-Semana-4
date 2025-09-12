API Inicial con FastAPI - Bootcamp

Autor: Andersopmn
Contacto: WITER365@users.noreply.github.com.

Privacidad: Correo configurado como privado siguiendo las recomendaciones de GitHub
Fecha de creación: 2025-08-02 15:37:01
Ubicación del proyecto: /c/Users/Aprendiz/camilo-leon-bootcamp/mi-primera-api-fastapi
Equipo asignado: BOGDFPCGMP5669

Preparación del entorno local

Este proyecto está configurado para facilitar la colaboración sin afectar otros entornos del sistema:

Entorno virtual exclusivo: venv-personal/

Git configurado solo en este repositorio: No afecta otros proyectos

Dependencias aisladas: Paquetes instalados solo para este proyecto, evitando conflictos

▶️ Instalación y ejecución

Para poner en marcha la API localmente, sigue estos pasos:

 pip install dotenv

# Activar el entorno virtual
source venv-personal/bin/activate

# Instalar las dependencias
pip install -r requirements.txt

# Ejecutar la aplicación con recarga automática en el puerto 8000
uvicorn main:app --reload --port 8000