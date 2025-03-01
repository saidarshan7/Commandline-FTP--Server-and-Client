from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Configure FTP user
authorizer = DummyAuthorizer()
authorizer.add_user("ftp", "ftp", ".", perm="elradfmw")  # Change credentials as needed
authorizer.add_anonymous(".")

# Configure FTP handler
handler = FTPHandler
handler.authorizer = authorizer

# Set FTP Server IP and Port
server = FTPServer(("192.168.234.41", 2121), handler)

print("FTP Server started on port 21...")
server.serve_forever()
