


from tensorflow import keras



class cerebro:
    
    def __init__(self,entrada=8,salida=4):
        
        #cantidad de datos de entrada de la RNA
        self.entrada=entrada
        #cantidad de datos de salida de la RNA
        self.salida=salida   
        
        #se guardan las dimenciones de las matrices de la RNA
        self.estructura=[] 
        #se guarda el modelo de la RNA por individuo
        self.brain=self.model()
        
        
    def model(self):
        
        model_Q=keras.models.Sequential()
        model_Q.add(keras.layers.Dense(units=8,activation="tanh",input_dim=self.entrada,use_bias=False))
        model_Q.add(keras.layers.Dense(units=18,activation="tanh",use_bias=False))
        model_Q.add(keras.layers.Dense(units=18,activation="tanh",use_bias=False))
        model_Q.add(keras.layers.Dense(units=self.salida,activation="softmax",use_bias=False))
        model_Q.compile(loss="mse",optimizer=keras.optimizers.Adam(lr=0.001))
        
        val=[]
        for i in model_Q.weights:
            val.append(i.numpy().shape)
        self.estructura=val
        
        return model_Q
        


class nido:
    
    def __init__(self,poblacion=10):
        
        #cantidad de Snakes a crear
        self.poblacion=poblacion
        
        
        #Snake inteligentes
        self.snake_IA=self.dar_IA()
        
        #estructura de las redes neuronales de los cerebros
        self.estructura=self.snake_IA[0].estructura
        
        #peso de la RNA de cada Snkae
        self.pesos=self.gen_pesos()
        
        #se cargan los primeros pesos aleatorios
        self.set_pesos(self.pesos)
        
        #variable donde se guardará el desempeño de cada Snake
        self.desemp=[]
        
        #crea los pesos del cerebro de cada una de las Snake 
    def gen_pesos(self):
        
        total_pesos=[]
        for j in range(self.poblacion):
            
            pesos=[]
            k=0
            for i in self.estructura:   
                
                #crea pesos aleatorios
                #a=np.asarray((1-(-1))*np.random.random(i)-1)*0.1
                #deja los pesos originales
                a=self.snake_IA[j].brain.get_weights()[k]
                pesos.append(a)
                k+=1
            total_pesos.append(pesos)
        return total_pesos
    
    #crea una RNA para cada Snake
    def dar_IA(self):
        medusa=[]
        for i in range(self.poblacion):
            medusa.append(cerebro())
        return medusa
    
    #funcion para darle los pesos a las RNA
    def set_pesos(self,pesos):
        
        self.pesos=pesos
        
        for i in range(self.poblacion):
            self.snake_IA[i].brain.set_weights(self.pesos[i])