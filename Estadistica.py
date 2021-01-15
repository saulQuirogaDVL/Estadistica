import numpy as np
import math
import matplotlib.pyplot as plt
datos = input('Coloque la ruta del archivo txt: ')
cantDatos=list()
ListaSO=np.loadtxt(datos)
#elimina los repetidos de la lista
def eliminar_repetidos(lista):
    nueva=[]
    for elemento in lista:
        if not elemento in nueva:
            nueva.append(elemento)        
    return nueva

ListaSR=eliminar_repetidos(ListaSO)
#ordena los elementos de la lista(Bubble)
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

bubbleSort(ListaSR)

tam=range(len(ListaSO))
tam2=range(len(ListaSR))

for i in  tam2:   
   cont=0
   for j in tam:
          if ListaSR[i]==ListaSO[j]: 
              cont+=1
   cantDatos.append(cont)
  
def Calcular_Frecuencia(ListaF):
    suma=0
    tamanio=range(len(ListaF))
    for i in tamanio:
        suma += ListaF[i]
    return suma

totalDatos=Calcular_Frecuencia(cantDatos)+1         
       
#media arimetica 
def Calcular_Media(ListaD):
    suma=0
    cont=0
    tamanio=range(len(ListaD))
    for u in tamanio:
        suma+=(ListaD[u])
        cont+=1
    return suma/cont

Media_Aritmetica=Calcular_Media(ListaSO)

#mediana
def Calcular_Mediana(ListaD):
    tamanio=len(ListaD)
    mitad=(tamanio%2)
    medio=int(tamanio/2)
    if(mitad==1):
        return ListaD[medio]
    else:
        return (ListaD[medio]+ListaD[medio-1])/2       
bubbleSort(ListaSO)
Mediana=Calcular_Mediana(ListaSO)
      
#moda
def Calcular_Moda(ListaD,ListaF):
    val_max=0
    fre_max=0
    valor_final=""
    tamanio=range(len(ListaF))
    for i in tamanio:
        if ListaF[i]>fre_max:
            fre_max=ListaF[i]
            val_max=ListaD[i]
            valor_final=val_max
        elif ListaF[i]==fre_max:
            valor_final="no tiene moda"
    return valor_final

Moda=Calcular_Moda(ListaSR,cantDatos)

#media geometrica
def Calcular_Geometrica(ListaD):
    suma=1
    cont=0
    tamanio=range(len(ListaD))
    for i in tamanio:
        suma*=ListaD[i]
        cont+=1
    return suma**(1 /cont)

Media_Geometrica=Calcular_Geometrica(ListaSO)

#media armonica
def Calcular_Armonica(ListaD):
    suma=0
    cont=0
    tamanio=range(len(ListaD))
    for i in tamanio:
        suma+=1/ListaD[i]
        cont+=1
    return cont/suma

Media_Armonica=Calcular_Armonica(ListaSO)

#desviacion media
def Calcular_Desviacion(ListaD):
    suma=0
    valor=0
    cont=0
    tamanio=range(len(ListaD))
    for i in tamanio:
        valor=ListaD[i]-Media_Aritmetica
        if(valor<0):
           valor=valor*-1
        suma+=valor
        cont+=1
    return suma/cont

Desviacion=Calcular_Desviacion(ListaSO)

#Desviacion estandar
def Calcular_Desviacion_Estandar(ListaD):
    suma=0
    valor=0
    cont=0
    tamanio=range(len(ListaD))
    for i in tamanio:
        valor=(ListaD[i]-Media_Aritmetica)**2
        suma+=valor
        cont+=1
    if(cont<=30):
        cont-1
    return math.sqrt(suma/cont)

Desviacion_Estandar=Calcular_Desviacion_Estandar(ListaSO)   

#varianza
def Calcular_Varianza(desv_est):
    return desv_est**2

Varianza=Calcular_Varianza(Desviacion_Estandar)   

#dispersion relativa
def Calcular_Dispercion(desv_est,med_arit):
    return (desv_est/med_arit)*100

Dispercion=Calcular_Dispercion(Desviacion_Estandar,Media_Aritmetica)

#momento respecto de 0
def Calcular_Momento(ListaD,NDM):
    suma=0
    cont=0
    tamanio=range(len(ListaD))
    for i in tamanio:
        suma+=ListaD[i]**NDM
        cont+=1
    return suma/cont

momento_uno=Calcular_Momento(ListaSO,1)
momento_dos=Calcular_Momento(ListaSO,2)
momento_tres=Calcular_Momento(ListaSO,3)
momento_cuatro=Calcular_Momento(ListaSO,4)

#momento respecto de cualquier origen
def Calcular_Momento_X(ListaD,NDM,const):
    suma=0
    cont=0
    tamanio=range(len(ListaD))
    for i in tamanio:
        suma+=(ListaD[i]-const)**NDM
        cont+=1
    return suma/cont

