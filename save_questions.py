import sqlite3
from askfm import *

db = sqlite3.connect('asks.db')
db.execute('''create table if not exists asks (username text,
                                               question text,
                                               answer text,
                                               img_url text,
                                               unique(question, answer))''')
db.commit()

if(len(sys.argv)==0):
    print("Usage: pull_user.py <username>")
    exit(0)

username = sys.argv[1]
user = getUser(username)

print 'Scraping complete, saving results.'

for answer_block in user['answers']:
    query_string = 'insert or ignore into asks values (?, ?, ?, ?)'
    db.execute(query_string, (user['username'], answer_block['question_text'], \
               answer_block['answer'], answer_block['img_reply_src']))

db.commit()
