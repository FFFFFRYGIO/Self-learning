from create_and_connect import db, session
from create_tables import List, ListUser, Users_of_list, Task
from import_from_xlsx import imported_lists, \
    imported_users, imported_users_of_list, imported_tasks

def imported():
    print("Imported rows:")
    print(
        "List:",len(imported_lists),
        "User:",len(imported_users),
        "Users_of_list:",len(imported_users_of_list),
        "Task:",len(imported_tasks),
        )

def insert_data():
    for i in imported_lists:
        session.add(i)
        session.commit()
    for i in imported_users:
        session.add(i)
        session.commit()
    for i in imported_users_of_list:
        session.add(i)
        session.commit()
    for i in imported_tasks:
        session.add(i)
        session.commit()

def check_data():
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

    print()

imported()
insert_data()
check_data()