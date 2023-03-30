from tkinter import Tk,Text,Button,END, Toplevel, font,re,Label
from tkinter import *
from collections import OrderedDict
from unittest.mock import seal
def tablas():
    tablas = Toplevel(ventana_principal)
    tablas = Interfaz(tablas)
def conjuntos():
    conjuntos = Toplevel(ventana_principal,height=300, width=300)
    conjuntos = Conjunt(conjuntos)
    
def sucesiones():
    sucesiones = Toplevel(ventana_principal,height=400, width=500)
    sucesiones = Sus(sucesiones)

def funciones():
    funciones = Toplevel(ventana_principal,height=400, width=900)
    funciones = Fun(funciones)


class pantallaprincipal:
    def __init__(self, ventana):
        #Inicializar la ventana con un título
        self.ventana=ventana
        self.ventana.title("Inicio")
        Label(text="FCC TOOLKIT", bg="Lightblue", width="30", height="2", font=("Calibri", 13)).pack()#ETIQUETA CON TEXTO
        Label(text="Fundamentos de Ciencias Computacionales", bg="Lightgray", width="30", height="1", font=("Calibri", 8)).pack()
        Label(text="").pack()
        Button(text="Tablas de verdad",height="2", width="15",command=tablas).pack()
        Button(text="Conjuntos", height="2", width="15", command= conjuntos).pack()
        Button(text="Sucesiones", height="2", width="15", command= sucesiones).pack()
        Button(text="Funciones", height="2", width="15", command= funciones).pack()
        Button(text="Salir", height="2", width="15").pack()
        Label(text="").pack()
        Label(text="Sofia & Marlem", bg="Lightgray", width="30", height="1", font=("Calibri", 8)).pack()

