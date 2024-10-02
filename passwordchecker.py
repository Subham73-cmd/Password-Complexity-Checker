import re
def check_password_complexity(password):
    length_criteria=len(password)>=9
    uppercase_criteria=bool(re.search(r'[A-Z]', password))
    lowercase_criteria=bool(re.search(r'[a-z]', password))
    number_criteria=bool(re.search(r'[0-9]', password))
    special_char_criteria=bool(re.search(r'[\W_]', password))
    if length_criteria and uppercase_criteria and lowercase_criteria and number_criteria and special_char_criteria:
        return "Strong Password"
    else:
        response="Weak Password. Consider the following suggestions: \n"
        if not length_criteria:
            response+="Ensure the password is atleast 9 characters long.\n"
        if not uppercase_criteria:
            response+="Include atleast one uppercase character.\n"
        if not number_criteria:
            response+="Include atleast one digit.\n"
        if not special_char_criteria:
            response+="Include atleast one special character.\n"
        return response
def main():
    print("Password Complexity Checker")
    password=input("Enter your password: ")
    result=check_password_complexity(password)
    print(result)
if __name__=="__main__":
    main()
    
