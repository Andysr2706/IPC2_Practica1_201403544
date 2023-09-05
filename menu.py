import sys
import ListaSimple as ListaSimple
import graphviz as graphviz
import pieza as pieza

class Menu:

    ListaPieza = ListaSimple.Lista_simple()
    AnchoTablero = 0
    AlturaTablero = 0
    
    def menuprincipal():
            #os.system("cls")
            ruta = ''
            
            

            print("\n-----------------------Practica 1 IPC 2-----------------------")
            print("            Andy Jeferson Salas Ramirez 201403544")

            CondicionMenu = True
            SeleccionMenu = 0

            while CondicionMenu == True:
                print("-------------------------Coloréalo-------------------------")
                print("1. Crear Tablero.")
                print("2. Agregar piezas.")
                print("3. Datos del estudiante.")
                print("4. salir.\n")
                print("-------------------------Guatematel-------------------------")
                SeleccionMenu = int(input())

                if SeleccionMenu ==1:
                    print('')
                    print("------------------------------------------------------------")
                    print('')
                    print("Por favor ingrese el ancho del tablero. ")
                    Menu.ListaPieza.cabeza = None
                    Menu.AnchoTablero = int(input())
                    print('')
                    print("------------------------------------------------------------")
                    print('')
                    print("Por favor ingrese el alto del tablero. ")
                    print('')
                    Menu.AlturaTablero = int(input())
                    print('')
                    print("------------------------------------------------------------")
                    print("Tablero creado exitosamente. \n")
                    print('')
                    
                if SeleccionMenu == 2:
                    ColorPieza     = ''
                    ColorPiezaA    = ''
                    FilaPieza      = 0
                    ColumnaPieza   = 0
                    CondicionPieza = True

                    while CondicionPieza == True:
                        print('')
                        print("------------------------------------------------------------")
                        print('')
                        print("Por favor elija su color. ")
                        print('AZUL')
                        print('ROJO')
                        print('VERDE')
                        print('PURPURA')
                        print('NARANJA')
                        print('')
                        print("------------------------------------------------------------")
                        print('')
                        ColorPieza = str(input())
                        print('')
                        print("------------------------------------------------------------")
                        print('')
                        print(ColorPieza + ': ')
                        print("Por favor ingrese la fila en la que desea colocar la pieza. ")
                        print("Rango: 1 - " + str(Menu.AlturaTablero))
                        FilaPieza = int(input())
                        print('')
                        print("------------------------------------------------------------")
                        print('')
                        print("Por favor ingrese la columna en la que desea colocar la pieza. ")
                        print("Rango: 1 - " + str(Menu.AnchoTablero))
                        ColumnaPieza = int(input())
                        print('')
                        print("------------------------------------------------------------")
                        print('')
                        print('Pieza Color: ' + ColorPieza + ', Fila: ' +str(FilaPieza) +', Columna: ' +str(ColumnaPieza)+' Agregada exitosamente.')
                        
                        if(ColorPieza == 'AZUL'):
                            ColorPiezaA = 'A'
                        elif(ColorPieza == 'ROJO'):
                            ColorPiezaA = 'R'
                        elif(ColorPieza == 'VERDE'):
                            ColorPiezaA = 'V'
                        elif(ColorPieza == 'PURPURA'):
                            ColorPiezaA = 'P'
                        elif(ColorPieza == 'NARANJA'):
                            ColorPiezaA = 'N'

                        NuevoDato = pieza.pieza(FilaPieza, ColumnaPieza, ColorPieza, ColorPiezaA)

                        Menu.ListaPieza.agregar_al_inicio(NuevoDato)
                        NodoAuxiliar = Menu.ListaPieza.cabeza
                        Menu.ListaPieza.cabeza = Menu.ordenarListaElementos(NodoAuxiliar)

                        print('')
                        print("------------------------------------------------------------")
                        print('Tablero actual: ')
                        print("")

                        NodoAuxiliar = Menu.ListaPieza.cabeza
                        filatablero = ''
                        filaactual = 1
                        columnaactual = 1

                        CondicionImpresion = True

                        while CondicionImpresion:
                            columnaactual = 1
                            for columnaactual in range(1, Menu.AnchoTablero + 1):
                                if NodoAuxiliar != None:
                                    if(NodoAuxiliar.dato.fila == filaactual and NodoAuxiliar.dato.columna == columnaactual):

                                        if columnaactual == 1:
                                            filatablero = '| '+NodoAuxiliar.dato.colorA+' | '
                                            NodoAuxiliar = NodoAuxiliar.siguiente
                                        else:
                                            filatablero = filatablero +  NodoAuxiliar.dato.colorA +' | '
                                            NodoAuxiliar = NodoAuxiliar.siguiente
                                    elif columnaactual ==1:
                                        filatablero = '|   | '
                                    elif columnaactual < Menu.AnchoTablero:
                                        filatablero = filatablero + '  | '
                                    elif columnaactual == Menu.AnchoTablero:
                                        filatablero =filatablero + '  |'


                                elif columnaactual == 1:
                                    filatablero = '|   | '
                                elif columnaactual < Menu.AnchoTablero:
                                    filatablero = filatablero + '  | '
                                elif columnaactual == Menu.AnchoTablero:
                                    filatablero =filatablero + '  |'
                                
                            
                            if filaactual == Menu.AnchoTablero and columnaactual == Menu.AlturaTablero:

                                if NodoAuxiliar !=None:
                                    if NodoAuxiliar.dato.fila == filaactual and NodoAuxiliar.dato.columna == columnaactual:
                                        filatablero = filatablero + ' |' + NodoAuxiliar.dato.colorA +' |'
                                        NodoAuxiliar = NodoAuxiliar.siguiente
                                
                            print(filatablero)

                            filatablero = ''
                            

                            if   filaactual == Menu.AlturaTablero and columnaactual == Menu.AnchoTablero:
                                CondicionImpresion = False

                            filaactual = filaactual + 1

                        print("------------------------------------------------------------")
                        print("")
                        print('Desea agregar mas piezas?. S/N')
                        decision = str(input())
                        if(decision == 'S'):
                            CondicionPieza = True
                            
                        elif(decision == 'N'):
                            CondicionPieza = False

                            print('')
                            print("------------------------------------------------------------")
                            print('')
                            print('Generando Grafica: ')
                            Menu.graficarMuestra(Menu.ListaPieza.cabeza)

                if SeleccionMenu == 3:
                    print('')
                    print("------------------------------------------------------------")
                    print('Nombre Estudiante: Andy Jeferson Salas Ramirez')
                    print('Carnet: 201403544')
                    print('Curso: Iroduccion a la Programacion y Computacion 2 Seccion A')
                    print("------------------------------------------------------------")
                    print('')
                    
                if SeleccionMenu == 4:
                    sys.exit()

    def ordenarListaElementos(cabeza):
        nodolista           = ListaSimple.Nodo(None)
        nodolista.siguiente = cabeza
        
        FilaActual    = 0
        FilaSiguiente = 0
        ColumnaActual  = 0
        ColumnaSiguiente = 0
        ExisteOrden     = True

        while ExisteOrden:
            ExisteOrden  = False
            nodotemporal = nodolista
            
            while nodotemporal.siguiente and nodotemporal.siguiente.siguiente:

                primero = nodotemporal.siguiente
                segundo = primero.siguiente

                FilaActual    = int(primero.dato.fila)
                FilaSiguiente = int(segundo.dato.fila)
                
                if FilaActual > FilaSiguiente:
                    nodotemporal.siguiente = segundo
                    primero.siguiente      = segundo.siguiente
                    segundo.siguiente      = primero
                    ExisteOrden = True 
                nodotemporal = nodotemporal.siguiente
            
        cabeza = nodolista.siguiente

        nodolista           = ListaSimple.Nodo(None)
        nodolista.siguiente = cabeza
        ExisteOrden     = True

        while ExisteOrden:
            ExisteOrden  = False
            nodotemporal = nodolista
            
            while nodotemporal.siguiente and nodotemporal.siguiente.siguiente:

                primero = nodotemporal.siguiente
                segundo = primero.siguiente

                FilaActual    = int(primero.dato.fila)
                FilaSiguiente = int(segundo.dato.fila)
                ColumnaActual  = int(primero.dato.columna)
                ColumnaSiguiente  = int(segundo.dato.columna)
                
                if FilaActual == FilaSiguiente and ColumnaActual > ColumnaSiguiente:
                    nodotemporal.siguiente = segundo
                    primero.siguiente      = segundo.siguiente
                    segundo.siguiente      = primero
                    ExisteOrden = True 
                nodotemporal = nodotemporal.siguiente
            
        cabeza = nodolista.siguiente

        return cabeza
    

    def graficarMuestra(cabezadelista):

            x          = Menu.AnchoTablero
            y          = Menu.AlturaTablero
            NodoActual = cabezadelista
            nodotemporal  = ListaSimple.Nodo(None)

            
            f = graphviz.Digraph('prueba', filename='prueba.gv')

            f.attr('node', shape= 'circle', size= '1', style = 'filled')

            f.node('titulo', 'Coloréalo', fillcolor = 'white')

            fila = 0

            for n in range(x+1):
                ModuloActual = 'ND'+str(fila) +str(n)
                f.node(ModuloActual, str(n), fillcolor = 'white')
                f.edge('titulo', ModuloActual)

            ModuloAnterior = 'ND00'
            columna = 0
            for n in range(1, y+1):
                ModuloActual = 'ND'+str(n) +str(columna)
                f.node(ModuloActual, str(n), fillcolor = 'white')
                f.edge(ModuloAnterior, ModuloActual)
                ModuloAnterior = ModuloActual
                

            for filaactual in range(y):
                columnaactual = 1
                ModuloAnterior = 'ND' + str(filaactual)+str(columnaactual)
                
                filaactual = filaactual +1

                for columnaactual in range (1, x+1):
                    ModuloActual = 'ND' +str(filaactual)+ str(columnaactual)

                    if NodoActual !=None:

                        if NodoActual.dato.fila == filaactual and NodoActual.dato.columna == columnaactual:
                            color = ''
                            if NodoActual.dato.colorA =='A':
                                color = 'steelblue1'
                            elif NodoActual.dato.colorA =='R':
                                color = 'red'
                            elif NodoActual.dato.colorA =='V':
                                color = 'limegreen'
                            elif NodoActual.dato.colorA =='P':
                                color = 'darkorchid3'
                            elif NodoActual.dato.colorA =='N':
                                color = 'orange'

                            f.node(ModuloActual, str(NodoActual.dato.colorA), fillcolor = color)
                            ModuloAnterior = 'ND'+ str(filaactual-1) + str(columnaactual)
                            f.edge(ModuloAnterior, ModuloActual)
                            NodoActual = NodoActual.siguiente
                        else:
                            f.node(ModuloActual, '', fillcolor = 'white')
                            ModuloAnterior = 'ND'+ str(filaactual-1) +str(columnaactual)
                            f.edge(ModuloAnterior, ModuloActual)

                    else:
                        f.node(ModuloActual, '', fillcolor = 'white')
                        ModuloAnterior = 'ND'+ str(filaactual-1) +str(columnaactual)
                        f.edge(ModuloAnterior, ModuloActual)
                            





           
            f.render('./renders/prueba.gv', view=True)
        