from flask import g
from cli import *

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_db()
        db.cursor().execute('set search_path to team3_schema, "$user", public;')
    return db

def add_goal(add_type, add_user_id, add_unit, add_max):
    sql = "insert into goals (type, user_id, unit, max) values ('{type}', '{user_id}', '{unit}', '{max}');".format(type = add_type, user_id = add_user_id, unit = add_unit, max = add_max)
    results = query_db(sql, db = get_db(), pretty_print=True)
    return results
    
def select_goals(add_user_id):
    sql = "select * from goals where user_id = {user_id}".format(user_id = add_user_id)
    results = query_db(sql, db = get_db(), pretty_print=True)
    return results

def remove_goal(add_remove_goal_id):
    sql = "delete from goals where id = {remove_goal_id}".format(remove_goal_id = add_remove_goal_id)
    results = query_db(sql, db = get_db(), pretty_print=True)
    return results

def get_goal_result(add_user_id, add_goal_id):
    sql = "select goal_result from history where add_user_id = {user_id} and add_goal_id = {goal_id}".format(user_id = add_user_id, goal_id = add_goal_id)
    results = query_db(sql, db = get_db(), pretty_print=True)
    return results

def set_goal_level(new_goal_result, add_user_id, add_goal_id):
    sql = "update history set goal_result = {goal_result} where user_id = {user_id} and goal_id = {goal_id}".format(goal_result = new_goal_result, user_id = add_user_id, goal_id = add_goal_id)
    results = query_db(sql, db = get_db(), pretty_print=True)
    return results

# @app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
