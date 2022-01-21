#Termolector programado por Ricardo Catril Carrillo
#Github: ktrilu
#Email: catril.ricardo@gmail.com

import sys, glob, serial, configparser, os, threading, time, errno
from unittest.mock import DEFAULT
import tkinter as tk
from tkinter import Label, PhotoImage, StringVar, ttk
from tkcalendar import DateEntry
from datetime import datetime
from PIL import Image, ImageTk


class Paneles(tk.Toplevel):
    dispositivos = ['NO USAR','#01','#02','#03','#04','#05','#06','#07','#08','#09','#ah','#0B','#0C','#0D','#0E','#0F']
    
    def __init__(self):
        super().__init__()
        self.title("Paneles")
        self.geometry("830x400")
        self.config(background='RoyalBlue')
        self.fuente = 'Mukti Narrow'

        self.titulo_label = tk.Label(self, text="Configuracion de paneles\n ?Seleccione los paneles que utilizará para esta lectura",font=(self.fuente, 12))
        self.panel_label = tk.Label(self, text="Panel",font=(self.fuente, 12))
        self.dispositivo1_label = tk.Label(self, text="Dispositivo 1",font=(self.fuente, 12))
        self.dispositivo2_label = tk.Label(self, text="Dispositivo 2",font=(self.fuente, 12))
        self.dispositivo3_label = tk.Label(self, text="Dispositivo 3",font=(self.fuente, 12))
        
        self.panel1 = ttk.Combobox(self, values=['ACTIVADO', 'DESACTIVADO'], state="readonly", font=(self.fuente, 12))
        self.panel1_dispositivo1_combobox = ttk.Combobox(self, values=self.dispositivos, state="readonly", font=(self.fuente, 12))
        self.panel1_dispositivo2_combobox = ttk.Combobox(self, values=self.dispositivos, state="readonly", font=(self.fuente, 12))
        self.panel1_dispositivo3_combobox = ttk.Combobox(self, values=self.dispositivos, state="readonly", font=(self.fuente, 12))

        self.panel2 = ttk.Combobox(self, values=['ACTIVADO', 'DESACTIVADO'], state="readonly", font=(self.fuente, 12))
        self.panel2_dispositivo1_combobox = ttk.Combobox(self, values=self.dispositivos, state="readonly", font=(self.fuente, 12))
        self.panel2_dispositivo2_combobox = ttk.Combobox(self, values=self.dispositivos, state="readonly", font=(self.fuente, 12))
        self.panel2_dispositivo3_combobox = ttk.Combobox(self, values=self.dispositivos, state="readonly", font=(self.fuente, 12))
        
        self.panel3 = ttk.Combobox(self, values=['ACTIVADO', 'DESACTIVADO'], state="readonly", font=(self.fuente, 12))
        self.panel3_dispositivo1_combobox = ttk.Combobox(self, values=self.dispositivos, state="readonly", font=(self.fuente, 12))
        self.panel3_dispositivo2_combobox = ttk.Combobox(self, values=self.dispositivos, state="readonly", font=(self.fuente, 12))
        self.panel3_dispositivo3_combobox = ttk.Combobox(self, values=self.dispositivos, state="readonly", font=(self.fuente, 12))
        
        self.panel4 = ttk.Combobox(self, values=['ACTIVADO', 'DESACTIVADO'], state="readonly", font=(self.fuente, 12))
        self.panel4_dispositivo1_combobox = ttk.Combobox(self, values=self.dispositivos, state="readonly", font=(self.fuente, 12))
        self.panel4_dispositivo2_combobox = ttk.Combobox(self, values=self.dispositivos, state="readonly", font=(self.fuente, 12))
        self.panel4_dispositivo3_combobox = ttk.Combobox(self, values=self.dispositivos, state="readonly", font=(self.fuente, 12))
        
        self.panel5 = ttk.Combobox(self, values=['ACTIVADO', 'DESACTIVADO'], state="readonly", font=(self.fuente, 12))
        self.panel5_dispositivo1_combobox = ttk.Combobox(self, values=self.dispositivos, state="readonly", font=(self.fuente, 12))
        self.panel5_dispositivo2_combobox = ttk.Combobox(self, values=self.dispositivos, state="readonly", font=(self.fuente, 12))
        self.panel5_dispositivo3_combobox = ttk.Combobox(self, values=self.dispositivos, state="readonly", font=(self.fuente, 12))
        
        self.panel6 = ttk.Combobox(self, values=['ACTIVADO', 'DESACTIVADO'], state="readonly", font=(self.fuente, 12))
        self.panel6_dispositivo1_combobox = ttk.Combobox(self, values=self.dispositivos, state="readonly", font=(self.fuente, 12))
        self.panel6_dispositivo2_combobox = ttk.Combobox(self, values=self.dispositivos, state="readonly", font=(self.fuente, 12))
        self.panel6_dispositivo3_combobox = ttk.Combobox(self, values=self.dispositivos, state="readonly", font=(self.fuente, 12))

        self.guardar_paneles_button = ttk.Button(self, text="Guardar paneles", width=20, command=self.guardar_paneles)

        self.titulo_label.grid(row=0, sticky='ew', columnspan=5)
        self.panel_label.grid(row=1, sticky='ew', padx=5, pady=5)
        self.dispositivo1_label.grid(row=1, column=1, sticky='ew', padx=5, pady=5)
        self.dispositivo2_label.grid(row=1, column=2, sticky='ew', padx=5, pady=5)
        self.dispositivo3_label.grid(row=1, column=3, sticky='ew', padx=5, pady=5)

        self.panel1.grid(row=2, padx=5, pady=5)
        self.panel1_dispositivo1_combobox.grid(row=2, column=1, padx=5, pady=5)
        self.panel1_dispositivo2_combobox.grid(row=2, column=2, padx=5, pady=5)
        self.panel1_dispositivo3_combobox.grid(row=2, column=3, padx=5, pady=5)
        
        self.panel2.grid(row=3, padx=5, pady=5)
        self.panel2_dispositivo1_combobox.grid(row=3, column=1, padx=5, pady=5)
        self.panel2_dispositivo2_combobox.grid(row=3, column=2, padx=5, pady=5)
        self.panel2_dispositivo3_combobox.grid(row=3, column=3, padx=5, pady=5)
        
        self.panel3.grid(row=4, padx=5, pady=5)
        self.panel3_dispositivo1_combobox.grid(row=4, column=1, padx=5, pady=5)
        self.panel3_dispositivo2_combobox.grid(row=4, column=2, padx=5, pady=5)
        self.panel3_dispositivo3_combobox.grid(row=4, column=3, padx=5, pady=5)

        self.panel4.grid(row=5, padx=5, pady=5)
        self.panel4_dispositivo1_combobox.grid(row=5, column=1, padx=5, pady=5)
        self.panel4_dispositivo2_combobox.grid(row=5, column=2, padx=5, pady=5)
        self.panel4_dispositivo3_combobox.grid(row=5, column=3, padx=5, pady=5)

        self.panel5.grid(row=6, padx=5, pady=5)
        self.panel5_dispositivo1_combobox.grid(row=6, column=1, padx=5, pady=5)
        self.panel5_dispositivo2_combobox.grid(row=6, column=2, padx=5, pady=5)
        self.panel5_dispositivo3_combobox.grid(row=6, column=3, padx=5, pady=5)

        self.panel6.grid(row=7, padx=5, pady=5)
        self.panel6_dispositivo1_combobox.grid(row=7, column=1, padx=5, pady=5)
        self.panel6_dispositivo2_combobox.grid(row=7, column=2, padx=5, pady=5)
        self.panel6_dispositivo3_combobox.grid(row=7, column=3, padx=5, pady=5)


        self.guardar_paneles_button.grid(row=8, columnspan=4, pady=10)

        self.set_combobox()

    def set_combobox(self):
        self.paneles = configparser.ConfigParser()
        self.paneles.read('paneles.config')
        #PANEL1
        self.panel1.set(self.paneles['PANEL1']['activo'])

        self.panel1_dispositivo1_combobox.set(self.paneles['PANEL1']['dispositivo1'])
        self.panel1_dispositivo2_combobox.set(self.paneles['PANEL1']['dispositivo2'])
        self.panel1_dispositivo3_combobox.set(self.paneles['PANEL1']['dispositivo3'])

        #PANEL2
        self.panel2.set(self.paneles['PANEL2']['activo'])

        self.panel2_dispositivo1_combobox.set(self.paneles['PANEL2']['dispositivo1'])
        self.panel2_dispositivo2_combobox.set(self.paneles['PANEL2']['dispositivo2'])
        self.panel2_dispositivo3_combobox.set(self.paneles['PANEL2']['dispositivo3'])

        #PANEL3
        self.panel3.set(self.paneles['PANEL3']['activo'])

        self.panel3_dispositivo1_combobox.set(self.paneles['PANEL3']['dispositivo1'])
        self.panel3_dispositivo2_combobox.set(self.paneles['PANEL3']['dispositivo2'])
        self.panel3_dispositivo3_combobox.set(self.paneles['PANEL3']['dispositivo3'])
        
        #PANEL4
        self.panel4.set(self.paneles['PANEL4']['activo'])

        self.panel4_dispositivo1_combobox.set(self.paneles['PANEL4']['dispositivo1'])
        self.panel4_dispositivo2_combobox.set(self.paneles['PANEL4']['dispositivo2'])
        self.panel4_dispositivo3_combobox.set(self.paneles['PANEL4']['dispositivo3'])

        #PANEL5
        self.panel5.set(self.paneles['PANEL5']['activo'])

        self.panel5_dispositivo1_combobox.set(self.paneles['PANEL5']['dispositivo1'])
        self.panel5_dispositivo2_combobox.set(self.paneles['PANEL5']['dispositivo2'])
        self.panel5_dispositivo3_combobox.set(self.paneles['PANEL5']['dispositivo3'])

        #PANEL6
        self.panel6.set(self.paneles['PANEL6']['activo'])

        self.panel6_dispositivo1_combobox.set(self.paneles['PANEL6']['dispositivo1'])
        self.panel6_dispositivo2_combobox.set(self.paneles['PANEL6']['dispositivo2'])
        self.panel6_dispositivo3_combobox.set(self.paneles['PANEL6']['dispositivo3'])
        
    def guardar_paneles(self):
        #return
        #buscar combobox set
        #print(self.panel1_dispositivo1_combobox.get())
        #PANEL1
        self.paneles['PANEL1']['activo'] = self.panel1.get()

        self.paneles['PANEL1']['dispositivo1'] = self.panel1_dispositivo1_combobox.get()
        self.paneles['PANEL1']['dispositivo2'] = self.panel1_dispositivo2_combobox.get()
        self.paneles['PANEL1']['dispositivo3'] = self.panel1_dispositivo3_combobox.get()

        #PANEL2
        self.paneles['PANEL2']['activo'] = self.panel2.get()

        self.paneles['PANEL2']['dispositivo1'] = self.panel2_dispositivo1_combobox.get()
        self.paneles['PANEL2']['dispositivo2'] = self.panel2_dispositivo2_combobox.get()
        self.paneles['PANEL2']['dispositivo3'] = self.panel2_dispositivo3_combobox.get()

        #PANEL3
        self.paneles['PANEL3']['activo'] = self.panel3.get()

        self.paneles['PANEL3']['dispositivo1'] = self.panel3_dispositivo1_combobox.get()
        self.paneles['PANEL3']['dispositivo2'] = self.panel3_dispositivo2_combobox.get()
        self.paneles['PANEL3']['dispositivo3'] = self.panel3_dispositivo3_combobox.get()
        
        #PANEL4
        self.paneles['PANEL4']['activo'] = self.panel4.get()

        self.paneles['PANEL4']['dispositivo1'] = self.panel4_dispositivo1_combobox.get()
        self.paneles['PANEL4']['dispositivo2'] = self.panel4_dispositivo2_combobox.get()
        self.paneles['PANEL4']['dispositivo3'] = self.panel4_dispositivo3_combobox.get()

        #PANEL5
        self.paneles['PANEL5']['activo'] = self.panel5.get()

        self.paneles['PANEL5']['dispositivo1'] = self.panel5_dispositivo1_combobox.get()
        self.paneles['PANEL5']['dispositivo2'] = self.panel5_dispositivo2_combobox.get()
        self.paneles['PANEL5']['dispositivo3'] = self.panel5_dispositivo3_combobox.get()

        #PANEL6
        self.paneles['PANEL6']['activo'] = self.panel6.get()

        self.paneles['PANEL6']['dispositivo1'] = self.panel6_dispositivo1_combobox.get()
        self.paneles['PANEL6']['dispositivo2'] = self.panel6_dispositivo2_combobox.get()
        self.paneles['PANEL6']['dispositivo3'] = self.panel6_dispositivo3_combobox.get()

        #self.paneles['PANEL1']['dispositivo1']='ttttil'
        #self.paneles['PANEL1']['dispositivo2']='ttttil'
        paneles_guardar = open('paneles.config', 'w')
        self.paneles.write(paneles_guardar)

