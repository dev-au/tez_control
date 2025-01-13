# Tez Control

Tez Control is a command-line tool that allows users to interact with and control remote servers, generate configuration files, and execute custom commands. It is designed to make server management and configuration setup simple and efficient.

## Features

- **Connect to Real Server**: Enter and interact with a remote server directly from your terminal.
- **Generate Configuration Files**: Automatically generate configuration files like `.service` and `nginx.conf` for your project.
- **Run Custom Commands**: Execute commands on the server as per your project needs.
  
## Installation

You can install `tez-control` via pip:

```bash
pip install tez-control
```

## Usage

### Entering the Real Server

Once you have `tez-control` installed, you can connect to a remote server with the following command:

```bash
tez sv
```

This will prompt you to enter your server's host, user, and password (configured in your settings). Once connected, you will have an interactive terminal where you can run shell commands on the server.

You can navigate directories, run commands, and even cancel a command with `Ctrl+C`. Type `exit` to disconnect from the server.

### Generate Configuration Files

You can generate required configuration files (like `.service` and `nginx.conf`) for your project by running:

```bash
tez ex
```
### Configuration File (`.tez`)

`tez-control` uses a `.tez` configuration file to store connection details and project settings. The default location for this file is your home directory (`~/.tez`). Below is an example of what the file should look like:

```ini
[server]
SERVER_HOST=1.1.1.1
SERVER_USER=root
SERVER_PASSWORD=1234
SERVER_PORT=22

[project]
PROJECT_PATH=/path/project

[commands]
restart=git pull && sudo systemctl restart my_project
view=dir
```

Make sure to adjust the values for your specific server and project configuration.

## Contributing

If you'd like to contribute to `tez-control`, feel free to fork the repository and create pull requests. We welcome improvements, bug fixes, and new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


### Key Sections Added:

- **Entering the Real Server**: Describes how users can use the `tez sv` command to connect to a remote server interactively.
- **.tez Configuration File**: Generate example with `tez ex`
  
This `README.md` should help guide users in installing, configuring, and using `tez-control` effectively.

Let me know if you'd like further adjustments!