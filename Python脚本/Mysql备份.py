import os
import time
import datetime

DB_HOST = 'localhost'
DB_USER = 'root'
DB_USER_PASSWORD = '_root_user_password_'
#DB_NAME = '/backup/dbnames.txt'
DB_NAME = 'db_name'
BACHUP_PATH = '/bachup/dbbackup/'

DATETIME = time.strftime('%Y%m%d')

TODAYBACKUPPATH = BACHUP_PATH + DATETIME

# Checking if backup folder already exists or not. If not exists will create it.
print("creating backup folder")

if not os.path.exists(TODAYBACKUPPATH):
    os.makedirs(TODAYBACKUPPATH)

# Code for checking if you want to take single database backup or assinged multiple backups in DB_NAME.
print("checking for databases names file.")

if os.path.exists(DB_NAME):
    file1 = open(DB_NAME)
    multi =1
    print("Databases file found...")
    print("Starting backup of all dbs listed in file ") + DB_NAME
else:
    print("Databases file not found...")
    print("Starting backup of database ") + DB_NAME
    multi = 0

# Starting actual database backup process.
if multi:
    in_file = open(DB_NAME,"r")
    flength = len(in_file.readlines())
    in_file.close()
    p=1
    dbfile = open(DB_NAME,"r")

    while p <= flength:
        db = dbfile.readline()
        db = db[:-1]
        dumpcmd = "mysqldump -u " + DB_USER + "-p" + DB_USER_PASSWORD + " " + db + ">" + TODAYBACKUPPATH + "/" + db + ".sql"
        os.system(dumpcmd)

print("Backup script completed")
print("Your backups has been created in " + TODAYBACKUPPATH + " directory")