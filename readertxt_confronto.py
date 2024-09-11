import tkinter as tk
from tkinter import filedialog
bottoni = []

filename = filedialog.askopenfilename(initialdir = "/Users/Matteo/Desktop",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
filename_2 = filedialog.askopenfilename(initialdir = "/Users/Matteo/Desktop",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))

print(filename)
print(filename_2)


with open(filename) as fo:
    for line in fo:
        bottoni.append(line.split() [1])


n_robot = bottoni.count('robot')
print("Robot = {}".format(n_robot))

n_gioc = bottoni.count('giocattolo')
print("Giocattolo = {}".format(n_gioc))
            
n_pers = bottoni.count('altra_p')
print("Altra persona = {}".format(n_pers))

n_posterdietro = bottoni.count('poster_dietro')
print("Poster dietro = {}".format(n_posterdietro))

n_posterSX = bottoni.count('poster_sx')
print("Poster sinistra = {}".format(n_posterSX))

n_posterDX = bottoni.count('poster_dx')
print("Poster destra = {}".format(n_posterDX))

n_nowhere = bottoni.count('nowhere')
print("Nowhere = {}".format(n_nowhere))

n_tot = len(bottoni)
print("Totale analisi = {}".format(n_tot))

count_switch = 0
count_var = 0

i=2

#while i < (len(bottoni)):
#    if bottoni[i] != bottoni[i-1]:
#        if bottoni[i-2] != bottoni[i]:
#            count_switch += 1
#            i += 1
#        else:
#            count_var += 1
#            i +=1
#    else:
#        i+=1
#
#print("Il paziente ha effettuato {} cambi di target e {} cambi singoli".format(count_switch, count_var))

        

bottoniterapista = []
with open(filename_2) as f1:
    for line in f1:
        bottoniterapista.append(line.split() [1])

p=0
corr = 0

while p < len(bottoniterapista):
    if bottoni[p] == bottoniterapista[p] and bottoni[p] != 'nowhere':
        corr +=1
        p +=1
    else:
        p +=1

n= n_tot
perc = (corr/n)*100
print("Terapista e bambino hanno lo stesso target {} volte su un totale di {} target, che corrisponde al {}%".format(corr, n, perc))
