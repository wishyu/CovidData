import ftplib
import os

def upload_file():
    ftp_host = os.environ.get("ftp_host")
    ftp_username = os.environ.get("ftp_username")
    ftp_password = os.environ.get("ftp_password")
    filename = "/htdocs/files/"  + os.environ.get("COVID_TIMELINE_FILE")
    localfile = "/tmp/" + os.environ.get("COVID_TIMELINE_FILE")
    # open session
    session = ftplib.FTP(ftp_host, ftp_username, ftp_password)
    file = open(localfile, 'rb')  # file to send
    session.storbinary('STOR '+filename, file)  # send the file
    
    file.close()  # close file and FTP session
    session.quit()

def download_file():
    ftp_host = os.environ.get("ftp_host")
    ftp_username = os.environ.get("ftp_username")
    ftp_password = os.environ.get("ftp_password")
    filename = "/htdocs/files/"  + os.environ.get("COVID_TIMELINE_FILE")
    localfile = "/tmp/" + os.environ.get("COVID_TIMELINE_FILE")
    # open session
    session = ftplib.FTP(ftp_host, ftp_username, ftp_password)
    f = open(localfile, 'wb')  # save into local file
    print('RETR ' + filename)
    session.retrbinary('RETR ' + filename, f.write, 1024)
    
    f.close()  # close file and FTP session
    session.quit()
    # Open local file
    # f = open(localfile, 'rb')
    # content = f.read()