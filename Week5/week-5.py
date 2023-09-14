import csv
field=['Sid','Sname','City','Contact']
r=[['1','Om','Surat','7689054432'],
   ['2','Sai','Bardoli','6578459801'],
   ['3','Ram','Vyara','8907654320'],
   ['4','Kishan','Bharuch','9087653421'],
   ['5','Radha','Ahemdabad','0987654321']]
filename="c:\\sqlite3\\csv\\student.csv"
for i in range(5):
    sid=int(input('Enter Student Id : '))
    sname=input('Enter Student Name : ')
    city=input('Enter Student City : ')
    contact=int(input('Enter Student Contact : '))
    r.append((sid,sname,city,contact))
    l.append(r)
with open(filename,'w',newline=' ')as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(field)
    csvwriter.writerows(r)
    csvwriter.writerows(l)
with open(filename,'r') as csvfile:
    csvreader=csv.reader(csvfile)
    for record in csvreader:
        print(record)