class Termolector(tk.Tk):
    hora_actual = datetime.now()
    
    

    def __init__(self):
        #################################
        #PARAMETROS DE INICIO Y GLOBALES#
        #################################
        super().__init__()
        self.color_primario = 'RoyalBlue'
        self.color_secundario = 'DarkGoldenrod'
        self.fuente = 'Mukti Narrow'
        self.title("Termolector")
        self.geometry('1280x720')
        self.config(background=self.color_primario)
        self.imagen = PhotoImage(file='logosimbologia.png', width=280, height=350)
        self.iconphoto(False, self.imagen)

        #CREACION DE FRAMES
        self.titulo_frame = tk.Frame(self, background=self.color_secundario, width=1280, height=70, highlightbackground='black', highlightthickness=2)
        self.section_frame = tk.Frame(self, background=self.color_secundario, width=1280/2, height=580, padx=10, pady=20, highlightbackground='black', highlightthickness=2)
        self.lecturas_frame = tk.Frame(self, background=self.color_primario, width=1280/2, height=580, padx=10, pady=20)
        self.footer_frame = tk.Frame(self, background=self.color_secundario, width=1280, height=70, highlightbackground='black', highlightthickness=2)

        #GRID CONFIGURE FRAMES
        #self.grid_columnconfigure(0, weight=1)
        #self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        #self.grid_rowconfigure(2, weight=1)
        
        #GRID FRAMES
        self.titulo_frame.grid(row=0, sticky='ew', columnspan=10)
        self.section_frame.grid(row=1, sticky='ew', padx=30)
        self.lecturas_frame.grid(row=1, column=1 ,sticky='ew')
        self.footer_frame.grid(row=2, sticky='ew', columnspan=10)

        ##############
        #TITULO FRAME#
        ##############

        #ELEMENTOS TITULO FRAME
        self.titulo_tabel = tk.Label(self.titulo_frame, text="Termolector CITEC UBB", font=(self.fuente, 25 , 'bold'), background=self.color_secundario, fg='White', relief=tk.RIDGE, padx=10)
        self.ruta_citec_imagen = Image.open("logo-citec.png")
        self.ruta_citec_imagen= self.ruta_citec_imagen.resize((170,100), Image.ANTIALIAS)
        self.citec_imagen = ImageTk.PhotoImage(self.ruta_citec_imagen)
        self.citec_imagen_label = Label(self.titulo_frame, image=self.citec_imagen)
        
        #GRID TITULO FRAME#
        self.titulo_tabel.grid(row=0, columnspan=10, padx=350)
        self.citec_imagen_label.grid(row=0, column=9, pady=10)

        #SECCION DE PARAMETROS FRAME
        #ELEMENTOS DE PARAMETROS FRAME
        self.nombre_carpeta_label = tk.Label(self.section_frame, text="Nombre de experimento: ", font=(self.fuente, 12), background=self.color_secundario, width=25, highlightbackground='black', highlightthickness=2, relief=tk.RAISED)
        self.puerto_com_label = tk.Label(self.section_frame, text="Seleccione puerto COM: ", font=(self.fuente, 12), background=self.color_secundario, width=25, highlightbackground='black', highlightthickness=2, relief=tk.RAISED)
        self.intervalo_lectura_label = tk.Label(self.section_frame, text="Intervalo de lectura: ", font=(self.fuente, 12), background=self.color_secundario, width=25, highlightbackground='black', highlightthickness=2, relief=tk.RAISED)
        self.fecha_inicio_label = tk.Label(self.section_frame, text="Seleccione fecha de inicio:  ", font=(self.fuente, 12), background=self.color_secundario, width=25, highlightbackground='black', highlightthickness=2, relief=tk.RAISED)
        self.fecha_termino_label = tk.Label(self.section_frame, text="Seleccione fecha de término:  ", font=(self.fuente, 12), background=self.color_secundario, width=25, highlightbackground='black', highlightthickness=2, relief=tk.RAISED)
        self.hora_label = tk.Label(self.section_frame, text="hora: ", font=(self.fuente, 12), background=self.color_secundario, highlightbackground='black', highlightthickness=2, relief=tk.RAISED)
        self.dos_puntos_label = tk.Label(self.section_frame, text=":", font=(self.fuente,12, 'bold'), background=self.color_secundario)
        self.hora_label2 = tk.Label(self.section_frame, text="hora: ", font=(self.fuente, 12), background=self.color_secundario, highlightbackground='black', highlightthickness=2, relief=tk.RAISED)
        self.dos_puntos_label2 = tk.Label(self.section_frame, text=":", font=(self.fuente,12, 'bold'), background=self.color_secundario)
        
        self.nombre_carpeta_entry = tk.Entry(self.section_frame, width=26, font=(self.fuente, 12))
        self.puerto_com_combobox = ttk.Combobox(self.section_frame, values=self.buscar_puertos(), width=25, state="readonly", font=(self.fuente, 12))
        self.intervalo_lectura_spinbox = ttk.Spinbox(self.section_frame, from_=1, to=3600, increment=1, state="readonly", width=24, font=(self.fuente, 12))
        self.fecha_inicio = DateEntry(self.section_frame, width=25, font=(self.fuente, 12))
        self.hora_inicio = ttk.Spinbox(self.section_frame, from_=0, to=23, increment=1, width=2, font=(self.fuente, 12))
        self.minuto_inicio = ttk.Spinbox(self.section_frame, from_=0, to=59, increment=1, width=2, font=(self.fuente, 12))
        self.fecha_termino = DateEntry(self.section_frame, width=25, font=(self.fuente, 12))
        self.hora_termino = ttk.Spinbox(self.section_frame, from_=0, to=23, increment=1, width=2, font=(self.fuente, 12))
        self.minuto_termino = ttk.Spinbox(self.section_frame, from_=0, to=59, increment=1, width=2, font=(self.fuente, 12))
        self.configurar_paneles_button = ttk.Button(self.section_frame, text="Configurar paneles", width=20, command=self.configurar_paneles, padding=10)
        
        #INICIALIZANDO SPINBOX
        self.intervalo_lectura_spinbox.set('1')
        self.hora_inicio.set(self.hora_actual.hour)
        self.minuto_inicio.set(self.hora_actual.minute)
        self.hora_termino.set(self.hora_actual.hour)
        self.minuto_termino.set(self.hora_actual.minute)

        #GRID DE PARAMETROS FRAME
        #LABELS
        self.nombre_carpeta_label.grid(row=0, sticky='w', padx=10, pady=10)
        self.puerto_com_label.grid(row=1, sticky='w', padx=10, pady=10)
        self.intervalo_lectura_label.grid(row=2, sticky='w', padx=10, pady=10)
        self.fecha_inicio_label.grid(row=3, padx=10, pady=10)
        self.hora_label.grid(row=3, column=2, padx=10)
        self.dos_puntos_label.grid(row=3, column=4, padx=5 )
        self.fecha_termino_label.grid(row=4, padx=10, pady=10)
        self.hora_label2.grid(row=4, column=2, padx=5)
        self.dos_puntos_label2.grid(row=4, column=4)

        #ELEMENTS
        self.nombre_carpeta_entry.grid(row=0, column=1, sticky='w')
        self.puerto_com_combobox.grid(row=1, column=1, sticky='w')
        self.intervalo_lectura_spinbox.grid(row=2, column=1, sticky='w')
        self.fecha_inicio.grid(row=3, column=1, sticky='w')
        self.hora_inicio.grid(row=3, column=3, sticky='w', padx=5)
        self.minuto_inicio.grid(row=3, column=5, sticky='w', padx=5)
        self.fecha_termino.grid(row=4, column=1, sticky='w')
        self.hora_termino.grid(row=4, column=3, sticky='w', padx=5)
        self.minuto_termino.grid(row=4, column=5, sticky='w', padx=5)
        self.configurar_paneles_button.grid(row=5, columnspan=6, padx=10, pady=20, sticky='e')
        
        ###################################
        #SECCION CUADRO DE LECTURAS FRAME.#
        ###################################

        #ELEMENTOS CUADRO DE LECTURAS FRAME.
        self.cuadro_lecturas_text = tk.Text(self.lecturas_frame, height=27, width=55)
        self.cuadro_lecturas_text.insert(tk.INSERT,"hola")
        self.cuadro_lecturas_text.delete('1.0', tk.END)
        
        #GRID CUADRO DE LECTURAS FRAME
        self.cuadro_lecturas_text.grid(row=0)

        ######################
        #SECCION FOOTER FRAME#
        ######################
        self.comenzar_button = ttk.Button(self.footer_frame, text="Comenzar lectura", width=25, command=self.comenzar, padding=19)

        self.comenzar_button.grid(row=0, padx=550, pady=10, columnspan=10)
    
    def comenzar(self):
        self.paneles = configparser.ConfigParser()
        self.paneles.read('paneles.config')
        if not self.definir_puerto():
            return
        self.definir_parametros()
        
        if not self.crear_archivos():
            return

        self.comenzar_lectura()

    def definir_parametros(self):
        self.nombre_carpeta = self.nombre_carpeta_entry.get()
        self.segundos = int(self.intervalo_lectura_spinbox.get())
        self.date_init = self.hora_inicio.get()+":"+self.minuto_inicio.get()+" "+str(self.fecha_inicio.get_date())
        self.date_end = self.hora_termino.get()+":"+self.minuto_termino.get()+" "+str(self.fecha_termino.get_date())
        self.fecha_hora_inicio = datetime.strptime(self.date_init, '%H:%M %Y-%m-%d')
        self.fecha_hora_termino = datetime.strptime(self.date_end, '%H:%M %Y-%m-%d')
        
        #print(self.paneles['PANEL1']['dispositivo1'])
        #self.paneles['PANEL1']['dispositivo1']='ttttil'
        #paneles_guardar = open('paneles.config', 'w')
        #self.paneles.write(paneles_guardar)
        #print(self.buscar_puertos())
    
    def buscar_puertos(self):
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

    def configurar_paneles(self):
        self.paneles_ventana = Paneles()
        self.paneles_ventana.resizable(False, False)
        self.paneles_ventana.set_combobox()

    def definir_puerto(self):
        puerto_seleccionado = self.puerto_com_combobox.get()
        try:
            self.puerto = serial.Serial(port = puerto_seleccionado, baudrate = 9600, timeout = 1.0)
            self.puerto.parity= serial.PARITY_NONE
            self.puerto.bytesize=serial.EIGHTBITS
            self.puerto.stopbits=serial.STOPBITS_ONE
                
            return True
        except (OSError, serial.SerialException):
            self.cuadro_lecturas_text.delete('1.0', tk.END)
            self.cuadro_lecturas_text.insert(tk.INSERT, "Puerto no válido")
            return False

    
    def crear_archivos(self):
        cont = 0
        self.archivos = [None, None , None , None , None , None , None , None , None , None]

        try:
            os.mkdir('Experimentos')
        except OSError:
            print()
            
        try:
            os.mkdir('Experimentos/'+self.nombre_carpeta)
        except OSError as e:
            if e.errno == errno.EEXIST:
                self.cuadro_lecturas_text.delete('1.0', tk.END)
                self.cuadro_lecturas_text.insert(tk.INSERT, "Nombre duplicado de experimento")
                return False
        
        for panel in self.paneles.sections():
            print(self.paneles[panel]['activo'])
            if self.paneles[panel]['activo'] == 'ACTIVADO':
                self.archivos[cont] = open('Experimentos/'+self.nombre_carpeta+'/'+panel+".txt" , "w")
            cont+=1
        print(self.archivos)
        return True
        

    def comenzar_lectura(self):
        self.t1 = threading.Thread(target=self.lectura)
        self.t1.start()

    def lectura(self):
        caracteres = "+0.123456789-"
        print(self.fecha_hora_inicio)

        while datetime.now() < self.fecha_hora_inicio:
            time.sleep(1)

        while self.fecha_hora_inicio < datetime.now() < self.fecha_hora_termino:
            aux = 0
            for panel in self.paneles.sections():
                if self.paneles[panel]['activo'] == 'ACTIVADO':
                    tiempo = time.strftime('%d-%m-%Y %H:%M:%S')
                    self.archivos[aux].write(tiempo)
                    if self.paneles[panel]['dispositivo1'] != 'NO USAR':
                        self.dispositivo= self.paneles[panel]['dispositivo1']+'\r\n'
                        self.puerto.write(self.dispositivo.encode('ascii'))
                        self.value = self.puerto.readline()
                        self.value = str(self.value)
                        self.value = ''.join(x for x in self.value if x in caracteres)
                        self.value = self.value.lstrip('987654321')
                        self.archivos[aux].write(' ' + str(self.value))

                    if self.paneles[panel]['dispositivo2'] != 'NO USAR':
                        self.dispositivo= self.paneles[panel]['dispositivo2']+'\r\n'
                        self.puerto.write(self.dispositivo.encode('ascii'))
                        self.value = self.puerto.readline()
                        self.value = str(self.value)
                        self.value = ''.join(x for x in self.value if x in caracteres)
                        self.value = self.value.lstrip('987654321')
                        self.archivos[aux].write(' ' + str(self.value))

                    if self.paneles[panel]['dispositivo3'] != 'NO USAR':
                        self.dispositivo= self.paneles[panel]['dispositivo3']+'\r\n'
                        self.puerto.write(self.dispositivo.encode('ascii'))
                        self.value = self.puerto.readline()
                        self.value = str(self.value)
                        self.value = ''.join(x for x in self.value if x in caracteres)
                        self.value = self.value.lstrip('987654321')
                        print(self.value)
                        self.archivos[aux].write(' ' + str(self.value))

                    self.archivos[aux].write("\n")
                    self.archivos[aux].flush()
                aux += 1
            print(aux)
            time.sleep(self.segundos)
        self.puerto.close()
        self.cuadro_lecturas_text.delete('1.0', tk.END)
        self.cuadro_lecturas_text.insert(tk.INSERT, "Lectura terminada")

if __name__ == "__main__":
    termolector = Termolector()
    termolector.resizable(False, False)
    termolector.mainloop()
