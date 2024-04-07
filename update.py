from sqlalchemy import Transaction
import stripe
import streamlit as st
import mysql.connector
import webbrowser
import pandas as pd


def update_customers():
    stripe.api_key = "sk_test_51Ot9BvK8CtsB2sc74BA3mcV4A3fw4UpdufyAXjdtdqRZygDesPLHWdaaIwbc8qbaDnt7AHKpJgjNRUVag6jddeHg00L03ItGtG"
    #database
    conn = mysql.connector.connect(host = "localhost",
                              port = "3306",
                              user = "root",
                              passwd = "123",
                              db = "doctor")
    

    cursor = conn.cursor()
    customers = cursor.execute('SELECT * FROM Customers')

    results = cursor.fetchall()

    # Convert results to a pandas DataFrame

    df = pd.DataFrame(results, columns=['name', 'id','gmail'])
    n = len(df['name'])
    x = df['id'][n-1]

    customers2 = stripe.Customer.list()
    customers_table = cursor.execute("SELECT * FROM Customers")
    results = cursor.fetchall()
    ##update data
    name_customers2 = [c.name for c in customers2]
    id_customers2 = [c.id for c in customers2]
    gmail_customers2 = [c.email for c in customers2]


    if id_customers2[0]!=x:
        cursor.execute(
        'INSERT INTO Customers(name,id,gmail) VALUES (%s,%s,%s);',
        (name_customers2[0],id_customers2[0],gmail_customers2[0]))
        conn.commit()
    cursor.close()

    #update transaction

def update_transaction():

    stripe.api_key = "sk_test_51Ot9BvK8CtsB2sc74BA3mcV4A3fw4UpdufyAXjdtdqRZygDesPLHWdaaIwbc8qbaDnt7AHKpJgjNRUVag6jddeHg00L03ItGtG"
    #database
    conn = mysql.connector.connect(host = "localhost",
                              port = "3306",
                              user = "root",
                              passwd = "123",
                              db = "doctor")
    

    cursor = conn.cursor()
    transactions = stripe.BalanceTransaction.list()
    customers = stripe.Customer.list()
    transactions_id = [trans.id for trans in transactions]
    types = [trans.type for trans in transactions]
    Net = [trans.net for trans in transactions]
    Amount = [trans.amount for trans in transactions]
    Fee = [trans.fee for trans in transactions]
    Des = [trans.description for trans in transactions]
    Name = [cus.name for cus in customers]
    trans = cursor.execute('SELECT *from transactions')
    result = cursor.fetchall()
    df = pd.DataFrame(result,columns=['ID','Name','Type','Net','Amount','Fee','Description'])
    curren  = df['ID'][len(df['ID'])-1]
    
    if transactions_id[0] !=curren:
        cursor.execute('INSERT INTO transactions (ID,Name,Type,Net,Amount,Fee,Description) '
                       'VALUES (%s,%s,%s,%s,%s,%s,%s);',
                        transactions_id[0],Name[0],types[0],Net[0],Amount[0],Fee[0],Des[0])
        
        conn.commit()
    cursor.close()








                                                


    


