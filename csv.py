#coding:utf-8
import csv
csvfile = file('csv_test.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['����', '����', '�绰'])
data = [
    ('С��', '25', '1234567'),
    ('С��', '18', '789456')
]
writer.writerows(data)

csvfile.close()