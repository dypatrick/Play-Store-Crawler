#Daniel Patrick
#Harshit Verma
#Following is a web crawler program used to generate google play store app rankings on third party sites
#The crawler will provide a list of the app name with its rank and href identification.
from bs4 import BeautifulSoup
import requests
import mysql
import mysql.connector #Used to connect python script with mysql database


#Used to send a request to the web with the provide link to return the text or HTML formated documents to be scrapped
source = requests.get('https://www.appbrain.com/stats/google-play-rankings').text
soup = BeautifulSoup(source, 'lxml')

#Checks for the requested data in the 'div' tag of the html
#As long as their is existing data following into the defined  fields, the for loop will continue to run
for s in soup.findAll('div', {'class': 'data-table-container topmargin-m'}):
    for v in s.table.tbody.findAll('tr'):
        rank = v.td.text
        for u in v.findAll('td', {'class': 'ranking-app-cell'}):
            name = u.a.text
            hrefid = u.a.get('href')
            print('name:', name, 'href:', hrefid)
            #It is important to note that the scrapped data from this appbrain.py script will be stored on the same database with the scrap2.py script

            # Generates a connection between Python and MySQL to the provided database
            con = mysql.connector.connect(host='10.103.92.251', user='googleplay', passwd='googleplay', port='3306', database='googleplay')
            cursor = con.cursor()

            # Data that has been gather and saved in its respective field name will be inserted accordingly apptable table in the googleplay database
            insert_query = "INSERT INTO apptable (name, href) VALUES (%s, %s)"
            cursor.execute(insert_query, (name, hrefid))
            con.commit()
            cursor.close()

            # Terminates connection between MySQL and Python upon completion
            con.close()