constante=1
momento_uno_x=Calcular_Momento_X(ListaSO,1,constante)
momento_dos_x=Calcular_Momento_X(ListaSO,2,constante)
momento_tres_x=Calcular_Momento_X(ListaSO,3,constante)
momento_cuatro_x=Calcular_Momento_X(ListaSO,4,constante)

#momento respecto a la media
momento_dos_M=momento_dos_x-(momento_uno_x**2)
momento_tres_M=momento_tres_x-((3*momento_uno_x)*momento_dos_x)+(2*(momento_uno_x**3))
momento_cuatro_M=momento_cuatro_x-((4*momento_uno_x)*momento_tres_x)+((6*(momento_uno_x**2))*momento_dos_x)-(3*(momento_uno_x**4))

#sesgo
def Calcular_Sesgo(med,mod,desv_est,median):
    if(mod=="no tiene moda"):
        return (3*(med-median))/desv_est
    else:
        return (med-mod)/desv_est

def Calcular_Direccion_Sesgo(valor):
    if(valor>0):
        return "derecha"
    else:
        return "izquierda"
    
def Calcular_Distribucion_Sesgo(valor):
    if(valor<0):
        valor=valor*-1
    if(valor==0):
        return "simetrica"
    elif(valor>0 and valor<=0.10):
        return "ligeramente sesgado"
    elif(valor>0.10 and valor<=0.30):
        return "moderadamente sesgado"
    elif(valor>0.30 and valor<=1):
        return "marcadamente sesgado"
    
    
#Sesgo=round(Calcular_Sesgo(Media_Aritmetica,Moda,Desviacion_Estandar,Mediana),2)

Sesgo=(momento_tres_M)/(Desviacion_Estandar**3)
if(Sesgo>0):
    Sesgo=(round(Sesgo-3,3))
else:
    Sesgo=(round(Sesgo,3))
    
Direccion_Sesgo=Calcular_Direccion_Sesgo(Sesgo)  
Distribucion_Sesgo=Calcular_Distribucion_Sesgo(Sesgo)     

#curtosis

Curtosis=(momento_cuatro_M)/(Desviacion_Estandar**4)
if(Curtosis>0):
    Curtosis=(round(Curtosis-3,3))
else:
    Curtosis=(round(Curtosis,3))

Distribucion_Curtosis=""

if(Curtosis<0):
        Curtosis=Curtosis*-1

if(Curtosis==0.263):
     Distribucion_Curtosis="Mesocutica"
elif(Curtosis>0.263):
    Distribucion_Curtosis="Leptocurtica"
elif(Curtosis<0.263):
    Distribucion_Curtosis="Platicurtica"
    
#histogramas
X=[x for x in range(len(ListaSR))]
plt.bar(ListaSR,X,label='Datos 1',width=0.5,color='lightblue')
plt.title('Gradico de barras')
plt.ylabel('Frecuencias')
plt.xlabel('Datos') 
plt.legend()
plt.show()

#C:\Users\hp\Documents\Univalle\Estadistica Computacional\Proyecto_Final

print("La media aritmetica es: "+str(round(Media_Aritmetica,2)))
print("La mediana es: "+str(Mediana))
print("La moda es: "+str(Moda))  
print("La media geometrica es:"+str(round(Media_Geometrica,2)))   
print("La media armonica es:"+str(round(Media_Armonica,2)))  
print("La desviacion media es: "+str(round(Desviacion,2)))
print("La desviacion estandar es: "+str(round(Desviacion_Estandar,2)))
print("La dispercion absoluta: "+str(round(Desviacion_Estandar,2)))      
print("La dispecion relativa es: "+str(round(Dispercion,2))+"%")
print("Momentos respecto de 0:")
print("momento uno: "+str(momento_uno))
print("momento dos: "+str(momento_dos))
print("momento tres: "+str(momento_tres))
print("momento cuatro: "+str(momento_cuatro))
print("Momentos respecto de cualquier origen (X="+str(constante)+")")
print("momento uno X: "+str(momento_uno_x))
print("momento dos X: "+str(momento_dos_x))
print("momento tres X: "+str(momento_tres_x))
print("momento cuatro X: "+str(momento_cuatro_x))
print("Momentos respecto a la media")
print("momento dos M: "+str(momento_dos_M))
print("momento tres M: "+str(momento_tres_M))
print("momento cuatro M: "+str(momento_cuatro_M))
print("Sesgo: "+str(Sesgo))
print("el sesgo es "+str(Distribucion_Sesgo)+" hacia la "+str(Direccion_Sesgo))
print("Curtosis: "+str(Curtosis))
print("la curtosis es: "+str(Distribucion_Curtosis))


      
    

          
           
       