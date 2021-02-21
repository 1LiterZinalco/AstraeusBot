import datetime

# File handling
def file(mode, filename, *content):
    if(mode == "r"):
        file = open(filename,"r")
        file_content = file.read()
        file.close()
        return str(file_content)
    else:
        file = open(filename, mode)
        file.write(str(content[0]))
        file.close()

# Permission system
def check_permission(executor):
    staff = [
        267633670532104193, # 1LiterZinalco
        274988761186566144 # Min3styl3r
    ]
    if executor in staff:
        return True
    else:
        return False
