# add your code in this file

import sqlite3
from sys import argv

conn = sqlite3.connect('ntz.db')
c = conn.cursor()

def remember(ntz_info):
  sql = "Please insert values"
  c.execute(sql,ntz_info)
  conn.commit()

def forget(ntz_name):
  sql = "Type values you wish to forget"
  c.execute(sql,(ntz_name))

def clear():
  sql = "Clearing notes in NTZ"
  c.execute(sql)

def retrieve_all():
  sql = "SELECT * FROM NTZ"
  c.execute(sql)

def edit(note_name,note_data):
  sql = "Edit your current notes"
  c.execute(sql,note_name,note_data)



def append():
  sql = "Append value to your notes"
  c.execute(sql)


# main function
def cli():
  if argv[1] == 'r':
    new_note_data = ((argv[2],argv[3]))
    remember(new_note_data)
  elif argv[1] == '-c':
    append(argv[2])
  elif argv[1] == 'f':
    forget(argv[2])
  elif argv[1] == 'e':
    edit(argv[2])
  elif argv[1] == 'clear':
    clear()
  elif argv[1] == 'ntz':
    retrieve_all()

def get_args():
  return argv
  
# run the main function
cli()
