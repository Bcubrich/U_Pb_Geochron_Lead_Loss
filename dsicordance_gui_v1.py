#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    May 29, 2019 01:55:26 PM MDT  platform: Windows NT
###############################################################################
###############################################################################
#need to add in
#import MODOAnalysis
import sys
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.backends.backend_tkagg as tkagg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from tkinter.filedialog import askopenfilename
#from tkinter.filedialog import asksaveasfile
from matplotlib.figure import Figure
import matplotlib.transforms
#import itertools
#from pykrige.uk import UniversalKriging
#from matplotlib.mlab import griddata

#from tkinter import *
###############################################################################
###############################################################################

global lambda68
global lambda75
global  u238_u235
global avagadro

lambda68=0.155125*10**-9
lambda75=0.98485*10**-9
u238_u235=137.88
avagadro=(6.0221409*10**23)

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import dsicordance_gui_v1_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    dsicordance_gui_v1_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    dsicordance_gui_v1_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        self.fig_canvas=None
        self.extra_206_loss=0
        self.extra_207_loss=0
        self.max_discordance=0
        self.sample_t=1*10**6
        self.fig=None
        self.ax=None
        self.t=np.linspace(0,5,501)
        self.t=self.t*10**9
        self.pb206_u238=np.e**(lambda68*self.t)-1
        self.pb207_u235=np.e**(lambda75*self.t)-1
        self.toolbar=None
        self.t_labels_t=self.t[::100]/(10**9)
        self.t_labels_x=self.pb207_u235[::100]-2.5
        self.t_labels_y=self.pb206_u238[::100]
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 

        top.geometry("1042x751+458+132")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        self.frame = tk.Frame(top)
        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.221, rely=0.133, relheight=0.83
                , relwidth=0.742)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief='ridge')
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=773)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.029, rely=0.133, height=21, width=97)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Sample Age (Ma)''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.029, rely=0.24, height=21, width=96)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Max Discordance''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.029, rely=0.346, height=21, width=105)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Pb207 Loss''')

        self.Scale1 = tk.Scale(top, from_=1.0, to=4500.0, command=self.sample_age)
        self.Scale1.place(relx=0.029, rely=0.16, relwidth=0.175, relheight=0.0
                , height=61, bordermode='ignore')
        self.Scale1.configure(activebackground="#ececec")
        self.Scale1.configure(background="#d9d9d9")
        self.Scale1.configure(font="TkTextFont")
        self.Scale1.configure(foreground="#000000")
        self.Scale1.configure(highlightbackground="#d9d9d9")
        self.Scale1.configure(highlightcolor="black")
        self.Scale1.configure(length="176")
        self.Scale1.configure(orient="horizontal")
        self.Scale1.configure(tickinterval="1500.0")
        self.Scale1.configure(troughcolor="#d9d9d9")

        self.Scale2 = tk.Scale(top, from_=0, to=99, command=self.max_disc)
        self.Scale2.place(relx=0.029, rely=0.26, relwidth=0.102, relheight=0.0
                , height=61, bordermode='ignore')
        self.Scale2.configure(activebackground="#ececec")
        self.Scale2.configure(background="#d9d9d9")
        self.Scale2.configure(font="TkTextFont")
        self.Scale2.configure(foreground="#000000")
        self.Scale2.configure(highlightbackground="#d9d9d9")
        self.Scale2.configure(highlightcolor="black")
        self.Scale2.configure(orient="horizontal")
        self.Scale2.configure(tickinterval="99.0")
        self.Scale2.configure(troughcolor="#d9d9d9")

        self.Scale3 = tk.Scale(top, from_=0, to=100, command=self.scale_207)
        self.Scale3.place(relx=0.029, rely=0.379, relwidth=0.102, relheight=0.0
                , height=61, bordermode='ignore')
        self.Scale3.configure(activebackground="#ececec")
        self.Scale3.configure(background="#d9d9d9")
        self.Scale3.configure(font="TkTextFont")
        self.Scale3.configure(foreground="#000000")
        self.Scale3.configure(highlightbackground="#d9d9d9")
        self.Scale3.configure(highlightcolor="black")
        self.Scale3.configure(orient="horizontal")
        self.Scale3.configure(tickinterval="100.0")
        self.Scale3.configure(troughcolor="#d9d9d9")

        self.Label3_2 = tk.Label(top)
        self.Label3_2.place(relx=0.029, rely=0.466, height=21, width=105)
        self.Label3_2.configure(activebackground="#f9f9f9")
        self.Label3_2.configure(activeforeground="black")
        self.Label3_2.configure(background="#d9d9d9")
        self.Label3_2.configure(disabledforeground="#a3a3a3")
        self.Label3_2.configure(foreground="#000000")
        self.Label3_2.configure(highlightbackground="#d9d9d9")
        self.Label3_2.configure(highlightcolor="black")
        self.Label3_2.configure(text='''Pb206 Loss''')

        self.Scale4 = tk.Scale(top, from_=0.0, to=100, command=self.scale_206)
        self.Scale4.place(relx=0.029, rely=0.506, relwidth=0.102, relheight=0.0
                , height=61, bordermode='ignore')
        self.Scale4.configure(activebackground="#ececec")
        self.Scale4.configure(background="#d9d9d9")
        self.Scale4.configure(font="TkTextFont")
        self.Scale4.configure(foreground="#000000")
        self.Scale4.configure(highlightbackground="#d9d9d9")
        self.Scale4.configure(highlightcolor="black")
        self.Scale4.configure(orient="horizontal")
        self.Scale4.configure(tickinterval="100.0")
        self.Scale4.configure(troughcolor="#d9d9d9")
                              
        self.Quit = tk.Button(top, command=self.quitit)
        self.Quit.place(relx=0.005, rely=0.75, height=25, width=147)
        self.Quit.configure(background="#FF0000")
        self.Quit.configure(disabledforeground="#a3a3a3")
        self.Quit.configure(foreground="#000000")
        self.Quit.configure(highlightbackground="#d9d9d9")
        self.Quit.configure(highlightcolor="black")
        self.Quit.configure(pady="0")
        self.Quit.configure(takefocus="0")
        self.Quit.configure(text='''Quit''')
        
        self.plot()

    def quitit(self):
#        print(self.sample_t)
        root.quit()
        root.destroy()
        sys.exit("Script No Longer Running")
        
    def plot(self):
        if self.fig==None:
            self.fig=Figure()
        if self.ax==None:
            self.ax=self.fig.add_subplot(111)
        self.ax.cla()
        self.ax.plot(self.pb207_u235,self.pb206_u238, label='Concordia')
        for x,y,s in zip(self.t_labels_x,self.t_labels_y,self.t_labels_t):
            self.ax.text(x,y,s)
#        self.ax.scatter(grid_x,grid_y,s=50,marker='+',c='0',alpha=0.5,linewidth=1, label='Grid Locations')
#        self.preview_ax.set_aspect(aspect='equal')
        self.ax.set_title('Effect of Pb207 and Pb206 Fractionation on Concordia Plot')
        self.ax.set_ylabel(r'$\frac{{}^{206}Pb}{{}^{238}U}$', fontsize=16)
        self.ax.set_xlabel(r'$\frac{{}^{207}Pb}{{}^{235}U}$', fontsize=16)
        
        
        pb76=((1/u238_u235)*(np.e**(lambda75*self.sample_t)-1))/(np.e**(lambda68*self.sample_t)-1)
        u238_sample_est=int(np.around((1/238)*(10**-9)*avagadro,0))*10
        u238_sample=np.array([0.01,0.0125, 0.0175,0.025,0.05,0.1,0.2,0.5,1, 10])*u238_sample_est
        pb206_sample=u238_sample*(np.e**(lambda68*self.sample_t)-1)
        pb207_sample=pb206_sample*pb76
        u235_sample=pb207_sample/(np.e**(lambda75*self.sample_t)-1)
#        print(pb76)
        pb206_sample+=-min(pb206_sample)*self.max_discordance
        pb207_sample=pb206_sample*pb76
        
        
        
        
        pb206_u238_sample=pb206_sample/u238_sample
        pb207_u235_sample=pb207_sample/u235_sample
        
        t238=np.log(pb206_u238_sample+1)/lambda68
        discordance=t238/self.sample_t*100-100
        
        
        
        pb206_test=(1-self.extra_206_loss)*pb206_sample
        pb207_test=(1-self.extra_207_loss)*pb207_sample
        pb206_u238_test=pb206_test/u238_sample
        pb207_u235_test=pb207_test/u235_sample
        
        #test_207_206=pb207_test/pb206_test
        
        
        new_76_age=pb207_test[0]/pb206_test[0]
        
        def age_76(new_76_age):
            t_test=1000
            i=0
            #global diff
            diff=100
            while np.abs(diff)>0.01 and i<2000:
                i+=1
                pb76_test=((1/u238_u235)*(np.e**(lambda75*t_test)-1))/(np.e**(lambda68*t_test)-1)
                diff=new_76_age-pb76_test
                if diff >0:
                    t_test+=100000000
                if diff <0:
                    t_test+=-100000000
        #        print ('{}. {}'.format(i,diff))
        #    print (diff)
            while np.abs(diff)>0.0001 and i<2000:
                i+=1
                pb76_test=((1/u238_u235)*(np.e**(lambda75*t_test)-1))/(np.e**(lambda68*t_test)-1)
                diff=new_76_age-pb76_test
                if diff >0:
                    t_test+=1000000
                if diff <0:
                    t_test+=-1000000
        #        print ('{}. {}'.format(i,diff))
            while np.abs(diff)>0.000001 and i<2000:
                i+=1
                pb76_test=((1/u238_u235)*(np.e**(lambda75*t_test)-1))/(np.e**(lambda68*t_test)-1)
                diff=new_76_age-pb76_test
                if diff >0:
                    t_test+=10000
                if diff <0:
                    t_test+=-10000
        #        print ('{}. {}'.format(i,diff))
            while np.abs(diff)>0.0000001 and i<2000:
                i+=1
                pb76_test=((1/u238_u235)*(np.e**(lambda75*t_test)-1))/(np.e**(lambda68*t_test)-1)
                diff=new_76_age-pb76_test
                if diff >0:
                    t_test+=1000
                if diff <0:
                    t_test+=-1000
        #        print ('{}. {}'.format(i,diff))
            return (t_test)
                
    
        self.ax.scatter(pb207_u235_sample,pb206_u238_sample, label='Normal Discordance', c='g',alpha=0.5) 
        self.ax.scatter(pb207_u235_test,pb206_u238_test, label='Fractionated Discordance',c='purple',alpha=0.5) 
        self.ax.text(80,0.55, 'Sample 7/6 Age={:.3f} Ga'.format(int(self.sample_t)/10**9))
        self.ax.text(80,0.5, 'Observed 7/6 Age={:.3f} Ga'.format(age_76(new_76_age)/10**9))
        self.ax.legend(loc=4)
#        self.ax.text()
        
        if self.fig_canvas==None:
            self.fig_canvas =  FigureCanvasTkAgg(self.fig, master=self.Canvas1)        
        self.fig_canvas.get_tk_widget().pack()
        
        self.fig_canvas.draw()
        
        if self.toolbar==None:
            self.toolbar=tkagg.NavigationToolbar2Tk(self.fig_canvas, self.frame)
        self.toolbar.update()
        self.frame.place(relx=0.22, rely=0.08, relheight=0.05
                , relwidth=0.75)
        self.fig_canvas.get_tk_widget().pack(fill="both", expand=True)
        
        
        
        

    def sample_age(self,val):
        self.sample_t=int(val)*10**6
        self.plot()
#        print(self.sample_t)

    def max_disc(self,val):
        self.max_discordance=int(val)/100
        self.plot()
#        print(self.max_discordance)

    def scale_207(self,val):
        self.extra_207_loss=int(val)/100
        self.plot()
#        print(self.extra_207_loss)

    def scale_206(self,val):
        self.extra_206_loss=int(val)/100
        self.plot()
#        print(self.extra_206_loss)
        
    
                              

if __name__ == '__main__':
    vp_start_gui()





