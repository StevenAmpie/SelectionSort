
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QTransform, QPixmap, QPainter, QFont 
import sys
from  ScreenMenu import ScreenMenu
from ScreenAnimation import ScreenAnimation
from presentacion import ScreenPresentacion
from IntroAlgoritmo import IntroAlgoritmo




#clase logica de los carros:

class App(QtWidgets.QMainWindow):

    #Constructor
    def __init__(self):
        super().__init__()

        #Objetos de Interfaz:

        
        self.ScreenPresentacion = ScreenPresentacion()
        self.ScreenIntro = IntroAlgoritmo()
        self.ScreenMenu = ScreenMenu()
        self.ScreenAnimation = ScreenAnimation()
       
        

        
        
        #self.ScreenMenu.setupUi(self)
        self.objectAnimationScreen = QtWidgets.QMainWindow()
        self.objectMenuScreen = QtWidgets.QMainWindow()
        self.objectIntroScreen = QtWidgets.QMainWindow()

        
        
         

         #Setups
        self.ScreenIntro.setupUi(self.objectIntroScreen)
        self.ScreenMenu.setupUi(self.objectMenuScreen)
        self.ScreenAnimation.setupUi(self.objectAnimationScreen)
        self.ScreenPresentacion.setupUi(self)
        
        

        

                #VARIABLES DEL METODO: cantBarcos()

        self.previous_value = self.ScreenMenu.spinBoxCantElementos.value() 

        self.listaNums=[self.ScreenMenu.spinBox1, self.ScreenMenu.spinBox2,
                        self.ScreenMenu.spinBox3, self.ScreenMenu.spinBox4,
                        self.ScreenMenu.spinBox5,self.ScreenMenu.spinBox6,
                        self.ScreenMenu.spinBox7, self.ScreenMenu.spinBox8, 
                        self.ScreenMenu.spinBox9, self.ScreenMenu.spinBox10]


        self.listaCarros=[
                         self.ScreenAnimation.car1, self.ScreenAnimation.car2, 
                         self.ScreenAnimation.car3, self.ScreenAnimation.car4, 
                         self.ScreenAnimation.car5, self.ScreenAnimation.car6,  
                         self.ScreenAnimation.car7, self.ScreenAnimation.car8,
                         self.ScreenAnimation.car9, self.ScreenAnimation.car10]
        


        self.carros=["car1","car2", "car3", "car4",
                     "car5", "car6", "car7", "car8"]
        
        self.array=[]
       
       

    #LOGICA DE EVENTOS:

            #Deshabilitar la linea de edicion del spinBox
       
        self.ScreenMenu.spinBoxCantElementos.lineEdit().setDisabled(True) 

         #Volver invisibles las entradas, al principio de la ejecucion
        
        self.ScreenAnimation.ButtonIniciarSortFin.setVisible(False)

        for i in range(8,10):
             self.listaNums[i].setVisible(False)

        #Evento de cambio en el spinBox
        self.ScreenMenu.spinBoxCantElementos.valueChanged.connect(self.cantNums)


        #Eventos de cambio de pantalla
        self.ScreenMenu.ordenarButton.clicked.connect(self.changeScreenAnimation)
        self.ScreenPresentacion.pushButton.clicked.connect(self.changeScreenPresentacion)
        self.ScreenIntro.pushButton.clicked.connect(self.changeScreenMenu)
        self.ScreenAnimation.ButtonIniciarSort.clicked.connect(self.changeBotonIniciar)
        self.ScreenAnimation.ButtonIniciarSort.clicked.connect(self.selectionSort)

        self.flag = 0
        
        
        

        

    #Metodos
        
    def selectionSort(self):
            
            for i in range(len(self.array)):

                min_index = i

                # Encontrar el índice del mínimo
                for j in range(i + 1, len(self.array)):
                    if self.array[j] <= self.array[min_index]:
                        min_index = j

                # Intercambiar elementos en la lista de números
                self.array[i], self.array[min_index] = self.array[min_index], self.array[i]

    
                # Intercambiar en la self.lista2 de carros
                self.listaCarros[i], self.listaCarros[min_index] = self.listaCarros[min_index], self.listaCarros[i]

            
            print(self.array)
            QTimer.singleShot(1000, self.mostrarAnimacion)

    def mostrarAnimacion(self):

        
        print(self.flag)
         
        if(self.flag < self.ScreenMenu.spinBoxCantElementos.value()):

            
            print(self.flag)

            print(self.listaCarros[self.flag].objectName())

            QTimer.singleShot(1000, lambda: self.run(self.listaCarros[self.flag], self.flag))
            print(f'El carro {self.listaCarros[self.flag].objectName()} va en el parqueo {self.flag}')

            QTimer.singleShot(3000, lambda: self.delay())
            
            
        
        else:
            
            pass
    
    def delay(self):
        QTimer.singleShot(300, lambda: self.sumarFlag())
        QTimer.singleShot(2000, lambda: self.mostrarAnimacion())
         

    def sumarFlag(self):
         self.flag+=1
        

    def cantNums(self, value):
        #metodo para reducir o aumentar la cantidad de entradas  
        if value > self.previous_value:  
                      
                self.listaNums[value-1].setVisible(True)

        elif value < self.previous_value:
                self.listaNums[self.previous_value-1].setVisible(False)

        # Actualizar el valor anterior
        self.previous_value = value


    
    def changeScreenAnimation(self):
         
        if(self.ScreenMenu.spinBoxCantElementos.value() == 8):
              self.ScreenAnimation.car9.setVisible(False)
              self.ScreenAnimation.car10.setVisible(False)
         
        elif(self.ScreenMenu.spinBoxCantElementos.value() == 9):
              self.ScreenAnimation.car10.setVisible(False)
         
        for i in range(self.ScreenMenu.spinBoxCantElementos.value()):
              self.addNumberTopToLabel(str(self.listaNums[i].value()), self.listaCarros[i])
        
        for i in range(self.ScreenMenu.spinBoxCantElementos.value()):

            self.array += [self.listaNums[i].value()]
        

         


        self.objectMenuScreen.hide()
        self.objectAnimationScreen.show()
         

    def changeScreenMenu(self):
         
         self.objectIntroScreen.hide()
         self.objectMenuScreen.show()

    def changeScreenPresentacion(self):
         
         
         self.hide()
         self.objectIntroScreen.show()

    def changeBotonIniciar(self):
         
        self.ScreenAnimation.ButtonIniciarSort.setVisible(False)
        self.ScreenAnimation.ButtonIniciarSortFin.setVisible(True)

        #Funcion para controlar el tiempo entre evento de la subclase QtCore.Qtimer
        QtCore.QTimer.singleShot(5000, self.changeBotonFinal)
     
    
    def changeBotonFinal(self):
         
        self.ScreenAnimation.ButtonIniciarSortFin.setVisible(False)
        self.ScreenAnimation.ButtonIniciarSort.setVisible(True)
    
    def rotarCarro(self, grados, car):

        
        current_pixmap = car.pixmap()    
        transform = QTransform().rotate(grados)
        rotated_pixmap = current_pixmap.transformed(transform, mode=Qt.SmoothTransformation)
        car.setPixmap(rotated_pixmap)


    def addNumberTopToLabel(self, num, label):

        current_pixmap = label.pixmap()   
        # Crear un nuevo QPixmap para editarlo
        new_pixmap = QPixmap(current_pixmap)
        painter = QPainter(new_pixmap)

        # Configurar fuente y color del texto
        font = QFont("MS Shell Dlg 2", 64, QFont.Bold)
        painter.setFont(font)
        painter.setPen(Qt.black)  # Cambiar color del texto si es necesario

        # Dibujar el texto encima del pixmap
        text_rect = new_pixmap.rect()
        painter.drawText(text_rect, Qt.AlignCenter, num)

        painter.end()  # Terminar la pintura

        # Asignar el pixmap modificado al QLabel
        label.setPixmap(new_pixmap)
    

    def delayFunciones(self, funcionName, argFuncion1, argFuncion2, time):
         

         self.timer = QTimer(self) #Crea un objeto de la clase Qtimer
         self.timer.setSingleShot(True)  # Solo ejecutar una vez
         self.timer.timeout.connect(lambda: funcionName(argFuncion1, argFuncion2)) #pasa en un lambda la funcion con su argumento
         self.timer.start(time)  #inicia el temporizador con el tiempo ingresado en la funcion 


    def run(self, car, posicionParqueo):
         
         listaPosiciones=[self.ScreenAnimation.posicion1, self.ScreenAnimation.posicion2, self.ScreenAnimation.posicion3,
                          self.ScreenAnimation.posicion4, self.ScreenAnimation.posicion5, self.ScreenAnimation.posicion6,
                          self.ScreenAnimation.posicion7, self.ScreenAnimation.posicion8, self.ScreenAnimation.posicion9,
                          self.ScreenAnimation.posicion10
                         ]

         
         print(f'{posicionParqueo}')
         
         
         if(car.x()>listaPosiciones[posicionParqueo].x()):
              print(listaPosiciones[posicionParqueo].objectName())
              print(f'{car.objectName()} != {listaPosiciones[posicionParqueo].objectName()}')
              print(f'{car.x()}>{listaPosiciones[posicionParqueo].x()} and  {car.y()} > {listaPosiciones[posicionParqueo].y()} and {posicionParqueo}')
              print("se fue a la izquierda")
              
              self.moverCarro(car, posicionParqueo, 270, 90)

         elif(car.x()<listaPosiciones[posicionParqueo].x()):
              print(f'{car.x()}<{listaPosiciones[posicionParqueo].x()}')
              
              print("se fue a la derecha")
              self.moverCarro(car, posicionParqueo, 90, 270)

         elif(car.x()==listaPosiciones[posicionParqueo].x()):


            print(f"solo retrocedio, porque {car.x()} == {listaPosiciones[posicionParqueo].x()}")
            x=car.x()
            y=car.y()
        
            self.motion = QtCore.QPropertyAnimation(car, b"geometry")
            self.motion.setDuration(2000)  
            # el primer parametro, va de 0 a 1
            self.motion.setKeyValueAt(0, QtCore.QRect(x,y,0,0))
            self.motion.setKeyValueAt(0.5, QtCore.QRect(x,y+150,0,0))
            self.motion.setKeyValueAt(1, QtCore.QRect(listaPosiciones[posicionParqueo].x(),y+300,0,0))
            

            self.motion.start()
        

    def moverCarro(self, car, posicionParqueo, grado1, grado2):

        listaPosiciones=[self.ScreenAnimation.posicion1, self.ScreenAnimation.posicion2, self.ScreenAnimation.posicion3,
                          self.ScreenAnimation.posicion4, self.ScreenAnimation.posicion5, self.ScreenAnimation.posicion6,
                          self.ScreenAnimation.posicion7, self.ScreenAnimation.posicion8, self.ScreenAnimation.posicion9,
                          self.ScreenAnimation.posicion10
                         ]
         
        

        x=car.x()
        y=car.y()
    
        self.motion = QtCore.QPropertyAnimation(car, b"geometry")
        
        self.motion.setDuration(5000)  # Duración en milisegundos, en este caso, 5 segundos
        # el primer parametro, va de 0 a 1
        self.motion.setKeyValueAt(0, QtCore.QRect(x,y,0,0))
        self.motion.setKeyValueAt(0.5, QtCore.QRect(x,y+150,0,0))

        self.delayFunciones(self.rotarCarro, argFuncion1=grado1, 
                            argFuncion2=car, time=2500)
        

        self.motion.setKeyValueAt(0.75, QtCore.QRect(
                listaPosiciones[posicionParqueo].x(),y+150,0,0)) # y simula basicamente steps
        
        self.delayFunciones(self.rotarCarro, argFuncion1=grado2, 
                            argFuncion2=car,time=3800)


    

        self.motion.setKeyValueAt(1, QtCore.QRect(listaPosiciones[posicionParqueo].x(),y+300,0,0))
        

        
        self.motion.start()
        
    #Main
if __name__ == "__main__":

    appSwitch = QtWidgets.QApplication(sys.argv)
    window1 = App()
    window1.show()
    sys.exit(appSwitch.exec_())