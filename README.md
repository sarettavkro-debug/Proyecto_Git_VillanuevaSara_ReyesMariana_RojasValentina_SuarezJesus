# BiblioStock CLI - Biblioteca Horizonte

Sistema de inventario y préstamos por terminal en Python.

## Integrantes
- Dev 1: Sara Villanueva 
- Dev 2: Mariana Reyes
- Dev 3: Valentina Rojas
- Dev 4: Jesus Suarez

Estado del proyecto: en desarrollo

Estructura del proyecto
Proyecto_Git_ApellidoNombre/
├── main.py            # menú principal y flujo del programa
├── inventario.py      # registrar, listar y buscar ítems
├── prestamos.py       # registrar préstamos y devoluciones
├── persistencia.py    # guardar y cargar datos en JSON
├── capturas/          # capturas de pantalla para este README
├── .gitignore
└── README.md

## Resolución del conflicto de fusión

Pendiente: Describir en qué archivo y línea apareció el conflicto, cómo se identificó (git status), cómo se resolvió y adjuntar las capturas.

## Evidencia de Corrección de Error y Flujo de Trabajo en Git

## 1. Flujo Inicial y Comandos Básicos de Git

### Clonación del Repositorio (git clone)
Para obtener una copia local del proyecto en el entorno de desarrollo:
git clone https://github.com/sarettavkro-debug/Proyecto_Git_VillanuevaSara_ReyesMariana_RojasValentina_SuarezJesus
#### Sincronización de Cambios (git pull)
Para mantener la rama local actualizada con los últimos cambios en la nube:
git pull origin main
### Explicación del comando git switch -c
El comando git switch -c <nombre-rama> realiza dos acciones simultáneas:
1. -c (create): Crea una nueva rama local.
2. switch: Cambia el entorno de trabajo directamente a esa rama.
Se utiliza para aislar el desarrollo de una nueva funcionalidad o corrección (fix/*) sin afectar la rama estable main.

## 2. Reproducción del Error en Terminal

Al intentar cargar un archivo JSON inexistente, vacío o corrupto mediante la función cargar_json(), Python lanza una excepción:
python -c "from persistencia import cargar_json; cargar_json('libros.json')"
Resultado en consola:
Traceback (most recent call last):
FileNotFoundError: [Errno 2] No such file or directory: 'libros.json'
 
Ver captura: 
![Captura](./Imagenes/Captura1Error.png)

## 3. Creación de la Rama de Corrección (fix/*)

Se creó la rama aislada fix/carga-archivo-vacio para implementar la solución:
git switch -c fix/carga-archivo-vacio
git branch
Salida de confirmación:
feature/persistencia
* fix/carga-archivo-vacio
main
Ver captura:
![Captura](Imagenes/Captura2Error.png)

## 4. Implementación del Manejo de Excepciones (try/except)

En el archivo persistencia.py, se estructuró la función con un bloque try/except para capturar json.JSONDecodeError y FileNotFoundError, devolviendo una lista vacía [] si ocurre un fallo:
![Captura](Imagenes/Captura3Error.png)

## 5. Guardado, Commit y Push a GitHub

Se registraron los cambios en Git y se publicaron en el repositorio remoto:
git add .
git commit -m "fix: manejar archivo JSON vacío o corrupto"
git push origin fix/carga-archivo-vacio
Confirmación en terminal:
[fix/carga-archivo-vacio 9263f84] fix: manejar archivo JSON vacío o corrupto
4 files changed, 6 insertions(+), 3 deletions(-)
create mode 100644 libros.json
Ver captura:
![Captura](Imagenes/Captura4Error.png)

## 6. Sincronización Final con la Rama main
Posterior a la integración del Pull Request en GitHub por parte de Dev 1, se cambió a la rama main y se descargaron las actualizaciones:
git switch main
git pull origin main
Confirmación de actualización:
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
Ver captura:
![Captura](Imagenes/Captura5Error.png)

## Repositorio
https://github.com/sarettavkro-debug/Proyecto_Git_VillanuevaSara_ReyesMariana_RojasValentina_SuarezJesus


## Comandos de Git utilizados
(Espacio para los desarrolladores)

jesus y Valentina

link: https://drive.google.com/drive/folders/11oC8UiiHweiGcsoUbwqi3s50hQPPHHTJ?usp=sharing
