import sqlite3
import csv




conn=sqlite3.connect("data_img.db")

c=conn.cursor()


table = """ CREATE TABLE img_data (
            name text NOT NULL,
            link text NOT NULL,
            link_hd text NOT NULL,
            des text

        ) """

def insert(name,link,link_hd,des):

    querry_str=f"INSERT INTO img_data values ('{name}','{link}','{link_hd}','{des}')"
    c.execute(querry_str)
    conn.commit()


#conn.commit() 
def check(link):
    select=f"SELECT * FROM img_data Where link like '{link}'"
    c.execute(select)
    count=c.fetchall()
    return(len(count))


def import_csv_to_sql():
    with open('link.csv', mode ='r')as file1:
        csvFile = csv.reader(file1)
        count=0
        for lines in csvFile:
            if check(lines[1])>0 :
                continue
            else:
                
                insert(lines[0],lines[1],lines[2],lines[3])
                
                count+=1
        print(f"{count} records were inserted !")

def xoa_toan_bo():
    # Delete all rows from table
    c.execute('DELETE FROM img_data');

    print('We have deleted', c.rowcount, 'records from the table.')

# Commit the changes to db			
    conn.commit()
def xem_tat_ca():
    select="SELECT * FROM img_data;"
    c.execute(select)
    conn.commit()
    rows = c.fetchall()
    for row in rows:
        print(row)

def xoa():
    querry="DELETE FROM img_data WHERE name LIKE 'cho'"
    c.execute(querry)
    conn.commit()
def top(conn,c,num):
    querry=f"SELECT * FROM img_data ORDER BY RANDOM() LIMIT {num};"
    aa=c.execute(querry)
    conn.commit()
    return list(aa)
def search(conn1,cc,input1):
    querry=f"SELECT * FROM img_data Where des like '%{input1}%'  LIMIT 15"
    aa=cc.execute(querry)
    rows = cc.fetchall()
    conn1.commit()
    
    return list(rows)

conn.close()