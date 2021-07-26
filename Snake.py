import pygame
import random
import numpy as np
#import pandas as pd
from vision_2 import vision

class Snake:
    
    def __init__(self):
        
        pygame.init()
    

        self.cabeza=[150,150]
        self.cuerpo=[[150,150],[140,150],[130,150]]
        self.cant_hambre=0
        self.direc=["derecha","izquierda","arriba","abajo"]        
        self.direccion=np.random.choice(self.direc,1,p=[0.25,0.25,0.25,0.25])        
        self.movimiento=False        
        self.run=True
        self.score=0
        self.devolver=True
        
        self.kiwi_pos=self.kiwi()
        self.vision=vision
        
        self.fps=pygame.time.Clock()        
        self.pause=False        
        self.text_color=(200,60,80)
        self.font=pygame.font.Font(None,30)
        self.display=pygame.display.set_mode(size=(550,250))
        
        self.main()
        pygame.quit()
        
    def kiwi(self):
        lugar=([random.randint(0,24)*10,random.randint(0,24)*10])
        
        return lugar

    def main(self):     
        
        
        #crea la fruta de forma aleatoria y se asegura que no coincida con el cuerpo
        while self.kiwi_pos in self.cuerpo:
            self.kiwi_pos=self.kiwi()           

        
        while self.run:
            
            #determina cuando se cierra la ventana
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.run =False
                    
                    
                  ############################   
                  ##lectura posicion
            
                if event.type==pygame.KEYDOWN:
                    
                    self.movimiento=True
                    
                    if event.key==pygame.K_RIGHT and self.direccion!=self.direc[1]:
                        self.direccion=self.direc[0]
                    
                    if event.key==pygame.K_LEFT and self.direccion!=self.direc[0]:
                        self.direccion=self.direc[1]                    
                    
                    if event.key==pygame.K_UP and self.direccion!=self.direc[3]:
                        self.direccion=self.direc[2]     
                        
                    if event.key==pygame.K_DOWN and self.direccion!=self.direc[2]:
                        self.direccion=self.direc[3]   
                        
                    
    #pause
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_p:
                            self.pause=True
                        elif event.key==pygame.K_s:
                            self.pause=False
                            
                    if self.pause==True:
                        
                        pygame.time.delay(3000)
                        
                        self.pause=False
                        
                    if self.pause==False:
                        pygame.time.delay(0)
                        continue 
    
              ############################   
              ##escritura posicion
            
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
            
                #### crear comida y crecer
                if self.cabeza==self.kiwi_pos:
                    self.kiwi_pos=self.kiwi()
                    self.score=self.score+1
                    self.cant_hambre=0
    
                else:
                    self.cuerpo.pop()
    
            self.display.fill(color=(0,0,0))
            
            ####  muerte
            if self.cabeza in self.cuerpo[1:] or self.cabeza[0]<0  or self.cabeza[0]>240 or self.cabeza[1]<0 or self.cabeza[1]>240:
                pygame.time.delay(500)
                self.cabeza=[150,150]
                self.cuerpo=[[150,150],[140,150],[130,150]]
                self.cant_hambre=0
                self.movimiento=False        
                self.score=0
                self.kiwi_pos=self.kiwi()
                while self.kiwi_pos in self.cuerpo:
                    self.kiwi_pos=self.kiwi() 
                        
                #self.run=False
                
            #### dibujar a snake
            
            pygame.draw.rect(self.display,(0,200,0), pygame.Rect(self.cabeza[0],self.cabeza[1],10,10))
            for pos in self.cuerpo[1:]:            
                pygame.draw.rect(self.display,(200,200,200), pygame.Rect(pos[0],pos[1],10,10))
                
                
            ####grafica kiwi    
            pygame.draw.rect(self.display,(169,6,6),pygame.Rect(self.kiwi_pos[0],self.kiwi_pos[1],10,10))
            
            #### tabla de info
            pygame.draw.rect(self.display,(255,255,255), pygame.Rect(250,0,300,250))
            
            #### grafica info
            
            
            info_pos=("x: "+str(self.cabeza[0])+" y: "+str(self.cabeza[1]))
            
            self.cant_hambre+=1
            
            info_hambre=("frames sin comer: "+str(self.cant_hambre))
            
            texto=self.font.render(("score: "+str(self.score)),0,self.text_color)
            dis_pos=self.font.render(info_pos,0,self.text_color)        
            hambre=self.font.render(info_hambre,0,self.text_color)
            
            self.display.blit(texto,(270,20))
            self.display.blit(dis_pos,(270,50))
            self.display.blit(hambre,(270,80))
            
            pygame.display.flip()
            
            self.dev_vista()
              
            self.fps.tick(10)
        
    
 
    
    def dev_vista(self):
        if self.devolver==True:
            print(self.vision(self.cuerpo,self.kiwi_pos))
            

culebra=Snake()