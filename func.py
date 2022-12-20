
FIlEPATH="cred.txt"

def get_cred(filepath=FIlEPATH):
    with open(filepath,'r') as file:
        creds=file.readlines()
    return creds

def write_cred(creds,filepath=FIlEPATH):
    with open(filepath,'w') as file:
        file.writelines(creds)

# print(__name__)