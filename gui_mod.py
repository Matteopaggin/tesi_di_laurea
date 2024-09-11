import tkinter as tk
from PIL import Image, ImageTk
import time
import os
import csv
import imageio
#from win32api import GetSystemMetrics
from tkinter import filedialog

os.environ["IMAGEIO_FFMPEG_EXE"]="/Users/matteo/Documents/audio-orchestrator-ffmpeg/bin/ffmpeg"
screenWidth = 1600
screenHeight = 1200
SMALL_FONT= ("Verdana", int(screenHeight*0.013)) #24

LARGE_FONT= ("Verdana", int(screenHeight*0.023)) #24

BOLD_LARGE_FONT= ("Verdana", int(screenHeight*0.023), "bold") #24

MEDIUM_LARGE_FONT= ("Verdana", int(screenHeight*0.027)) #36

LARGE_LARGE_FONT= ("Verdana", int(screenHeight*0.035)) #54

LOCALTE = 0

RADIO_BUTTON_WIDTH = int(screenWidth*0.015) #20
RADIO_BUTTON_HEIGHT = int(screenHeight*0.004) #3
TEXT_BOX_WIDTH = int(screenWidth*0.015) 
TEXT_BOX_HEIGHT = int(screenHeight*0.004)

#%%
class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        # Language choice - pt or it
        lang = 'it'
        container = tk.Frame(self)
        # self.minsize(1700,1000)
        self.minsize(int(screenWidth*0.2),int(screenHeight*0.2))
        
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.folder_path = None
        self.frames = {}
        self.v_reader = None
        self.image = None
        self.canvas = None
        self.vidlen = 0
        self.tempos = None
        self.counter = 0
        self.patient = False
        self.text = "Where is the patient looking to?"
        self.app_data = {"TName":    tk.StringVar(),
                         "PName":    tk.StringVar(),
                         "NSession": tk.StringVar(),
                        }
        # self.levels = {
        #     PageOne:       "Level1",
        #     PageOnehalf:   "Level1"
        # }
        self.strings=list()

        for F in (PageZero,StartPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        

        self.show_frame(PageZero)
        # new_window = tk.Toplevel(tk.Tk())
        # image = tk.PhotoImage(file="C:\\Users\\Laura\\Documents\\ExpGulbenkian\\treno.png")
        
        
    def registercontext(self,context):
        self.context=context

    def on_closing(self):
        print('on_closing')
        if self.v_reader is not None:
            self.v_reader.close()
        self.destroy()
    
    def show_frame(self, cont):
        # print('PName',self.app_data["PName"].get())
        # print('TName',self.app_data["TName"].get())
        # print('NSession',str(self.app_data["NSession"].get()))
        # if cont is not PageZero and cont is not StartPage:
        #     self.strings.append(self.levels[cont])
        # if cont is PageEval1:
        #     self.context['evalstate'].trigger('start_session')
        frame = self.frames[cont]
        frame.tkraise()

class PageZero(tk.Frame):
    
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent)
        self.controller = controller
        
        button2 = tk.Button(self,text="Browse", height = 5, width= 20, font=BOLD_LARGE_FONT,command=lambda: self.browse_button())
        button2.place(relx=0,rely=0)

    def browse_button(self):
        # Allow user to select a directory and store it in global var
        # called folder_path
        # filename = filedialog.askopenfilename(initialdir = "C:\\Users\\LAURA01\\Desktop\\data_laura\\data_laura\\Dados",title = "Select file",filetypes = (("avi files","*.avi"),("all files","*.*")))

        filename = filedialog.askopenfilename(initialdir = "/Users/matteo/Desktop",title = "Select file",filetypes = (("avi files","*.avi"),("all files","*.*")))

        self.controller.folder_path = filename
        # print(filename)
        print(self.controller.folder_path)
        if self.controller.folder_path is not None:
            self.controller.show_frame(StartPage)
            self.controller.tempos = self.read_tempos(filename)
            self.controller.minsize(int(screenWidth*0.9),int(screenHeight*0.9))
            self.controller.v_reader = imageio.get_reader(self.controller.folder_path)
            self.controller.vidlen = len(self.controller.tempos)
            # self.controller.vidlen = self.controller.v_reader.count_frames()
            print('Initial video len:', self.controller.vidlen)
            # self.controller.image = self.controller.v_reader.get_next_data().copy()
            # frame_image = ImageTk.PhotoImage(Image.fromarray(self.controller.image))
            # self.canvas = tk.Canvas(parent,  width=1100, height=720)
            # self.canvas.pack()

    def read_tempos(self,filename):
        parentpath=os.path.dirname(filename)
        basename = os.path.basename(filename)
        newfile = parentpath+'/tempos' + basename[5:-3]+'txt'
        print(newfile)
        # newfile = parentpath+'/tempos_cutted.txt'
        with open(newfile) as f:
            lines = [line.rstrip() for line in f]
        return lines
  
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.rate = 30
        self.window = parent
        self.controller = controller
        self.label = tk.Label(self, text= 'Visual analysis', font=BOLD_LARGE_FONT)
        self.label.place(relx=0.32,rely=0.1)

        self.counter = -1
        self.filedirend = '\\visual_analysis.txt'
        
        robot = 'indica-robot'
        in_look = 'inizia a guardare'
        in_point = 'indica'
        ffwd = '2,5 secondi'
        fbwd = '-2,5 secondi'
        fwd = 'mezzo secondo'
        bwd = '-mezzo secondo'


        

        # win = tk.Toplevel()
        # self.center(win)
        # if the panel is not None, we need to initialize it
        self.panel = None
        self.delay = 15
        
        button = tk.Button(self, height = 1, width= 12, text=robot,font=BOLD_LARGE_FONT,bg="blue",
                            command=lambda: self.write_file(robot))
        button.place(relx=0.815,rely=0.20)

        button2 = tk.Button(self, height = 1, width= 12, text=in_look,font=BOLD_LARGE_FONT,bg="red",
                            command=lambda: self.write_file(in_look))
        button2.place(relx=0.815,rely=0.30)

        button3 = tk.Button(self, height = 1, width= 12, text=bwd,font=BOLD_LARGE_FONT,bg="red",
                            command=lambda: self.setrate(-6))
        button3.place(relx=0.815,rely=0.40)


        button5 = tk.Button(self, height = 1, width= 12, text=fwd,font=BOLD_LARGE_FONT,bg="red",
                            command=lambda: self.setrate(6))
        button5.place(relx=0.815,rely=0.50)


        button6 = tk.Button(self, height = 1, width= 12, text=fbwd,font=BOLD_LARGE_FONT,bg="red",
                            command=lambda: self.setrate(-30))
        button6.place(relx=0.815,rely=0.60)

        button7 = tk.Button(self, height = 1, width= 12, text=ffwd,font=BOLD_LARGE_FONT,bg="red",
                            command=lambda: self.setrate(30))
        button7.place(relx=0.815,rely=0.70)

        button8 = tk.Button(self, height = 1, width= 12, text=in_point,font=BOLD_LARGE_FONT,bg="red",
                            command=lambda: self.write_file(in_point))
        button8.place(relx=0.815,rely=0.80)

        #button3 = tk.Button(self, height = 2, width= 7, text=robot,font=BOLD_LARGE_FONT,bg="green",
        #                    command=lambda: self.write_file(robot))
        #button3.place(relx=0.87,rely=0.54)
        #self.controller.bind('a',self.write_file(robot))


        # button4 = tk.Button(self, height = 5, width= 10, text=self.controller.dicionario['L4'],font=BOLD_LARGE_FONT,bg="yellow",
        #                     command=lambda: controller.show_frame(PageFour))
        # button4.place(relx=0.2,rely=0.6)

        # button5 = tk.Button(self, height = 5, width= 10, text=self.controller.dicionario['L5'],font=BOLD_LARGE_FONT,bg="purple",
        #                     command=lambda: controller.show_frame(PageFive))
        # button5.place(relx=0.5,rely=0.6)

        # button6 = tk.Button(self, height = 5, width= 10, text=self.controller.dicionario['Eval'],font=BOLD_LARGE_FONT,bg="orange",
        #                     command=lambda: controller.show_frame(PageEval1))
        # button6.place(relx=0.8,rely=0.6)
        
    def write_file(self, text):
        if self.controller.v_reader is not None:
            #totaltime = float(self.controller.tempos[-1]) - float(self.controller.tempos[0])
            #timerate = totaltime/3
            # rate = int(len(self.controller.tempos)/timerate)
            if self.counter >= -1:
                parentpath  = os.path.dirname(self.controller.folder_path)
                current_time = self.controller.tempos[self.counter]
                f = open(parentpath + self.filedirend,'a')
                f.write(current_time+ ' ' +text+'\n')
                f.close()
            

    def setrate(self, mod_rate):
        self.rate = mod_rate
        if self.counter + self.rate < self.controller.vidlen:
            if self.counter == -1:
                self.counter = 0
            else:     
                self.counter = self.counter + self.rate
            print('curr_frame:',self.counter)
            #if self.counter > -1:
            self.controller.v_reader.set_image_index(self.counter)
            self.controller.image = self.controller.v_reader.get_next_data().copy()
            
            image = Image.fromarray(self.controller.image)
            resized = image.resize((1000,600),Image.Resampling.LANCZOS)
            imagePI = ImageTk.PhotoImage(resized)
            if self.panel is None:
                self.panel = tk.Label(self, image=imagePI)
                self.panel.image = imagePI
                self.panel.place(relx=0.1,rely=0.2)
            # otherwise, simply update the panel
            else:
                self.panel.configure(image=imagePI)
                self.panel.image = imagePI
        else:
            self.controller.onclosing()

            

app = SeaofBTCapp()
app.protocol('WM_DELETE_WINDOW', app.on_closing)
app.mainloop()
# %%
