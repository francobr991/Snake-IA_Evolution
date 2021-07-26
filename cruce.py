import numpy as np

def next_gen(old_gen,core,struc):
    
    new_gen=[]
        
    while len(new_gen)<len(old_gen):

        # 1.a. primero se realiza el combate para escoger a un padre, se enfrentan 2 Snakes aleatorias
        winner=combate(core,2)
        # 1.b. se escoge al padre aleatorio
        #aparecido=np.random.randint(0,len(core))
        aparecido=np.random.choice(np.where(np.asarray(core)>np.mean(core))[0])
        while winner==aparecido:
            aparecido=np.random.randint(0,len(core))
        
        # 2.a. extender las neuronas
        padre_1=extender(old_gen[winner])
        padre_2=extender(old_gen[aparecido])
        
        # 2.b iterar para cruzar cada una de las neuronas
        hijo_1=[]
        hijo_2=[]
        
        for i in range(len(padre_1)):
            #crea el peso de capa i de la neurona
            frag_hijos=cruce([padre_1[i],padre_2[i]])
            
            #decide si se muta el fragmento del hijo 1
            if np.random.random_sample(1)>0.1:
                hijo_1.append(mutar(frag_hijos[0]))
            else:
                hijo_1.append(frag_hijos[0])
                
            #decide si se muta el fragmento del hijo 2
            if np.random.random_sample(1)>0.1:
                hijo_2.append(mutar(frag_hijos[1]))
            else:
                hijo_2.append(frag_hijos[1])
        
        new_gen.append(reordenar(hijo_1,struc))
        new_gen.append(reordenar(hijo_2,struc))
        
    return new_gen

#se le ingresan los 2 padres y devuelve la decendencia 
def cruce(mat_1):           
    lim=np.random.randint(1,len(mat_1[0])-1)
    
    hijos=np.vstack((np.concatenate((mat_1[0][0:lim],mat_1[1][lim:])),np.concatenate((mat_1[1][0:lim],mat_1[0][lim:])))) 
    return hijos  

#se le ingresa un cromosoma y muta el 10% de sus alelos
def mutar(mutar):
    cromosoma=np.copy(mutar)    
    for pos in range(len(cromosoma)):
        if np.random.random_sample(1)>0.9:       
            cromosoma[pos]=cromosoma[pos]+(cromosoma[pos]*np.random.choice([1,-1])*0.1)
    return cromosoma

#rendimiento es la lista de Scores y p es la cantidad de elementos a enfrentar
#devuelve un numero de posicion 
def combate(rendimiento,p):    
    pos=[np.random.randint(len(rendimiento))]
    for i in range(0,p-1):
        pos.append(np.random.randint(len(rendimiento)))
    
    best=rendimiento[pos[0]]
    
    best_pos=pos[0]
    
    for i in range(1,len(pos)):
        if rendimiento[pos[i]]>best:
            best=rendimiento[pos[i]]
            best_pos=pos[i]
    return best_pos

#convierte las matrices en vectores
def extender(info):
    valores=info.copy()
    val_ext=[]
    
    for i in range(len(valores)):
        val_ext.append(np.reshape(valores[i],-1))
    return val_ext

#convierte los vectores en las matrices
def reordenar(dat,orden):
    ordenado=[]
    for i,j in zip(dat,orden):
        ordenado.append(np.reshape(i,j))
    return ordenado