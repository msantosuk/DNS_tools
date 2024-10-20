# DNS Query Tool

## Description
This is a simple Python-based tool designed to perform DNS queries on a provided URL. It can also install several essential networking utilities (`dnsutils`, `curl`, `traceroute`, `whois`, and `nmap`) on Ubuntu.

## Features
- Performs DNS lookups for a user-specified URL using the `host` command.
- Optionally installs networking tools required for DNS lookups and network diagnostics.
- Provides an interactive command-line interface.

## Requirements
- **Python 3** (Tested on Python 3.12)
- **Ubuntu** (Tested on Ubuntu)

### Dependencies
The script will prompt the user to install the following utilities if they are not already installed:

- `dnsutils`
- `curl`
- `traceroute`
- `whois`
- `nmap`

## Installation
Clone this repository and navigate to the script directory:

```bash
git clone <repository-url>
cd <repository-directory>
```

Ensure the script is executable:

```bash
chmod +x dns_tool.py
```

## Usage

Run the script with:

```bash
python3 dns_tool.py
```

Upon launching, the tool will prompt you with the following options:

- **Install DNS query tools**: The script will ask if you want to install the necessary utilities (`dnsutils`, `curl`, `traceroute`, `whois`, and `nmap`).
- **Perform DNS query**: Enter a URL to perform a DNS lookup using the `host` command.

### Example

1. After running the script, you will see an option to install necessary tools:
    ```plaintext
     DNS Query Tool
     ----------------
     Do you wanna install the DNS query tools? (Y/N)
    ```

2. Once the tools are installed, you can enter a URL to perform a DNS query:
    ```plaintext
     DNS Query Tool
     ----------------
     Enter the URL to perform DNS query: example.com
    ```

3. The script will display the DNS results and offer options for more queries or to exit.

## License
This project is free to use and modify by anyone.
