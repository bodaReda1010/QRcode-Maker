from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from qrcode.image.styles.colormasks import *
import PIL
from PIL import Image
from tkinter import filedialog
import os

class App:
    def __init__(self , app):
        self.app = app
        self.app.geometry('450x550+450+50')
        self.app.title('Qr-Code-Marker')
        self.app.config(background = 'white')
        self.app.resizable(False , False)
        self.app.iconbitmap(r'qr.ico')
        global photo
        photo = PhotoImage(file = 'qr.png')
        title = Label(self.app , text = 'Qr-Code-Marker' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 26))
        title.pack(fill = X)
        lbl1 = Label(self.app , image = photo)
        lbl1.place(x= 80 , y = 100)

        btn_basic = Button(self.app , text = 'Basic' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 26) , command = self.open_basic)
        btn_basic.place(x = 20 , y = 430 , width = 100 , height = 40)

        btn_standard = Button(self.app , text = 'Satandard' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 26) , command = self.open_standard)
        btn_standard.place(x = 135 , y = 430 , width = 150 , height = 40)

        btn_pro = Button(self.app , text = 'Premium' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 26) , command = self.open_premium)
        btn_pro.place(x = 300 , y = 430 , width = 130 , height = 40)

    def open_basic(self):
        basic = Tk()
        Basic(basic)
        basic.mainloop()
    
    def open_standard(self):
        standard = Tk()
        Standard(standard)
        standard.mainloop()

    def open_premium(self):
        premium = Tk()
        Premium(premium)
        premium.mainloop()
class Basic:
    def __init__(self , basic):
        self.basic = basic
        self.basic.geometry('400x300+80+50')
        self.basic.title('Qr-Code-Marker')
        self.basic.config(background = 'white')
        self.basic.resizable(False , False)
        self.basic.iconbitmap(r'qr.ico')

        title = Label(self.basic , text = 'Qr-Code-Marker' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 26))
        title.pack(fill = X)

        global link_entry
        global title_entry

        lbl_link = Label(self.basic , text = 'Put The Link Here' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' ,14))
        lbl_link.place(x = 0 , y = 100)
        link_entry = Entry(self.basic , bd = 2 , justify = 'left' , fg = 'black', font = ('Times' ,14))
        link_entry.place(x = 150 , y = 100 , width = 240)

        lbl_link = Label(self.basic , text = 'Put The Title Here' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' ,14))
        lbl_link.place(x = 0 , y = 150)
        title_entry = Entry(self.basic , bd = 2 , justify = 'left' , fg = 'black', font = ('Times' ,14))
        title_entry.place(x = 150 , y = 150 , width = 240)

        convert_btn_basic =  Button(self.basic , text = 'Convert' , bg = '#2A0B3D' , fg = 'white' , font = ('Times' , 14) , command = self.make_basic)
        convert_btn_basic.place(x = 135 , y = 200 , width = 100 , height = 40)

    def make_basic(self):
        url = link_entry.get()
        title = title_entry.get()
        img = qrcode.make(url)
        img.save(f"{title}.png")

class Standard:
    def __init__(self , standard):
        self.standard = standard
        self.standard.title('Qr-Code-Maker')
        self.standard.geometry('600x250+600+50')
        self.standard.config(background = 'white')
        self.standard.resizable(False , False)
        self.standard.iconbitmap(r'qr.ico')

        global standard_entry
        global fillcolor_entry
        global backcolor_entry
        global adress_entry

        title = Label(self.standard , text = 'Qr-Code-Maker' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 26))
        title.pack(fill = X)

        adress_label = Label(self.standard , text = 'Title' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 20))
        adress_label.place(x = 80 , y = 50)
        adress_entry = Entry(self.standard , bd = 2 , width = 20 , font = ('Times' , 20))
        adress_entry.place(x = 270 , y = 50)

        standard_label = Label(self.standard , text = 'Put The Link Here' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 20))
        standard_label.place(x = 30 , y = 115)
        standard_entry = Entry(self.standard , bd = 2 , width = 20 , font = ('Times' , 20))
        standard_entry.place(x = 270 , y = 115)

        fillcolor_label = Label(self.standard , text = 'Fill Color' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 20))
        fillcolor_label.place(x = 7 , y = 210)
        fillcolor_entry = Entry(self.standard , bd = 2 , width = 5 , font = ('Times' , 20))
        fillcolor_entry.place(x = 140 , y = 210)

        backcolor_label = Label(self.standard , text = 'Backcolor' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 20))
        backcolor_label.place(x = 230 , y = 210)
        backcolor_entry = Entry(self.standard , bd = 2 , width = 5 , font = ('Times' , 20))
        backcolor_entry.place(x = 370 , y = 210)

        convert_btn_standard = Button(self.standard , text = 'Convert' , bg = '#2A0B3D' , fg = 'white' , font = ('Times' , 14) , command = self.make_standard)
        convert_btn_standard.place(x = 485 , y = 205 , width = 100 , height = 40)

    def make_standard(self):
        url = standard_entry.get()
        title = adress_entry.get()
        fill_color = fillcolor_entry.get()
        back_color = backcolor_entry.get()
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 4,
        )
        qr.add_data(url)
        qr.make(fit = True)
        img = qr.make_image(fill_color = fill_color , back_color = back_color).convert('RGB')
        img.save(f"{title}.png")

