# Easyrun :bike:

Sistema de automatización de préstamo de bicicletas dentro del campus de la Universidad Nacional de Colombia, incorporando la conexión entre estaciones y facilitando el proceso que a la fecha se implementa. El sistema tiene como objetivo proncipa reducir los tiempos en el uso del servicio, especialmente en los puntos de prestámo y entrega, además de permitir un control sobre la trasabilidad de cada bicileta.

Integrantes: 

* Ana Milena Espinosa Jiménez
* Laura Valentina Moreno Castro
* Johan Stevens Higuera Espinel
* Omar Andrés Cely Villate
* Juan Felipe González Pardo
* Kishvari Osorio Delgado

## Requerimientos Funcionales ##

El sistema debe ser capaz como mínimo de satisfacer los siguientes requisitos:

* Llevar registro de las bicicletas activas en el sistema, así como su disponibilidad y condición general.
* Presentar una interfaz de usuario para la selección, entrega y reporte del estado de la bicileta.
* Reconocer a través de RFID el carnet estudiantil como único requisito para utilizar el servicio. 
* Asegurar y liberar automáticamente las bicicletas que se solicitan y entregan en el sistema. 
* Comunicar bidireccionalmente el estado de las bicicleras y los usuarios con la base de datos.
* Utilizar la información de la base de datos para cordinar los préstamos entre estaciones.
* Notificar a los operarios cuando se llene o vacíe el cupo de las estaciones de modo que puedan redistribuir las bicicletas.

## Requerimientos no Funcionales ##

* Permitir el uso de perfiles diferenciados para usuarios y administradores.
* Tener un apropiado manejo de la información y datos personales de los usuarios.
* Utilizar únicamente bandas ISM del espectro.
* Alimentarse de la red eléctrica de la universidad.
* Presentar una eficiencia de potencia (Entrada salida) superior al 80%.
* Tener un factor de potencia superior a 0.9 en concordancia con la regulación colombiana.

## Descripción general y viaje del cliente ##

Con el fin de determinar un camino viable para el proyecto, se plantea un diagrama de bloques general con el fin de aclarara las variables y perifericos que intervienen en la solución. Dentro de este diagrama, se busca aclara que partes componen el sistema de manera poco específica y con esto fijar los componentes que se deben tener en cuenta en el diseño del sistema embebido.

![Imagen](https://github.com/felipeg86/Easyrun/blob/7021e59d89bb2bfd1115d05f9bedde976ee1c1a8/Images/Diagrama%20General.jpg)

También resulta pertinente la construcción de un viaje de usuario para definir primordialmente las funcionalidades y posibles soluciones que se pueden plantear al problema. La siguiente figura representa de manera superficial los pasos que un estudiante debe realizar al utilizar el servicio. Clasificando cada proceso dentro de la estación que se hace.

![Imagen](https://github.com/felipeg86/Easyrun/blob/main/Images/Embebidos%20-%20Frame%201.jpg) 

## Diagrama de Bloques ##

El siguiente diagrama de bloques describe el funcionamiento de Easyrun, definiendo las relaciones y organización de todo el proceso interno, sus entradas y sus salidas.

![Imagen](https://github.com/felipeg86/Easyrun/blob/ca067636eb22f11a325dc4f5554fbd1dd7c24521/Images/Diagrama%20de%20bloques_1.jpg) 
![Imagen](https://github.com/felipeg86/Easyrun/blob/ca067636eb22f11a325dc4f5554fbd1dd7c24521/Images/Diagrama%20de%20bloques_2.jpg) 

## Diagrama de Despliegue del proyecto ##

Los nodos de hardware, sus comunicaciones y los componentes que se ejecutan en cada uno de ellos se presentan en el diagrama siguiente.

![Imagen](https://github.com/felipeg86/Easyrun/blob/main/Images/Diagrama%20sistema.png)


## [Diseño de la PCB](https://github.com/felipeg86/Easyrun/tree/main/Circuit%20Design)
## [Código del microcontrolador](https://github.com/felipeg86/Easyrun/tree/main/Micropython)
## [Diseño de la carcaza](https://github.com/felipeg86/Easyrun/tree/main/Case%20Design)
