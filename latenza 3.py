from tkinter import filedialog
import os

filename = filedialog.askopenfilename(initialdir = "/Users",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))

print('File analizzato:' + filename)

code_pat = []
pat = []

rend = '\\latenza.txt'
parentpath  = os.path.dirname(filename)


with open(filename) as fo:
    for line in fo:
        code_pat.append(line.split() [0])
        pat.append(line.split() [1])

guarda=0
guarda_robot = 0
nonguarda=0
latenza = []
totale = len(pat)
p=0
#print(pat)

while p <= (totale-2): 
    if pat[p] == 'indica':
        if pat[p+1] == 'inizia':
            latenza.append(str(float(code_pat[p+1])-float(code_pat[p])))
            guarda +=1
            p+=1
        elif pat[p+1] == 'indica' or pat[p+1] == 'indica-robot':
            nonguarda +=1
            p+=1
    elif pat[p] == 'indica-robot':
        if pat[p+1] == 'inizia':
            latenza.append(str(float(code_pat[p+1])-float(code_pat[p])))
            guarda_robot +=1
            p+=1
        elif pat[p+1] == 'indica' or pat[p+1] == 'indica-robot':
            nonguarda +=1
            p+=1
    else:
        p+=1

for line in latenza:
    f = open(parentpath + rend,'a')
    f.write('latenza '+':'+str(line)+'\n')
    f.close()

latenzatot = 0
latenzamedia = 0
guardatot = guarda + guarda_robot

for lat in latenza:
    latenzatot = latenzatot + float(lat)

if guardatot != 0:
    latenzamedia = latenzatot/guardatot
else:
    latenzamedia = 0


f = open(parentpath + rend,'a')
f.write('Il bambino ha risposto alle indicazioni del TERAPISTA '+str(guarda)+' volte.'+'\n'+'Il bambino ha risposto alle indicazioni del ROBOT '+str(guarda_robot)+' volte. \n'+'NON ha risposto '+str(nonguarda)+' volte. \n'+'Latenza media di '+str(latenzamedia)+' secondi'+'\n')
f.close()

