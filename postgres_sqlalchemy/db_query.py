from itertools import count
from create_and_connect import db, session
from create_tables import List, ListUser, Users_of_list, Task
from sqlalchemy import func

def print_data():
    print('\nListUser') #ListUser
    query_users = session.query(ListUser).all()
    for i in query_users:
        print(f"{i.uid}.User: {i.username}\tEmail: {i.email}\tPassword: {i.password}")
    
    print('\nList') #List
    query_users = session.query(List).all()
    for i in query_users:
        print(f"{i.lid}.Name: {i.name}\tPiority: {i.priority}")

    print('\nUsers_of_list') #Users_of_list
    query_users = session.query(Users_of_list).all()
    for i in query_users:
        print(f"User: {i.user_id}\tList: {i.list_id}")
    
    print('\nTask') #Task
    query_users = session.query(Task).all()
    for i in query_users:
        print(f"{i.tid}.List: {i.list_id}\tDescription: {i.description}\tIs done: {i.is_done}")


def lists_and_tasks():
    """query to make:
    SELECT l.name, t.description
    FROM list l
    JOIN task t on t.list_id = l.lid
    """
    print("\nAll lists with all their tasks:")
    query = session.query(List.name, Task.description).join(Task).filter(List.lid == Task.list_id).all()
    for i in query:
        print(f"List: {i[0]}\tTask: {i[1]}")

def users_and_tasks():
    """query to make: (note: all users of list has to do all tasks from this list)
    SELECT u.username, t.description
    FROM listuser u
    JOIN users_of_list o on u.uid = o.user_id
    JOIN list l on l.lid = o.list_id
    JOIN task t on t.list_id = l.lid
    """
    print("\nAll users with all their tasks:")
    query = session.query(
        ListUser.username, Task.description
        ).join(Users_of_list).filter(Users_of_list.user_id == ListUser.uid
        ).join(List).filter(List.lid == Users_of_list.list_id
        ).join(Task).filter(Task.list_id == List.lid
        ).order_by(ListUser.uid, Task.list_id, Task.tid)
    for i in query:
        print(f"User: {i[0]}\tTask: {i[1]}")

def count_list_tasks():
    """query to make:
    SELECT l.name, count(t.description)
    FROM  list l
    JOIN task t on t.list_id = l.lid
    GROUP BY l.name
    """
    print("\nNumber od tasks in lists:")
    query = session.query(
        List.name, func.count(Task.tid)
    ).join(Task).filter(Task.list_id == List.lid
    ).group_by(List.name).all()
    for i in query:
        print(f"User: {i[0]}\tNumber of tasks: {i[1]}")


def first_row():
    query = session.query(List.name, Task.description).join(Task).filter(List.lid == Task.list_id).all()
    print(query)

#print_data()
#lists_and_tasks()
#users_and_tasks()
#count_list_tasks()
first_row()