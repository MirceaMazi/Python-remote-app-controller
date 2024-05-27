# Remote Application Controller

A Python-based server-client system for remotely controlling applications such as Firefox, Microsoft Word, and Notepad. The server can execute commands to start, stop, restart, and check the status of these applications. The client connects to the server to send commands and receive the execution results.

## Features

- **Remote Control**: Start, stop, restart, and check the status of applications.
- **Applications Supported**: Any app, but you have to add the path and commands inside the dictionary present in the server.py file
- **Client-Server Architecture**: Simple and effective communication using sockets.

## Requirements

- Python 3.x
- Windows OS (for application paths and commands)

## Setup

### Server

1. Clone the repository.
    ```sh
    git clone https://github.com/yourusername/remote-application-controller.git
    cd remote-application-controller
    ```
2. Add any of the apps that you want to be able to remotely control.
3. Start the server.
    ```sh
    python server.py
    ```

### Client

1. Connect to the server using the client.
    ```sh
    python client.py
    ```

## Usage

### Commands

- **List Applications**
    ```
    list
    ```
    Lists all controllable applications.

- **List Commands for an Application**
    ```
    commands <application>
    ```
    Lists all available commands for the specified application (e.g., `commands firefox`).

- **Start an Application**
    ```
    start <application>
    ```
    Starts the specified application (e.g., `start notepad`).

- **Stop an Application**
    ```
    stop <application>
    ```
    Stops the specified application (e.g., `stop word`).

- **Restart an Application**
    ```
    restart <application>
    ```
    Restarts the specified application (e.g., `restart firefox`).

- **Check Application Status**
    ```
    status <application>
    ```
    Checks if the specified application is running (e.g., `status firefox`).

