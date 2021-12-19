import ftplib
import os

def upload_file():
    # open session
    os.environ.get("ftp_host")
    os.environ.get("ftp_username")
    os.environ.get("ftp_password")

    session = ftplib.FTP(os.environ.get("ftp_host"), os.environ.get("ftp_username"), os.environ.get("ftp_password"))
    file = open(os.environ.get("COVID_TIMELINE_FILE"), 'rb')  # file to send
    session.storbinary('STOR '+os.environ.get("COVID_TIMELINE_FILE"), file)  # send the file
  
    file.close()  # close file and FTP session
    session.quit()

def download_file():
    # open session
    session = ftplib.FTP(os.environ.get("ftp_host"), os.environ.get("ftp_username"), os.environ.get("ftp_password"))
    f = open(os.environ.get("COVID_TIMELINE_FILE"), 'wb')  # save into local file
    session.retrbinary('RETR ' +os.environ.get("COVID_TIMELINE_FILE"), f.write, 1024)
    
    f.close()  # close file and FTP session
    session.quit()
    # Open local file
upload_file()