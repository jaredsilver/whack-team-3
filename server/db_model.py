"""
    Connect to a vertica database and run queries
"""
from flask import g
import vertica_python

import re
import os

try:
    DB_NAME = os.environ['DB_NAME']
except Exception, e:
    DB_NAME = 'test'

try:
    DB_USER = os.environ['DB_USER']
except Exception, e:
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
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = vertica_python.connect(**conn_info)
    return db


def query_db(query, args=(), one=False):
    print query
    cur = get_db().cursor()

    try:
        cur.execute(query, args)
        rv = cur.fetchall()

        # Turn into colname->val dict representation of tuple
        # this isn't very efficient but will suffice for now
        rv = [make_dicts(cur, row) for row in rv]
    except Exception, e:
        print e
        rv = [{'error': e}]

    cur.close()
    return (rv[0] if rv else None) if one else rv

def select_one():
    """
        Select 1 from database
    """
    sql = "SELECT 1"
    results = query_db(sql)
    print results
    return results

def select_a():
    """
        Select 1 from database
    """
    sql = "SELECT a from foo"
    results = query_db(sql)
    print results
    return results


# @app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()