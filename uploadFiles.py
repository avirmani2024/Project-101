import dropbox
import os

from dropbox.files import WriteMode


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
        

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for fileName in files:

                main_path = os.path.join(root, files)

                relative_path = os.path.relpath(main_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(main_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))


def main():
    access_token = access_token = 'XnGlOWp1tfAAAAAAAAAAAe53BKUCPjxEAmGi1ceLni9hJJkhpiSOYZAvGRqfafnE'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path: "))
    file_to = str(input("Enter the full path for uploading to dropbox: "))

    transferData.upload_file(file_from, file_to)
    transferData = TransferData(access_token)


    transferData.upload_file(file_from, file_to)



main()
