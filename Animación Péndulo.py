from vpython import *

# Realizado en Computación Científica II

display(width=600,height=600,center=vector(0,12,0),background=color.white)
g=9.8 # Aceleración de la gravedad
bob=sphere(pos=vector(5,2,0),radius=3,color=color.blue)
pivot=vector(0,20,0)
roof=box(pos=pivot,size=vector(10,0.5,10),color=color.green)
rod=cylinder(pos=pivot,axis=bob.pos-pivot,radius=0.3,color=color.red)
t=0 # Tiempo
dt=0.01 # Intervalo de tiempo
l=mag(bob.pos-pivot) # Longuitud del péndulo
cs=(pivot.y-bob.pos.y)/l # Cálculo del ángulo
theta=acos(cs) # Ángulo en la dirección vertical
vel=0.0 # Velocidad angular
while (t<100):
 rate(100) # Máximo de 100 cálculos por segundo
 acc=-g/l*sin(theta) # Actualizamos la aceleración angular
 theta=theta+vel*dt #  Actualizamos la posición angular
 vel=vel+acc*dt #  Actualizamos la velocidad angular
 bob.pos=vector(l*sin(theta),pivot.y-l*cos(theta),0) # Calculamos la posición
 rod.axis=bob.pos-rod.pos 
 t=t+dt # Actualizamos el tiempo