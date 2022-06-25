import code
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
import main
import txtopp as tp

Builder.load_file('MainKivy.kv')

savelocation = tp.read_string(file='C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Math Input software 3/files/savelocation.txt')


namespath = 'C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Math Input software 3/files/unicode_chart/symbol_name.txt'
codepath = 'C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Math Input software 3/files/unicode_chart/code.txt'
codevaluez = namespath + 'external'



print(codevaluez)

class InputLayout(FloatLayout):
    
    pass
    

class MIS(App):
    def build(self):
        try:
            return InputLayout()
        except:
            print("--------None----------")
            
            
    def getinput(self):
        value = self.root.ids.textinput.text
        self.root.ids.textinput.text = main.ProcessText(value)
        
    
    def AddSymbol(self):
        symbolname = self.root.ids.symbolnamein.text
        symbol = self.root.ids.symbolin.text
        
        print(symbolname, symbol)
        
        self.root.ids.symbolnamein.text = 'Add Symbol Name'
        self.root.ids.symbolin.text = 'Add Symbol'
        
        tp.add_object(file=namespath, object=symbolname, separator='\n')
        tp.add_object(file=codepath, object=symbol, separator='\n')
        
                
        

if __name__=='__main__':
    MIS().run()