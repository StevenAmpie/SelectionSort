
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QTransform, QPixmap, QPainter, QFont, QIcon
import sys


from ScreenMenu import ScreenMenu
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
        
        

        

                #VARIABLES 

        self.previousValue = self.ScreenMenu.spinBoxCantElementos.value() 

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
        
        self.listaCarros2=[
                         self.ScreenAnimation.car1, self.ScreenAnimation.car2, 
                         self.ScreenAnimation.car3, self.ScreenAnimation.car4, 
                         self.ScreenAnimation.car5, self.ScreenAnimation.car6,  
                         self.ScreenAnimation.car7, self.ScreenAnimation.car8,
                         self.ScreenAnimation.car9, self.ScreenAnimation.car10]
        

        self.minIndex = 0

        self.indicesMinimos = []

        self.arrayAux = []

        self.carrosPrueba = []


        self.listaParqueos=[self.ScreenAnimation.parqueo1, self.ScreenAnimation.parqueo2, self.ScreenAnimation.parqueo3,
                          self.ScreenAnimation.parqueo4, self.ScreenAnimation.parqueo5, self.ScreenAnimation.parqueo6,
                          self.ScreenAnimation.parqueo7, self.ScreenAnimation.parqueo8, self.ScreenAnimation.parqueo9,
                          self.ScreenAnimation.parqueo10
                         ]
        
        self.array=[]

        self.flag = 0


       
       

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
        
        

            
        

    #Metodos
        
    def selectionSort(self):
            
            self.arrayAux.sort()


            if(self.array != self.arrayAux):
                 
                   

            
                for i in range(len(self.array)):

                    self.minIndex = i

                    # Encontrar el índice del mínimo
                    for j in range(i + 1, len(self.array)):
                        if self.array[j] < self.array[self.minIndex]:
                            self.minIndex = j
                            
                        
                    if self.array != self.arrayAux:
                        self.indicesMinimos+=[self.minIndex]
                    

                    #if(len(self.indicesMinimos) == 0):
                        
                     #   self.indicesMinimos = [len(self.array)-1 for i in range(len(self.array))]  
                        
                        
                    # Intercambiar elementos en la lista de números

                    self.array[i], self.array[self.minIndex] = self.array[self.minIndex], self.array[i]
                    
        
                    # Intercambiar widgets de la lista de carros
                    self.listaCarros[i], self.listaCarros[self.minIndex] = self.listaCarros[self.minIndex], self.listaCarros[i]
            
            
            else:
                 self.indicesMinimos = [i for i in range(len(self.array))]
             
                
            QTimer.singleShot(1000, self.mostrarAnimacion) #dispara la animacion 1 segundo despues de ordenar el codigo


    def mostrarAnimacion(self):

        timeDelay = 10000
       
        
        
        if(self.flag < self.ScreenMenu.spinBoxCantElementos.value()):

        

            QTimer.singleShot(1000, lambda: self.run(self.listaCarros[self.flag], self.flag))
            


            if (self.flag<len(self.indicesMinimos)):


                if(self.listaCarros2[self.flag].x()==self.listaParqueos[self.indicesMinimos[self.flag]].x()):
                     timeDelay = 3000
                else:
                     QTimer.singleShot(6000, lambda: self.run2(self.listaCarros2[self.flag], self.indicesMinimos[self.flag]))



            QTimer.singleShot(timeDelay, lambda: self.delay())
            
            
        
        else:

            pass
            

    def delay(self):

        try:
            self.listaCarros2[self.flag], self.listaCarros2[self.indicesMinimos[self.flag]] = self.listaCarros2[self.indicesMinimos[self.flag]], self.listaCarros2[self.flag]
        except IndexError:
             pass
        
        QTimer.singleShot(1000, lambda: self.sumarFlag())

        QTimer.singleShot(2000, lambda: self.mostrarAnimacion())
        
         
    def sumarFlag(self):
         self.flag+=1
        

    def cantNums(self, value):
        #metodo para reducir o aumentar la cantidad de entradas  
        if value > self.previousValue:  
                      
                self.listaNums[value-1].setVisible(True)

        elif value < self.previousValue:
                self.listaNums[self.previousValue-1].setVisible(False)

        # Actualizar el valor anterior
        self.previousValue = value


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
            self.arrayAux += [self.listaNums[i].value()]

            

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
    

    #NO UTILIZADA TODAVIA, PENDIENTE PARA FUTURAS UPDATES
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
        font = QFont("MS Shell Dlg 2", 52, QFont.Bold)
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
         
         if(car.x()>listaPosiciones[posicionParqueo].x()):
              
              
              
              self.moverCarro(car, posicionParqueo, 270, 90)

         elif(car.x()<listaPosiciones[posicionParqueo].x()):
              
              
              
              
            self.moverCarro(car, posicionParqueo, 90, 270)


         elif(car.x()==listaPosiciones[posicionParqueo].x()):



            
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


    def intercambiarCarro(self, car, posicionParqueo, grado1, grado2):

        listaParqueos=[self.ScreenAnimation.parqueo1, self.ScreenAnimation.parqueo2, self.ScreenAnimation.parqueo3,
                          self.ScreenAnimation.parqueo4, self.ScreenAnimation.parqueo5, self.ScreenAnimation.parqueo6,
                          self.ScreenAnimation.parqueo7, self.ScreenAnimation.parqueo8, self.ScreenAnimation.parqueo9,
                          self.ScreenAnimation.parqueo10
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
                listaParqueos[posicionParqueo].x(),y+150,0,0)) # y simula basicamente steps
        
        self.delayFunciones(self.rotarCarro, argFuncion1=grado2, 
                            argFuncion2=car,time=3800)


    

        self.motion.setKeyValueAt(1, QtCore.QRect(listaParqueos[posicionParqueo].x(), y, 0,0))
        

        
        self.motion.start()
    

    def run2(self, car, posicionParqueo):
         
     
         
         self.listaParqueos=[self.ScreenAnimation.parqueo1, self.ScreenAnimation.parqueo2, self.ScreenAnimation.parqueo3,
                          self.ScreenAnimation.parqueo4, self.ScreenAnimation.parqueo5, self.ScreenAnimation.parqueo6,
                          self.ScreenAnimation.parqueo7, self.ScreenAnimation.parqueo8, self.ScreenAnimation.parqueo9,
                          self.ScreenAnimation.parqueo10
                         ]

         
         
         if(car.x()>self.listaParqueos[posicionParqueo].x()):
              
              
              
              self.intercambiarCarro(car, posicionParqueo, 270, 90)

         elif(car.x()<self.listaParqueos[posicionParqueo].x()):
              

              

              
              
              self.intercambiarCarro(car, posicionParqueo, 90, 270)

    
    

    #Main
if __name__ == "__main__":

    appSwitch = QtWidgets.QApplication(sys.argv)
    windowStart = App()
    #windowStart.setWindowIcon(QIcon("InfoImages/LogoApp.ico"))
    windowStart.show()
    sys.exit(appSwitch.exec_())