import numpy as np
import pygame
from Cuerpo import cuerpo
from cerebro import nido
from cruce import next_gen
import pickle

class Snake:
    
    def __init__(self,cant_pob):
        
        #cantidad de población
        self.cant_pob=cant_pob
        self.generacion=0
        
        
        self.k_v=0
        
        #creamos el cuerpo
        self.gusano=[]
        self.vidas=[]
        self.scores=[]
        for i in range(0,cant_pob):
            self.gusano.append(cuerpo(i+1))
            self.vidas.append(self.gusano[i].live)
            self.scores.append(self.gusano[i].life_time)
        
        #creamos la inteligencia de snake
        self.brain=nido(self.cant_pob) 
        
        #mejores pesos
        self.genios=[]
        #variables de Pygame
        pygame.init()
        self.run=True    
        self.fps=pygame.time.Clock()                
        self.text_color=(200,60,80)
        self.font=pygame.font.Font(None,30)
        self.display=pygame.display.set_mode(size=(550,250))
        
        
        #corre la funcion principal
        self.main()
        
        pygame.quit()
        
   # def calc_falla(self):   
    
    def deci(self,x):
        return self.brain.snake_IA[x].brain.predict_step(self.gusano[x].vision(self.gusano[x].cuerpo,self.gusano[x].kiwi_pos))
        

    def main(self):     
                 

        
        while self.run:
            
            self.display.fill(color=(0,0,0))
            #determina cuando se cierra la ventana
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.run =False
                    
                    
              ##################################################################   
              ##lectura posicion
                
            for i in range(0,self.cant_pob):
                
                
                    
            
                #ejecuta las acciones si el Snake esta vivo
                if self.gusano[i].live==1:
                    
                    #predice el movimineto de cada Snake
                    decision=self.deci(i)                    
                    self.pred_mov=np.argmax(decision)
                            #self.pred_mov=np.random.choice([0,1,2,3])
                    
                            #print("decision del Snake #",i+1," es: ",self.pred_mov)

                    #mueve cada Snake
                    self.gusano[i].mov(self.pred_mov)
                    
                    #evalua si la snake debe morir
                    self.gusano[i].muerte()
                    
                    #lleva el tiempo de vida
                    self.gusano[i].life_time+=1
                    
                    #lleva el conteo de los gusanos vivos
                    if self.gusano[i].live==0:
                        self.vidas[i]=0
                        self.scores[i]=self.gusano[i].life_time+(self.gusano[i].score*100)
                        

                #### dibujar a snake
            if self.vidas[self.k_v]==0 and (1 in self.vidas):
                self.k_v=np.random.choice(np.where(np.asarray(self.vidas)==1)[0])

            pygame.draw.rect(self.display,(0,200,0), pygame.Rect(self.gusano[self.k_v].cabeza[0],self.gusano[self.k_v].cabeza[1],10,10))
            for pos in self.gusano[self.k_v].cuerpo[1:]:            
                pygame.draw.rect(self.display,(200,200,200), pygame.Rect(pos[0],pos[1],10,10))


            ####grafica kiwi    
            pygame.draw.rect(self.display,(169,6,6),pygame.Rect(self.gusano[self.k_v].kiwi_pos[0],self.gusano[self.k_v].kiwi_pos[1],10,10))
            #####################################################################
            #reinicio
            
            if not(1 in self.vidas):
                print("generacion: ",self.generacion)
                
                
                
                self.genios.append(self.brain.pesos[np.argmax(self.scores)])
                
                
                self.generacion+=1
                #print(self.vidas)
                print(self.scores)
                ##################################
                ##################################
                #################################
                #ejecutar crear nueva generacion
                
                N_pesos=next_gen(self.brain.pesos,self.scores,self.brain.estructura)
                self.brain.set_pesos(N_pesos)
                
                
                #####################################
                ####################################
                ###################################
                
                
                for i in range(self.cant_pob):
                    self.gusano[i].reinicio()
                    self.vidas[i]= self.gusano[i].live
            
            ####################################################################
            
            
            #### tabla de info
            pygame.draw.rect(self.display,(255,255,255), pygame.Rect(250,0,300,250))
            
            #### grafica info
            
            
            info_pos=("x: "+str(self.gusano[self.k_v].cabeza[0])+" y: "+str(self.gusano[self.k_v].cabeza[1]))
            
            info_hambre=("frames sin comer: "+str(self.gusano[self.k_v].cant_hambre))
            
            texto=self.font.render(("score: "+str(self.gusano[self.k_v].score)),0,self.text_color)
            dis_pos=self.font.render(info_pos,0,self.text_color)        
            hambre=self.font.render(info_hambre,0,self.text_color)
            #texto_gen=self.font.render(("Generacion: "+str(self.generacion)),0,self.text_color)
            
            self.display.blit(texto,(270,20))
            self.display.blit(dis_pos,(270,50))
            self.display.blit(hambre,(270,80))
            
            pygame.display.flip()
            

            self.fps.tick(90)
            
vibora=Snake(60)

#with open("genios.pkl","wb") as save:
#    pickle.dump(vibora.genios,save)