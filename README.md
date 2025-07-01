# Password Complexity Checker

A simple Python script to check the strength of your password and provide actionable suggestions for improvement. This tool uses regular expressions to verify that your password meets common security best practices.

## Features

- Checks for minimum length (9 characters)
- Requires at least one uppercase letter
- Requires at least one lowercase letter
- Requires at least one digit
- Requires at least one special character
- Provides clear feedback and suggestions for weak passwords

## How to Use

1. **Clone or download this repository.**
2. **Run the script in your terminal:**
    ```bash
    python password_checker.py
    ```
3. **Follow the prompt:**  
   Enter your password when asked.
4. **View the result:**  
   The script will tell you if your password is strong or suggest improvements.

## Example

```
Password Complexity Checker
Enter your password: MyPass123
Weak Password. Consider the following suggestions: 
Include atleast one special character.
```

```
Password Complexity Checker
Enter your password: MyStr0ng!Pass
Strong Password
```

## Requirements

- Python 3.x (no external dependencies)

## Customization

You can modify the password policy by editing the regular expressions or the minimum length in the `check_password_complexity` function.


**Protect your accounts with strong passwords!**
