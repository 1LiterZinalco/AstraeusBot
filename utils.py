import datetime

##############################################################################################################
### File handling ############################################################################################
##############################################################################################################

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

##############################################################################################################
### Permission system ########################################################################################
##############################################################################################################

def check_permission(executor):
    staff = [
        267633670532104193, # 1LiterZinalco
        274988761186566144 # Min3styl3r
    ]
    if executor in staff:
        return True
    else:
        return False

##############################################################################################################
### Logging ##################################################################################################
##############################################################################################################

# Checking if log file already exists and if not, creating one.
def checkfile(id):
    if(id == 0):
        # Regular log
        try:
            # File is already existing
            file_log = open("/var/www/html/bots/astraeus/" + str(datetime.date.today()) + ".md", "r")
            file_log.close()
        except:
            # File is not existing, creating Markdown head
            file_log = open("/var/www/html/bots/astraeus/" + str(datetime.date.today()) + ".md", "w")
            file_log.write("| Time | Channel | Content |\n| :------------- | :------------- | :------------- |\n")
            file_log.close()
    else:
        # Debug log
        try:
            # File is already existing
            file_log = open("/var/www/html/bots/astraeus/debug.md", "r")
            file_log.close()
        except:
            # File is not existing, creating Markdown head
            file_log = open("/var/www/html/bots/astraeus/debug.md", "w")
            file_log.write("| Datetime | Content |\n| :------------- | :------------- |\n")
            file_log.close()

#============================================================================================================#

# Removing formatting that makes the log look ugly
def format(content):
    content = content.replace("\r", " ")
    content = content.replace("\n", " ")
    return content

#============================================================================================================#

# Custom logging module. Because every other logging module seems to be crap.
def log(*args):
    if(len(args) == 1):
        # Logging without channel
        content = format(args[0]) # Removing formatting that makes the log look ugly
        print("{} | {}".format(str(datetime.datetime.now()), content))
        checkfile(0) # Checking if log file already exists and if not, creating one.
        # Writing to file
        file_log = open("/var/www/html/bots/astraeus/" + str(datetime.date.today()) + ".md", "a")
        #file_log.write("| " + str(datetime.datetime.now().time()) + " | | " + content + " |\n")
        file_log.write("| {} | | {} |\n".format(str(datetime.datetime.now().time()), content))
        file_log.close()
    elif(len(args) == 2):
        # Logging with channel
        if(args[0] != "DEBUG"):
            # Regular log
            content = format(args[1]) # Removing formatting that makes the log look ugly
            print("{} | {} | {}".format(str(datetime.datetime.now()), args[0], content))
            checkfile(0) # Checking if log file already exists and if not, creating one.
            # Writing to file
            file_log = open("/var/www/html/bots/astraeus/" + str(datetime.date.today()) + ".md", "a")
            #file_log.write("| " + str(datetime.datetime.now().time()) + " | " + args[0] + " | " + args[1] + " |\n")
            file_log.write("| {} | {} | {} |\n".format(str(datetime.datetime.now().time()), args[0], content))
            file_log.close()
        else:
            # Debug log
            content = format(args[1]) # Removing formatting that makes the log look ugly
            checkfile(1) # Checking if log file already exists and if not, creating one.
            # Writing to file
            file_log = open("/var/www/html/bots/astraeus/debug.md", "a")
            #file_log.write("| " + str(datetime.datetime.now()).replace(" ", "_") + " | " + args[1] + " |\n")
            file_log.write("| {} | {} |".format(str(datetime.datetime.now()).replace(" ", "_"), args[1]))
            file_log.close()
    else: # Logging Error
        print("There has been an error while logging.")
