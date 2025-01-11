#!/usr/bin/env python3


import os
import subprocess
class ManPage:
   def __init__(self):
       self.man_info()
   def man_info(self):
       try:
              INFO = """

SQLPOST(1)                                   

NAME
    sqlpost.py - SQL Injection Tester with Selenium

SYNOPSIS
    sqlpost.py-U URL [OPTIONS]

DESCRIPTION

       QL Injection Login Exploit is a Python-based tool crafted for testing SQL injection vulnerabilities specifically in login forms.
       Powered by Selenium, it automates the process of injecting a range of SQL payloads into username and password fields,
       exploiting common weak spots in web authentication systems. Using a custom wordlist,
       it targets the most popular attack vectors in login forms and detects any flaws in how the server handles SQL commands.
       The tool runs quietly in the background, testing various payloads against login fields through multiple input methods,
       including form-based username/password, CSS selectors, and XPath locators. Designed for penetration testers and security enthusiasts,
       it’s a fast and effective way to identify exploitable SQL injection vulnerabilities in login systems—without manual effort.


       usage: sql.py [-h] -U URL [-uf USER_FORM] [-pf PASS_FORM] [-w WORDLIST] [-e ERROR] [-uc UCSS] [-pc PCSS] [-ux UXPATH] [-px PXPATH] [-ui IDUSER] [-pi IDPASS] [-p PASSWORD]
              [-u USERNAME] [-f USERFORCE] [-C] [-L LENGTH] [-l] [-T TIME]

              SQL Injection Tester with Selenium

              options:
                -h,              --help                            show this help message and exit
                --man                                              show this man page
                -U URL,          --url URL                         Target URL of the login page
                -uf USER_FORM,   --user_form USER_FORM             Name of the username input field
                -pf PASS_FORM,   --pass_form PASS_FORM             Name of the password input field
                -w WORDLIST,     --wordlist WORDLIST               File containing the list of SQL commands to test
                -e ERROR,        --error ERROR                     Error message to identify unsuccessful login attempts
                -uc UCSS,        --UCSS UCSS                       CSS selector for the username input field
                -pc PCSS,        --PCSS PCSS                       CSS selector for the password input field
                -ux UXPATH,      --UXpath UXPATH                   XPath for the username input field
                -px PXPATH,      --PXpath PXPATH                   XPath for the password input field
                -ui IDUSER,      --IDUSER IDUSER                   ID for the username input field
                -pi IDPASS,      --IDPASS IDPASS                   ID for the password input field
                -p PASSWORD,     --password PASSWORD               Specific password to test
                -u USERNAME,     --username USERNAME               Specific username to test
                -f USERFORCE,    --userforce USERFORCE             Force a specific username into the wordlist
                -C,              --Continue                        Continue scanning through the entire wordlist
                -L LENGTH,       --Length LENGTH                   Set the expected page length to compare with the original page
                -l,              --live                            Show the web browser window (disable headless mode)
                -T TIME,         --time                            TIME Sleep duration between requests
                                                                             

OPTIONS
       --man  
            show this man page.
       -U, --url URL
            Target URL of the login page to test for SQL injection (required).

       -uf, --user_form FIELD_NAME
            The "name" attribute of the username input field in the HTML form. 
            Use this option if the username field is identified by its name attribute (optional).

       -pf, --pass_form FIELD_NAME
            The "name" attribute of the password input field in the HTML form.
            Use this option if the password field is identified by its name attribute (optional).

       -w, --wordlist FILE
            Specify a file containing a list of SQL payloads to test. 
            Each line in the file represents a separate SQL command to inject.
            Default wordlist: `sql` (optional).

       -e, --error MESSAGE
           Specify an error message to identify unsuccessful login attempts. 
           For example, 
           "Invalid username or password" helps determine whether a login attempt failed due to incorrect credentials (optional).

       -uc, --UCSS SELECTOR
            Provide a CSS selector to locate the username input field. 
            This is useful when the form uses CSS classes or IDs for field identification (optional).

       -pc, --PCSS SELECTOR
            Provide a CSS selector to locate the password input field. 
            Like the username field, 
            this is helpful for modern web applications with complex form structures (optional).

       -ux, --UXpath XPATH
            Specify the XPath for the username input field.
             XPath is useful for locating elements when the DOM structure is dynamic or lacks unique identifiers (optional).

       -px, --PXpath XPATH
            Specify the XPath for the password input field. 
            Similar to the username field, this option provides flexibility in locating form elements in complex HTML structures (optional).

       -ui, --IDUSER ID
            Specify the "ID" attribute of the username input field. This is commonly used when the username field has a unique ID attribute (optional).

       -pi, --IDPASS ID
            Specify the "ID" attribute of the password input field. 
            This is similar to the username field ID and ensures precise targeting of the password field (optional).

       -u, --username USERNAME
           Provide a specific username to test during the SQL injection attack. 
           This can be a known username or an entry from the wordlist (optional).

       -p, --password PASSWORD
           Provide a specific password to test during the SQL injection attack. 
           Useful for login forms requiring a fixed password with varying usernames (optional).

       -f, --userforce USERNAME
           Replace occurrences of "admin" in the wordlist with the specified username. 
           This allows for targeted testing with a customized username while using a generic wordlist (optional).

       -C, --Continue
           Continue testing all SQL payloads from the wordlist, 
           even after finding a successful login. 
           This option is helpful for identifying multiple vulnerabilities or bypass techniques (optional).

       -L, --Length LENGTH
           Set the expected page length to compare against the original page. 
           This helps detect differences in page responses, which can indicate a successful or unsuccessful injection (optional).

       -l, --live
           Run the tool in live mode, displaying the browser window instead of running in headless mode. 
           This allows real-time observation of form interactions and responses. Default: headless mode (optional).

       -T, --time SECONDS
           Pause for a specified number of seconds between requests. 
           This reduces the risk of detection by server-side monitoring systems and prevents overloading the target server (optional).

EXIT STATUS
    0   Successful execution.
    1   Error occurred during execution.

EXAMPLES
    Test a login page using default wordlist:
        sqlpost.py -U http://example.com/login

    Test with a specific wordlist and username field:
        sqlpost.py -U http://example.com/login -w payloads.txt -uf username -pf password

    Test with XPath selectors and display the browser:
        sqlpost.py -U http://example.com/login -ux "//input[@name='user']" -px "//input[@name='pass']" -l

    Use custom username and password with delay:
        sqlpost.py -U http://example.com/login -u admin -p secret -T 1

AUTHOR
    Written by [Your Name].

REPORTING BUGS
    Report bugs to <jac11devel@gmail.com>.

COPYRIGHT
    This is free software; you may redistribute it under the terms of the MIT License.

SEE ALSO
    selenium(1), python(1)

 """
              subprocess.run(['echo', INFO], text=True, check=True, stdout=subprocess.PIPE)
              subprocess.run(['more'], input=INFO, text=True)
       except KeyboardInterrupt:
              exit()              
if __name__=='__main__':
       ManPage()