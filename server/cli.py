def make_dicts(cursor, row):
    """
        Turn query results into dictionaries keyed by column name
    """
    colnames = [col[0] for col in cursor.description]

    fmtrow = {}
    for idx, value in enumerate(row):
      fmtrow[colnames[idx]] = value

    return fmtrow


def get_db():
    import vertica_python

    import re
    import os

    try:
        DB_NAME = os.environ['DB_NAME']
    except Exception as e:
        DB_NAME = 'test'

    try:
        DB_USER = os.environ['DB_USER']
    except Exception as e:
        DB_USER = 'dbadmin'

    DB_PASSWORD = ''
    # DB_HOST = os.environ['DB_HOST']
    DB_HOST = "http://ec2-52-90-190-153.compute-1.amazonaws.com/"

    conn_info = {'host': DB_HOST,
                 'port': 5433,
                 'user': DB_USER,
                 'password': '',
                 'database': DB_NAME,
                 # 10 minutes timeout on queries
                 'read_timeout': 600,
                 # default throw error on invalid UTF-8 results
                 'unicode_error': 'strict',
                 # SSL is disabled by default
                 'ssl': False}

    db = vertica_python.connect(**conn_info)
    return db

def query_db(query, args=(), one=False):
    print(query)
    cur = get_db().cursor()

    try:
        cur.execute(query, args)
        rv = cur.fetchall()

        # Turn into colname->val dict representation of tuple
        # this isn't very efficient but will suffice for now
        rv = [make_dicts(cur, row) for row in rv]
    except Exception as e:
        print(e)
        rv = [{'error': e}]

    cur.close()
    return (rv[0] if rv else None) if one else rv

from db_util import *

if __name__ == "__main__":
    import sys
    db = connect_to_db()

    print "Welcome to the mini Vertica client! Enter your queries or type '\\q' to quit"
    line = raw_input("> ")
    while not line.strip() == "\\q":
        if len(line):
            while not line[-1] == ";":
                line += raw_input("(cont)> ")
            if line.split(' ')[0] == "insert":
                line += "; commit;"

            query_db(line, pretty_print=True)
        line = raw_input("> ")

