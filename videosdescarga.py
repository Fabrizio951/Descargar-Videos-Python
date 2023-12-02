import yt_dlp
from tkinter import*
from tkinter import messagebox as MessageBox
from tkinter import filedialog
import os
import json
import sys
#Funciones-----------------------------------------------
def acciona():
    # Ingresar URL
    url = video.get()
    #Ingresar lugar donde se va a guardar
    ubicacion_archivo = obtener_ruta_guardada()
    #Tipo video o audio bestaudio/best
    format = 'bestaudio/best'

    ydl_opts= {
        'outtmpl' : f'{ubicacion_archivo}/%(title)s.%(ext)s',
        'format' : format
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        
def accionv():
    # Ingresar URL
    url = video.get()
    #Ingresar lugar donde se va a guardar
    ubicacion_archivo = obtener_ruta_guardada()
    #Tipo video o audio bestaudio/best
    format = 'mp4'

    ydl_opts= {
        'outtmpl' : f'{ubicacion_archivo}/%(title)s.%(ext)s',
        'format' : format
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def obtener_ruta_guardada():
    try:
        # Intentar cargar la última ruta guardada desde un archivo de configuración
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)
            return config_data.get('ubicacion_archivo', obtener_ruta_predeterminada())
    except (FileNotFoundError, json.JSONDecodeError):
        # En caso de errores, devolver la ruta predeterminada
        return obtener_ruta_predeterminada()

def obtener_ruta_predeterminada():
    # Ruta predeterminada: escritorio del usuario
    return os.path.join(os.path.expanduser('~'), 'Desktop')

def seleccionar_ruta():
    # Abrir el cuadro de diálogo para seleccionar una ruta
    ruta_seleccionada = filedialog.askdirectory()
    if ruta_seleccionada:
        # Guardar la ruta seleccionada en el archivo de configuración
        guardar_ruta_seleccionada(ruta_seleccionada)
        return ruta_seleccionada
    else:
        # Devolver la ruta predeterminada si el usuario cancela la selección
        return obtener_ruta_predeterminada()

def guardar_ruta_seleccionada(ruta):
    # Guardar la ruta seleccionada en un archivo de configuración
    config_data = {'ubicacion_archivo': ruta}
    with open('config.json', 'w') as config_file:
        json.dump(config_data, config_file)

def infoAu():
    MessageBox.showinfo("Creador","Nombre: Fabrizio Santiago Zuñiga Arivilca\nhttps://github.com/Fabrizio951")
def infoPro():
    MessageBox.showinfo("Datos","Versión: 1.0.0\nRuta selecionada: "+obtener_ruta_guardada())
#--------------------------------------------------------
# Obtener la ruta del script principal (donde se encuentra el ejecutable)
ruta_script = sys.argv[0]
directorio_script = os.path.dirname(os.path.realpath(ruta_script))

# Construir la ruta completa al archivo .ico
ruta_icono = os.path.join(directorio_script, 'vid.ico')

root = Tk()
root.config(bd=50)
root.title("Contenidos Multimedia")

root.iconbitmap(ruta_icono)

#Menu bar-------------------------------------------------
menubar= Menu(root)
root.config(menu=menubar)
helpmenu=Menu(menubar,tearoff=0)

menubar.add_cascade(label="Información",menu=helpmenu)
helpmenu.add_command(label="Información sobre el autor",command=infoAu)
helpmenu.add_command(label="Información sobre el programa",command=infoPro)

#-----------------------------------------------------------

boton_seleccionar_ruta = Button(root, text="Seleccionar Ruta", command=seleccionar_ruta)
boton_seleccionar_ruta.grid(row=0, column=0,padx=(0,150),pady=(0,20))

instrucciones=Label(root,text="Ingresar link para descarga")
instrucciones.grid(row=1,column=0,pady=5)

video=Entry(root,width=40)
video.grid(row=2,column=0,padx=5, pady=15)

boton=Button(root,text="Descargar Audio",command=acciona)
boton.grid(row=3,column=0,padx=(0,110))

boton=Button(root,text="Descargar Video",command=accionv)
boton.grid(row=3,column=0,padx=(110,0))

root.mainloop()