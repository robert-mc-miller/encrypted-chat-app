import socket, rsa


s = socket.socket()
class PublicKey:
    def __init__(self, n, e):
        self.n = n
        self.e = e


def host(username):
    #Allowing connection and generating keys
    print("Generating encryption keys...")
    pubKey, privKey = rsa.newkeys(1024)
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)
    print("Hosting - IP: " + IPAddr)
    port = 8080
    s.bind(('', port))
    s.listen(5)
    c, addr = s.accept()

    #Transferring keys
    c.send(str(pubKey.n).encode('utf8'))
    c.send(str(pubKey.e).encode('utf8'))
    n = int(c.recv(4096).decode('utf8'))
    e = int(c.recv(4096).decode('utf8'))
    encKey = PublicKey(n, e)

    #Sending Messages
    while True:
        data = rsa.decrypt(c.recv(4096), privKey).decode('utf8')
        print(data)
        data = input('You: ')
        if data.lower() == 'close':
            data = (username + ' (host) closed connection.').encode('utf8')
            c.send(rsa.encrypt(data, encKey))
            c.close()
            break
        else:
            data = (username + ': ' + data).encode('utf8')
            c.send(rsa.encrypt(data, encKey))
        

def guest(username):
    #Atempting connection and generating keys
    print("Generating encryption keys...")
    pubKey, privKey = rsa.newkeys(1024)
    ip = input("Hosting IP address\n>>> ")
    s.connect((ip, 8080))

    #Trasferring Keys
    n = int(s.recv(4096).decode('utf8'))
    e = int(s.recv(4096).decode('utf8'))
    encKey = PublicKey(n, e)
    s.send(str(pubKey.n).encode('utf8'))
    s.send(str(pubKey.e).encode('utf8'))
    
    #Sending Messages
    while True:
        data = input('You: ')
        if data.lower() == 'leave':
            data = (username + ' left.').encode('utf8')
            s.send(rsa.encrypt(data, encKey))
            s.close()
            break
        else:
            data = (username + ': ' + data).encode('utf8')
            s.send((rsa.encrypt(data, encKey)))
        print(rsa.decrypt(s.recv(4096), privKey).decode('utf8'))


def main():
    role = input('[Host or Guest]\n>>> ')
    while role.lower() != 'host' and role.lower() != 'guest':
        role = input('Please re-enter (HOST or GUEST)\n>>> ')
    if role.lower() == 'host':
        host(input('Enter your desired username\n>>> '))
    else:
        guest(input('Enter your desired username\n>>> '))

main()
        
