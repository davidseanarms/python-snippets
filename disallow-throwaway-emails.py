## function as part of a larger user registration database script

def verify_email_service(email):
    #Temporary email service domains
    temp_domains = ["mailinator.com", "guerrillamail.com", "temp-mail.org", "dodgit.com"]
    #Split the email address into parts
    username, domain = email.split("@")
    #Check if the domain is one of the temporary services
    if domain in temp_domains:
        return False
    else:
        return True

#Example
print(verify_email_service("name@mailinator.com")) #False
print(verify_email_service("name@example.com")) #True
