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
                print("3. Salir.\n")
                print("-------------------------Guatematel-------------------------")
                SeleccionMenu = int(input())

                if SeleccionMenu ==1:
                    print('')
                    print("------------------------------------------------------------")
                    print('')
                    print("Por favor ingrese el ancho del tablero. ")
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
                        print("Rango: 1 - " + str(Menu.AnchoTablero))
                        FilaPieza = int(input())
                        print('')
                        print("------------------------------------------------------------")
                        print('')
                        print("Por favor ingrese la columna en la que desea colocar la pieza. ")
                        print("Rango: 1 - " + str(Menu.AlturaTablero))
                        ColumnaPieza = int(input())
                        print('')
                        print("------------------------------------------------------------")
                        print('')
                        print('Pieza Color: ' + ColorPieza + ', Fila: ' +str(FilaPieza) +', Columna: ' +str(ColumnaPieza))
                        
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
                        print('')
                        print('Pieza agregada Exitosamente.')
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
                            for columnaactual in range(1, Menu.AlturaTablero + 1):
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
                                    elif columnaactual < Menu.AlturaTablero:
                                        filatablero = filatablero + '  | '
                                    elif columnaactual == Menu.AlturaTablero:
                                        filatablero =filatablero + '  |'


                                elif columnaactual == 1:
                                    filatablero = '|   | '
                                elif columnaactual < Menu.AlturaTablero:
                                    filatablero = filatablero + '  | '
                                elif columnaactual == Menu.AlturaTablero:
                                    filatablero =filatablero + '  |'
                                
                            
                            if filaactual == Menu.AnchoTablero and columnaactual == Menu.AlturaTablero:

                                if NodoAuxiliar !=None:
                                    if NodoAuxiliar.dato.fila == filaactual and NodoAuxiliar.dato.columna == columnaactual:
                                        filatablero = filatablero + ' |' + NodoAuxiliar.dato.colorA +' |'
                                        NodoAuxiliar = NodoAuxiliar.siguiente
                                
                            print(filatablero)

                            filatablero = ''
                            

                            if   filaactual == Menu.AnchoTablero and columnaactual == Menu.AlturaTablero:
                                CondicionImpresion = False

                            filaactual = filaactual + 1

                        print("------------------------------------------------------------")
                        print("")
                        print('Desea agregar mas piezas?. s/n')
                        decision = str(input())
                        if(decision == 'S'):
                            CondicionPieza = True
                            
                        elif(decision == 'N'):
                            CondicionPieza = False

                            print('')
                            print("------------------------------------------------------------")
                            print('')
                            print('Generando Grafica: ')

                if SeleccionMenu == 3:
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