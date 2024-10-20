# Import necessary modules
import subprocess
import os
import validators
import sys
import time


# Main program entry point
def main():
    """
    The main entry point of the DNS Query Tool.
    
    This function is responsible for:
    1. Clearing the screen and printing a header.
    2. Asking the user if they want to install the required tools.
    3. If yes, updating the package list and installing the necessary tools.
    4. Passing control to the `main_input` function to get the initial URL input.
    
    Parameters:
    None
    
    Returns:
    None
    """
    clear_screen()
    print(" \n DNS Query Tool")
    print(" ----------------")
    v_install = str(input(" Do you wanna install the DNS query tools? (Y/N) ")).lower()
    if v_install == "y":
        subprocess.run(['sudo','apt-get', 'update'], check=True)
        check_install('dnsutils')
        check_install('curl')
        check_install('traceroute')
        check_install('whois')
        check_install('nmap')
    main_input()


# Function to get user input and perform a DNS query
def main_input():
    """
    Get user input (a URL), validate it, and pass it on to further processing.
    
    This function is responsible for getting the initial input from the user,
    validating it, and then passing it on to the `main_options` function for further handling.
    
    Parameters:
    None
    
    Returns:
    None
    """
    clear_screen()
    while True:      
        global url 
        while True:
            clear_screen()

            print(" \n DNS Query Tool")
            print(" ----------------")
            url = input(" Enter the URL to perform DNS query: ").strip()
            if url == "":
                clear_screen()
                sys.exit()
            try:
                subprocess.run(['host', url], check=True)
            except subprocess.CalledProcessError as e:
                if e.returncode > 0:
                    print("\n< Invalid URL! >")
                    time.sleep(2)
                    continue
               
            full_url = "https://"+url      
            if is_valid_url(full_url):
                break 

        main_options(url)


# Function to validate a URL using the validators module
def is_valid_url(url: str) -> bool:
    """
    Validate a URL using the validators.url function.
    
    This function takes a URL as input and returns True if it's valid, False otherwise.
    
    Parameters:
    url (str): The URL to be validated.
    
    Returns:
    bool: Whether the provided URL is valid or not.
    """
    return validators.url(url)


# Function to retrieve DNS records using a 'dig' query
def get_dns_records(url: str) -> subprocess.CompletedProcess:
    """
    Perform a 'dig' query on the provided URL to retrieve its DNS records.
    
    This function uses the 'dig' command-line tool with the '+short' option to return only the IP addresses.
    
    Parameters:
    url (str): The URL for which DNS records are to be retrieved.
    
    Returns:
    subprocess.CompletedProcess: The result of running the 'dig' query, containing the DNS records.
    """
    # Run the 'dig' command with the '+short' option and capture output
    return subprocess.run(['dig', '+short', url], capture_output=True, text=True)


# Main program loop
def main_options(url: str) -> None:
    while True:
        clear_screen()

        # Display available tools
        print(" Execute the specified command in a Linux terminal")
        print(" URL: ", url)
        print(" \n Available commands:\n")
        print(" 1 - nslookup")
        print(" 2 - host")
        print(" 3 - dig")
        print(" 4 - curl")
        print(" 5 - traceroute")
        print(" 6 - whois")
        print(" 7 - nmap")

        choice = input("\n Select a command to execute: ")
       
        if choice == "1":
            f_nslookup(url)
        elif choice == "2":
            f_host(url)
        elif choice == "3":
            f_dig(url)
        elif choice == "4":
            f_curl(url)          
        elif choice == "5":
            f_traceroute(url)
        elif choice == "6":
            f_whois(url)            
        elif choice == "7":
            f_nmap(url)
        else:
            return   

