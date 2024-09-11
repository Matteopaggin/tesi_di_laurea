from tkinter import filedialog
import os

filename = filedialog.askopenfilename(initialdir = "/Users",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
filename1 = filedialog.askopenfilename(initialdir = "/Users",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))

print('File analizzato:' + filename)
print(filename1)

#liste iniziali da confrontare
code_pres = []
code_pat = []
pres = []
pat = []

#liste pulite da scrivere
ultima = []
code_ultima = []

#liste dei cancellati
cancellati=[]
code_cancellati=[]

rend = '\\ultima.txt'
parentpath  = os.path.dirname(filename)

#paziente
with open(filename) as fo:
    for line in fo:
        code_pat.append(line.split() [0])
        pat.append(line.split() [1])

#presenza
with open(filename1) as f1:
    for line in f1:
        code_pres.append(line.split() [0])
        pres.append(line.split() [1])

#print(pres)
#print(pat)

#conto i cancellati
numcanc = 0
p=0
while p < len(pat):    
    if pat[p] == 'nowhere': 
        if pres[p]== 'Fuori':
            cancellati.append(pat[p])
            code_cancellati.append(code_pat[p])
            numcanc +=1
            p=p+1
        else:
            ultima.append(pat[p])
            code_ultima.append(code_pat[p])
            p=p+1
    else:
        ultima.append(pat[p])
        code_ultima.append(code_pat[p])
        p=p+1

#scrivo i comandi corretti
i=0
while i < len(ultima):
    f = open(parentpath + rend,'a')
    f.write(code_ultima[i]+' '+ultima[i]+'\n')
    f.close()
    i+=1

if numcanc != 0:
    #numero dei cancellati
    f = open(parentpath + rend,'a')
    f.write('Sono stati cancellati '+str(numcanc)+' nowhere.\nI cancellati sono:\n')
    f.close()

    #scrivo i cancellati
    g=0
    while g<len(cancellati):
        f = open(parentpath + rend,'a')
        f.write(code_cancellati[g]+' '+cancellati[g]+'\n')
        f.close()
        g+=1
else:
    f = open(parentpath + rend,'a')
    f.write('Non sono stati cancellati nowhere.\n')
    f.close()

