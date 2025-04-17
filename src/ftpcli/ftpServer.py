from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

def main():
    # Create a directory for FTP files if it doesn't exist
    ftp_directory = "ftp_files"
    if not os.path.exists(ftp_directory):
        os.makedirs(ftp_directory)

    # Initialize the authorizer for managing users
    authorizer = DummyAuthorizer()

    # Add a user (username: user, password: password, directory: ftp_files)
    # Permissions: read (r), write (w), delete (d), list (l), make dir (m)
    authorizer.add_user("user", "password", ftp_directory, perm="elradfmw")

    # Set up the FTP handler
    handler = FTPHandler
    handler.authorizer = authorizer

    # Optional: Customize banner
    handler.banner = "Welcome to the Python FTP Server"

    # Define the server address and port
    address = ("127.0.0.1", 2121)  # localhost, port 2121
    server = FTPServer(address, handler)

    # Set a limit for connections
    server.max_cons = 256  # Maximum simultaneous connections
    server.max_cons_per_ip = 5  # Maximum connections per IP

    print(f"FTP server started on {address[0]}:{address[1]}")
    print(f"User: user, Password: password, Directory: {ftp_directory}")

    # Start the server
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the FTP server...")
        server.close_all()

if __name__ == "__main__":
    main()