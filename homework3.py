import collections
def ord_prefixspan(filename,min_sup):
    print("entered function")
    with open(filename) as f:
        lines = [line.rstrip('\n') for line in f]
    SDB=[]
    for line in lines:
        print(line)
        x=line.split(',')[1]
        SDB.append(x[2:-1])
    print('SDB is :',SDB)

    final_output=recfunc('',SDB,min_sup)
    print(final_output)

def getPDB(item,SDB):
    PDB=[]
    for transaction in SDB:
        if(transaction.find(item)!=-1):
            PDB.append(transaction[transaction.find(item)+1:])
    return PDB

def recfunc(prefix, PDB, min_sup):
    print(prefix,PDB)
    freq_patterns={}
    f={}
    for i in PDB:
        already_visited=set()
        for j in i:
            if(j not in already_visited):
                already_visited.add(j)
                if j in f:
                    f[j]+=1
                else:
                    f[j]=1
    f_sorted=collections.OrderedDict(sorted(f.items()))
    c={}
    for key,value in f_sorted.items():
        if(value>=min_sup):
            c[key]=value
            freq_patterns[prefix+key]=value
    print(c)
    for key in c:
        ss=recfunc(prefix+key, getPDB(key, PDB), min_sup)
        freq_patterns.update(ss)

    return freq_patterns
    
    

