import time
import _thread

clk = 0
s = bytearray([0x91, 0x87, 0xEE, 0xEC, 0x2C, 0x25, 0x21, 0x0E, 0x1B, 0xA5, 0xC0, 0x9C, 0x2E, 0x42, 0xFD, 0xBF, 0x93, 0x96, 0xC1, 0xCE, 0xC6, 0xDF])
t = bytearray([0x74, 0x5A, 0x1B, 0x67, 0xde, 0x34, 0xf6, 0x34, 0x67, 0x5A, 0x8B, 0x74, 0x5A, 0x1B, 0x67, 0xDE, 0x34, 0xF6, 0x34, 0x67, 0x5A, 0x8B, 0x31, 0x3B, 0x36, 0x30, 0x2C, 0x03, 0x3F, 0x66, 0x24, 0x08, 0x66, 0x24, 0x08, 0x39, 0x67, 0x23, 0x08, 0x24, 0x36, 0x39, 0x64, 0x2A])
j = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

def banner():
    print(" _____ ___________   _____            ___      _           _         _____  _____  __   _____  ");
    print("/  __ \_   _|  ___| /  ___|          / _ \    | |         (_)       / __  \|  _  |/  | |  _  |");
    print("| /  \/ | | | |_    \ `--.  ___  ___/ /_\ \ __| |_ __ ___  _ _ __   `' / /'| |/' |`| |  \ V / ");
    print("| |     | | |  _|    `--. \/ _ \/ __|  _  |/ _` | '_ ` _ \| | '_ \    / /  |  /| | | |  / _ \ ");
    print("| \__/\ | | | |     /\__/ /  __/ (__| | | | (_| | | | | | | | | | | ./ /___\ |_/ /_| |_| |_| |");
    print(" \____/ \_/ \_|     \____/ \___|\___\_| |_/\__,_|_| |_| |_|_|_| |_| \_____/ \___/ \___/\_____/");
    print("\n \t\t\t\t\t\t\t\t\tBY @CS3GROUP ");

def ticker():
    global clk
    while True:
        time.sleep(1)
        clk += 1

def tr1(msg, debug):
    i = 0
    while(i < len(msg)):
        if debug:
            print("tr1  j[{}] = 22 ^ {} = {}".format(i, ord(msg[i]), len(msg) ^ ord(msg[i])))
        j[i] = len(msg) ^ ord(msg[i])
        time.sleep(0.2)
        i += 1

def tr2(msg, debug):
    i = 0
    global clk
    while(i < len(msg)):
        time.sleep(0.4)
        j[i] ^= t[clk*2] ^ ord("\x80")
        if debug:
            print("tr2  j[{}] ^= t[{}] ^ {} = {}".format(i, clk*2, ord("\x80"), j[i]))
            print("t[{}] = {}".format(clk*2, hex(t[clk*2],)))
        i += 1

def crack():
    t_values = bytearray([0x74, 0x74, 0x1b, 0x1b, 0xde, 0xde, 0xde, 0xf6, 0xf6, 0x67, 0x67, 0x67, 0x8b, 0x8b, 0x5a, 0x5a, 0x5a, 0x67, 0x67, 0x34, 0x34, 0x34])
    flag = ''
    res = None
    for i in range(22):
        for k in range(1, 255):
            res = 22 ^ k ^ t_values[i] ^ ord("\x80")
            if s[i] == res:
                flag += chr(k)
                break
    print(flag)

def main(debug = False):
    banner()
    msg = input("Introduce tu flag y comprueba si es la correcta: ")
    #msg = "secadmin{xxxxxxxxxxxx}"
    _thread.start_new_thread(ticker, ())
    _thread.start_new_thread(tr1, (msg, debug,))
    _thread.start_new_thread(tr2, (msg, debug,))
    time.sleep(13)

    if (s == j):
        print("la flag es: {}\n Enhorabuena !!! \n".format(msg))
    else:
        print("Me parece que te faltan unas cruzcampo")
        crack()

main(False)
