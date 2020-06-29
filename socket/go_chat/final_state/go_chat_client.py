if __name__ == "__main__":

    import sys
    import socket
    import select
    import errno
    import asyncio
    from aioconsole import ainput

    HEADER_LENGTH = 10

    IP = sys.argv[1]
    PORT = int(sys.argv[2])

    # Check whether chat client was opened without specifying IP and PORT
    # If yes, then print IP and PORT to console
    if len(sys.argv) == 4 and sys.argv[3] == "True":
        print("IP: {0}, PORT: {1}".format(IP, PORT))

    my_username = input("Username: ")

    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to a given ip and port
    client_socket.connect((IP, PORT))

    # Set connection to non-blocking state, so .recv() call won't block, just return some exception we'll handle
    client_socket.setblocking(False)

    # Prepare username and header and send them
    username = my_username.encode('utf-8')
    username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
    client_socket.send(username_header + username)


    async def send_message():
        while True:
            # Wait for user to input a message
            message = await ainput(f'{my_username} > ')
        
            # If message is not empty - send it
            if message:
                # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
                message = message.encode('utf-8')
                message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
                client_socket.send(message_header + message)


    async def received_messages():
        while True:
            await asyncio.sleep(30)
            try:
                # Now we want to loop over received messages (there might be more than one) and print them
                while True:
                    # Receive our "header" containing username length, it's size is defined and constant
                    username_header = client_socket.recv(HEADER_LENGTH)

                    # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
                    if not len(username_header):
                        print('Connection closed by the server')
                        sys.exit()

                    # Convert header to int value
                    username_length = int(username_header.decode('utf-8').strip())

                    # Receive and decode username
                    username = client_socket.recv(username_length).decode('utf-8')

                    # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
                    message_header = client_socket.recv(HEADER_LENGTH)
                    message_length = int(message_header.decode('utf-8').strip())
                    message = client_socket.recv(message_length).decode('utf-8')

                    # Print message
                    print(f'\n{username} > {message}')
                    send_message()

            except IOError as e:
                # This is normal on non blocking connections - when there are no incoming data error is going to be raised
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print('Reading error: {}'.format(str(e)))
                    sys.exit()

                # We just did not receive anything
                pass

            except Exception as e:
                # Any other exception - something happened, exit
                print('Reading error: '.format(str(e)))
                sys.exit()

    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(send_message())
        asyncio.ensure_future(received_messages())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()

