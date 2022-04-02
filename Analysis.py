import numpy as np
import pandas as pd
import glob


def read_xvg(F,ncol):
    f=open(F,"r")
    p=f.readlines()
    q=len(p)
    arr=[]
    for i in range (ncol):
        arr.append([]) 
    for line in p:
        if line[0:1] != "@" and line[0:1] != "#":
            for k in range (len(arr)):
                arr[k].append(float(line.split()[k]))
    for i in range (len(arr)):
        arr[i]=np.asarray(arr[i])
    return arr


def convert_energy(energy):
    energy=energy*0.238
    return energy


def sum(file):
    f=read_xvg(file,ncol=3)
    a=f[1]
    b=f[2]
    sum=a+b
    sum=convert_energy(sum)
    return sum


F=glob.glob("xvgs/*.xvg")
F.sort()



Residues=[]
IE=[]
for i in range (len(F)):
    X=np.average(sum(F[i]))
    Residues.append(i+1)
    IE.append(X)



df=pd.DataFrame({"Resid":Residues,
		"Interaction Energy(kcal/mol)": IE})

df.to_csv("Interaction_energy.csv",sep="\t",index=False)