# Function to run nslookupo with user input
def f_nslookup(url: str) -> None:
    """
    Run the nslookup command with user input.
    
    This function repeatedly prompts the user for a command choice and attempts to run the corresponding nslookup command.
    
    Parameters:
    url (str): The URL to pass as an argument to the nslookup command.
    """    
    while True:
        clear_screen()
        print(" Execute the specified nslookup command")
        print("\n Available commands:\n")
        print(" 1 - Run a basic A record lookup.")
        print(" 2 - Run an A record lookup with the '-type=any' option.")
        print(" 3 - Run an NS record lookup with the '-type=ns' option.")
        print(" 4 - Run a PTR record lookup with the '-type=ptr' option.")
        print(" 5 - Run a MX record lookup with the '-type=mx' option.")
        print(" 6 - Run a SOA record lookup with the '-type=soa' option.")
        print(" 7 - Run a TXT record lookup with the '-type=txt' option.")

        choice = input("\n Select a command to execute: ")
        clear_screen()

        if choice == "1":
            subprocess.run(['nslookup', url])
        elif choice == "2":
            subprocess.run(['nslookup', '-type=any', url])
        elif choice == "3":
            subprocess.run(['nslookup', '-type=ns', url])
        elif choice == "4":
            subprocess.run(['nslookup', '-type=ptr', url])
        elif choice == "5":
            subprocess.run(['nslookup', '-type=mx', url])
        elif choice == "6":
            subprocess.run(['nslookup', '-type=soa', url])
        elif choice == "7":
            subprocess.run(['nslookup', '-type=txt', url])
        else:
            return
        input("\n < Press enter to continue... >")


# Function to run dig with user input
def f_dig(url: str) -> None:
    """
    Run the dig command with user input.
    
    This function repeatedly prompts the user for a command choice and attempts to run the corresponding dig command.
    
    Parameters:
    url (str): The URL to pass as an argument to the dig command.
    """     
    while True:
        clear_screen()
        print(" Execute the specified dig command")
        print("\n Available commands:\n")
        print(" 1 - Run a basic A record lookup.")
        print(" 2 - Run an A record lookup with the '+short' option.")
        print(" 3 - Run an NS record lookup with the '+ns' option.")
        print(" 4 - Run a PTR record lookup with the '+ip6.arpa' option.")
        print(" 5 - Run a MX record lookup with the '+mx' option.")
        print(" 6 - Run a SOA record lookup with the '+soa' option.")
        print(" 7 - Run a TXT record lookup with the '+txt' option.")

        choice = input("\n Select a command to execute: ")
        clear_screen()

        if choice == "1":
            subprocess.run(['dig', url])
        elif choice == "2":
            subprocess.run(['dig', '+short', url])
        elif choice == "3":
            subprocess.run(['dig', 'ns', url])
        elif choice == "4":
            subprocess.run(['dig', '@8.8.8.8', url, 'PTR'])
        elif choice == "5":
            subprocess.run(['dig', '@8.8.8.8', url, 'MX'])
        elif choice == "6":
            subprocess.run(['dig', '+short', url, 'SOA'])
        elif choice == "7":
            subprocess.run(['dig', '@8.8.8.8', url, 'TXT'])
        else:
            return
        input("\n < Press enter to continue... >")


# Function to run dig with user input
def f_host(url: str) -> None:
    """
    Run the host command with user input.
    
    This function repeatedly prompts the user for a command choice and attempts to run the corresponding host command.
    
    Parameters:
    url (str): The URL to pass as an argument to the host command.
    """      
    while True:
        clear_screen()
        print(" Execute the specified host command")
        print("\n Available commands:\n")
        print(" 1 - Run a basic A record lookup.")
        print(" 2 - Run an NS record lookup with the '-t ns' option.")
        print(" 3 - Run a PTR record lookup with the '-t cname' option.")
        print(" 4 - Run a MX record lookup with the '-t mx' option.")
        print(" 5 - Run a SOA record lookup with the '-t soa' option.")
        print(" 6 - Run a TXT record lookup with the '-t txt' option.")

        choice = input("\n Select a command to execute: ")
        clear_screen()

        if choice == "1":
            subprocess.run(['host', url])
        elif choice == "2":
            subprocess.run(['host', '-t', 'ns', url])
        elif choice == "3":
            subprocess.run(['host', '-t', 'cname', url])
        elif choice == "4":
            subprocess.run(['host', '-t', 'mx', url])
        elif choice == "5":
            subprocess.run(['host', '-t', 'soa', url])
        elif choice == "6":
            subprocess.run(['host', '-t', 'txt', url])
        else:
            return
        input("\n < Press enter to continue... >")


