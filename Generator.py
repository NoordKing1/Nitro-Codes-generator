import os
import time
import random, string
os.system("cls")

SellectR = True

def Codes_Gen():

    pc_name = os.getlogin()
    SellectR = False
    print("")

    much = int(input("[*] How much nitro codes you want: "))

    os.system("cls")
    print("""
            
        ░██████╗████████╗██████╗░██╗██╗░░██╗███████╗░░░░░░░██████╗░███████╗███╗░░██╗
        ██╔════╝╚══██╔══╝██╔══██╗██║██║░██╔╝██╔════╝░░░░░░██╔════╝░██╔════╝████╗░██║
        ╚█████╗░░░░██║░░░██████╔╝██║█████═╝░█████╗░░█████╗██║░░██╗░█████╗░░██╔██╗██║
        ░╚═══██╗░░░██║░░░██╔══██╗██║██╔═██╗░██╔══╝░░╚════╝██║░░╚██╗██╔══╝░░██║╚████║
        ██████╔╝░░░██║░░░██║░░██║██║██║░╚██╗███████╗░░░░░░╚██████╔╝███████╗██║░╚███║
        ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚══════╝░░░░░░░╚═════╝░╚══════╝╚═╝░░╚══╝
                                                        Developer: Strike-XD,#0001                  
                                                        Github: https://github.com/NoordKing1
    
        [*] Starting Please wait !

    """)
    time.sleep(3)
    print("[*] Generating {} codes !".format(much))
    print("")
    saveas = os.getcwd()
    f = open(saveas+"\\codes.txt", "w+")
    for i in range(much):
        code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        print(code)
        f.write(code+"\n")
        print("")
def Sellectors():
    print("""
            
        ░██████╗████████╗██████╗░██╗██╗░░██╗███████╗░░░░░░░██████╗░███████╗███╗░░██╗
        ██╔════╝╚══██╔══╝██╔══██╗██║██║░██╔╝██╔════╝░░░░░░██╔════╝░██╔════╝████╗░██║
        ╚█████╗░░░░██║░░░██████╔╝██║█████═╝░█████╗░░█████╗██║░░██╗░█████╗░░██╔██╗██║
        ░╚═══██╗░░░██║░░░██╔══██╗██║██╔═██╗░██╔══╝░░╚════╝██║░░╚██╗██╔══╝░░██║╚████║
        ██████╔╝░░░██║░░░██║░░██║██║██║░╚██╗███████╗░░░░░░╚██████╔╝███████╗██║░╚███║
        ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚══════╝░░░░░░░╚═════╝░╚══════╝╚═╝░░╚══╝
                                                        Developer: Strike-XD,#0001                  
                                                        Github: https://github.com/NoordKing1
    
        [1] Codes Generator
        [2] Codes Checker (beta)

    """)
    while SellectR == True:
        cmd = input("Sellect: ")
        if cmd == "1":

            Codes_Gen()
        if cmd == "2":

            Codes_Check()

Sellectors()