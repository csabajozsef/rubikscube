#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import numpy as np


# In[2]:


import pygame
import OpenGL


# In[3]:


import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


# In[4]:


class Cubie:
   
    def __init__(self,x=[-1,-1,-1]): # x y z irányban a színek
        self.l=np.array(x)
        
    def RL(self):
        # print("t")
        # füzetben ábra, z küröl forgatás, azaz első index helyén marad, másik 2 csere
        # kérdés az, hogy ez lehet-e jó reprezentáció cubiera? él, sarok forgatás vizualizáció úgy, hogy 
        # a hiányzó színek -1 esek? 
        self.l
        self.l[[1,2]]=self.l[[2,1]]  # x körüli forgatás, ez az R és L is, R' L' is

    def UD(self):
      self.l
      self.l[[0,2]]=self.l[[2,0]]
    
    def FB(self):
      self.l
      self.l[[0,1]]=self.l[[1,0]]

    def __str__(self):
        return str(self.l)


# In[5]:


class Cube:

    def __init__(self,x=[[[str(k)+str(j)+str(i) for i in range(3)] for j in range(3)]for k in range(3)]): # ide kell immutabel inicializálás, fix tárhely miatt
        self.l=np.array(x) #itt ha self.l=x volt akkor az a mindegyiknél létrejövő x=np.array([[[]]]) re mutatott?
        self.dict_of_num_cubie={} 
        self.dict_of_cubie_num={} 
    
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    self.dict_of_num_cubie[str(i)+str(j)+str(k)]=Cubie()

    def __str__(self):
        return str(self.l)
    
    def X_to_Y(self): #a numpy array-t átkonvertálja X szerinti rétegződésből Y szerinti rétegződésbe

      self.l[0,[0,2],:]=self.l[0,[2,0], :]
      self.l[[0,2], 0, :]=self.l[[2,0], 0, :]
      self.l[0,[0,1],:]=self.l[0,[1,0], :]
      self.l[[0,1], 0, :]=self.l[[1,0], 0, :]
      self.l[0,[0,2],:]=self.l[0,[2,0], :]
      self.l[0,[1,2],:]=self.l[0,[2,1], :]
      self.l[2,[0,1],:]=self.l[2,[1,0], :]
      self.l[1,[0,2],:]=self.l[1,[2,0], :]
      self.l[[1,2], 0, :]=self.l[[2,1], 0, :]
      self.l[1,[0,2],:]=self.l[1,[2,0], :]
      self.l[2,[0,1],:]=self.l[2,[1,0], :]

    def Y_to_X(self): #a numpy array-t átkonvertálja Y szerinti rétegződésből X szerinti rétegződésbe

      self.l[0,[0,1],:]=self.l[0,[1,0],:]
      self.l[[0,1],0,:]=self.l[[1,0], 0,:]
      self.l[0,[0,1],:]=self.l[0,[1,0],:]
      self.l[0,[0,2],:]=self.l[0,[2,0],:]
      self.l[[0,2],0,:]=self.l[[2,0],0,:]
      self.l[0,[0,2],:]=self.l[0,[2,0],:]
      self.l[1,[0,2],:]=self.l[1,[2,0],:]
      self.l[2,[0,1],:]=self.l[2,[1,0],:]
      self.l[[1,2],0,:]=self.l[[2,1],0,:]
      self.l[2,[0,1],:]=self.l[2,[1,0],:]
      self.l[1,[0,2],:]=self.l[1,[2,0],:]

    def X_to_Z(self): #a numpy array-t átkonvertálja X szerinti rétegződésből Z szerinti rétegződésbe

      self.l[0,:,[0,2]]=self.l[0,:,[2,0]]
      self.l[[0,2],:,0]=self.l[[2,0],:,0]
      self.l[0,:,[0,1]]=self.l[0,:,[1,0]]
      self.l[[0,1], :, 0]=self.l[[1,0],:, 0]
      self.l[0,:,[0,2]]=self.l[0,:,[2,0]]
      self.l[0,:,[1,2]]=self.l[0,:,[2,1]]
      self.l[2,:,[0,1]]=self.l[2,:,[1,0]]
      self.l[1,:,[0,2]]=self.l[1,:,[2,0]]
      self.l[[1,2],:, 0]=self.l[[2,1],:,0]
      self.l[1,:,[0,2]]=self.l[1,:,[2,0]]
      self.l[2,:,[0,1]]=self.l[2,:,[1,0]]

    def Z_to_X(self): #a numpy array-t átkonvertálja Z szerinti rétegződésből X szerinti rétegződésbe

      self.l[0,:,[0,1]]=self.l[0,:,[1,0]]
      self.l[[0,1],:,0]=self.l[[1,0],:,0]
      self.l[0,:,[0,1]]=self.l[0,:,[1,0]]
      self.l[0,:,[0,2]]=self.l[0,:,[2,0]]
      self.l[[0,2],:,0]=self.l[[2,0],:,0]
      self.l[0,:,[0,2]]=self.l[0,:,[2,0]]
      self.l[1,:,[0,2]]=self.l[1,:,[2,0]]
      self.l[2,:,[0,1]]=self.l[2,:,[1,0]]
      self.l[[1,2],:,0]=self.l[[2,1],:,0]
      self.l[2,:,[0,1]]=self.l[2,:,[1,0]]
      self.l[1,:,[0,2]]=self.l[1,:,[2,0]]
     
    def converter(to_what,self): #swtich
        pass

    def R(self): # x y z koordináták, z=0 front, x=2 right
        
        for i in self.l[2,:,:]:
            for j in i:
                print(j)
                self.dict_of_num_cubie[j].RL() # minden forgatott cubie saját helyzetét is megváltoztatja
        
        self.l[2,:,:]=self.l[2,:,:].transpose() # jobbra forg T aztán oszlopcsere
        self.l[2,:,[0,2]]=self.l[2,:,[2,0]]

    def L(self):

        for i in self.l[0,:,:]:
            for j in i:
                #print(j)
                self.dict_of_num_cubie[j].RL() # minden forgatott cubie saját helyzetét is megváltoztatja
        
        self.l[0,:,:]=self.l[0,:,:].transpose() # jobbra forg T aztán oszlopcsere
        self.l[0,:,[2,0]]=self.l[0,:,[0,2]]

    def U(self):

      self.X_to_Y()

      for i in self.l[0,:,:]:
            for j in i:
                #print(j)
                self.dict_of_num_cubie[j].UD()

      self.l[0,:,:]=self.l[0,:,:].transpose() # jobbra forg T aztán oszlopcsere
      self.l[0,:,[2,0]]=self.l[0,:,[0,2]]

      self.Y_to_X()
      
    def D(self):

      self.X_to_Y()
    
      for i in self.l[2,:,:]:
            for j in i:
                print(j)
                self.dict_of_num_cubie[j].UD()

      self.l[2,:,:]=self.l[2,:,:].transpose() # jobbra forg T aztán oszlopcsere
      self.l[2,:,[0,2]]=self.l[2,:,[2,0]]

      self.Y_to_X()

    def F(self):

      self.X_to_Z()

      for i in self.l[0,:,:]:
            for j in i:
                #print(j)
                self.dict_of_num_cubie[j].FB()

      self.l[2,:,:]=self.l[2,:,:].transpose() # jobbra forg T aztán oszlopcsere
      self.l[2,:,[0,2]]=self.l[2,:,[2,0]]

      self.Z_to_X()
      
     
    def B(self):

      self.X_to_Z()

      for i in self.l[2,:,:]:
            for j in i:
                print(j)
                self.dict_of_num_cubie[j].FB()

      self.l[0,:,:]=self.l[0,:,:].transpose() # jobbra forg T aztán oszlopcsere
      self.l[0,:,[2,0]]=self.l[0,:,[0,2]]

      self.Z_to_X()
      
    def R_r(self):

      for i in range(3):
        self.R()
  
    def L_r(self):

      for i in range(3):
        self.L()

    def U_r(self):

      for i in range(3):
        self.U()
    
    def D_r(self):

      for i in range(3):
        self.D()
    
    def F_r(self):

      for i in range(3):
        self.F()

    def B_r(self):

      for i in range(3):
        self.B()

    def mix(number_of_steps, self):
      
      for i in range(number_of_steps):
        a=random.randint(1,6)
        if a==1:
          self.R()
        if a==2:
          self.L()
        if a==3:
          self.U()
        if a==4:
          self.D()
        if a==5:
          self.F()
        if a==6:
          self.B()
        


