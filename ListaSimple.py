class Lista_simple(): 
    def __init__(self):
        self.cabeza = None
    
    # Método para agregar elementos en el frente de la linked list
    def agregar_al_inicio(self, dato):
        self.cabeza = Nodo(dato=dato, siguiente=self.cabeza)

    def agregar_al_final(self, dato):
        if self.cabeza == None:
            self.cabeza = Nodo(dato=dato, siguiente=self.cabeza)
        else:
            actual = self.cabeza

            while actual.siguiente != None:
                actual = actual.siguiente
            
            actual.siguiente = Nodo(dato=dato, siguiente=None)



class Nodo():
    
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente


    