class Interfaz:
    def __init__(self, ventana):
        #Inicializar la ventana con un título
        self.ventana=ventana
        self.ventana.title("Calculadora de Tablas de Verdad")

        #Agregar una caja de texto para que sea la pantalla de la calculadora
        self.pantalla=Entry(ventana, width=40, font=("Helvetica",15)) 
        self.pantalla.pack()

        #Ubicar la pantalla en la ventana
        self.pantalla.grid(row=0, column=0, columnspan=5, padx=6, pady=6)

        #Inicializar la operación mostrada en pantalla como string vacío
        self.operacion=""

        #Crear los botones de la calculadora
        boton1=self.crearBoton(u"\u232B",escribir=False)
        boton2=self.crearBoton("~")
        boton3=self.crearBoton("^")
        boton4=self.crearBoton("v")
        boton5=self.crearBoton("→")
        boton6=self.crearBoton("↔")
        boton7=self.crearBoton("(")
        boton8=self.crearBoton(")")
        boton11=self.crearBoton("=",escribir=False,ancho=8,alto=8)

        #Ubicar los botones con el gestor grid
        botones=[boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton11]
        contador=0
        col = 0
        while col < 2:
            for fila in range(1,5):
                botones[contador].grid(row=fila,column=col)
                contador+=1
            col+=1
        boton11.grid(row=1,rowspan=4,column=3)
        
        return


    #Crea un botón mostrando el valor pasado por parámetro
    def crearBoton(self, valor, escribir=True, ancho=15, alto=2):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica",15), command=lambda:self.click(valor,escribir))



    #Controla el evento disparado al hacer click en un botón
    def click(self, texto, escribir):
        #Si el parámetro 'escribir' es True, entonces el parámetro texto debe mostrarse en pantalla. Si es False, no.
        if not escribir:
            #Sólo calcular si hay una operación a ser evaluada y si el usuario presionó '='
            if texto=="=" and self.operacion!="":
                self.operacion=self.pantalla.get()
                expresion = str
                variables = []
                x = 0
                enunciados = []
                pi = 0
                pd = 0
                pi2 = 0
                fila1 = []
                an = 0
                l = 0
                ceros = 0 
                ###obtener la expresion
                expresion = self.operacion
                for i in range(0,len(expresion)):
                    if expresion[i].isalpha() and expresion[i] != 'v':
                        ex = " " + str(expresion[i])
                        variables.append(ex)
                    l = len(variables)

                #obtener los enunciados individuales a evaluar 
                for i in range(0,len(expresion)):
                    if expresion[i] == "(":
                        pi+=1
                        expresion = expresion[:i+1] + " " + expresion[i+1:]
                        for j in range(i+1,len(expresion)):
                            if expresion[j] == "(":
                                expresion = expresion[:j+1] + " " + expresion[j+1:]
                                pi+=1
                            elif expresion[j] == ")":
                                pd+=1
                            if pi == pd:
                                enunciados.append(expresion[i:j+1])
                                i = i+((j+1)-i)
                                break
                for i in range(0,len(expresion)):
                    if expresion[i] == "~":
                        if expresion[i+1] == "(":
                            pi2+=1
                            for j in range(i+1,len(expresion)):
                                if expresion[j] == "(":
                                    pi+=1
                                elif expresion[j] == ")":
                                    pd+=1
                                if pi == pd:
                                    enunciados.append(expresion[i:j+1])
                                    i = i+((j+1)-i)
                                    break
                        else:
                            enunciados.append(expresion[i:i+2])          
                enunciados.append(expresion[0:len(expresion)])

                ###eliminar variables duplicadas 
                while True:
                    if x >= len(variables):
                        break
                    y = x+1
                    while True:
                        if y >= len(variables):
                            break
                        if variables[x] == variables[y]:
                            del variables[y:y+1]
                        else:
                            y+=1
                    x+=1                 



                ###imprimir primera fila
                columnas = len(variables)
                filas = 2**len(variables)
                fila1 = variables + enunciados

                la3 = ""
                for i in range(0,len(fila1)):
                    la3+="|   "
                    la3+=fila1[i]  + "   "
                la3+="|"
                #asignar valores a la matriz inicial 
                matrizi = [[" " for x in range(columnas)]for y in range(filas)]
                for i in range(1,len(variables)+1):
                    for j in range(0,(filas//(2**i))):
                        for k in range(0+((2**i)*j),0+((2**i)*j)+(2**i)-1):
                            matrizi[k][i-1] = True 
                        for l in range(((2**i)*(j+1))-(2**(i-1) ),(2**i)*(j+1)):
                            matrizi[l][i-1] = False
                #reemplazar los signos

                for i in range(0,len(enunciados)):
                    if "→" in enunciados[i]:
                        a = enunciados[i]
                        j = 0
                        an = 0
                        while True:
                            if j >= len(a):
                                break
                            if a[j] == "→":   
                                a = a[:j] + "" + a[j+1:]
                                if a[j-2] == "(" or a[j-3] == "(":
                                    l = 2
                                else:
                                    l = 0
                                if an != 0:
                                    enunciados[i] = a[0:j-(j-an)+l+1] + " not " + a[j-(j-an)+l+1:j] + " or "+ a[j:]

                                else:                  
                                    enunciados[i] = a[:l] + "not " + a[l:j] + " or "+ a[j:] 
                                a = enunciados[i]
                                an = a.rfind("or")+2
                            j+=1
                    if "↔" in enunciados[i]:
                        a = enunciados[i]
                        j = 0
                        while True:
                            if j >= len(a):
                                break
                            if a[j] == "↔":   
                                enunciados[i] = a.replace("↔"," == ")
                            j+=1
                for i in range(0,len(enunciados)):
                    enunciados[i] = enunciados[i].replace("~", " not ")
                    enunciados[i] = enunciados[i].replace("v"," or ")
                    enunciados[i] = enunciados[i].replace("^"," and ")
                ###matriz de enunciados
                j = 0
                matrizen = [[" " for x in range(0,len(enunciados))]for y in range(filas)]
                for i in range(0,len(enunciados)):
                    p = " " + enunciados[i]
                    j = 0
                    ceros = 0
                    while True:
                        if j >= len(p):
                            break
                        if p[j-1:j+1] in variables:
                            index = variables.index(p[j-1:j+1])
                            enunciado = p.replace(p[j-1:j+1]," matrizi[.0]" + "[" + str(index) + "]")
                            p = enunciado
                        j+=1
                    for a in range(0,len(enunciado)):
                        if enunciado[a] == "0" and enunciado[a-1] == '.':
                            ceros += 1
                    for b in range(0,filas):
                        n = enunciado
                        if b == 0:
                            for v in range(0,ceros):
                                enunciado = n.replace(".0",str(b))
                        else:
                            enunciado = n.replace("i["+str(b-1),"i["+str(b))
                        matrizen[b][i] = eval(enunciado)
                        
                        

                matrizf = [[" " for x in range(0,len(variables)+len(enunciados))]for y in range(filas)]

                ###juntar las valores de ambas matrices en una sola
                for i in range(0,len(variables)+len(enunciados)):
                    for j in range(0,filas):
                        
                        if i < len(variables):
                            matrizf[j][i] = matrizi[j][i]
                        else:
                            matrizf[j][i] = matrizen[j][i-len(variables)]
                #imprimir la matriz final
                label=""
                for i in range(0,filas):
                    for j in range(0,len(enunciados)+len(variables)):
                        if matrizf [i][j] == True:
                            label += "| " + str(matrizf[i][j]) + " "
                        else:
                            label += "| "+ str(matrizf[i][j])
                    label+="| "+"\n"
                newWindow = Toplevel(ventana_principal)
                label3 = Label(newWindow, text = la3)
                label3.config(font=('Helvatical bold',20))
                label2 = Label(newWindow, text = label)
                label2.config(font=('Helvatical bold',20))
                label3.pack()
                label2.pack()

                self.operacion=""
                expresion = ""
                self.limpiarPantalla()
                self.mostrarEnPantalla(expresion)
            #Si se presionó el botón de borrado, limpiar la pantalla
            elif texto==u"\u232B":
                self.operacion=""
                self.limpiarPantalla()
        #Mostrar texto
        else:
            self.operacion=self.pantalla.get()
            self.mostrarEnPantalla(texto)
        return
    

    #Borra el contenido de la pantalla de la calculadora
    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete(0,END)
        return
    

    #Muestra en la pantalla de la calculadora el contenido de las operaciones y los resultados
    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END, valor)

        return

class Conjunt:
    global op
    op = ""
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora de conjuntos")
        self.pantalla=Entry(ventana, width=22, font=("Helvetica",15))
        self.pantalla.pack()
        self.pantalla.place(relx=.115,rely=0)
        self.pantalla2=Entry(ventana, width=22, font=("Helvetica",15))
        self.pantalla2.pack()
        self.pantalla2.place(relx=.115,rely=0.1)
        self.pantalla3=Entry(ventana, width=22, font=("Helvetica",15))
        self.pantalla3.pack()
        self.pantalla3.place(relx=.115,rely=0.2)
        conjuntoa = Label(ventana,text="A = {")
        conjuntoa.pack()
        conjuntoa.place(relx=0,rely=0)
        conjuntoaf = Label(ventana,text="}")
        conjuntoaf.pack()
        conjuntoaf.place(relx=.95,rely=0)
        conjuntob = Label(ventana,text="B = {")
        conjuntob.pack()
        conjuntob.place(relx=0,rely=0.1)
        conjuntobf = Label(ventana,text="}")
        conjuntobf.pack()
        conjuntobf.place(relx=.95,rely=0.1)
        conjuntoc = Label(ventana,text="C = {")
        conjuntoc.pack()
        conjuntoc.place(relx=0,rely=0.2)
        conjuntocf = Label(ventana,text="}")
        conjuntocf.pack()
        conjuntocf.place(relx=.95,rely=0.2)
        operacion = Label(ventana,text="Operación: ")
        operacion.pack()
        operacion.place(relx=0,rely=0.3)
        lista = StringVar()
        lista.set("Operacion")
        options = [
            "Unión",
            "Interseccion",
            "Diferencia",
            "Diferencia simetrica"
        ]
        
        optionsu = StringVar()
        optionsu.set("A U B")
        listadu = ["A U B",
                "B U C",
                "A U C"]
        
        optionsin = StringVar()
        optionsin.set("A ∩ B")
        listadi = ["A ∩ B",
                "B ∩ C",
                "A ∩ C"]
        
        optionsd = StringVar()
        optionsd.set("A - B")
        listad = ["A - B",
                "B - C",
                "A - C"]  
        optionsds = StringVar()
        optionsds.set("A ∆ B")
        listads = ["A ∆ B",
                    "B ∆ C",
                    "A ∆ C"]
        
        unio = OptionMenu(ventana,optionsu, *listadu)
        intersection = OptionMenu(ventana,optionsin, *listadi)
        dropds = OptionMenu(ventana,optionsds, *listads) 
        drop = OptionMenu(ventana,lista, *options)
        drop.pack()
        drop.place(relx=0.21,rely=0.3)
        dif = OptionMenu(ventana,optionsd,*listad)
        str = self.pantalla.get()
        lista1 = str.split(",")
        str = self.pantalla2.get()
        listb = str.split(",")
        str = self.pantalla3.get()
        listc = str.split(",")

        def calcularuni():
            p = Label(ventana,text = "                                                                                                                                                                                                                             \n                                                                                                                                                                                                                                                                                               \n                                                                                                                                                                                                                                                                                                                                \n                                                                                                                                                                                                                                          ")  
            p.pack()
            p.place(relx=0.0,rely=0.8)
            str = self.pantalla.get()
            lista1 = str.split(",")
            str = self.pantalla2.get()
            listb = str.split(",")
            str = self.pantalla3.get()
            listc = str.split(",")
            opc =  optionsu.get()
            if opc == "A U B":
                string = "A U B = {"
                for i in range(len(lista1)):
                    string+=lista1[i] + ", "
                string+="} U {"
                for i in range(len(listb)):
                    string+=listb[i] + ", "
                string+="}"
                string2 = string[5:]
                x = 0
                while True:
                    if x >= len(string2):
                        break
                    if string2[x] in lista1 and string2[x] in listb:
                        string2= string2[:x] + "\u0332" + string2[x:]
                        x+=4
                    else:
                        x+=1
                string3 ="= {"
                mylist = lista1
                i = 0
                for i in range(len(listb)):
                    mylist.append(listb[i])
                final_list=list(OrderedDict.fromkeys(mylist))
                for i in range(len(final_list)):
                    string3+=final_list[i] + ", "
                string3 += "}"  
                p = Label(ventana,text = string)
                p.pack()
                p.place(relx = 0.25,rely=0.8)
                p2 = Label(ventana,text = string2)
                p2.pack()
                p2.place(relx=0.25,rely=0.86)
                p3 = Label(ventana,text=string3)
                p3.pack()
                p3.place(relx=0.25,rely=0.92)

            elif opc == "B U C":
                string = "B U C = {"
                for i in range(len(listb)):
                    string+=listb[i] + ", "
                string+="} U {"
                for i in range(len(listc)):
                    string+=listc[i] + ", "
                string+="}"
                string2 = string[5:]
                x = 0
                while True:
                    if x >= len(string2):
                        break
                    if string2[x] in listb and string2[x] in listc:
                        string2= string2[:x] + "\u0332" + string2[x:]
                        x+=4
                    else:
                        x+=1
                string3 ="= {"
                mylist = listb
                i = 0
                for i in range(len(listc)):
                    mylist.append(listc[i])
                final_list=list(OrderedDict.fromkeys(mylist))
                for i in range(len(final_list)):
                    string3+=final_list[i] + ", "
                string3 += "}"  
                p = Label(ventana,text = string)
                p.pack()
                p.place(relx = 0.25,rely=0.8)
                p2 = Label(ventana,text = string2)
                p2.pack()
                p2.place(relx=0.25,rely=0.86)
                p3 = Label(ventana,text=string3)
                p3.pack()
                p3.place(relx=0.25,rely=0.92)

            elif opc == "A U C":
                string = "A U C = {"
                for i in range(len(lista1)):
                    string+=lista1[i] + ", "
                string+="} U {"
                for i in range(len(listc)):
                    string+=listc[i] + ", "
                string+="}"
                string2 = string[5:]
                x = 0
                while True:
                    if x >= len(string2):
                        break
                    if string2[x] in lista1 and string2[x] in listc:
                        string2= string2[:x] + "\u0332" + string2[x:]
                        x+=4
                    else:
                        x+=1
                string3 ="= {"
                mylist = lista1
                i = 0
                for i in range(len(listc)):
                    mylist.append(listc[i])
                final_list=list(OrderedDict.fromkeys(mylist))
                for i in range(len(final_list)):
                    string3+=final_list[i] + ", "
                string3 += "}"  
                p = Label(ventana,text = string)
                p.pack()
                p.place(relx = 0.25,rely=0.8)
                p2 = Label(ventana,text = string2)
                p2.pack()
                p2.place(relx=0.25,rely=0.86)
                p3 = Label(ventana,text=string3)
                p3.pack()
                p3.place(relx=0.25,rely=0.92)

        def calcularint():
            p = Label(ventana,text = "                                                                                                                                                                                                                             \n                                                                                                                                                                                                                                                                                               \n                                                                                                                                                                                                                                                                                                                                \n                                                                                                                                                                                                                                          ")  
            p.pack()
            p.place(relx=0.0,rely=0.8)
            str = self.pantalla.get()
            lista1 = str.split(",")
            str = self.pantalla2.get()
            listb = str.split(",")
            str = self.pantalla3.get()
            listc = str.split(",")
            opc =  optionsin.get()

            if opc == "A ∩ B":
                string = "A ∩ B = {"
                for i in range(len(lista1)):
                    string+=lista1[i] + ", "
                string+="} ∩ {"
                for i in range(len(listb)):
                    string+=listb[i] + ", "
                string+="}"
                string2 = string[5:]
                x = 0
                while True:
                    if x >= len(string2):
                        break
                    if string2[x] in lista1 and string2[x] in listb:
                        string2= string2[:x] + "\u0332" + string2[x:]
                        x+=4
                    else:
                        x+=1
                string3 ="= {"
                list = lista1
                i = 0
                while True:
                    if i > len(lista1)-1:
                        break
                    if lista1[i] not in listb:
                        list.remove(lista1[i])
                        i-=1
                    else:
                        i+=1
                for i in range(len(list)):
                    string3+=list[i] + ", "
                string3 += "}"  
                p = Label(ventana,text = string)
                p.pack()
                p.place(relx = 0.25,rely=0.8)
                p2 = Label(ventana,text = string2)
                p2.pack()
                p2.place(relx=0.25,rely=0.86)
                p3 = Label(ventana,text=string3)
                p3.pack()
                p3.place(relx=0.25,rely=0.92)
                
            elif opc == "B ∩ C":
                string = "B ∩ C = {"
                for i in range(len(listb)):
                    string+=listb[i] + ", "
                string+="} ∩ {"
                for i in range(len(listc)):
                    string+=listc[i] + ", "
                string+="}"
                string2 = string[5:]
                x = 0
                while True:
                    if x >= len(string2):
                        break
                    if string2[x] in listb and string2[x] in listc:
                        string2= string2[:x] + "\u0332" + string2[x:]
                        x+=4
                    else:
                        x+=1
                string3 ="= {"
                list = listb
                i = 0
                while True:
                    if i > len(listb)-1:
                        break
                    if listb[i] not in listc:
                        list.remove(listb[i])
                        i-=1
                    else:
                        i+=1
                for i in range(len(list)):
                    string3+=list[i] + ", "
                string3 += "}"  
                p = Label(ventana,text = string)
                p.pack()
                p.place(relx = 0.25,rely=0.8)
                p2 = Label(ventana,text = string2)
                p2.pack()
                p2.place(relx=0.25,rely=0.86)
                p3 = Label(ventana,text=string3)
                p3.pack()
                p3.place(relx=0.25,rely=0.92)

            elif opc == "A ∩ C":
                string = "A ∩ C = {"
                for i in range(len(lista1)):
                    string+=lista1[i] + ", "
                string+="} ∩ {"
                for i in range(len(listc)):
                    string+=listc[i] + ", "
                string+="}"
                string2 = string[5:]
                x = 0
                while True:
                    if x >= len(string2):
                        break
                    if string2[x] in lista1 and string2[x] in listc:
                        string2= string2[:x] + "\u0332" + string2[x:]
                        x+=4
                    else:
                        x+=1
                string3 ="= {"
                list = lista1
                i = 0
                while True:
                    if i > len(lista1)-1:
                        break
                    if lista1[i] not in listc:
                        list.remove(lista1[i])
                        i-=1
                    else:
                        i+=1
                for i in range(len(list)):
                    string3+=list[i] + ", "
                string3 += "}"  
                p = Label(ventana,text = string)
                p.pack()
                p.place(relx = 0.25,rely=0.8)
                p2 = Label(ventana,text = string2)
                p2.pack()
                p2.place(relx=0.25,rely=0.86)
                p3 = Label(ventana,text=string3)
                p3.pack()
                p3.place(relx=0.25,rely=0.92)
            
            
        def calculardif():
            p = Label(ventana,text = "                                                                                                                                                                                                                             \n                                                                                                                                                                                                                                                                                               \n                                                                                                                                                                                                                                                                                                                                \n                                                                                                                                                                                                                                          ")  
            p.pack()
            p.place(relx=0.0,rely=0.8)
            str = self.pantalla.get()
            lista1 = str.split(",")
            str = self.pantalla2.get()
            listb = str.split(",")
            str = self.pantalla3.get()
            listc = str.split(",")
            opc =  optionsd.get()

            if opc == "A - B":
                string = "A - B = {"
                for i in range(len(lista1)):
                    string+=lista1[i] + ", "
                string+="} - {"
                for i in range(len(listb)):
                    string+=listb[i] + ", "
                string+="}"
                string2 = string[5:]
                x = 0
                while True:
                    if x >= len(string2):
                        break
                    if string2[x] in lista1 and string2[x] in listb:
                        string2= string2[:x] + "\u0332" + string2[x:]
                        x+=4
                    else:
                        x+=1
                string3 ="= {"
                list = lista1
                i = 0
                while True:
                    if i > len(lista1)-1:
                        break
                    if lista1[i] in listb:
                        list.remove(lista1[i])
                        i-=1
                    else:
                        i+=1
                for i in range(len(list)):
                    string3+=list[i] + ", "
                string3 += "}"  
                p = Label(ventana,text = string)
                p.pack()
                p.place(relx = 0.25,rely=0.8)
                p2 = Label(ventana,text = string2)
                p2.pack()
                p2.place(relx=0.25,rely=0.86)
                p3 = Label(ventana,text=string3)
                p3.pack()
                p3.place(relx=0.25,rely=0.92)
            elif opc == "B - C":
                string = "B - C = {"
                for i in range(len(listb)):
                    string+=listb[i] + ", "
                string+="} - {"
                for i in range(len(listc)):
                    string+=listc[i] + ", "
                string+="}"
                string2 = string[5:]
                x = 0
                while True:
                    if x >= len(string2):
                        break
                    if string2[x] in listb and string2[x] in listc:
                        string2= string2[:x] + "\u0332" + string2[x:]
                        x+=4
                    else:
                        x+=1
                string3 ="= {"
                list = listb
                i = 0
                while True:
                    if i > len(listb)-1:
                        break
                    if listb[i] in listc:
                        list.remove(listb[i])
                        i-=1
                    else:
                        i+=1
                for i in range(len(list)):
                    string3+=list[i] + ", "
                string3 += "}"  
                p = Label(ventana,text = string)
                p.pack()
                p.place(relx = 0.25,rely=0.8)
                p2 = Label(ventana,text = string2)
                p2.pack()
                p2.place(relx=0.25,rely=0.86)
                p3 = Label(ventana,text=string3)
                p3.pack()
                p3.place(relx=0.25,rely=0.92)
            elif opc == "A - C":
                string = "A - C = {"
                for i in range(len(lista1)):
                    string+=lista1[i] + ", "
                string+="} - {"
                for i in range(len(listc)):
                    string+=listc[i] + ", "
                string+="}"
                string2 = string[5:]
                x = 0
                while True:
                    if x >= len(string2):
                        break
                    if string2[x] in lista1 and string2[x] in listc:
                        string2= string2[:x] + "\u0332" + string2[x:]
                        x+=4
                    else:
                        x+=1
                string3 ="= {"
                list = lista1
                i = 0
                while True:
                    if i > len(lista1)-1:
                        break
                    if lista1[i] in listc:
                        list.remove(lista1[i])
                        i-=1
                    else:
                        i+=1
                for i in range(len(list)):
                    string3+=list[i] + ", "
                string3 += "}"  
                p = Label(ventana,text = string)
                p.pack()
                p.place(relx = 0.25,rely=0.8)
                p2 = Label(ventana,text = string2)
                p2.pack()
                p2.place(relx=0.25,rely=0.86)
                p3 = Label(ventana,text=string3)
                p3.pack()
                p3.place(relx=0.25,rely=0.92)
        def calculardifs():
            p = Label(ventana,text = "                                                                                                                                                                                                                             \n                                                                                                                                                                                                                                                                                               \n                                                                                                                                                                                                                                                                                                                                \n                                                                                                                                                                                                                                          ")  
            p.pack()
            p.place(relx=0.0,rely=0.8)
            str = self.pantalla.get()
            lista1 = str.split(",")
            str = self.pantalla2.get()
            listb = str.split(",")
            str = self.pantalla3.get()
            listc = str.split(",")
            opc =  optionsds.get()
            if opc == "A ∆ B":
                string = "A - B = {"
                for i in range(len(lista1)):
                    string+=lista1[i] + ", "
                string+="} - {"
                for i in range(len(listb)):
                    string+=listb[i] + ", "
                string+="}"
                string2 = string[5:]
                x = 0
                while True:
                    if x >= len(string2):
                        break
                    if string2[x] in lista1 and string2[x] in listb:
                        string2= string2[:x] + "\u0332" + string2[x:]
                        x+=4
                    else:
                        x+=1
                string3 ="= {"
                list = lista1
                i = 0
                while True:
                    if i > len(lista1)-1:
                        break
                    if lista1[i] in listb:
                        list.remove(lista1[i])
                        i-=1
                    else:
                        i+=1
                for i in range(len(list)):
                    string3+=list[i] + ", "
                string3 += "}"  
                p = Label(ventana,text = string)
                p.pack()
                p.place(relx = 0.25,rely=0.5)
                p2 = Label(ventana,text = string2)
                p2.pack()
                p2.place(relx=0.25,rely=0.56)
                p3 = Label(ventana,text=string3)
                p3.pack()
                p3.place(relx=0.25,rely=0.62)
                s2 = string3
                str = self.pantalla.get()
                lista1 = str.split(",")
                string = "B - A = {"
                for i in range(len(listb)):
                    string+=listb[i] + ", "
                string+="} - {"
                for i in range(len(lista1)):
                    string+=lista1[i] + ", "
                string+="}"
                string2 = string[5:]
                x = 0
                while True:
                    if x >= len(string2):
                        break
                    if string2[x] in lista1 and string2[x] in listb:
                        string2= string2[:x] + "\u0332" + string2[x:]
                        x+=4
                    else:
                        x+=1
                string3 ="= {"
                list = listb
                i = 0
                while True:
                    if i > len(listb)-1:
                        break
                    if listb[i] in lista1:
                        list.remove(listb[i])
                        i-=1
                    else:
                        i+=1
                for i in range(len(list)):
                    string3+=list[i] + ", "
                string3 += "}"  
                p = Label(ventana,text = string)
                p.pack()
                p.place(relx = 0.25,rely=0.7)
                p2 = Label(ventana,text = string2)
                p2.pack()
                p2.place(relx=0.25,rely=0.76)
                p3 = Label(ventana,text=string3)
                p3.pack()
                p3.place(relx=0.25,rely=0.82)
                s1 = "A ∆ B = (A - B)U(B - A)"
                print(s1)
                s3 = string3
                print(s3)
                s3 = s3.replace("=","")
                s4 = s2 + "U" + s3
                print(s4)
                s4.replace("=","")
                listaf=[]
                for i in range(len(s2)):
                    if s2[i].isdigit():
                        listaf.append(s2[i])
                for i in range(len(s3)):
                    if s3[i].isdigit():
                        listaf.append(s3[i])
                sfinal = ""
                for i in range(len(listaf)):
                    sfinal+=listaf[i] + ", "
                print(listaf)
                sf = s1 + s4 + " = {" + sfinal + "}"
                p4 = Label(ventana,text = sf)
                p4.pack()
                p4.place(relx=0,rely=0.9)
            elif opc == "B ∆ C":
                string = "B - C = {"
                for i in range(len(listb)):
                    string+=listb[i] + ", "
                string+="} - {"
                for i in range(len(listc)):
                    string+=listc[i] + ", "
                string+="}"
                string2 = string[5:]
                x = 0
                while True:
                    if x >= len(string2):
                        break
                    if string2[x] in listb and string2[x] in listc:
                        string2= string2[:x] + "\u0332" + string2[x:]
                        x+=4
                    else:
                        x+=1
                string3 ="= {"
                list = listb
                i = 0
                while True:
                    if i > len(listb)-1:
                        break
                    if listb[i] in listc:
                        list.remove(listb[i])
                        i-=1
                    else:
                        i+=1
                for i in range(len(list)):
                    string3+=list[i] + ", "
                string3 += "}"  
                p = Label(ventana,text = string)
                p.pack()
                p.place(relx = 0.25,rely=0.5)
                p2 = Label(ventana,text = string2)
                p2.pack()
                p2.place(relx=0.25,rely=0.56)
                p3 = Label(ventana,text=string3)
                p3.pack()
                p3.place(relx=0.25,rely=0.62)
                s2 = string3
                str = self.pantalla2.get()
                listb = str.split(",")
                string = "C - B = {"
                for i in range(len(listc)):
                    string+=listc[i] + ", "
                string+="} - {"
                for i in range(len(listb)):
                    string+=listb[i] + ", "
                string+="}"
                string2 = string[5:]
                x = 0
                while True:
                    if x >= len(string2):
                        break
                    if string2[x] in listc and string2[x] in listb:
                        string2= string2[:x] + "\u0332" + string2[x:]
                        x+=4
                    else:
                        x+=1
                string3 ="= {"
                list = listc
                i = 0
                while True:
                    if i > len(listc)-1:
                        break
                    if listc[i] in listb:
                        list.remove(listc[i])
                        i-=1
                    else:
                        i+=1
                for i in range(len(list)):
                    string3+=list[i] + ", "
                string3 += "}"  
                p = Label(ventana,text = string)
                p.pack()
                p.place(relx = 0.25,rely=0.7)
                p2 = Label(ventana,text = string2)
                p2.pack()
                p2.place(relx=0.25,rely=0.76)
                p3 = Label(ventana,text=string3)
                p3.pack()
                p3.place(relx=0.25,rely=0.82)
                s1 = "B ∆ C = (B - C)U(C - B)"
                print(s1)
                s3 = string3
                print(s3)
                s3 = s3.replace("=","")
                s4 = s2 + "U" + s3
                print(s4)
                s4.replace("=","")
                listaf=[]
                for i in range(len(s2)):
                    if s2[i].isdigit():
                        listaf.append(s2[i])
                for i in range(len(s3)):
                    if s3[i].isdigit():
                        listaf.append(s3[i])
                sfinal = ""
                for i in range(len(listaf)):
                    sfinal+=listaf[i] + ", "
                print(listaf)
                sf = s1 + s4 + " = {" + sfinal + "}"
                p4 = Label(ventana,text = sf)
                p4.pack()
                p4.place(relx=0,rely=0.9)
            elif opc == "A ∆ C":
                string = "A - C = {"
                for i in range(len(lista1)):
                    string+=lista1[i] + ", "
                string+="} - {"
                for i in range(len(listc)):
                    string+=listc[i] + ", "
                string+="}"
                string2 = string[5:]
                x = 0
                while True:
                    if x >= len(string2):
                        break
                    if string2[x] in lista1 and string2[x] in listc:
                        string2= string2[:x] + "\u0332" + string2[x:]
                        x+=4
                    else:
                        x+=1
                string3 ="= {"
                list = lista1
                i = 0
                while True:
                    if i > len(lista1)-1:
                        break
                    if lista1[i] in listc:
                        list.remove(lista1[i])
                        i-=1
                    else:
                        i+=1
                for i in range(len(list)):
                    string3+=list[i] + ", "
                string3 += "}"  
                p = Label(ventana,text = string)
                p.pack()
                p.place(relx = 0.25,rely=0.5)
                p2 = Label(ventana,text = string2)
                p2.pack()
                p2.place(relx=0.25,rely=0.56)
                p3 = Label(ventana,text=string3)
                p3.pack()
                p3.place(relx=0.25,rely=0.62)
                s2 = string3
                str = self.pantalla.get()
                lista1 = str.split(",")
                string = "C - A = {"
                for i in range(len(listc)):
                    string+=listc[i] + ", "
                string+="} - {"
                for i in range(len(lista1)):
                    string+=lista1[i] + ", "
                string+="}"
                string2 = string[5:]
                x = 0
                while True:
                    if x >= len(string2):
                        break
                    if string2[x] in lista1 and string2[x] in listc:
                        string2= string2[:x] + "\u0332" + string2[x:]
                        x+=4
                    else:
                        x+=1
                string3 ="= {"
                list = listc
                i = 0
                while True:
                    if i > len(listc)-1:
                        break
                    if listc[i] in lista1:
                        list.remove(listc[i])
                        i-=1
                    else:
                        i+=1
                for i in range(len(list)):
                    string3+=list[i] + ", "
                string3 += "}"  
                p = Label(ventana,text = string)
                p.pack()
                p.place(relx = 0.25,rely=0.7)
                p2 = Label(ventana,text = string2)
                p2.pack()
                p2.place(relx=0.25,rely=0.76)
                p3 = Label(ventana,text=string3)
                p3.pack()
                p3.place(relx=0.25,rely=0.82)
                s1 = "A ∆ C = (A - C)U(C - A)"
                print(s1)
                s3 = string3
                print(s3)
                s3 = s3.replace("=","")
                s4 = s2 + "U" + s3
                print(s4)
                s4.replace("=","")
                listaf=[]
                for i in range(len(s2)):
                    if s2[i].isdigit():
                        listaf.append(s2[i])
                for i in range(len(s3)):
                    if s3[i].isdigit():
                        listaf.append(s3[i])
                sfinal = ""
                for i in range(len(listaf)):
                    sfinal+=listaf[i] + ", "
                print(listaf)
                sf = s1 + s4 + " = {" + sfinal + "}"
                p4 = Label(ventana,text = sf)
                p4.pack()
                p4.place(relx=0,rely=0.9)
                print("")
        def option2():
            op = lista.get()
            if op == "Unión":
                unio.pack()
                unio.place(relx=0,rely=0.6)
                calcu = Button(ventana,text="calcular",command=calcularuni)
                calcu.pack()
                calcu.place(relx=0,rely=0.7)
            elif op == "Interseccion":
                intersection.pack()
                intersection.place(relx=0,rely=0.6)
                calcu = Button(ventana,text="calcular",command=calcularint)
                calcu.pack()
                calcu.place(relx=0,rely=0.7)
            elif op == "Diferencia":
                dif.pack()
                dif.place(relx=0,rely=0.6)
                calcu = Button(ventana,text="calcular",command=calculardif)
                calcu.pack()
                calcu.place(relx=0,rely=0.7)
            elif op  == "Diferencia simetrica":
                dropds.pack()
                dropds.place(relx=0,rely=0.6)
                calcu = Button(ventana,text="calcular",command=calculardifs)
                calcu.pack()
                calcu.place(relx=0,rely=0.7)
            
        
        cal = Button(ventana,text="Seleccionar",height="1", width="15",command=option2)
        cal.pack()
        cal.place(relx=0.3,rely=0.4)

class Sus:
    global op
    op = ""
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora de suseciones")
        self.pantalla=Entry(ventana, width=15, font=("Helvetica",15))
        self.pantalla.pack()
        self.pantalla.place(relx=.485,rely=0.1)
        self.pantalla2=Entry(ventana, width=8, font=("Helvetica",15))
        self.pantalla2.pack()
        self.pantalla2.place(relx=.300,rely=0.2)
        self.pantalla3=Entry(ventana, width=8, font=("Helvetica",15))
        self.pantalla3.pack()
        self.pantalla3.place(relx=.618,rely=0.2)
        conjuntoa = Label(ventana,text="Calcula tu sucesion!!")
        conjuntoa.pack()
        conjuntoa.place(relx=0.350,rely=0.02)
        conjuntoa = Label(ventana,text="Expresion algebraica:")
        conjuntoa.pack()
        conjuntoa.place(relx=0.2,rely=0.1)
        conjuntob = Label(ventana,text="Desde:")
        conjuntob.pack()
        conjuntob.place(relx=0.19,rely=0.2)
        conjuntoc = Label(ventana,text="Hasta:")
        conjuntoc.pack()
        conjuntoc.place(relx=0.505,rely=0.2)
        self.listbox= Listbox(ventana,width=30)

        def calsus():
            self.operacion=self.pantalla.get()
            self.limin=self.pantalla2.get()
            self.limmsup=self.pantalla3.get()
            formula=self.operacion.replace("k","x")
            contador = 0 
            py = 0.4
            ##Recursion
            def calcularsus(limin,limsup,operacion,contador):
                x = int(limsup)
                if x < int(limin):
                    return None 
                z = str(operacion)
                y = round(eval(operacion),4)
                if contador > 0:
                    z = "termino k(n-"+str(contador)+"): " + str(y)
                else:
                    z = "termino k(n): " + str(y) 
                self.listbox.insert(END,z)
                self.listbox.pack()
                self.listbox.place(relx=0.03, rely=0.4)
                calcularsus(limin,x-1,operacion,contador+1)
            suma = 0
            def calcularsumatoria(limin,limsup,operacion,suma):
                x = int(limsup)
                if x < int(limin):
                    z = "La sumatoria es: " + str(suma)
                    sum = Label(ventana,text=z)
                    sum.pack()
                    sum.place(relx= 0.5,rely=0.4) 
                    return None 
                y = eval(operacion)
                suma+=y
                calcularsumatoria(limin,x-1,operacion,suma)
            multi = 1
            def calcularmulti(limin,limsup,operacion,multi):
                x = int(limsup)
                if x < int(limin):
                    z = "La multiplicación es: " + str(multi)
                    mul = Label(ventana,text=z)
                    mul.pack()
                    mul.place(relx= 0.5,rely=0.5) 
                    return None 
                y = eval(operacion)
                multi*=y
                calcularmulti(limin,x-1,operacion,multi)
            calcularsus(self.limin,self.limmsup,formula,contador)
            calcularsumatoria(self.limin,self.limmsup,formula,suma)
            calcularmulti(self.limin,self.limmsup,formula,multi)
            print(self.operacion)
        cal = Button(ventana,text="Calcular",height="1", width="12", command=calsus)
        cal.pack()
        cal.place(relx=0.4,rely=0.3)

class Fun:
    global op
    op = ""
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Relaciones y Funciones")
        self.pantalla=Entry(ventana, width=15, font=("Helvetica",15))
        self.pantalla.pack()
        self.pantalla.place(relx=.402,rely=0.1)
        conjuntoa = Label(ventana,text="Identifica las propiedades de tu relacion!! introduce tus elementos de la siguiente manera (x,y);(x,y),..")
        conjuntoa.pack()
        conjuntoa.place(relx=0.250,rely=0.02)
        conjuntoa = Label(ventana,text="Introduce tu relacion = {")
        conjuntoa.pack()
        conjuntoa.place(relx=0.1,rely=0.1)
        conjuntoaf = Label(ventana,text="}")
        conjuntoaf.pack()
        conjuntoaf.place(relx= 0.685,rely= 0.1)
        lista =[]
        tuplas = []
        reflexividad = []
        reflexividad2 = []
        simetria = []
        simetria2 = []
        dominio=[]
        dominio2=[]
        cdominio=[]
        cdominio2=[]
        def relation():
            self.operacion=self.pantalla.get()
            self.operacion = self.operacion.replace('(','')
            self.operacion = self.operacion.replace(')','')
            lista = self.operacion.split(';')
            tuplas = [tuple(map(int,pair.split(',')))for pair in lista]
            for i in range(len(tuplas)):
                a = (tuplas[i][0],tuplas[i][0])
                reflexividad.append(a)
            reflexividad2 = list(set(reflexividad))
            for i in reflexividad2:
                if i not in tuplas:
                    r = False
                    break
                else:
                    r = True
            r1 = "Reflexividad: " + str(r)
            ref = Label(ventana,text=r1) 
            ref.pack()
            ref.place(relx=.450,rely=0.3) 

            for j in range(len(tuplas)):
                b = (tuplas[j][1],tuplas[j][0])
                simetria.append(b)
            simetria2 = list(set(simetria))
            for j in simetria2:
                if j not in tuplas:
                    s = False
                    break
                else:
                    s = True
            si = "Simetria:" + str(s)
            sim = Label(ventana,text=si)
            sim.pack()
            sim.place(relx=0.45,rely=0.4)

            transitividad = True
            for i in range(len(tuplas)):
                x = tuplas[i][1]
                if not transitividad:
                    break
                for j in range(1,len(tuplas)):
                    if x == tuplas[j][0]:
                        tranc = (tuplas[i][0],tuplas[j][1])
                        if tranc not in tuplas:
                            transitividad = False
                            break
                        else: 
                            transitividad = True
            if not transitividad:
                t = "transitividad = " + str(transitividad) + " no esta el punto: " + str(tranc)
            else:
                t = "transitividad = " + str(transitividad)
            trans = Label(ventana,text=t)
            trans.pack()
            trans.place(relx=0.45,rely=0.5)

            for i in range(len(tuplas)):
                a = (tuplas[i][0])
                dominio.append(a)
                dominio2 = list(set(dominio))
            d = "dominio=" + str(dominio2)
            dom = Label(ventana,text=d)
            dom.pack()
            dom.place(relx=.450,rely=0.6)

            for i in range(len(tuplas)):
                a = (tuplas[i][1])
                cdominio.append(a)
                cdominio2=list(set(cdominio))
            c = "condomio = " + str(cdominio2)
            con = Label(ventana,text=c)
            con.pack()
            con.place(relx=0.45,rely=0.7) 

                
            

            
            funcion = True
            for i in range(len(tuplas)):
                if not funcion:
                    break
                for j in range(1,(len(tuplas))):
                    if (tuplas[i][0] == tuplas[j][0]) and (tuplas[i][1] != tuplas[j][1]):
                        coor = (tuplas[j][0],tuplas[j][1])
                        funcion = False
                        break
            if not funcion:
                fu = "Es función?: "+str(funcion)+ " Está el punto:  " + str(coor)
            else:
                fu = "Es función?:"+str(funcion)
            fun = Label(ventana,text=fu)
            fun.pack()
            fun.place(relx=0.45,rely=0.8)         
            
        cal = Button(ventana,text="Calcular",height="1", width="12",command=relation)
        cal.pack()
        cal.place(relx=0.4,rely=0.2)
    
        

ventana_principal= Tk()
calculadora=pantallaprincipal(ventana_principal)
mainloop()
