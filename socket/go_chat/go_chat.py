if __name__ == "__main__":
    import os
    import sys
    import socket
    IP, PORT = "", ""
    input_arguments = len(sys.argv)
    print(input_arguments)
    if input_arguments > 1:
        for i, arg in enumerate(sys.argv):
            if arg == "--server":
                try:
                    temp = sys.argv[i + 1].split(':')
                    IP, PORT = temp[0], temp[1]
                except IndexError:
                    print("No argument provided")
    else:
        print("Server argument no provided")

    print("len IP: ", len(IP), " len PORT: ", len(PORT))
    if len(IP) == 0:
        # setting default IP
        # IP = socket.gethostname()
        IP = "127.0.0.1"
    if len(PORT) == 0:
        # setting default PORT
        PORT = 1234

    os.system("gnome-terminal -e 'bash -c \"python3 go_chat_server.py {0} {1}; bash\" '".format(IP, PORT))
    os.system("gnome-terminal -e 'bash -c \"python3 go_chat_client.py {0} {1}; bash\" '".format(IP, PORT))
    os.system("gnome-terminal -e 'bash -c \"python3 go_chat_client.py {0} {1}; bash\" '".format(IP, PORT))

# s.connect((socket.gethostname(), 1243))

