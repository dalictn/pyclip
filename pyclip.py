import os
import socket
import sys
import pyperclip
import typer
from typing import Optional
from typing_extensions import Annotated


def main(ip: Annotated[Optional[str], typer.Argument()] = None, port: Annotated[Optional[int], typer.Argument()] = None):
    
    
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



    #create server function
    def CreateServer():


        #default port
        ip = ''
        port = 11223





        try:
        # With the help of bind() function 
        # binding ip and port
            soc.bind((ip, port))
        
        except socket.error as message:
            
            # if any error occurs then with the 
            # help of sys.exit() exit from the program
            print('[?] Bind failed. Error Code : '
                + str(message[0]) + ' Message '
                + message[1])
            sys.exit()
            

        print("[!] clipboard created. Now listening for connections on port: " + str(port))

        soc.listen(9)
        
        
        conn, address = soc.accept()
        print("[!] "+ address[0] + " connected")


                    
        # send a thank you message to the client. encoding to send byte type. 
        conn.send('Clippy!'.encode()) 
        
        return conn

    def ConnectToServer(ip, port):
        soc.connect(ip, port)





    def SendText(conn):

        while True:
            conn.send(pyperclip.waitForNewPaste())


    
    if ip == None:
        CreateServer()
    else:
        ConnectToServer(ip, port)

    







if __name__ == "__main__":
    typer.run(main)