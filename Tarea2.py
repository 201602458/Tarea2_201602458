class NodoD :
    def __init__(self, dato):
        self.siguiente=None
        self.anterior=None
        self.dato=dato

class ListaDobleC:
    def __init__(self):
        self.primero=None
        self.ultimo=None
        
        
    def Insertar(self,valor):
        nuevo=NodoD(valor)
        if(self.primero==None):
            self.primero=nuevo
            self.ultimo=nuevo
        else:
           self.ultimo.anterior=nuevo
           nuevo.siguiente=self.ultimo 
           self.ultimo=nuevo
           self.ultimo.anterior=self.primero
           self.primero.siguiente=self.ultimo

    def Mostrar(self):
        temporal=self.primero
        while(temporal != self.ultimo):
            print(temporal.dato)

            temporal=temporal.anterior
        print(self.ultimo.dato)
        

    def Buscar(self, numero):
        temporal=self.primero
        while(temporal != self.ultimo):
            if(str(numero)==str(temporal.dato)):

                print(" Anterior: "+ str(temporal.siguiente.dato) + " - Actual: "+ str(temporal.dato)+ " - Siguiente: "+ str(temporal.anterior.dato))

            temporal=temporal.anterior

        if(str(numero)==str(self.ultimo.dato)):

                print(" Anterior: "+ str(self.ultimo.siguiente.dato) + " - Actual: "+ str(self.ultimo.dato)+ " - Siguiente: "+ str(self.ultimo.anterior.dato))

        

 
class index:

    def __init__ (self):
            self.opcion="opcion"
           

def main():
    var=ListaDobleC()
    while True:
        op=input("Ingrese un numero (Ingrese F para finalizar la lista): ")

        if op == 'F':   #carritos son pilas            
            var.Mostrar()
            num=input("Ingrese un numero a buscar: ")
            var.Buscar(num)
            break
        else:
            var.Insertar(op)
            




if __name__ == "__main__":
    main()
           

    