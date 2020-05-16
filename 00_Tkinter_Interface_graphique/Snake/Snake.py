# -*- coding: utf-8 -*-
"""
Created on May 16 2020

@author: Daniel Hryniewski
"""
from tkinter import *
from random import randint


#Coordonnée cube aleatoire
def random_cube():
    global window_width, window_height
    lx = []
    ly = []
    for i in range(window_width):
        if i % 20 == 0:
            lx.append(i)
    for i in range(window_height):
        if i % 20 == 0:
            ly.append(i)
    cube_x0 = lx[randint(0, len(lx)-1)]
    cube_y0 = ly[randint(0, len(ly)-1)]
    return cube_x0, cube_y0
        
# Aller vers le haut
def action_up(event):
    global dx, dy
    if dy != 20:
        dy = -20
        dx = 0

# Aller ves le bas
def action_down(event):
    global dx, dy
    if dy != -20:
        dy = 20
        dx = 0
    
# Aller vers la droite
def action_right(event):
    global dx, dy
    if dx != -20:
        dy = 0
        dx = 20

# Aller vers la gauche
def action_left(event):
    global dx, dy
    if dx != 20:
        dy = 0
        dx = -20


window_play = 400
window_width = 500
window_height = window_play - 100
points = 0 #Points initiaux (influance sur la vitesse mouvement)
speed = 180 #Vitesse de mouvement initiale
dx = 20 # Deplacement horizentale initiale
dy = 0 # Deplacement verticale initiale

# Coordonné snake
x0, y0 = 200, 200
snake = [[80,200], [100,200], [120,200], [140,200]]

# Coordonné cube
cube_x0 = random_cube()[0]
cube_y0 = random_cube()[1]

# Creation de la fenetre du jeux
root = Tk()
root.title("Snake")
canvas = Canvas(root, width=window_width-2, height=window_play, bg="white")
canvas.pack(fill="both", expand=True)


#les touches de clavier
canvas.bind_all("<Up>", action_up)
canvas.bind_all("<Down>", action_down)
canvas.bind_all("<Right>", action_right)
canvas.bind_all("<Left>", action_left)


def main():
    
    global x0, y0, dx, dy, cube_x0, cube_y0, snake
    global window_width, window_height, points, speed, canvas
    
    #Verification de defaire
    if -1 < x0 < window_width and -1 < y0 < window_height and [x0,y0] not in snake[0:len(snake)-1]:
        
        # Supprimer tout sur l'ecran
        canvas.delete("all")

        # mouvement du Snake
        snake.append([snake[len(snake)-1][0]+dx,snake[len(snake)-1][1]+dy])
        for i in range(len(snake)):
            if i != 0:
                snake[i-1] = snake[i]
        snake.pop(len(snake)-1)
        
        # Coordonné de la tete du snake
        x0 = snake[len(snake)-1][0]
        y0 = snake[len(snake)-1][1]
        
        
        # Afficher tout les element du jeu
        playground = canvas.create_rectangle(0, 0, window_width, window_height, width=1, outline='#9AEDFF', fill="#9AEDFF")
        cube = canvas.create_rectangle(cube_x0, cube_y0, cube_x0+20, cube_y0+20, width=1, fill="red")
        num_score = canvas.create_text(120, window_play-window_play/10, text=str(points),font=('CourierNew',18))
        text_points = canvas.create_text(window_width/10, window_play-window_play/10, text="Score:",font=('CourierNew',18))
        
        for i in snake: #Afficher Snake
            if i == snake[len(snake)-1]:
                snake_head = canvas.create_rectangle(i[0], i[1], i[0]+20, i[1]+20, width=1, fill="#00611C")
            else:
                canvas.create_rectangle(i[0], i[1], i[0]+20, i[1]+20, width=1, fill="green")  


        if x0 == cube_x0 and y0 == cube_y0: #Snake mange un cube
            points += 10
            
            while [cube_x0, cube_y0] in snake: #Ne pas afficher de cube sur le snake
                
                # Supprimer l'ancien cube et afficher un nouveau
                canvas.delete(cube)
                canvas.itemconfigure(num_score, text=str(points))
                cube_x0 = random_cube()[0]
                cube_y0 = random_cube()[1]
                cube = canvas.create_rectangle(cube_x0, cube_y0, cube_x0+20, cube_y0+20, width=1, fill="red")
            
            # ajouter un cube au snake
            snake.reverse()
            snake.append([snake[0][0]-dx, snake[0][1]-dy])   
            snake.reverse()
        
        
        canvas.after(int(speed-points/5), main) #en millisecondes
        
    else: # En cas de defaite:
        canvas.create_text(window_width/2, window_height/2, text="Game Over",font=('CourierNew',24))
        

if __name__=="__main__":
    main()
    
    
root.mainloop()