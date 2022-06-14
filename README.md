# Test Scraping nivel básico - [ScrapeX.io](http://www.scrapex.io)


## Dependencias usadas

---

* Se usaron las librerias: [Requests](https://pypi.org/project/requests/), [Pandas](https://pypi.org/project/pandas/) y [Rich](https://pypi.org/project/rich/)
* [Requests](https://pypi.org/project/requests/) se utilizo para extaer los datos de https://gorest.co.in/public/v2/users y de https://gorest.co.in/public/v2/comments 
* [Pandas](https://pypi.org/project/pandas/) se utilizo para darle una estructura mas legible a los datos, y tambien para modificarlos y poder realizar diferentes querys. 
* [Rich](https://pypi.org/project/rich/) se utilizo para darle otro formato y color a la tipografia

## Desarrollo

---

1. En el modulo `main.py ` se desarrollo todo el codigo, en el cual hay dos funciones, una que extrae los datos de los usuarios,  
y otra que extrae los datos de los comentarios 
2. Los datos se extraen mediante un get de requests, y se devuelven en formato .json 
3. El resto del codigo se desarrolla en el entry point del script, donde en primer lugar se invoca y se trae la data en formato 
.json de las 2 funciones previamente mencionadas. 
4. Luego se usa a la libreria rich para darle color y formato a los prints que se van a mostrar en pantalla. 
5. Despues se aprovecho que los datos se mostraban en una lista de diccionarios, para transformarlos en un dataframe de pandas, 
para que se puedan visualizar de una forma mas legible y poder generar modificaciones en los datos como la traduccion de los datos 
de "gender" y "status" 
6. Se realizo una query en el dataframe, que buscaba 2 condiciones(gender == femenino y status == activo) 
7. Se imprimieron estos dataframes con sus respectivos titulos con diferentes colores 
8. Se decidio exportar los 3 dataframes en formato .csv para en caso de que, si se desea compartir los datos con el cliente 
esto sea mas facil. 

## Instrucciones 

--- 

* Una vez que las dependencias esten instaladas, el codigo se pueden correr facilmente desde el `Run ` de cualquier IDE de python. 
* Tambien se puede ejecutar desde la cmd, moviendose a la ubicacion del archivo y ejecutando `python main.py `.

