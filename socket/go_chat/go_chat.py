if __name__ == "__main__":
    import os
    import sys
    IP, PORT = "", ""
    input_arguments = len(sys.argv)
    if input_arguments > 1:
        for i, arg in enumerate(sys.argv):
            if arg == "--server":
                try:
                    temp = sys.argv[i + 1].split(':')
                    IP, PORT = temp[0], temp[1]
                except IndexError:
                    print("No argument provided")
                else:
                    print(f"IP {IP}, PORT {PORT}")
                    os.system(
                        "gnome-terminal -e 'bash -c \"python3 go_chat_server.py {0} {1}; bash\" '".format(IP, PORT))
                    os.system(
                        "gnome-terminal -e 'bash -c \"python3 go_chat_client.py {0} {1}; bash\" '".format(IP, PORT))
                    os.system(
                        "gnome-terminal -e 'bash -c \"python3 go_chat_client.py {0} {1}; bash\" '".format(IP, PORT))
    else:
        print("Server argument no provided")

# s.connect((socket.gethostname(), 1243))

