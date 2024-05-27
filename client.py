import socket

def send_request(command):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))
    client.send(command.encode('utf-8'))
    
    response = client.recv(4096).decode('utf-8')
    client.close()
    return response

if __name__ == '__main__':
    while True:
        command = input('Enter command (list, commands <app>, start <app>, stop <app>, restart <app>, status <app>): ')
        if command in ['exit', 'quit']:
            break
        response = send_request(command)
        print(response)
