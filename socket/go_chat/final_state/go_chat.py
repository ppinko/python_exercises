if __name__ == "__main__":

    import os
    import sys
    
    # check provided arguments
    IP, PORT = "", ""
    no_arguments = False
    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv):
            if arg == "--server":
                try:
                    temp = sys.argv[i + 1].split(':')
                    IP, PORT = temp[0], temp[1]
                except IndexError:
                    print("No argument provided")
    else:
        print("Server argument no provided")

    # when no arguments provided, set default IP and PORT
    if len(IP) == 0:
        # setting default IP
        IP = "127.0.0.1"
        no_arguments = True
    if len(PORT) == 0:
        # setting default PORT
        PORT = 1234
        no_arguments = True

    # open server window
    os.system("gnome-terminal -e 'bash -c \"python3 go_chat_server.py {0} {1}; bash\" '".format(IP, PORT))
    
    # open two clients' windows
    os.system("gnome-terminal -e 'bash -c \"python3 go_chat_client.py {0} {1} {2}; bash\" '".format(IP, PORT, no_arguments))
    os.system("gnome-terminal -e 'bash -c \"python3 go_chat_client.py {0} {1}; bash\" '".format(IP, PORT))

