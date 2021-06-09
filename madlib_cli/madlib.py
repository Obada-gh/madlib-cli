# print('Welcome to my game I hope you doing will,you need to input things to make the game work :)')

def read_template(path):
    '''
    to read the .txt files in assets folder.
    '''
    try:
        with open(path) as file:
           return file.read().strip()
    except FileNotFoundError:
        return('I can not find the file man')
    except Exception as a:
        return(f'Error {a}')
    

# print(read_template('assets/game.txt'))

myText = read_template('assets/game.txt')
import re
words = re.findall('{.*?}',myText)
newText= re.sub('{.*?}','{}',myText)
userArr=[]

def parse_template(arr):
    '''
    to take the user inputs.
    '''
    for i in arr :
        print(f'please enter {i}:')
        userInput = input()
        userArr.append(userInput)



def  merge(arr):
    '''
    to replace {} with the user input
    '''
    formatedText=newText.format(*arr)
    print(formatedText)

parse_template(words)  
merge(userArr)






# # Python3 program to demonstrate the
# # use of replace() method 
 
# string = "geeks for geeks geeks geeks geeks"
  
# # Prints the string by replacing all
# # geeks by Geeks
# print(string.replace("geeks", "Geeks"))
 
# # Prints the string by replacing only
# # 3 occurrence of Geeks 
# print(string.replace("geeks", "GeeksforGeeks", 3))


# print(f"""
# I the {Adjective} and {Adjective1} {First_Name1} have {Past_Tense_Verb}{First_Name2}'s {Adjective2} sister and plan to steal her {Adjective3} {Plural_Noun1}!

# What are a {Large_Animal} and backpacking {Small_Animal} to do? Before you can help {Girl_Name}, you'll have to collect the {Adjective4} {Plural_Noun2} and {Adjective5} {Plural_Noun3} that open up the {Number_one_fifty} worlds connected to A {First_Name3} Lair. There are {number1} {Plural_Noun4} and {number2} {Plural_Noun5} in the game, along with hundreds of other goodies for you to find.
# """)


# with open('../assets/spam.txt') as file:
#     print(file.read())

# with open('../assets/spam.txt') as file:
#     print(file.readlines())


###################################################

# def divide(a, b):
#     try:
#         a = float(a)
#         b = float(b)
#         print(f'The result of {a}/{b} is {a/b}')
#     except ValueError:
#         print('Data you entered are not numbers')
#     except ZeroDivisionError:
#         print('You cant divide by Zero dude')
#     except Exception as e:
#         print('Something went wrong! Check it out below: ')
#         print(e)
#     else:
#         print('All good!')
#     finally:
#         print('Thank you for using our app')

# def get_input_and_divide():
#     a = input('Enter first number: ')
#     b = input('Enter second number: ')
#     divide(a, b)


# if __name__ == '__main__':    
#     get_input_and_divide()






