import numpy as np
import pandas as pd

def vision(body,food):
    total_vista=[]
    head=body[0]
    
    
    ##derecha
    if (head[0]==240 or ([head[0]+10,head[1]] in body)):
        safe_der=0
    else:
        safe_der=1
        
    if (head[1]==food[1] and food[0]>=head[0]):
        kiwi_der=1
    else:
        kiwi_der=0
        
    vista=np.array([safe_der,kiwi_der])        
    total_vista.append(vista)
    
    
    ##izquierda
    if (head[0]==0 or ([head[0]-10,head[1]] in body)):
        safe_iz=0
    else:
        safe_iz=1
        
    if (head[1]==food[1] and food[0]<=head[0]):
        
        kiwi_iz=1
    else:
        kiwi_iz=0
        
    vista=np.array([safe_iz,kiwi_iz])        
    total_vista.append(vista)
        
    ##arriba
    if (head[1]==0 or ([head[0],head[1]-10] in body)):
                   
        safe_arr=0
    else:
        safe_arr=1
        
    if (head[0]==food[0] and food[1]<=head[1]):
        kiwi_arr=1
    else:
        kiwi_arr=0
 
    vista=np.array([safe_arr,kiwi_arr])        
    total_vista.append(vista)
    
    ##abajo
    if (head[1]==240 or ([head[0],head[1]+10] in body)):
        safe_ab=0
    else:
        safe_ab=1
        
    if (head[0]==food[0] and food[1]>=head[1]):
        kiwi_ab=1
    else:
        kiwi_ab=0
        
    vista=np.array([safe_ab,kiwi_ab])        
    total_vista.append(vista)
    
    datos=pd.DataFrame(columns=["safe","Kiwi"],
                       index=["Derecha","Izquierda","Arriba","Abajo"],data=total_vista)
    
    #print(datos)  
    return np.reshape(total_vista,[1,8])