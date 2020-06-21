if __name__ == "__main__":
    import os
    import sys
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
    else:
        print("Server argument no provided")

    os.system("gnome-terminal -e 'bash -c \"python3 go_chat_server.py; bash\" '")
    os.system("gnome-terminal -e 'bash -c \"python3 go_chat_client.py; bash\" '")
    os.system("gnome-terminal -e 'bash -c \"python3 go_chat_client.py; bash\" '")


