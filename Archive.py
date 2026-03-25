import csv
import os

Name_archive = 'archive.csv'
fields = ['product', 'price', 'quantity']

def Load():
    if not os.path.exists(Name_archive):
        return[]
    with open(Name_archive, mode='r',encoding='utf-8') as x:
        return list(csv.DictReader(x))