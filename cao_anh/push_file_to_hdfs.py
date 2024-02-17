import subprocess
import os
#kq=subprocess.run(["hdfs","dfs","-ls","/"],capture_output=True, text=True)
list_file=os.listdir("/home/shibe/hadoop_frontend/cao_anh/img_folder")
#cmd="hdfs dfs -put /home/shibe/hadoop_frontend/cao_anh/img_folder/cat-pet-animal-domestic-104827.jpeg /"
#result=subprocess.Popen(cmd,shell=True)
path="/home/shibe/hadoop_frontend/cao_anh/img_folder"
path_Of_All_File=[]
for x in list_file:
    path_Of_All_File.append(os.path.join(path,x))
def push_Toan_bo_file():

    c=len(path_Of_All_File)
    i=0

    for x in path_Of_All_File:
        if x==c:
            break
        
        try:

            cmd_PUT=f"hdfs dfs -put {x} /"
            try:
                result=subprocess.Popen(cmd_PUT,shell=True)
                result.wait()
                print("Tai len HDFS thanh cong !")
                i+=1
            
            except:
                print("failed")
                continue

        except:
            print("that bai !")  

        
             
def xoa_sau_khi_push():
        for count,x in enumerate(path_Of_All_File):
            try:

                os.remove(x)
                print(count,"- xoa thanh cong !")


                    
            except:
                print("failed")
def xoa_toan_bo_file_HDFS():
  

            cmd_PUT="hdfs dfs -rm -R '/*'"
            try:
                result=subprocess.Popen(cmd_PUT,shell=True).wait()
                if result.returncode==None:
                    print("push thanh cong")
                    
            except:
                print("failed")


import sqlite3
import csv


class importdata:
    def __init__(self):
        self.conn=sqlite3.connect("data_img.db")

        self.c=self.conn.cursor()





    def insert(self,name,link,link_hd,des):
        link_hd=f"http://localhost:9870/webhdfs/v1/{name}?op=OPEN"

        querry_str=f"INSERT INTO img_data values ('{name}','{link}','{link_hd}','{des}')"
        self.c.execute(querry_str)
        self.conn.commit()


    #conn.commit() 
    def check(self,link):
        select=f"SELECT * FROM img_data Where link like '{link}'"
        self.c.execute(select)
        count=self.c.fetchall()
        return(len(count))



    def import_csv_to_sql(self):
        with open('link.csv', mode ='r')as file1:
            csvFile = csv.reader(file1)
            count=0
            for lines in csvFile:
                if self.check(lines[1])>0 :
                    continue
                else:
                    
                    self.insert(lines[0],lines[1],lines[2],lines[3])
                    
                    count+=1
            print(f"{count} records were inserted !")

#push_Toan_bo_file()
#xoa_toan_bo_file_HDFS()