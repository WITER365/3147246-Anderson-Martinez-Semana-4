Mi Primera API FastAPI - Bootcamp

👤 Desarrollador: Camilo Andrés León Roldán
📧 Email: Camilo-Leon@users.noreply.github.com

🔒 Privacidad: Correo configurado de forma privada según las recomendaciones de GitHub
📅 Fecha de creación: 2025-08-02 15:37:01
📂 Ruta del proyecto: /c/Users/Aprendiz/camilo-leon-bootcamp/mi-primera-api-fastapi
💻 Equipo de trabajo: BOGDFPCGMP5669

🔧 Configuración en el entorno local

Este proyecto está preparado para trabajo colaborativo, pero manteniendo un entorno aislado:

Entorno virtual dedicado: venv-personal/

Configuración de Git solo para este proyecto: No afecta otros repositorios

Dependencias separadas: Las librerías están aisladas para evitar conflictos con otras instalaciones

🚀 Instalación y ejecución
# 1. Activar el entorno virtual
source venv-personal/bin/activate

# 2. Instalar las dependencias
pip install -r requirements.txt

# 3. Ejecutar el servidor de desarrollo
uvicorn main:app --reload --port 8000

📝 Notas del desarrollador

Git configurado de forma local: Solo para este proyecto, sin alterar la configuración global

Correo en GitHub privado: Para proteger datos personales

Entorno aislado: Todas las librerías están dentro de venv-personal/

Puerto predeterminado: 8000 (se puede cambiar en caso de conflicto)

Estado actual del bootcamp: Semana 1 - Fase de configuración

🛠️ Solución de problemas

Si el entorno virtual no se activa:

rm -rf venv-personal && python3 -m venv venv-personal


Si hay conflicto con el puerto: Cambiar el valor de --port en el comando de ejecución

Si Git no funciona: Verificar el nombre y correo con

git config user.name
git config user.email


Para cambiar el correo en Git: Configurar el correo privado desde Settings → Emails en GitHub

Reflexión final - Semana 4

Comprendí la importancia de las pruebas unitarias con pytest para detectar problemas antes de que afecten a toda la API.

Usé SQLite para practicar con bases de datos reales, aprendiendo sobre migraciones y ambientes separados para desarrollo y pruebas.

Reorganicé la estructura del proyecto separando archivos como models.py, schemas.py, crud.py y main.py, lo que facilita el trabajo en equipo y la escalabilidad del proyecto.

En esta etapa siento que la API ha pasado de ser un simple ejercicio a un proyecto más cercano a un entorno profesional.