# In[6]:


def cube_drawer(c):
 
    counter=0
    list_of_touples=[]

    for i in c.l[:,:,:]: # x=2 re nézzük= R oldal
        # i a sor
        #print(i)
        for j in i:
            # j az elem
            print(j)
            for k in j:
                #print(cube.dict_of_num_cubie[j])
                #cube.dict_of_num_cubie[j].l[0]=dict_of_color_num[ninestring[stringindex]] # 0 mert a cubie 0.eleme az x koord, 
                print(counter,c.dict_of_num_cubie[k])
                list_of_touples.append((counter,c.dict_of_num_cubie[k].l))
                counter+=1


    vertices= (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
        )

    vertices16=tuple([tuple([vertex[0]-2,vertex[1]+2,vertex[2]-2])for vertex in vertices ])
    vertices25=tuple([tuple([vertex[0]-2,vertex[1]+2,vertex[2]])for vertex in vertices ])
    vertices21=tuple([tuple([vertex[0]-2,vertex[1]+2,vertex[2]+2])for vertex in vertices ])

    vertices10=tuple([tuple([vertex[0]-2,vertex[1],vertex[2]-2])for vertex in vertices ])
    vertices5=tuple([tuple([vertex[0]-2,vertex[1],vertex[2]])for vertex in vertices ])
    vertices27=tuple([tuple([vertex[0]-2,vertex[1],vertex[2]+2])for vertex in vertices ])

    vertices14=tuple([tuple([vertex[0]-2,vertex[1]-2,vertex[2]-2])for vertex in vertices ])
    vertices8=tuple([tuple([vertex[0]-2,vertex[1]-2,vertex[2]])for vertex in vertices ])
    vertices15=tuple([tuple([vertex[0]-2,vertex[1]-2,vertex[2]+2])for vertex in vertices ])

    # ez az x[0] az x[:::] sorrendben

    vertices23=tuple([tuple([vertex[0],vertex[1]+2,vertex[2]-2])for vertex in vertices ])
    vertices3=tuple([tuple([vertex[0],vertex[1]+2,vertex[2]])for vertex in vertices ])
    vertices12=tuple([tuple([vertex[0],vertex[1]+2,vertex[2]+2])for vertex in vertices ])

    vertices7=tuple([tuple([vertex[0],vertex[1],vertex[2]-2])for vertex in vertices ])
    #vertices
    vertices4=tuple([tuple([vertex[0],vertex[1],vertex[2]+2])for vertex in vertices ])

    vertices9=tuple([tuple([vertex[0],vertex[1]-2,vertex[2]-2])for vertex in vertices ])
    vertices6=tuple([tuple([vertex[0],vertex[1]-2,vertex[2]])for vertex in vertices ])
    vertices26=tuple([tuple([vertex[0],vertex[1]-2,vertex[2]+2])for vertex in vertices ])

    # ez az x[1] az x[:::] sorrendben

    vertices19=tuple([tuple([vertex[0]+2,vertex[1]+2,vertex[2]-2])for vertex in vertices ])
    vertices11=tuple([tuple([vertex[0]+2,vertex[1]+2,vertex[2]])for vertex in vertices ])
    vertices18=tuple([tuple([vertex[0]+2,vertex[1]+2,vertex[2]+2])for vertex in vertices ])

    vertices24=tuple([tuple([vertex[0]+2,vertex[1],vertex[2]-2])for vertex in vertices ])
    vertices2=tuple([tuple([vertex[0]+2,vertex[1],vertex[2]])for vertex in vertices ])
    vertices13=tuple([tuple([vertex[0]+2,vertex[1],vertex[2]+2])for vertex in vertices ])

    vertices17=tuple([tuple([vertex[0]+2,vertex[1]-2,vertex[2]-2])for vertex in vertices ])
    vertices22=tuple([tuple([vertex[0]+2,vertex[1]-2,vertex[2]])for vertex in vertices ])
    vertices20=tuple([tuple([vertex[0]+2,vertex[1]-2,vertex[2]+2])for vertex in vertices ])

    vertices_of_all_cubies=[vertices16,
                            vertices25,
                            vertices21,

                            vertices10,
                            vertices5,
                            vertices27,

                            vertices14,
                            vertices8,
                            vertices15,

                            vertices23,
                            vertices3,
                            vertices12,

                            vertices7,
                            vertices,
                            vertices4,

                            vertices9,
                            vertices6,
                            vertices26,

                            vertices19,
                            vertices11,
                            vertices18,

                            vertices24,
                            vertices2,
                            vertices13,

                            vertices17,
                            vertices22,
                            vertices20

                           ]
    edges = ((0,1),
             (0,3),
             (0,4),
             (2,1),
             (2,3),
             (2,7),
             (6,3),
             (6,4),
             (6,7),
             (5,1),
             (5,4),
             (5,7))

    surfaces = ((3, 2, 7, 6), #xyz xyz
                (1, 5, 7, 2), 
                (0, 1, 2, 3),

                (4, 5, 1, 0), 
                (4, 0, 3, 6),
                (6, 7, 5, 4),)

    dict_of_num_color={1: "R", 2:"Y",3:"W", 4:"B", 5:"O", 6:"G"}
    dict_of_color_num={"R":1, "Y":2,"W":3, "B":4, "O":5, "G":6}
    dict_of_colornum_rbg={1: (1, 0, 0), 2:(1, 1, 0),3:(256, 256, 256), 4:(0, 0, 1), 5:(252, 173, 3), 6:(0, 1, 0)}

    colors = ((1, 0, 0), # red
              (0, 1, 0), # green
              (252, 173, 3), #orange
              (1, 1, 0), #yellow
              (256, 256, 256), # white 
              (0, 0, 1)) # blue

    def Cube_3d(vertices,colornums): # colornumsban  ()
        # először surfaces and color

        glBegin(GL_QUADS)

        cnum=2
        for surface in surfaces: 
            cnum+=1
            cnum=cnum%3

            for vertex in surface:

                if colornums[cnum] in dict_of_colornum_rbg.keys():
                    glColor3fv(dict_of_colornum_rbg[colornums[cnum]])
                else:

                    glColor3fv((252,0,210))
                glVertex3fv(vertices[vertex])

        glEnd()

        glBegin(GL_LINES) # line-drawing code
        for edge in edges: 
            for vertex in edge:
                glVertex3fv(vertices[vertex]) # sorban a pontok minden élre
        glEnd()

    def gameloop():

        pygame.init()
        display = (800,600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

        glTranslatef(0.0,0.0, -20) # z irábyan -5 move a kamerának, hogy lássuk a kockát

        glRotatef(25, 2, 1, 0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:
                        pygame.quit()
                    if event.key == pygame.K_LEFT:
                        glTranslatef(-0.5,0,0)
                    if event.key == pygame.K_RIGHT:
                        glTranslatef(0.5,0,0)

                    if event.key == pygame.K_UP:
                        glTranslatef(0,1,0)
                    if event.key == pygame.K_DOWN:
                        glTranslatef(0,-1,0)
                if event.type == pygame.MOUSEMOTION:
                    mouseMove = pygame.mouse.get_rel()

                    #glRotatef(mouseMove[0]*0.1, 0.0, 1.0, 0.0)
                    glRotatef(mouseMove[0]*0.1, 0.0, 1.0, 0.0)
                    #glRotatef(1.0, mouseMove[1]*0.1, 1.0, 0.0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        glTranslatef(0,0,1.0)

                    if event.button == 5:
                        glTranslatef(0,0,-1.0)


            #glRotatef(1, 1, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # clear

            glEnable (GL_DEPTH_TEST)
            num_of_colors=6
            # itt lenne az, hogy meghívjuk a kocka manipluációkat?
            # itt olvassuk végig a face színeket és adjuk tovább


            counter=0

            # itt minden cubie a nagy cubeban egy kicsi
            # minden kis cubie.l (color 3as kellene, hogy átadódjon)

            for tup in list_of_touples:
                vertices=vertices_of_all_cubies[tup[0]]
                chosen_tree=tup[1]
                Cube_3d(vertices,chosen_tree)

            '''for vertices in vertices_of_all_cubies:
                Cube_3d(vertices,chosen_three)
                counter+=1
                counter=counter%num_of_colors'''

            #Cube(vertices2)
            pygame.display.flip() # updates the display
            pygame.time.wait(10) # wait?

    gameloop()


# In[7]:


def cube_all_side_loader(cube,string="".join(["W"*9,"Y"*9,"B"*9,"O"*9,"G"*9,"R"*9])):
    sorrend="UDLFRB"
    sides=[
    cube.l[:,2,:],
    cube.l[:,0,:],
    cube.l[0,:,:],
    cube.l[:,:,0],
    cube.l[2,:,:],
    cube.l[:,:,2],   
    ]

    tuples_of_strings=[]
    counter_of_sides=0
    for i in range(0,len(string),9):
        print(string[i:i+9]) 
        tuples_of_strings.append((string[i:i+9],sorrend[counter_of_sides],sides[counter_of_sides]))
        counter_of_sides+=1
        tuples_of_strings
        # minde 3 koord lehet 0 1 2 ez 3*3*3 aza 27 koord amik a cubiek
        # oldalak:x - 0:: , 2::
        #    z- ::0 ::2  

    dict_of_num_color={1: "R", 2:"Y",3:"W", 4:"B", 5:"O", 6:"G"}
    dict_of_color_num={"R":1, "Y":2,"W":3, "B":4, "O":5, "G":6}

    index=0

    for i in sides: # x=2 re nézzük= R oldal
        ninestring=tuples_of_strings[index][0]
        print(ninestring)
        #index+=1
        # i a sor
        #print(i)
        stringindex=0
        for j in i:
            for k in j:
            # j az elem
                print(k)
                #print(cube.dict_of_num_cubie[j])
                if tuples_of_strings[index][1]=="U" or tuples_of_strings[index][1]=="D":
                    cube.dict_of_num_cubie[k].l[1]=dict_of_color_num[ninestring[stringindex]] # 0 mert a cubie 0.eleme az x koord, 
                if tuples_of_strings[index][1]=="R" or tuples_of_strings[index][1]=="L":
                    cube.dict_of_num_cubie[k].l[0]=dict_of_color_num[ninestring[stringindex]] # 0 mert a cubie 0.eleme az x koord, 
                if tuples_of_strings[index][1]=="F" or tuples_of_strings[index][1]=="B":
                    cube.dict_of_num_cubie[k].l[2]=dict_of_color_num[ninestring[stringindex]] # 0 mert a cubie 0.eleme az x koord, 

                print(cube.dict_of_num_cubie[k])
                #cube.dict_of_num_cubie[j].L()
                #print(cube.dict_of_num_cubie[j])
                stringindex+=1
        index+=1
        #print(dict_of_num_cubie[j])  


# In[ ]:




