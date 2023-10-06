
# Healtcare Cure Formulario

El objetivo de esta prueba automatizada es simular la interacción de un usuario con un sistema de reservas de citas médicas y validar la funcionalidad de la aplicación.


## Prerrequisitos
- Python 3.7 o superior
- Selenium 4.0 o superior
- Chrome WebDriver para versiones 114.0 de Google Chrome
- Chrome WebDriver Manager para versiones 115.0 o superior de Google Chrome
- Chrome for Testing para versiones 115.0 o superior de Google Chrome

## Entorno de Prueba
- Navegador: Chrome


## Datos de Prueba
- Usuario: 'John Doe'
- Contraseña: 'ThisIsNotAPassword'
- Fecha de Cita Ingresada: '10/10/2023'
- Comentario: 'Esta es una reserva para servicios de atención médica.'


# Pasos de la Prueba
## Paso 1: Iniciar Sesión
- Abrir la URL de la aplicación: 'https://katalon-demo-cura.herokuapp.com/'
- Hacer clic en el botón 'Make Appointment'.
- Ingresar el nombre de usuario y contraseña proporcionados.
- Presionar 'Enter' para iniciar sesión.

 
## Paso 2: Completar el Formulario
- Seleccionar la instalación hospitalaria.
- Seleccionar el programa 'Medicaid'.
- Ingresar la fecha de cita deseada ('10/10/2023').
- Proporcionar el comentario: 'Esta es una reserva para servicios de atención médica.'
- Hacer clic en el botón 'Book Appointment'.


## Paso 3: Verificar la Información
- Extraer la respuesta de la pagina de la reserva con la hora de la ejecución de la prueba.
- Cerrar navegador


## Resultados Esperados
- El usuario debería poder iniciar sesión exitosamente.
- El formulario de cita debería completarse correctamente.
- La información mostrada debería ser igual a la información ingresada.
