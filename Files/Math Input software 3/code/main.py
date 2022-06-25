import txtopp as tp


def StrToLst(string):
    mylist = []
    for i in string:
        mylist.append(i)
        
    return mylist 



def ProcessText(value):
    
    try:
        

        namespath = 'C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Math Input software 3/files/unicode_chart/symbol_name.txt'
        codepath = 'C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Math Input software 3/files/unicode_chart/code.txt'

        
        names = tp.read_list(file=namespath, separator='\n')
        codes = tp.read_list(file=codepath, separator='\n')

        codedict = {}

        for i in range(len(names)):
            codedict[names[i]] = codes[i]

        valuelist = StrToLst(value)
        print(valuelist)
            
        valuelists = value.split(' ')
        for item in valuelists:
            if item in names:
                i = valuelists.index(item)
                valuelists.remove(item)
                valuelists.insert(i, codedict[item])

        newvalue = ''
        for item in valuelists:
            if valuelists.index(item) == len(valuelists)-1:
                newvalue = newvalue+item
            else:
                newvalue = newvalue+item+' '
            
        print(newvalue)
        return newvalue
    except:
        return ''
