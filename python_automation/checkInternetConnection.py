import socket

def check_internet_connection():
    try:
        # Attempt to connect to a well-known host (in this case, Google's DNS server)
        socket.create_connection(("8.8.8.8", 53))
        print("Internet connection is available!")
        return True
    except socket.error:
        print("No internet connection!")
        return False

# Example usage
check_internet_connection()