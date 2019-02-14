#Punto que tiene una coordenada x, e y. Además puedo moverlo arriba (y+1) y abajo (y-1).
#El vector es como un punto pero además tiene longitud.
#crea un punto
#crea un vector
#calcula la longitud del vector
#mueve arriba el vector y abajo
#calcula la longitud del vector
punto_X = input('Introduce un punto X:')
punto_Y = input('Introduce un punto Y:')
punto_X2 = input('Introduce un punto X:')
punto_Y2 = input('Introduce un punto Y:')
Puntos = [punto_X,punto_Y]
Puntos_2 = [punto_X2,punto_Y2]
class Punto():
    def __init__(self):
        self.punto_x = Puntos[0]
        self.punto_y = Puntos[1]
    def get_punto_x(self):
        return self.punto_x
    def get_punto_y(self):
        return self.punto_y
punto = Punto()
print('\n','La coordenada X1 es:',punto.get_punto_x(),'\n','La coordenada Y1 es:',punto.get_punto_y())

class Vector(Punto):
    def __init__(self):
        self.punto_x = Puntos[0]
        self.punto_y = Puntos[1]
        self.punto_x2 = Puntos_2[0]
        self.punto_y2 = Puntos_2[1]
    def get_punto_x2(self):
        return self.punto_x2
    def get_punto_y2(self):
        return self.punto_y2
vector = Vector()
print('\n','La coordenada X2 es:',vector.get_punto_x2(),'\n','La coordenada Y2 es:',vector.get_punto_y2())

x1 = vector.punto_x
y1 = vector.punto_y
x2 = vector.punto_x2
y2 = vector.punto_y2
solucion_vector_x = (int(x2)-int(x1))
solucion_vector_y = (int(y2)-int(y1))
print('\n','El vector formado por los puntos anteriores es:',solucion_vector_x,solucion_vector_y)
vector_x_y = [solucion_vector_x,solucion_vector_y]

class Modulo(Vector):
    def __init__(self):
        self.component_x = vector_x_y[0]
        self.component_y = vector_x_y[1]
    def get_component_x(self):
        return self.component_x
    def get_component_y(self):
        return self.component_y
modulo = Modulo()
solucion_modulo = ( (modulo.get_component_x())**2  +  (modulo.get_component_y())**2 ) ** (1/2)
print('Su módulo es:',solucion_modulo)

class Up(Vector):
    def __init__(self):

        self.punto_y_new = Puntos[1] + 1

    def get_punto_y_new(self):
        return self.punto_y_new
#ACABAR EN CASA  
