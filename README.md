# Easyrun :bike:

Sistema de automatización de préstamo de bicicletas dentro del campus de la Universidad Nacional de Colombia, incorporando la conexión entre estaciones y facilitando el proceso que a la fecha se implementa. El sistema tiene como objetivo proncipa reducir los tiempos en el uso del servicio, especialmente en los puntos de prestámo y entrega, además de permitir un control sobre la trasabilidad de cada bicileta.

Integrantes: 

* Ana Milena Espinosa Jiménez
* Laura Valentina Moreno Castro
* Johan Stevens Higuera Espinel
* Juan Felipe González Pardo

## Descripción Funcional ##

Dentro de las funcionalidades que podría abarcar este tipo de proyecto, se acota el alcance a las siguientes funcionalidades: 

* Reconocimiento RFID del carnet estudiantil como único requisito para utilizar el servicio. 
* Desbloqueo y aseguramiento automático de la bicicleta. 
* Interacción bidireccional con la base de datos.
* Sistema de evaluación del estado de la bicileta.
* Conexión entre estaciones.
* Alimentación del sistema mediante la red eléctrica universitaria.

## Descripción no Funcional ##

Sin embargo, se excluyen del proyecto otros requerimientos fuera del alcance.

* Implementación de más de dos puesto de prestamo y entrega.
* Alimentación del sistema con fuentes externas renovables (solar).
* Automatización de la redistribución de bicicletas entre las estaciones. 

## Descripción general y viaje del cliente ##

Con el fin de determinar un camino viable para el proyecto, se plantea un diagrama de bloques general con el fin de aclarara las variables y perifericos que intervienen en la solución. Dentro de este diagrama, se busca aclara que partes componen el sistema de manera poco específica y con esto fijar los componentes que se deben tener en cuenta en el diseño del sistema embebido.

![Imagen](https://github.com/felipeg86/Easyrun/blob/main/Images/DiagramaBloques%20-%20General.jpg)

También resulta pertinente la construcción de un viaje de usuario para definir primordialmente las funcionalidades y posibles soluciones que se pueden plantear al problema. La siguiente figura representa de manera superficial los pasos que un estudiante debe realizar al utilizar el servicio. Clasificando cada proceso dentro de la estación que se hace.

![Imagen](https://github.com/felipeg86/Easyrun/blob/main/Images/Embebidos%20-%20Frame%201.jpg) 

## Diagrama de Bloques ##

El siguiente diagrama de bloques describe el funcionamiento de Easyrun, definiendo las relaciones y organización de todo el proceso interno, sus entradas y sus salidas.

![Imagen](https://github.com/felipeg86/Easyrun/blob/ca067636eb22f11a325dc4f5554fbd1dd7c24521/Images/Diagrama%20de%20bloques_1.jpg) 
![Imagen](https://github.com/felipeg86/Easyrun/blob/ca067636eb22f11a325dc4f5554fbd1dd7c24521/Images/Diagrama%20de%20bloques_2.jpg) 

## [Diseño de la PCB](https://github.com/felipeg86/Easyrun/tree/main/Circuit%20Design)
## [Código del microcontrolador](https://github.com/felipeg86/Easyrun/tree/main/Micropython)
## [Diseño de la carcaza](https://github.com/felipeg86/Easyrun/tree/main/Case%20Design)

