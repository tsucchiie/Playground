#writen by Arindra 065

import csv #import lib csv

pertandingan=[]
waktu=[] #list kosong, nanti diisi dari csv
tempat=[] #ini juga

with open('data3.csv', newline='') as csvfile: #buka file csv
    reader = csv.reader(csvfile, delimiter=';') #membaca row, split ;
    for row in reader:

        pertandingan.append(row[1]) #ms var pert
        tempat.append(row[2]) #ms var tempat
        waktu.append(row[3]) #ms var waktu

    tempat.remove(tempat[0])
    pertandingan.remove(pertandingan[0]) #hapus list judul ('Tempat')
    waktu.remove(waktu[0]) #ini juga ('Waktu')

    #tempat=[1,2,3,4,5,2,6,44,2,43,6,5,7,8,2,3,4,234,75,12,86,24,9] #data smt

x = range(len(waktu)) #
#waktu.sort() #BUG ganjel biar ga crash xixixi


# Insertion sort
start = 0
while start != (len(waktu)*len(waktu)):
    start+=1

    n=int((start/(len(waktu)*len(waktu)))*100)
    print ('loading ',n,'%')

    for a in x:
        save= waktu[a]
        if waktu[a] > waktu[(a-1)] and a !=0:
            del waktu[a]###
            waktu.insert((a-1),save)
            break
        

print ('\nhasil:\n')
for e in waktu:
    print(e)
    
