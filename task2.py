import re

def is_valid_email(email):
    # Regex pattern for valid email: username@domain.com
    pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'
    #^ start,$ end,[\w\.-]-represents the username befor @ ,[a-zA-Z]{2,}- represents only letters with atleast two characters like com, org.
    
    if re.match(pattern, email):
        return True
    else:
        return False

# Test cases
print(is_valid_email("user@domain.com"))   #  True
print(is_valid_email("user@domain"))       # False
print(is_valid_email("john.doe@example.com1"))  # false
print(is_valid_email("user@work.com"))         # True
print(is_valid_email("userdomain.com"))    #  False
print(is_valid_email("user@.com"))   #False