# Function to run curl with user input
def f_curl(url: str) -> None:
    """
    Run the curl command with user input.
    
    This function repeatedly prompts the user for a command choice and attempts to run the corresponding curl command.
    
    Parameters:
    url (str): The URL to pass as an argument to the curl command.
    """    
    while True:
        clear_screen()
        print(" Execute the specified curl command")
        print("\n Available commands:\n")
        print(" 1 - Run a basic HTTP request.")
        print(" 2 - Run an HTTP request with the '-X' option (custom method).")
        print(" 3 - Run a check Page HTTP Headers.")
        print(" 4 - Run a check use HTTP/2 Protocol.")
        print(" 5 - Run a check for only response header.")
        print(" 6 - Run a check request and response header.")
        print(" 7 - Run a check ignore any SSL certificate error.")

        choice = input("\n Select a command to execute: ")
        clear_screen()

        if choice == "1":
            subprocess.run(['curl', url])
        elif choice == "2":
            method = input("\nEnter the custom HTTP method (1-GET / 2-POST / 3-PUT / 4-DELETE): ")
            clear_screen()
            if method == "1":
                subprocess.run(['curl', '-X', 'GET', url])
            elif method == "2":
                subprocess.run(['curl', '-X', 'POST', url])
            elif method == "3":
                subprocess.run(['curl', '-X', 'PUT', url])
            elif method == "4":
                subprocess.run(['curl', '-X', 'DELETE', url])                                
            else:
                input("< Invalid choice... Press enter to continue... >")
                continue
        elif choice == "3":
            subprocess.run(['curl', '-I', f'https://{url}'])
        elif choice == "4":
            subprocess.run(['curl', '--http2', f'https://{url}'])
        elif choice == "5":
            subprocess.run(['curl', '--head', f'https://{url}'])
        elif choice == "6":
            subprocess.run(['curl', '-v', f'https://{url}'])            
        elif choice == "7":
            subprocess.run(['curl', '--insecure', url])
        else:
            return
        input("\n < Press enter to continue... >")


# Function to run traceroute with user input
def f_traceroute(url: str) -> None:
    """
    Run the traceroute command with user input.
    
    This function repeatedly prompts the user for a command choice and attempts to run the corresponding traceroute command.
    
    Parameters:
    url (str): The URL to pass as an argument to the traceroute command.
    """    
    while True:
        clear_screen()
        print(" Execute the specified traceroute command")
        print("\n Available commands:\n")
        print(" 1 - Run a basic traceroute.")
        print(" 2 - Run a traceroute with the '-T' option (TCP SYN).")
        print(" 3 - Run a traceroute with the '-n' option (numerical output).")
        print(" 4 - Run a traceroute with the '-d' option (decimal output).")
        print(" 5 - Run a traceroute with the '-p' option (ping trace).")
        print(" 6 - Run a traceroute with the '--tcp' option (TCP trace).")
        print(" 7 - Run a traceroute with the '-4' option (IPv4 only).")
        print(" 8 - Run a traceroute with the '-6' option (IPv6 only).")

        choice = input("\n Select a command to execute: ")
        clear_screen()

        if choice == "1":
            subprocess.run(['traceroute', url])
        elif choice == "2":
            subprocess.run(['sudo', 'traceroute', '-T', url])
        elif choice == "3":
            subprocess.run(['traceroute', '-n', url])
        elif choice == "4":
            subprocess.run(['traceroute', '-d', url])
        elif choice == "5":
            subprocess.run(['ping', '-c', '10', url])
        elif choice == "6":
            subprocess.run(['mtr', '--tcp', '--report', url])
        elif choice == "7":
            subprocess.run(['traceroute', '-4', url])
        elif choice == "8":
            subprocess.run(['traceroute', '-6', url])
        else:
            return
        input("\n < Press enter to continue... >")


