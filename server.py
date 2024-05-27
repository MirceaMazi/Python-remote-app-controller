import socket
import subprocess
import threading

firefox_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
word_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
notepad_path = 'notepad.exe' 

applications = {
    'firefox': {
        'start': f'start "" "{firefox_path}"',
        'stop': 'taskkill /IM firefox.exe /F',
        'restart': f'taskkill /IM firefox.exe /F && start "" "{firefox_path}"',
        'status': 'tasklist | findstr firefox.exe'
    },
    'word': {
        'start': f'start "" "{word_path}"',
        'stop': 'taskkill /IM WINWORD.EXE /F',
        'restart': f'taskkill /IM WINWORD.EXE /F && start "" "{word_path}"',
        'status': 'tasklist | findstr WINWORD.EXE'
    },
     'notepad': {
        'start': f'start "" "{notepad_path}"',
        'stop': 'taskkill /IM notepad.exe /F',
        'restart': f'taskkill /IM notepad.exe /F && start "" "{notepad_path}"',
        'status': 'tasklist | findstr notepad.exe'
    }
}

def handle_client(client_socket):
    try:
        while True:
            request = client_socket.recv(1024).decode('utf-8')
            if not request:
                break

            request_parts = request.split()
            command = request_parts[0]
            if command == 'list':
                response = '\n'.join(applications.keys())
            elif command == 'commands':
                app_name = request_parts[1]
                response = '\n'.join(applications[app_name].keys())
            elif command in ['start', 'stop', 'restart', 'status']:
                app_name = request_parts[1]
                if app_name in applications and command in applications[app_name]:
                    cmd = applications[app_name][command]
                    if command == 'restart':
                        subprocess.run(applications[app_name]['stop'], shell=True, capture_output=True, text=True)
                        result = subprocess.Popen(applications[app_name]['start'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    elif command == 'start':
                        result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    else:
                        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

                    if command == 'status':
                        response = 'Running' if result.returncode == 0 else 'Not running'
                    else:
                        if command in ['start', 'restart']:
                            response = 'Firefox started'
                        else:
                            response = result.stdout if result.returncode == 0 else result.stderr
                else:
                    response = 'Invalid application or command'
            else:
                response = 'Unknown command'

            client_socket.send(response.encode('utf-8'))
    finally:
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print('Server listening on port 9999')

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    start_server()
