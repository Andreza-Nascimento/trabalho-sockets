import socket
import threading

clientes = []

def main():
    
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # Protocolos IPv4 e TCP, respectivamente

    try:
        servidor.bind(('localhost', 2560))
        servidor.listen()                                             # É possível definir a quantidade de conexões
    except:
        return print('\nFalha no servidor')

    while True:
        cliente, endereco = servidor.accept()
        clientes.append(cliente)

        processo_clientes = threading.Thread(target=recebe_compartilha, args=[cliente])

def recebe_compartilha(cliente):                                                  # Receber e compartilhar mensagens
    while True:
        try:
            mensagem = cliente.recv(2048)
            compartilhamento(mensagem, cliente)
        except:
            remover_cliente(cliente)
            break

def compartilhamento(mensagem, cliente):                              # Broadcast
    for cliente_numero in clientes:
        if cliente_numero != cliente:
            try:
                cliente_numero.send(mensagem)
            except:
                remover_cliente(cliente_numero)

def remover_cliente(cliente):                                          # Remover cliente da lista do servidor
    clientes.remove(cliente)

main():