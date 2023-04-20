# CLI command for local is: mongodump --uri="mongodb://localhost:27017/temp1" --gzip --archive | mongorestore --uri="mongodb://localhost:27017/temp9" --nsFrom="temp1.*" --nsTo="temp9.*" --nsInclude="*" --gzip --archive
import os

# ISSUE: for now we will not use as this is issue of running cli command using python , File upload in json format will be used
# os.system('mongodump --uri="mongodb://localhost:27017/temp1" --gzip --archive | mongorestore --uri="mongodb://localhost:27017/temp11" --nsFrom="temp1.*" --nsTo="temp11.*" --nsInclude="*" --gzip --archive')
import subprocess

# subprocess.run(
#     ['mongodump --uri="mongodb://localhost:27017/temp1" --gzip --archive | mongorestore --uri="mongodb://localhost:27017/temp11" --nsFrom="temp1.*" --nsTo="temp11.*" --nsInclude="*" --gzip --archive '])
# subprocess.run(
#     ['mongoimport C:/Users/Harsheet/Downloads/books/books.json -d bookdb -c books --drop'])

# ISSUE:  manually set the target db and target collection , overwrite it


def migrate(path):
    stri = 'mongoimport\t'+path+'\t-d bookdb -c books --drop'
    print(stri)
    os.system(stri)
    return "done"
