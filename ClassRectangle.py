#Importar matplotlib
import matplotlib.pyplot as plt

#Crear la clase Rectangle
class Rectangle(object):

    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height
        self.width = width
        self.color = color

    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()

#Crear un objeto de la clase Rectangle
FatYellowRectangle = Rectangle(20, 5, 'yellow')

#Dibujar el objeto creado
FatYellowRectangle.drawRectangle()
