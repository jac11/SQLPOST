# SQLPOST_

**A Python script for automated SQL injection testing.**

SQLPOST is a powerful and flexible tool designed to simplify SQL injection testing in login forms. Built with Python and Selenium, it automates the process of injecting payloads and analyzing responses, making it an essential tool for penetration testers and security researchers.

With support for custom wordlists, advanced field targeting methods, real-time browser observation, and configurable delays to avoid detection, SQLPOST adapts seamlessly to diverse scenarios. Its comprehensive feature set, including error message handling, specific username and password testing, and continuous wordlist testing, ensures precision and thoroughness in identifying vulnerabilities.

The inclusion of the man flag further enhances usability, providing detailed documentation for all options. SQLPOST empowers users to uncover weaknesses in authentication systems effectively, helping to secure applications against potential threat

## Key Features:

*    Automated Testing: Streamlined testing of multiple SQL payloads against target URLs.
*    Versatile Input Handling: Supports various input field types (Name, CSS Selector, XPath, ID) for accurate targeting.
*    Flexible Customization: Customize username, password, error messages, and other parameters to tailor scans to specific targets.
*    User-Friendly Interface: Provides clear output, progress indicators, and informative messages.
*    Headless and Live Modes: Operate in headless mode for automated scans or with a visible browser window for manual inspection and debugging.
*    Cross-Platform Compatibility: Designed to work on various operating systems.

## Installation

  * Install Required Libraries:
```
    pip install selenium
```
  * Install geckodriver (for Firefox):
        Download the appropriate geckodriver executable for your operating system from the official website.
        Place the geckodriver executable in your system's PATH or in the same directory as this script.
--------------------------------------------------------------------------------------------------
## Usage
```
python sqlpost.py -U <target_url> -uf <username_field> -pf <password_field> 
```
* Command-Line Options:

| Option | Long Option | Description |
|---|---|---|
| --div |  |  Specify the path to the Firefox WebDriver executable. |
| -U | --url | Target URL of the login page. |
| -uf | --user_form | Name of the username input field. |
| -pf | --pass_form | Name of the password input field. |
| -w | --wordlist | File containing the list of SQL commands to test (default: 'sql'). |
| -e | --error | Error message to identify unsuccessful login attempts. |
| -uc | --UCSS | CSS selector for the username input field. |
| -pc | --PCSS | CSS selector for the password input field. |
| -ux | --UXpath | XPath for the username input field. |
| -px | --PXpath | XPath for the password input field. |
| -ui | --IDUSER | ID for the username input field. |
| -pi | --IDPASS | ID for the password input field. |
| -p | --password | Specific password to test. |
| -u | --username | Specific username to test. |
| -f | --userforce | Force a specific username into the wordlist. |
| -C | --Continue | Continue scanning through the entire wordlist. |
| -l | --live | Show the web browser window (disable headless mode). |
| -T | --time | Sleep duration between requests. |
| --man |  | Show this help message. |

Example Usage:
Bash

python sql_injector.py -U "https://example.com/login" -uf "username" -pf "password" -w "custom_payloads.txt"

This command will target the login page at https://example.com/login, use the input fields named "username" and "password," and utilize a custom wordlist of SQL payloads.
Here’s a reformatted version where all details are presented as examples for easier understanding:

---

### Examples of `sqlpost.py` Usage

1. **Basic Test with Default Wordlist:**
   ```bash
   sqlpost.py -U http://example.com/login -uf username -pf password
   ```
   *This tests a login page using the default wordlist to identify SQL injection vulnerabilities.*

2. **Test with Custom Wordlist and Field Names:**
   ```bash
   sqlpost.py -U http://example.com/login -w payloads.txt -uf username -pf password
   ```
   *This uses a specific wordlist (`payloads.txt`) and specifies the username and password fields by their `name` attributes.*

3. **Use XPath Selectors in Live Mode:**
   ```bash
   sqlpost.py -U http://example.com/login -ux "//input[@name='user']" -px "//input[@name='pass']" -l
   ```
   *This employs XPath selectors for the username and password fields and enables live mode to observe interactions.*

4. **Test with Custom Username, Password, and Delay:**
   ```bash
   sqlpost.py -U http://example.com/login -u admin -p secret -T 1
   ```
   *This tests using a specific username (`admin`), password (`secret`), and introduces a 1-second delay between requests.*

5. **Continue Testing Even After Success:**
   ```bash
   sqlpost.py -U http://example.com/login -w payloads.txt -C
   ```
   *This continues testing all SQL payloads from the wordlist, even after a successful login is found.*

6. **Test by Targeting Fields via CSS Selectors:**
   ```bash
   sqlpost.py -U http://example.com/login -uc .username-class -pc .password-class
   ```
   *This identifies input fields using CSS selectors for the username and password.*

7. **Target Fields Using ID Attributes:**
   ```bash
   sqlpost.py -U http://example.com/login -ui username-id -pi password-id
   ```
   *This targets input fields via their `id` attributes in the HTML.*

8. **Set Expected Page Length to Compare Responses:**
   ```bash
   sqlpost.py -U http://example.com/login -L 2000
   ```
   *This sets the expected page length to detect differences in responses caused by SQL injection attempts.*


9. **Replace Default Username in the Wordlist:**
    ```bash
    sqlpost.py -U http://example.com/login -f join
    ```
    *This replaces occurrences of the default `admin` username in the wordlist with `custom_user`.*

-------------------------------------------------
## Developer
* jac11devel@gmail.com
----------------------------------------------------
