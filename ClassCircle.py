#Importar matplotlib
import matplotlib.pyplot as plt

#Crear la clase Circle
class Circle(object):

    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)

    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

#Crear un objeto de la clase Circle
RedCircle = Circle(10, 'red')

#Dibujar el objeto creado
RedCircle.drawCircle()
