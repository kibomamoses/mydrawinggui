
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

class Paint:
    def __init__(self):

        self.root=Tk()
        self.root.title("Drawing Gui")
        self.root.resizable(0,0)
        self.root.geometry("700x600+500+20")

        self.w=600
        self.h=300

        self.labinfo=Label(self.root, text="Paint Windows", width=50, font=("sans 14 bold"))
        self.labinfo.pack()
        self.my_canva=Canvas(self.root, width=self.w,height=self.h, bg="white")
        self.my_canva.pack(pady=16)
        self.brush_color = "black"
        self.brush_color_canva = "white"

        self.my_canva.bind('<B1-Motion>', self.paint)

        self.brush_options_frame=Frame(self.root)
        self.brush_options_frame.pack(pady=20)
        self.brush_size_frame=LabelFrame(self.brush_options_frame, text="Brush Size")
        self.brush_size_frame.grid(row=0, column=0, padx=50)

        self.my_slider=ttk.Scale(self.brush_size_frame, from_=1, to=100, command=self.change_brush_size, orient=VERTICAL, value=10)
        self.my_slider.pack(pady=10, padx=10)

        self.slide_label=Label(self.brush_size_frame, text=self.my_slider.get())
        self.slide_label.pack(pady=5)

        self.brush_type_frame=LabelFrame(self.brush_options_frame, text="Brush Type", height=300)
        self.brush_type_frame.grid(row=0, column=1, padx=50)
        self.brush_type=StringVar()
        self.brush_type.set('round')
        self.brush_type_radio1=Radiobutton(self.brush_type_frame, text="Round", variable=self.brush_type, value="round")
        self.brush_type_radio2 = Radiobutton(self.brush_type_frame, text="Slash", variable=self.brush_type, value="butt")
        self.brush_type_radio3 = Radiobutton(self.brush_type_frame, text="Diamond", variable=self.brush_type, value="projecting")
        self.brush_type_radio1.pack(anchor=W)
        self.brush_type_radio2.pack(anchor=W)
        self.brush_type_radio3.pack(anchor=W)

        self.change_colors_frame=LabelFrame(self.brush_options_frame, text="Change Color")
        self.change_colors_frame.grid(row=0, column=2)

        self.brush_color_button=Button(self.change_colors_frame, text="Brush Color", command=self.change_brush_color)
        self.brush_color_button.pack(pady=10, padx=10)
        self.canvas_color_button = Button(self.change_colors_frame, text="Canvas Color", command=self.change_canvas_color)
        self.canvas_color_button.pack(pady=10, padx=10)


        self.options_frame=LabelFrame(self.brush_options_frame, text="Options Programs")
        self.options_frame.grid(row=0, column=3, padx=50)


        self.clear_Button=Button(self.options_frame, text="Clear Screen", command=self.clear_screen)
        self.clear_Button.pack(padx=10, pady=10)


        self.root.mainloop()
    def clear_screen(self):
        self.my_canva.delete(ALL)

    def change_brush_color(self):
        self.brush_color = "black"
        self.brush_color=colorchooser.askcolor(self.brush_color)[1]
        self.color_label=Label(self.root, text=self.brush_color)
        self.color_label.pack(pady=20)

    def change_canvas_color(self):
        self.brush_color_canva = "black"
        self.brush_color_canva = colorchooser.askcolor(self.brush_color)[1]
        self.my_canva.config(bg=self.brush_color_canva)
        self.color_label1 = Label(self.root, text=self.brush_color_canva)
        self.color_label1.pack(pady=20)

    def change_brush_size(self, thing):
        self.slide_label.config(text='%0.0f'% float(self.my_slider.get()))
    def paint(self, e):
        #brus paraments
        brush_width='%0.0f'% float(self.my_slider.get())
        brush_color =str(self.brush_color)
        brush_type =self.brush_type.get()
        #obteniendo posiciones
        x1=e.x
        y1=e.y
        x2 = e.x+1
        y2= e.y+1
        self.my_canva.create_line(x1, y1, x2, y2, fill=brush_color,width=brush_width, capstyle=brush_type, smooth=True)
if __name__ == '__main__':
    apppaint=Paint()

