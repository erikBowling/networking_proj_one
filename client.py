# Name: Erik Bowling
# Date: September 29, 2023
# Class: 4100-002 Networking
# Assignment: Project 1

import sys, getopt, socket, os, re, datetime, logging

# Main function. This gets called at the bottom of this script. Starting point is below.

def main_client(server_ip: str, port: int, log_file: str) -> None:
    """
    @param server_ip: The ip address of the server listening for your connection
    @param port: The port the server is listening on for your connection
    @param log_file: The path to the local log file to write your output to.

    This function creates a tcp socket connection to the server and facilitates sending messages back and forth.
    """

    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    server_socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.info("Client starting. Attempting connection to server.")

    try:
        # Create the connection
        server_socket.connect((server_ip, port))
        server_socket.settimeout(10)
        logging.info(f"TCP connection established to {server_ip} on port {port}")

        print("This client sends a message to the server. ")
        
        # Get user input for message to send to server
        message: str = input("What message do you want to send to the server?: ")
        logging.info(f"Sending message '{message}' to server.")

        # Send message to server
        server_socket.send(message.encode())

        print("Sent message. Waiting for response...")
        from_server = server_socket.recv(4096)

        # Change response log based on return value from server. 
        if from_server.decode() == "":
            print("The server responded with nothing.")
            logging.info("No message recieved from the server.")
        else:
            print(f"Recieved: {from_server.decode()}")
            logging.info(f"Recieved: {from_server.decode()}")
            
    except Exception as e:
        print(f"Encountered error: {e}")
        logging.error(f"{e} for {server_ip} on port {port}")
        sys.exit(1)



###########################################################
#  Entry Point for script. Main function gets called below.
###########################################################


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

    # Validate server address
    if opt == "-s":
        if not re.match('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', arg):
            print("Invalid IP address")
            sys.exit(1)

        server_ip = arg

    # Validate port
    if opt == "-p":
        if not re.match('[0-9]+', arg) or int(arg) == 0:
            print("Invalid port")
            sys.exit(1) 
            
        port = int(arg)

    # Validate local log file
    if opt == "-l":
        if not os.path.exists(arg):
            # Create log file
            with open(arg, "w") as log_file:
                print(f"Created {arg} file.")
                log_file.write(f"{datetime.datetime.now()}")
        
        local_log_file = arg


# Calling the main function
main_client(server_ip, port, local_log_file)
