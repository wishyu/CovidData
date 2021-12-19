import ftplib
from dotenv import load_dotenv


load_dotenv()
def upload_file():
    # open session
    session = ftplib.FTP(ftp_host, ftp_username, ftp_password)
    file = open(localfile, 'rb')  # file to send
    session.storbinary('STOR '+filename, file)  # send the file
  
    file.close()  # close file and FTP session
    session.quit()

def download_file():
    # open session
    session = ftplib.FTP(ftp_host, ftp_username, ftp_password)
    f = open(localfile, 'wb')  # save into local file
    session.retrbinary('RETR ' + filename, f.write, 1024)
    
    file.close()  # close file and FTP session
    session.quit()
    # Open local file
    f = open(localfile, 'rb')
    content = f.read()

upload_file()