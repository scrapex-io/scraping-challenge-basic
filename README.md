Webscraping challenge entry level

# Test Scraping nivel básico - [ScrapeX.io](http://www.scrapex.io)


## Instrucciones para repositorio GIT

---

1. Clonar el repositorio en local
2. Dejar tal cual la rama main y crear un nuevo branch "develop" y trabajar el challenge en ese branch.
3. Agregar al usuario `noctilukkas` como colaborador dentro del repositorio
4. Desarrollar lo que se indica en la siguiente sección en Python3. Si existen supuestos, estos deben definirse claramente en el README
5. Cuando el desarrollo esté listo pushear la rama develop y crear un PR (Pull Request) a main.
6. Notificar mediante email cuando esté listo y enviar el link del repositorio privado.


## Instrucciones de desarrollo

---

* El desarrollo se trata de consumir una API de prueba, en donde se requiere extraer cierta información 
y luego manipularla para obtener una presentación acorde.
* Para este test utilizaremos el sitio: https://gorest.co.in/ 

## Instrucciones


1. En el modulo `main.py ` hay un método ya implementado que consume un endpoint de una api de prueba que trae usuarios
y luego muestra por pantalla todos los datos obtenidos.
2. Se requiere mejorar los datos a mostrar, por un lado se requiere darle un formato mas amigable para el usuario:
3. Para esto se debe mostrar los siguientes datos por cada usuario, en forma de listado.
    * Nombre: {nombre}
    * Genero: {genero} 
    * Email: {email} 
    * Status: {status}

4. Se necesita filtrar solo los usuarios Femeninos y Activos .
5. [BONUS] Como bonus se requiere implementar el método extract comments de forma analoga al metodo de users, mostrando los 
siguientes datos
    * Nombre
    * Email
    * Comentario
6. [BONUS] Se debe incluir un archivo requeriments.txt con las dependencias que requiera el script.
7. [BONUS] Traducir los datos de gender (male/female) por masculino / femenino y status (acive/inactive) por activo/inactivo
8. Detallar en el Readme las instruciones para ejecutar el script.

## Consejos y pistas

---
* Usar la librería [Requests](http://docs.python-requests.org/en/master/)
* Recorrer los listados para armar el output sugerido.
* Hacer uso de `print(f"Algún texto: {var}")`
* **[SUPERBONUS]** Cualquier mejora que se te ocurra para implementarm o para enriquecer el ejercicio es sumamente valorable
por nosotros.

## En qué nos fijaremos

---
* Correcto uso de GIT
* Orden y claridad del código

## Aclaraciones finales

---

* No dudes en consultar cualquier cosa que no entiendas, o no te quede claro.
* Si hay alguna cuestión que no podés codificarla, intenta explicarlo con palabras en comentarios en el codigo sobre como podrias hacerlo.
