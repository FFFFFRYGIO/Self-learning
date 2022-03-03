from create_and_connect import db, session
from create_tables import List, ListUser, Users_of_list, Task
from sqlalchemy import delete

def insert_test_data():
    new_user = ListUser(username = 'radoslaw', email='radek.r@g.c', password='123')
    new_list = List(name = 'shoplist')
    new_user_of_list = Users_of_list(user_id = 1, list_id = 1)
    new_task = Task(list_id = 1, description = 'testtask')
    test_inserts = [new_user, new_list, new_user_of_list, new_task]
    
    for i in test_inserts:
        session.add(i)
        session.commit()

def check_test_data():
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

def delete_test_data():
    del_user = ListUser(username = 'radoslaw', email='radek.r@g.c', password='123')
    del_list = List(name = 'shoplist')
    del_user_of_list = Users_of_list(user_id = 1, list_id = 1)
    del_task = Task(list_id = 1, description = 'testtask')
    test_del = [del_user, del_list, del_user_of_list, del_task]

    for i in test_del:
        session.delete(i)
        session.commit()


#insert_test_data()
#check_test_data()
#delete_test_data()