# Function to run nmap with user input
def f_nmap(url: str) -> None:
    """
    Run the nmap command with user input.
    
    This function repeatedly prompts the user for a command choice and attempts to run the corresponding nmap command.
    
    Parameters:
    url (str): The URL to pass as an argument to the nmap command.
    """
    while True:
        clear_screen()
        print(" Execute the specified nmap command")
        print("\n Available commands:\n")
        print(" 1 - Run a basic nmap scan.")
        print(" 2 - Run an nmap scan with the '--script' option.")
        print(" 3 - Run an nmap scan with the '-sS' option (syn scan).")
        print(" 4 - Run an nmap scan with the '-sT' option (TCP connect scan).")
        print(" 5 - Run an nmap scan with the '-P0' option.")
        print(" 6 - Run an nmap scan with the '--traceroute' option.")
        print(" 7 - Run an nmap scan with the '--reason' option.")

        choice = input("\n Select a command to execute: ")
        clear_screen()

        if choice == "1":
            subprocess.run(['nmap', url])
        elif choice == "2":
            subprocess.run(['nmap', '--script', 'ntp-info', url])
        elif choice == "3":
            subprocess.run(['sudo', 'nmap', '-sS', url])
        elif choice == "4":
            subprocess.run(['nmap', '-sT', url])
        elif choice == "5":
            subprocess.run(['nmap', '-P0', url])
        elif choice == "6":
            subprocess.run(['sudo','nmap', '--traceroute', url])
        elif choice == "7":
            subprocess.run(['nmap', '--reason', url])
        else:
            return
        input("\n < Press enter to continue... >")


# Function to run whois with user input
def f_whois(url: str) -> None:
    """
    Run the whois command with user input.
    
    This function repeatedly prompts the user for a command choice and attempts to run the corresponding whois command.
    
    Parameters:
    url (str): The URL to pass as an argument to the whois command.
    """    
    while True:
        clear_screen()
        print(" Execute the specified whois command")
        print("\n Available commands:\n")
        print(" 1 - Run a basic whois query.")
        print(" 2 - Run a whois query with the '--server' option.")
        print(" 3 - Run a whois query with the '-h' option.")
        print(" 4 - Run a whois query with the '--timeout' option.")
        print(" 5 - Run a whois query with the '--retry' option.")

        choice = input("\n Select a command to execute: ")
        clear_screen()

        if choice == "1":
            subprocess.run(['whois', url])
        elif choice == "2":
            subprocess.run(['whois', '-h', 'whois.iana.org', url])
        elif choice == "3":
            subprocess.run(['whois', '-h', 'whois.arpa', url])
        elif choice == "4":
            subprocess.run(['whois', '--timeout=10', url])
        elif choice == "5":
            subprocess.run(['whois', '--retry=3', url])
        else:
            return
        input("\n < Press enter to continue... >")


# Function to clear the terminal screen
def clear_screen() ->None:
    """
    Clear the terminal screen.
    
    This function checks if the operating system is POSIX (i.e., Linux or macOS)
    and uses the 'clear' command accordingly. For Windows, it uses 'cls'.
    """ 
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


# Function to check and install required packages
def check_install(package: str) -> None:
    """
    Check if a package is installed, and install it if not.
    
    This function uses the 'apt policy' command to check if a package is already installed.
    If not, it attempts to install the package using 'sudo apt-get install'.
    
    Parameters:
    package (str): The name of the package to check or install.
    """    
    result = subprocess.run(['apt', 'policy', package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)
    if 'install ok installed' in result.stdout:
        print(f"{package} is already installed.")
    else:
        print(f"{package} is not installed. Installing...")
        subprocess.run(['sudo', 'apt-get', 'install', '-y', package], check=True)


if __name__ == "__main__":
    main()
