class pieza:
    
    fila:int
    columna:int
    color:str
    colorA:str

    def __init__(self,fila,columna,color,colorA) -> None:
        self.fila    = fila
        self.columna = columna
        self.color   = color
        self.colorA = colorA