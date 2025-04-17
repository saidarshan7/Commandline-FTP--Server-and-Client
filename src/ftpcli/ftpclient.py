import ftplib
import os

class FTPClient:
    def __init__(self, host, username, password, port=21):
        self.ftp = ftplib.FTP()
        self.host = host
        self.username = username
        self.password = password
        self.port = port

    def connect(self):
        """Connect to the FTP server."""
        try:
            self.ftp.connect(self.host, self.port)
            self.ftp.login(self.username, self.password)
            print(f"Connected to {self.host} as {self.username}")
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False

    def disconnect(self):
        """Disconnect from the FTP server."""
        try:
            self.ftp.quit()
            print("Disconnected from server")
        except Exception as e:
            print(f"Disconnect failed: {e}")

    def list_files(self):
        """List files in the current directory."""
        try:
            files = self.ftp.nlst()
            print("Files in current directory:")
            for file in files:
                print(file)
            return files
        except Exception as e:
            print(f"Error listing files: {e}")
            return []

    def change_directory(self, directory):
        """Change to the specified directory."""
        try:
            self.ftp.cwd(directory)
            print(f"Changed directory to {directory}")
            return True
        except Exception as e:
            print(f"Failed to change directory: {e}")
            return False

    def upload_file(self, local_path, remote_path):
        """Upload a file to the FTP server."""
        try:
            with open(local_path, 'rb') as file:
                self.ftp.storbinary(f'STOR {remote_path}', file)
            print(f"Uploaded {local_path} to {remote_path}")
            return True
        except Exception as e:
            print(f"Upload failed: {e}")
            return False

    def download_file(self, remote_path, local_path):
        """Download a file from the FTP server."""
        try:
            with open(local_path, 'wb') as file:
                self.ftp.retrbinary(f'RETR {remote_path}', file.write)
            print(f"Downloaded {remote_path} to {local_path}")
            return True
        except Exception as e:
            print(f"Download failed: {e}")
            return False

    def delete_file(self, remote_path):
        """Delete a file on the FTP server."""
        try:
            self.ftp.delete(remote_path)
            print(f"Deleted {remote_path}")
            return True
        except Exception as e:
            print(f"Delete failed: {e}")
            return False

def main():
    # Example usage
    ftp_client = FTPClient(
        host=input("Enter Host (IP Addr. or URL) :"),
        username=input("Enter Username :"),
        password=input("Enter Password :")
    )

    if ftp_client.connect():
        # List files
        ftp_client.list_files()

        # Change directory
        ftp_client.change_directory('uploads')

        # Upload a file
        ftp_client.upload_file('local_file.txt', 'remote_file.txt')

        # Download a file
        ftp_client.download_file('remote_file.txt', 'downloaded_file.txt')

        # Delete a file
        ftp_client.delete_file('remote_file.txt')

        # Disconnect
        ftp_client.disconnect()

if __name__ == "__main__":
    main()