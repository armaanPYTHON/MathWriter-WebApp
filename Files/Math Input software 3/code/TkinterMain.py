from tkinter import *
import main

def MainTkinter():
    
    themecolor1 = '#212120'
    
    
    root = Tk()
    root.title('Math Input Software')
    root.geometry('800x600')
    root.config(bg=themecolor1)
    
    
    #Designs
    InputDesign = {
        'bd':0
    }
    
    
    textinput = Text(root, InputDesign)
    textinput.place(relheight=0.9, relwidth=0.6, relx=0.3, rely=0.1)
    
    
    def ConvertToCode(e=None):
        value = textinput.get('1.0', END)
        value = value.strip('\n')
        textinput.delete('1.0', END)
        
        output = main.ProcessText(value)
        textinput.insert('1.0', output)
    
    
    textinput.bind('<Return>', ConvertToCode)
    
    
    mainloop()

MainTkinter()