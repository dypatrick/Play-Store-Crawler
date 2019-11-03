#Harshit Verma
#Daniel Patrick
#Following program is a web crawler script used to generate application details from Google Play Store.
#The program will scrap the name of the app, its document identification(doc-id), and the link(href) to the app.
from bs4 import BeautifulSoup
import requests #used to request html documents from the web
import mysql
import mysql.connector #Used to connect python script with mysql database

#Used to send a request to the web with the provide link to return the text or HTML formated documents to be scrapped
source = requests.get('https://play.google.com/store/apps/collection/topselling_free?hl=en').text
soup = BeautifulSoup(source, 'html.parser')

#Checks for the requested data in the 'div' tag of the html
#As long as their is existing data following into the defined  fields, the for loop will continue to run
for start in soup.findAll('div', {'class': 'card no-rationale square-cover apps small'}):
    docid = start.get('data-docid') #Obtains the docid of the app located under data-docid in the scrapped HTML stored in soup variable
    hrefid = start.a.get('href') #Obtains the href of the app located under data-docid in the scrapped HTML stored in soup variable
    name = start.div.div.a.get('aria-label') #Obtains the name of the app located under data-docid in the scrapped HTML stored in soup variable

    #Data obtained is stored in its relating field to be inserted into the database
    print('name:', name, 'docid:', docid, 'HREF:', hrefid)

    #Generates a connection between Python and MySQL to the provided database
    con = mysql.connector.connect(host='10.103.92.251', user='googleplay', passwd='googleplay', port='3306', database='googleplay')
    cursor = con.cursor()

    #Data that has been gather and saved in its respective field name will be inserted accordingly to gpdetails table in googleplay database
    insert_query = "INSERT INTO gpdetails (name, docid, href) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (name, docid, hrefid))
    con.commit()
    cursor.close()

    #Terminates connection between MySQL and Python upon completion
    con.close()


