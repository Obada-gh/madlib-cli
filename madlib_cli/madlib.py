def welcome():
    
    return('Welcome to my game I hope you doing will,you need to input things to make the game work :)')

def read_template(path):
    '''
    to read the .txt files in assets folder.
    '''
    try:
        with open(path) as file:
         return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError('I can not find the file man')
    except Exception as a:
        return(f'Error {a}')
    

import re

def parse_template(myText):
    words = re.findall('{(.*?)}',myText)
    newText= re.sub('{.*?}','{}',myText)
    
    return newText,tuple(words)


def  merge(text,tubl):
    '''
    to replace {} with the user input
    '''
    formatedText=text.format(*tubl)
    return formatedText


def userInput(tubl):
    arr=[]
    for i in tubl:
        userIn=input(f'please enter {i} ')
        arr.append(userIn)
    
    return arr


if __name__ == '__main__':

   welcome()
   read=read_template('assets/game.txt')
   newtext,tubl=parse_template(read)
   userAns=userInput(tubl)
   print(merge(newtext,userAns))

   
  
   





