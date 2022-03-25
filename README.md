# Proyecto del Viajero.
Definición del problema
Como requerimiento del Curso de programación nº IFCT-06092022, se procede a crear un código en lenguaje de programación Python que resuelva el siguiente problema: Dado un viajero, se propone recorrer varias ciudades no definidas, es decir el viajero puede elegir cuales son los destinos de su preferencia, cuyas distancias, en kilómetros son igualmente diferentes: 
## Objetivo:
Se pide:
1.	Todas las posibles combinaciones de las ciudades por visitar.
2.	Las distancias para cada una de las rutas.
3.	Las gráficas y/o mapas de cada una de las rutas.
## Planteamiento del problema: 
“El problema del viajante fue definido en los años 1800s por el matemático irlandés W. R. Hamilton y por el matemático británico Thomas Kirkman. El Juego Icosian de Hamilton fue un puzle recreativo basado en encontrar un ciclo de Hamilton. Todo parece indicar que la forma general del TSP fue estudiada, por primera vez por matemáticos en Viena y Harvard, durante los años 1930s. Destacándose Karl Menger, quien definió los problemas, considerando el obvio algoritmo de fuerza bruta, y observando la no optimalidad de la heurística de vecinos más cercanos” (Wikipedia)
Una vez definido el problema se procede a estructurar el código en tres partes principales:
1.	Todas las posibles combinaciones de rutas.
2.	Todas las distancias entre ciudades dadas dos coordenadas para cada ruta posible.
3.	Todos los mapas y/o graficas posibles para las rutas, que muestre la ciudad y la distancia entre cada uno de los puntos.
## Recursos utilizados:
Para el desarrollo del código se utilizó:
1.	Se desarrolló en un entorno e Windows 10.
2.	Se utilizó PYTHON 3.10.2, como lenguaje de programación. 
3.	VISUAL STUDIO CODE, como editor de código.
4.	Se utilizo GITHUB, para intercambio de información y versiones
5.	Consulta a expertos.
## Problemas encontrados:
•	Una vez definido el problema y seleccionados los recursos. Para el desarrollo del código se hizo necesario actualizar los diferentes módulos de Python, para lo cual hizo falta instalar varias aplicaciones, entre las cuales esta get-pip que es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python. Este paso fue necesario para instalar el módulo MATPLOTLIB.PYPLOT de Python, a fin de ejecutar la interfase gráfica.
•	Se hizo necesario revisar la bibliografía sobre permutaciones y combinaciones y diseño de gráficas.
•	Revisión de la documentación oficial de Python en lo referente a definición de funciones y procedimientos.
•	Estructurar el código, de forma que sea haga fácil la comprensión del mismo.
Desarrollo del código:
En las primeras versiones se procedió a desarrollar las permutaciones de las ciudades de los distintos viajes, después de múltiples intentos se desarrolló satisfactoriamente y pudimos obtener todas las permutaciones correspondientes, correspondientes a 3 ciudades, inicialmente. Quedando el código funcional para hacerlo con un número indeterminado de ciudades o dicho de otra forma, con el número de ciudades que se quiera considerar.

Tras obtener las permutaciones, proseguimos calculando las distancias que se obtienen a través de las coordenadas de cada una de las ciudades, dando una comparativa de distancias de las rutas creadas en el punto anterior.

Finalmente, creamos una representación grafica de los dos puntos anteriormente, mostrándonos, la posición de las ciudades dadas, las rutas del viaje. Para la mejor comprensión del gráfico, se decidió añadir una leyenda con marcas circulares y diferentes colores indicativo de cada una de las ciudades.
Estado Actual
En su versión actual el código desarrollado, satisface todos los requerimientos planteados. El equipo se ha propuesto continuar con el desarrollo 

