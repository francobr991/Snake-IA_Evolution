import numpy as np
from vision_2 import vision
import random
class cuerpo:
    def __init__(self,name="name"):
        
        #llamar funciones externas
        self.vision=vision
        
        #caracteristias de la Snake
        self.name=name
        self.cabeza=[150,150]
        self.cuerpo=[[150,150],[140,150],[130,150]]
        self.cant_hambre=0
        self.life_time=0
        #caracteristicas de movimiento
        self.direc=["derecha","izquierda","arriba","abajo"]        
        self.direccion=np.random.choice(self.direc,1,p=[1,0,0,0])        
        self.movimiento=True 
        self.score=0
        self.pred_mov=[]
        self.live=1
                
        #crea la fruta de forma aleatoria y se asegura que no coincida con el cuerpo
        self.kiwi_pos=self.kiwi()
        while self.kiwi_pos in self.cuerpo:
            self.kiwi_pos=self.kiwi()              
        
        #funcion para crear el kiwi
    def kiwi(self):        
        lugar=([random.randint(0,24)*10,random.randint(0,24)*10])
        return lugar

        #determina si snake muere
    def muerte(self):        
        if self.cabeza in self.cuerpo[1:] or self.cabeza[0]<0  or self.cabeza[0]>240 or self.cabeza[1]<0 or self.cabeza[1]>240 or self.cant_hambre>200:
            self.movimiento=False
            self.live=0   
            #print("muerte de la Snake #",self.name)
            
        #da las condiciones iniciales para una nueva generación
    def reinicio(self):        
        self.cabeza=[150,150]
        self.cuerpo=[[150,150],[140,150],[130,150]]
        self.cant_hambre=0       
        self.score=0
        self.kiwi_pos=self.kiwi()
        self.live=1
        self.movimiento=True
        self.life_time=0
        while self.kiwi_pos in self.cuerpo:
            self.kiwi_pos=self.kiwi() 

        #calcula el movimiento 
    def mov(self,pred_mov):
        
        if pred_mov==0 and self.direccion!=self.direc[1]:
            
            self.direccion=self.direc[0]

        if pred_mov==1 and self.direccion!=self.direc[0]:
            self.direccion=self.direc[1]                    

        if pred_mov==2 and self.direccion!=self.direc[3]:
            self.direccion=self.direc[2]     

        if pred_mov==3 and self.direccion!=self.direc[2]:
            self.direccion=self.direc[3] 


        if self.movimiento==True:
            

            if self.direccion==self.direc[0] :
                self.cabeza[0]+=10

            if self.direccion==self.direc[1]:
                self.cabeza[0]-=10            

            if self.direccion==self.direc[2]:
                self.cabeza[1]-=10                  

            if self.direccion==self.direc[3]:
                self.cabeza[1]+=10     

            self.cuerpo.insert(0, list(self.cabeza))        
            
            
            self.cant_hambre+=1
            #### crear comida y crecer
            if self.cabeza==self.kiwi_pos:
                self.kiwi_pos=self.kiwi()
                
                self.score=self.score+1
                self.cant_hambre=0

            else:
                self.cuerpo.pop()  
            