# task 3

def is_valid_email(email):

    if "@" in email and email[0] != "@" and email[-1] != "@":
        local_part, domain_part = email.split("@")

        if "." in domain_part and domain_part[0] != "." and domain_part[-1] != ".":
            return True
    
    return False

email = input("Enter an email to validate: ")

if is_valid_email(email):
    print(f"'{email}' is a valid email.")
else:
    print(f"'{email}' is not a valid email.")