class Premium:
    def __init__(self, premium):
        self.premium = premium
        self.premium.title('Qr-Code-Maker')
        self.premium.geometry('600x450+20+48')
        self.premium.config(background = 'white')
        self.premium.resizable(False , False)
        self.premium.iconbitmap(r'qr.ico')

        title = Label(self.premium , text = 'Qr-Code-Maker' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 20))
        title.pack(fill = X)

        global e_pro
        global e_save
        global e_back_colors1
        global e_back_colors2
        global e_back_colors3
        global e_edge_color1
        global e_edge_color2
        global e_edge_color3
        global e_center_color1
        global e_center_color2
        global e_center_color3
        global e_photo

        title_label = Label(self.premium , text = 'Title' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 20))
        title_label.place(x = 50 , y = 50)
        e_save = Entry(self.premium , bd = 2 , width = 25 , font = ('Times' , 20))
        e_save.place(x = 120 , y = 50)

        photo_label = Label(self.premium , text = 'Put The Link Here' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 20))
        photo_label.place(x = 0 , y = 120)
        e_pro = Entry(self.premium , bd = 2 , width = 25 , font = ('Times' , 20))
        e_pro.place(x = 220 , y = 120)

        backcolor_label = Label(self.premium , text = 'Back Color' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 20))
        backcolor_label.place(x = 15 , y = 210)
        e_back_colors1 = Entry(self.premium , bd = 2 , width = 3 , font = ('Times' , 20))
        e_back_colors1.place(x = 155 , y = 210)
        e_back_colors2 = Entry(self.premium , bd = 2 , width = 3 , font = ('Times' , 20))
        e_back_colors2.place(x = 205 , y = 210)
        e_back_colors3 = Entry(self.premium , bd = 2 , width = 3 , font = ('Times' , 20))
        e_back_colors3.place(x = 255 , y = 210)

        edgecolor_label = Label(self.premium , text = 'Edge Color' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 20))
        edgecolor_label.place(x = 310 , y = 210)
        e_edge_color1 = Entry(self.premium , bd = 2 , width = 3 , font = ('Times' , 20))
        e_edge_color1.place(x = 450 , y = 210)
        e_edge_color2 = Entry(self.premium , bd = 2 , width = 3 , font = ('Times' , 20))
        e_edge_color2.place(x = 505 , y = 210)
        e_edge_color3 = Entry(self.premium , bd = 2 , width = 3 , font = ('Times' , 20))
        e_edge_color3.place(x = 555 , y = 210)

        centercolor_label = Label(self.premium , text = 'Center Color' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 20))
        centercolor_label.place(x = 15 , y = 260)
        e_center_color1 = Entry(self.premium , bd = 2 , width = 3 , font = ('Times' , 20))
        e_center_color1.place(x = 170 , y = 260)
        e_center_color2 = Entry(self.premium , bd = 2 , width = 3 , font = ('Times' , 20))
        e_center_color2.place(x = 225 , y = 260)
        e_center_color3 = Entry(self.premium , bd = 2 , width = 3 , font = ('Times' , 20))
        e_center_color3.place(x = 280 , y = 260)

        path_label = Label(self.premium , text = 'Path' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 20))
        path_label.place(x = 15 , y = 330)
        e_photo = Entry(self.premium , bd = 2 , width = 25 , font = ('Times' , 20))
        e_photo.place(x = 120 , y = 330)

        convert_btn_pro = Button(self.premium , text = 'Convert' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 20) , command = self.make_premium)
        convert_btn_pro.place(x = 350 , y = 380)

        open_btn = Button(self.premium , text = 'Open' , fg = 'white' , bg = '#2A0B3D' , font = ('Times' , 20) , command = self.open2)
        open_btn.place(x = 150 , y = 380)

    def open2(self):
        file = filedialog.askopenfile(mode = 'r' , filetypes = [('Files', '*.jpg'),('Files', '*.png')])
        if file:
            filepath = os.path.abspath(file.name)
            e_photo.insert(0 , str(filepath))

    def make_premium(self):
        m = e_pro.get()
        t = e_save.get()
        b1 = e_back_colors1.get()
        b2 = e_back_colors2.get()
        b3 = e_back_colors3.get()
        b4 = e_edge_color1.get()
        b5 = e_edge_color2.get()
        b6 = e_edge_color3.get()
        b7 = e_center_color1.get()
        b8 = e_center_color2.get()
        b9 = e_center_color3.get()
        p = e_photo.get()

        logo = PIL.Image.open(p)

        basewidth = 60

        wpercent = (basewidth/float(logo.size[0]))

        hsize = int(float(logo.size[1])*float(wpercent))
        logo = logo.resize((basewidth , hsize),PIL.Image.LANCZOS)

        qr = qrcode.QRCode(error_correction = qrcode.constants.ERROR_CORRECT_L)
        qr.add_data(m)
        qr.make()

        img = qr.make_image(image_factory = StyledPilImage , color_mask = RadialGradiantColorMask(back_color=(int(b1) , int(b2) , int(b3)) , edge_color=(int(b4) , int(b5) , int(b6)) , center_color=(int(b7) , int(b8) , int(b9))),module_drawer = RoundedModuleDrawer())
        pos = ((img.size[0]-logo.size[0])//2,(img.size[1]-logo.size[1])//2)
        img.paste(logo , pos)
        img.save(f"{t}.png")












app = Tk()
App(app)
app.mainloop()
