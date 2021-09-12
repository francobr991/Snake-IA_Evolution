# Snake-IA_Evolution

En este repositorio aplicamos la teoría de algoritmos genéticos para sintonizar los pesos de redes neuronales con el fin de resolver el juego clásico de Snake

![img_1](https://user-images.githubusercontent.com/65036764/132969413-24ef0e70-4e33-431c-9719-2ad2252e2c7e.png)


La parte grafica fue programada en pygame y para las redes neuronales se utilizó TensorFlow, el archivo game.yml tiene los paquetes necesarios para correr el código

En la siguiente imagen se muestra la conexión entre las funciones y clases de este código  

![img_2](https://user-images.githubusercontent.com/65036764/132969555-ddfeac2a-2e2a-4d7e-83c8-13cea1dcf21c.png)


La visión de cada serpiente es binaria en cada dirección, en el caso del movimiento detecta en las 4 direcciones si la casilla próxima es segura (1=si, 0=no), para el kiwi (punto rojo) detecta si esta presente en alguna de las 4 direcciones sin importar la distancia (1=si, 0=no)

![img_3](https://user-images.githubusercontent.com/65036764/132969675-15fe5d07-7c16-4608-bb5b-b925021ae456.PNG)
