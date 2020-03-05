import database
from DataGrabber import PageParse

def Populate(self):
    for pair in PageParse.data:
        database.con.execute('INSERT INTO bitcoin VALUES()')

