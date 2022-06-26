#Recuerden que tienen que instalar estas librerias... 
#si usan linux el imagetk lo instalan con
#sudo apt-get install python3-pil python3-pil.imagetk pa que no se la compliquen XD
#Talvez les sirva de algo a y si desean agregar mas cosas para mejorarlo haganlo
#pero me lo comparten para disfrutarlo tambien no sean Ronchas jejeje XD

from tkinter import *
from PIL import Image, ImageTk
import shutil         
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb


#abre la ventana
def abrir_ventana():
    leer=easygui.fileopenbox()
    return leer

# abre los archivos
def abrir_archivo():
    string = abrir_ventana()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmacion', "Archivo no encontrado!")

# copia los archivos
def copiar():
    origen = abrir_ventana()
    destino = filedialog.askdirectory()
    shutil.copy(origen,destino)
    mb.showinfo('confirmacion', "Archivo copiado !")

# elimina los archivos
def Eliminar():
    eliminararchivo = abrir_ventana()
    if os.path.exists(eliminararchivo):
        os.remove(eliminararchivo)             
    else:
        mb.showinfo('confirmation', "Archivo no encontrado!!")

# renombra los archivos
def Renombrar():
    Elige_archivo = abrir_ventana()
    path1 = os.path.dirname(Elige_archivo)
    extension=os.path.splitext(Elige_archivo)[1]
    print("Enter new name for the chosen file")
    nuevoNombre=input()
    path = os.path.join(path1, nuevoNombre+extension)
    print(path)
    os.rename(Elige_archivo,path) 
    mb.showinfo('confirmacion', "Archivo renombrado!!!")

# mueve los archivos
def mover():
    origen1 = abrir_ventana()
    destino1 =filedialog.askdirectory()
    if(origen1==destino1):
        mb.showinfo('confirmacion', "El origen y el destino son el mismo")
    else:
        shutil.move(origen1, destino1)  
        mb.showinfo('confirmacion', "Archivo movido!!... AZUCA....!!!")

# crea nuevas carpetas
def crear():
    NuevoFolderPath = filedialog.askdirectory()
    print("Nuevo nombre: ")

    NuevoFolder=input()
    path = os.path.join(NuevoFolderPath, NuevoFolder)  

    os.mkdir(path)
    mb.showinfo('confirmacion', "Carpeta Creada !")

# elimina las carpetas
def Eliminar_carpeta():
    eliminarcarpeta = filedialog.askdirectory()
    os.rmdir(eliminarcarpeta)
    mb.showinfo('confirmacion', "Carpeta Eliminada !")

# lista de los archivos en una carpeta determinada
def listar_archivos():
    carpetaList = filedialog.askdirectory()
    sortlist=sorted(os.listdir(carpetaList))       
    i=0
    print("Los archivos en esta", carpetaList, "Carpeta son:")
    while(i<len(sortlist)):
        print(sortlist[i]+'\n')
        i+=1

root = Tk()

# crea un canvas para insertar una imagen sexy y el color de fondo... no le pongan de trapitos xfa no la caguen :v
canv = Canvas(root, width=1000, height=375, bg='Gray')
canv.grid(row=0, column=2)
#aqui pueden elegir la imagen del fondo.. recuerden poner la direccion completa y la extension!!!
img = ImageTk.PhotoImage(Image.open("/home/frank/Downloads/top-60-sexiest-anime-girls-of-all-time-2020-best-of-comic-books-1.jpg"))  
canv.create_image(0, 0, anchor=NW, image=img)

# crea los botones y llama a las funciones
Label(root, text="Frank File Manager :v", font=("Helvetica", 16), fg="blue").grid(row = 5, column = 2)

Button(root, text = "Abrir Archivo", command = abrir_archivo).grid(row=15, column =2,)

Button(root, text = "Copiar Archivo", command = copiar).grid(row = 25, column = 2)

Button(root, text = "Eliminar Archivo", command = Eliminar).grid(row = 35, column = 2)

Button(root, text = "Renombrar Archivo", command = Renombrar).grid(row = 45, column = 2)

Button(root, text = "Mover un Archivo", command = mover).grid(row = 55, column =2)

Button(root, text = "Crea una Carpeta", command = crear).grid(row = 75, column = 2)

Button(root, text = "Eliminar una Carpeta", command = Eliminar_carpeta).grid(row = 65, column =2)

Button(root, text = "Lista todos los Archivos en el Directorio", command = listar_archivos).grid(row = 85,column = 2)

root.mainloop()