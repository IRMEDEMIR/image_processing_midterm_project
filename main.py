import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  
import subprocess
from PIL import Image, ImageTk

def process_image1():
    # İlgili Python dosyasını çalıştır
    subprocess.run(["python", "sigmoid.py"])
    messagebox.showinfo("Bilgi", "Görüntü işlemi tamamlandı.")

def display_image1():
    # Görüntüyü yükle
    image_path1 = "gc4.jpg"
    image1 = Image.open(image_path1)
    
    # Görüntüyü ölçeklendir
    image1 = image1.resize((400, 300), Image.LANCZOS)

    # Görüntüyü Tkinter formatına dönüştür
    tk_image1 = ImageTk.PhotoImage(image1)
    
    # Label widget'ı oluşturarak görüntüyü göster
    lbl_image1 = tk.Label(tab1, image=tk_image1)
    lbl_image1.image1 = tk_image1
    lbl_image1.pack()

def process_image2():
    # İlgili Python dosyasını çalıştır
    subprocess.run(["python", "yolcizgi.py"])
    messagebox.showinfo("Bilgi", "Görüntü işlemi tamamlandı.")

def display_image2():
    # Görüntüyü yükle
    image_path2 = "otoban.jpg"
    image2 = Image.open(image_path2)
    
    # Görüntüyü ölçeklendir
    image2 = image2.resize((400, 300), Image.LANCZOS)

    # Görüntüyü Tkinter formatına dönüştür
    tk_image2 = ImageTk.PhotoImage(image2)
    
    # Label widget'ı oluşturarak görüntüyü göster
    lbl_image2 = tk.Label(tab2, image=tk_image2)
    lbl_image2.image2 = tk_image2
    lbl_image2.pack()

def process_image2_1():
    # İlgili Python dosyasını çalıştır
    subprocess.run(["python", "cascadegoz.py"])
    messagebox.showinfo("Bilgi", "Görüntü işlemi tamamlandı.")    

def display_image2_1():
    # Görüntüyü yükle
    image_path2_1 = "bc06.webp"
    image2_1 = Image.open(image_path2_1)
    
    # Görüntüyü ölçeklendir
    image2_1 = image2_1.resize((400, 300), Image.LANCZOS)

    # Görüntüyü Tkinter formatına dönüştür
    tk_image2_1 = ImageTk.PhotoImage(image2_1)
    
    # Label widget'ı oluşturarak görüntüyü göster
    lbl_image2_1 = tk.Label(tab2, image=tk_image2_1)
    lbl_image2_1.image2_1 = tk_image2_1
    lbl_image2_1.pack()

def process_image3():
    # İlgili Python dosyasını çalıştır
    subprocess.run(["python", "gausdeblur.py"])
    messagebox.showinfo("Bilgi", "Görüntü işlemi tamamlandı.")

def process_image3_1():
    # İlgili Python dosyasını çalıştır
    subprocess.run(["python", "deblur2.py"])
    messagebox.showinfo("Bilgi", "Görüntü işlemi tamamlandı.")

def display_image3():
    # Görüntüyü yükle
    image_path3 = "araba.jpg"
    image3 = Image.open(image_path3)
    
    # Görüntüyü ölçeklendir
    image3 = image3.resize((400, 300), Image.LANCZOS)

    # Görüntüyü Tkinter formatına dönüştür
    tk_image3 = ImageTk.PhotoImage(image3)
    
    # Label widget'ı oluşturarak görüntüyü göster
    lbl_image3 = tk.Label(tab3, image=tk_image3)
    lbl_image3.image3 = tk_image3
    lbl_image3.pack()

def process_image4():
    # İlgili Python dosyasını çalıştır
    subprocess.run(["python", "soru4.py"])
    messagebox.showinfo("Bilgi", "Excel dosyası oluşturuldu.")

def display_image4():
    # Görüntüyü yükle
    image_path4 = "say.jpg"
    image4 = Image.open(image_path4)
    
    # Görüntüyü ölçeklendir
    image4 = image4.resize((400, 300), Image.LANCZOS)

    # Görüntüyü Tkinter formatına dönüştür
    tk_image4 = ImageTk.PhotoImage(image4)
    
    # Label widget'ı oluşturarak görüntüyü göster
    lbl_image4 = tk.Label(tab4, image=tk_image4)
    lbl_image4.image4 = tk_image4
    lbl_image4.pack()

# Ana pencere oluştur
root = tk.Tk()
root.title("Görüntü İşleme Uygulaması")

# Pencere boyutunu belirle
root.geometry("1200x800")

# Sekmeleri oluştur
tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Sigmoid İşlemler')
tab_control.add(tab2, text='Hough Transform')
tab_control.add(tab3, text='Deblurring')
tab_control.add(tab4, text='Koyu Yeşil Piksel')

tab_control.pack(expand=1, fill='both')

# Her sekme için bir buton oluştur
display_image1()
btn_process1 = tk.Button(tab1, text="İşlemleri gerçekleştir", command=process_image1)
btn_process1.pack(pady=10)

display_image2()
btn_process2 = tk.Button(tab2, text="Yol çizgileri", command=process_image2)
btn_process2.pack(pady=10)

display_image2_1()
btn_process2_1 = tk.Button(tab2, text="Göz tespiti", command=process_image2_1)
btn_process2_1.pack(pady=10)

display_image3()
btn_process3 = tk.Button(tab3, text="Gauss", command=process_image3)
btn_process3.pack(pady=10)
btn_process3_1 = tk.Button(tab3, text="Richardson-Lucy ", command=process_image3_1)
btn_process3_1.pack(pady=10)

display_image4()
btn_process4 = tk.Button(tab4, text="Koyu yeşil bölgeler", command=process_image4)
btn_process4.pack(pady=10)

# Pencereyi göster
root.mainloop()
