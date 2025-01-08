
# SQLPOST  - SQL Injection Tester

`SQLPOST ` is a Python-based tool designed to test SQL injection vulnerabilities on login pages. It leverages a list of SQL injection commands to attempt to bypass login forms and determine if the target is vulnerable to SQL injection attacks. It uses the `mechanize` library to interact with the web page and simulate user input.

## Features

- **SQL Injection Testing**: It attempts various SQL injection payloads using a list of predefined commands.
- **Customizable**: You can specify custom usernames, passwords, form fields, and error messages to test specific vulnerabilities.
- **Form Handling**: Supports POST and GET requests for custom login forms.
- **Error Handling**: Custom error messages can be used to detect login failures and potential vulnerabilities.
- **SSL Handling**: Supports SSL verification (or bypass) for secure connections.

## Requirements

- Python 3.x
- `mechanize` library
- `argparse` library
- `ssl` (for SSL connections)

To install the necessary libraries, run the following:

```bash
pip install mechanize
```

## Usage

### Command-line Arguments

This script requires several command-line arguments to function. Below is an overview of each option:

- `--URL` (Required): The target URL of the login page.
- `-c`, `--Code` (Optional): The file containing a list of SQL commands to try. If not provided, the default `sql` file will be used.
- `-fu`, `--UserForm` (Optional): The name of the HTML form's "username" field.
- `-FP`, `--PassForm` (Optional): The name of the HTML form's "password" field.
- `-E`, `--Error` (Optional): A specific error message to detect when login fails.
- `-pI`, `--PassInput` (Optional): Specify if the password field should be POSTed.
- `-uI`, `--UserInput` (Optional): Specify if the username field should be POSTed.
- `-N`, `--user` (Optional): A specific username to use for testing.
- `-P`, `--password` (Optional): A specific password to use for testing.

### Example Usage

```bash
python SQLPOST.py --URL http://example.com/login -c sql_commands.txt -fu username -FP password -E "Invalid credentials"
```

This example would test the target URL (`http://example.com/login`) using the SQL commands from `sql_commands.txt`. It specifies the form field names for the username (`username`) and password (`password`) and checks for the "Invalid credentials" error message to determine if login failed.

### SQL Injection Testing Flow

1. **Read Commands**: The script reads SQL commands from a file or default list.
2. **Make Request**: It sends POST requests to the login form with the username and password fields populated by the SQL commands.
3. **Check Response**: The script compares the response to the original login page to detect potential SQL injection success.
4. **Display Results**: If SQL injection succeeds, the script prints the login URL, status, and credentials. Otherwise, it reports the failure.

## Example Output

### Success:
```plaintext
[*] SQL Injection Command    : ' OR 1=1 --
[*] Login Page URL           : http://example.com/login
[*] Status                   : LOGIN
[+] username[username]      : admin
[+] password[password]      : password123
```

### Failure:
```plaintext
[*] SQL Injection Command    : ' OR 1=1 --
[*] Login Page URL           : http://example.com/login
[*] Status                   : NOT LOGIN
```

## Error Handling

- The script will attempt to detect login failures based on the specified error message.
- If no error message is provided, the tool will use the original page's content to determine whether login was successful.
- Errors such as connection issues or invalid URLs will cause the script to exit gracefully with a message.

## Troubleshooting

1. **Connection Issues**: Ensure the target URL is correct and reachable.
2. **Form Field Names**: If the tool fails to find the correct form fields (`username` and `password`), double-check the field names in the login page's HTML.
3. **SSL Errors**: If you encounter SSL verification issues, use the `ssl._create_unverified_context` option to bypass SSL verification.

## License

This tool is provided for educational and ethical penetration testing purposes only. Use it responsibly and with permission from the target website owner.
