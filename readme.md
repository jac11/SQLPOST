# SQLPOST_

**A Python script for automated SQL injection testing.**


SQLPOST_ is a Python-based tool designed to automate the process of SQL injection testing against web applications.
It leverages the Selenium library to interact with web browsers and efficiently test various SQL payloads on login forms.

**Features:**

- **Automated testing:** Efficiently tests multiple SQL payloads against login forms.
- **Configurable:** Supports various input field types (Name, CSS Selector, XPath, ID).
- **Flexible:** Allows for customization of username, password, and error messages.
- **User-friendly:** Provides clear output and progress indicators.
- **Headless mode:** Can be run in headless mode for automated scans.
- **Live mode:** Can be run with a visible browser window for manual inspection.


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
| -L | --Length | Set the expected page length to compare with the original page. |
| -l | --live | Show the web browser window (disable headless mode). |
| -T | --time | Sleep duration between requests. |
| --man |  | Show this help message. |

Example Usage:
Bash

python sql_injector.py -U "https://example.com/login" -uf "username" -pf "password" -w "custom_payloads.txt"

This command will target the login page at https://example.com/login, use the input fields named "username" and "password," and utilize a custom wordlist of SQL payloads.

