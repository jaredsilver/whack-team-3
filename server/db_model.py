"""
    Connect to a vertica database and run queries
"""
from flask import g
from cli import *

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_db()
        db.cursor().execute('set search_path to team3_schema, "$user", public;')

    return db

def select_one():
    """
        Select 1 from database
    """
    sql = "SELECT 1"
    results = query_db(sql, db = get_db(), pretty_print=True)
    #print "FROM INSIDE SELECT ONE" + results
    return results

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

def add_goal():
    sql = "insert into goals (type) values ('sleep');"
    results = query_db(sql, db = get_db(), pretty_print=True)
    return results

def select_goals(add_user_id):
    "Selects all the goals of a particular user"
    sql = "SELECT type, user_id, id, unit, max FROM goals WHERE user_id = add_user_id"
    results = query_db(sql, db = get_db(), pretty_print=True)
    #print results
    return results

def remove_goal(remove_goal_id):
    "removes the goal with the given ID from the database"
    sql = "DELETE FROM goals WHERE id = remove_goal_id"

def select_a():
    """
        Select 1 from database
    """
    sql = "SELECT a from foo"
    results = query_db(sql)
    print(results)
    return results


# @app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
