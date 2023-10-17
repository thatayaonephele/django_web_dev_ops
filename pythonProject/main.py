import socket, sys, tkinter
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    port = 12345
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a node
    s = socket.socket()
#    ip = socket.gethostbyname('www.google.com')
#    print(ip)

    s.bind(('', port))
    s.listen(20)
    while (True):
        c, addr = s.accept()
        print("Got a connection from %s", addr)
        c.send('Welcome to my client-server network'.encode())
        c.close()  #close the client-server network
        break  #end iteration & close program
    sys.exit()

     
#print(f"Server connection for ip address {ip} was successful")
# See PyCharm help at https://wwwprint(f"{str[:9]}\n");.jetbrains.com/help/pycharm/
