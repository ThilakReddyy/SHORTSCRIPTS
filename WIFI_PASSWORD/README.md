# Wi-Fi Password Retrieval Script

This Python script allows you to retrieve Wi-Fi network names and their associated passwords on a Windows system using the `netsh` command-line utility.

## Prerequisites

- This script is designed to work on a Windows operating system.
- Python 3.x should be installed on your system.

## Usage

1. Clone this repository or download the script to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory where the script is located.

4. Run the script using Python:
   ```python wifipassword.py```

5. The script will execute and display a list of Wi-Fi network names (SSIDs) along with their respective passwords (if available).

## How It Works

The script performs the following steps:

1. It uses the `subprocess` module to run the `netsh` commands needed to retrieve Wi-Fi information.

2. First, it fetches a list of available Wi-Fi network names (profiles) using the `netsh wlan show profiles` command.

3. It then parses the output to extract the network names.

4. For each network name, it runs `netsh wlan show profile name="NETWORK_NAME" key=clear` to retrieve the password (if available).

5. The script prints out the network name and password, if found.

## Note

- Running this script may require administrative privileges, as the `netsh` utility often requires elevated access to retrieve Wi-Fi passwords.

- Make sure to use this script responsibly and only on networks that you have permission to access. Unauthorized access to Wi-Fi networks is illegal and unethical.
