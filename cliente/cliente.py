import socket
import threading

def main ():

    cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)                      # Protocolos IPv4 e TCP, respectivamente
    
    try:
        cliente.connect(('localhost', 2560))                                        # Tentativa de conexão com o servidor
    except:
        return print('\nFalha na conexão')

    usuario = input('Digite seu nome: ')
    print('\nVocê está conectado')

    # Para que as duas funções operem paralelamente de modo simultâneo
    processo_envia = threading.Thread(target=envia, args=[cliente, usuario])
    processo_recebe = threading.Thread(target=recebe, args=[cliente])

    processo_envia.start()
    processo_recebe.start()

def envia (cliente, usuario):                                                       # Função destinada para o envio de mensagens
    while True:
        try:
            mensagem = input('\n')
            cliente.send(f'<{usuario}> {mensagem}'.encode('utf-8')) 
        except:
            return

def recebe (cliente):                                                               # Função destinada para o recebimento de mensagens
    while True:
        try:
            mensagem = cliente.recv(2048).decode('utf-8')
            print(mensagem+'\n')
        except:
            print('\nErro na conexão')
            print('Pressione ENTER')
            cliente.close()
            break

main ()
