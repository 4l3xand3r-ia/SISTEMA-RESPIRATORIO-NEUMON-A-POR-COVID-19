"""
Proyecto: neumonia (COVID-19)


Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México


Nombre del alumno: Alexander Torres Avila
Número de control: 21212848
Correo institucional: l21212848@tectijuana.edu.mx


Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
# Librerías para cálculo numérico y generación de gráficas
import numpy as np
import math as m
import matplotlib.pyplot as plt 
import control

x0,t0,tF,dt = 0,0,30,1E-3
N = round((tF-t0)/dt)+1 
t = np.linspace(t0,tF,N) 

# Paciente sano
c1=0.005
c2=0.200
c3=0.200
l1=0.001
l2=0.250
r1=2
r2=0.5
a1 = c1*c2*c3*l1*l2
a2 = c1*c2*c3*l1*r2+c1*c2*c3*l2*r1
a3 = c1*c2*l1+c1*c3*l1+c2*c3*l1+c2*c3*l2+c1*c2*c3*r1*r2
a4 = c1*c2*r1+c1*c3*r1+c2*c3*r1+c2*c3*r2
a5 = c2+c3
num = [a5]
den = [a1,a2,a3,a4,a5]
sys = control.tf(num,den) 
print('Paciente sano (control):')
print(sys)

#Paciente Enfermo
c1=0.005
c2=0.350
c3=0.350
l1=0.001
l2=0.400
r1=5
r2=1
a1 = c1*c2*c3*l1*l2
a2 = c1*c2*c3*l1*r2+c1*c2*c3*l2*r1
a3 = c1*c2*l1+c1*c3*l1+c2*c3*l1+c2*c3*l2+c1*c2*c3*r1*r2
a4 = c1*c2*r1+c1*c3*r1+c2*c3*r1+c2*c3*r2
a5 = c2+c3
num = [a5]
den = [a1,a2,a3,a4,a5]
sysE = control.tf(num,den) 
print('Paciente enfermo (caso):')
print(sysE)

#Controlador
Rr = 1.4272E5
Re = 4648.0
Ce = 2.3563E-6
Cr = 1E-6
numPID = [Re*Rr*Ce*Cr,Re*Ce+Rr*Cr,1]
denPID = [Re*Cr,0]
PID = control.tf(numPID,denPID)

#Control de tratamiento
X = control.series(PID,sysE)
sysPID = control.feedback(X,1,sign=-1)
print('Sistema con tratamiento:')
print(sysPID)

#Respiracion normal
u = 2.5*np.sin(m.pi/2*t)
fig1 = plt.figure()
ts,Vs = control.forced_response(sys,t,u,x0)
plt.plot(t,Vs,"-",color = [0,1,0],label = "PA(t): Control")
ts,Ve = control.forced_response(sysE,t,u,x0)
plt.plot(t,Ve,"-",color = [0.6,0.4,0.8],label = "PA(t): Caso")
ts,pid = control.forced_response(sysPID,t,Vs,x0)
plt.plot(t,pid,"--",color = [0,0.4,1],label = "PA(t): Tratamiento")
plt.grid(False)
plt.xlim(0,30)
plt.xticks(np.arange(0,31,5))
plt.ylim(-2.5,2.5)
plt.yticks(np.arange(-2.5,3,0.5))
plt.xlabel('$t$ [s]')
plt.ylabel('$V(t)$ $[V]$')
plt.legend(bbox_to_anchor = (0.5,-0.23),loc = 'center',ncol = 3)
plt.show()
fig1.set_size_inches(10,4)
fig1.savefig('Respiración_normal.png',dpi = 1000,bbox_inches = 'tight')
fig1.savefig('Respiración_normal.pdf',dpi = 1000,bbox_inches = 'tight')

#respiracion Anormal (Taquipnea)
u1 = 1.5*np.sin(m.pi*t)
fig2 = plt.figure()
ts,Vs = control.forced_response(sys,t,u1,x0)
plt.plot(t,Vs,"-",color = [0,1,0],label = "PA(t): Control")
ts,Ve = control.forced_response(sysE,t,u1,x0)
plt.plot(t,Ve,"-",color = [0.6,0.4,0.8],label = "PA(t): Caso")
ts,pid = control.forced_response(sysPID,t,Vs,x0)
plt.plot(t,pid,"--",color = [0,0.4,1],label = "PA(t): Tratamiento")
plt.grid(False)
plt.xlim(0,30)
plt.xticks(np.arange(0,31,5))
plt.ylim(-1.5,1.5)
plt.yticks(np.arange(-1.5,2,0.5))
plt.xlabel('$t$ [s]')
plt.ylabel('$V(t)$ $[V]$')
plt.legend(bbox_to_anchor=(0.5,-0.23),loc = 'center',ncol = 3)
plt.show()
fig2.set_size_inches(10,4)
fig2.savefig('Respiración_Neumonia.png',dpi = 1000,bbox_inches = 'tight')
fig2.savefig('Respiración_Neumonia.pdf',dpi = 1000,bbox_inches = 'tight')