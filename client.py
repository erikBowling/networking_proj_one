# Name: Erik Bowling
# Date: September 29, 2023
# Class: 4100-002 Networking
# Assignment: Project 1

import sys, getopt, socket, threading, os, re, datetime

def main():

    pass

# validate user Input
# Call main


# Checking for valid inputs
for flag in ["-s", "-p", "-l"]:
    if flag not in sys.argv:
        print("Invalid input arguments. client.py -s <SERVER_IP> -p <PORT> -l <LOCAL_LOG_FILE>")
        sys.exit(1)

# Parsing the command line arguments by flag
opts, args = getopt.getopt(sys.argv[1:], "s:p:l:")

server_ip: str = ""
port: int = 0
local_log_file: str = ""

# Validate command line arguments
for opt, arg in opts:
    if opt == "-s":
        if not re.match('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', arg):
            print("Invalid IP address")
            sys.exit(1)

        server_ip = arg

    if opt == "-p":
        if not re.match('[0-9]+', arg) or int(arg) == 0:
            print("Invalid port")
            sys.exit(1) 
            
        port = int(arg)

    if opt == "-l":
        if not os.path.exists(arg):
            # Create log file
            with open(arg, "w") as log_file:
                print(f"Created {arg} file.")
                log_file.write(datetime.now())
        
        local_log_file = arg





# test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# test.connect(("34.41.65.177", 8001))
