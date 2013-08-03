# -*- coding: UTF-8 –*- ：# -*- coding: UTF-8 –*-

class item:
    def __init__(self,number):
        self.number = number
        self.miss = -1 
        self.times = 0
        
        self.last_occur     = 0
        self.max_missed_len =0

    def __cmp__(self, other):  

        if self.number == other.number  and self.miss == -1: 
           return 0
        
        if   self.miss > other.miss :  
           return 1  
        elif self.miss < other.miss:  
           return - 1
        else:
            return 0
        
    def __getitem__(self, key):  
        pass 
 
def  missrate(number,currunt,total):
    L = number %10
    number = (number -L) / 10
    M =  number % 10
    number = (number -M) / 10    
    H =  number % 10

    if L == M and M ==H:
        stand_time = 1      
    elif L == M or  M ==H or L == H:
        stand_time = 3
    else:
        stand_time = 6

    if currunt == 0: return 0
    return currunt/(total/1000)*stand_time       

def static_rate(number):
    #print  "number ", number
    if number > 0 and number < 3000:
        L = number %10
        number = (number -L) / 10    
        s_t[number] +=1
        return
    elif number > 4000:
        print "too big number occur"
        #exit(0)
    
s_t = [0 for i in range(3000)]  

    
codelist=[]


for H in range(0,10):
    for M in range(H,10):
        for L in range(M,10):
            it = item( H *100 + M*10 +L)
            codelist.append(it)
           

#print 

fileHandle = open ( "D:\\Program Files\\3D500\\Data\\sdhistory.xml" )  
history= fileHandle.read()  
fileHandle.close()


#取出原始数据，并加工
import re

code = re.compile(' code=\"(?P<HN>\d),(?P<MN>\d),(?P<LN>\d)\"')

allcode = code.finditer(history)

cnt = 0
for item in allcode:
    
    #print int(item.group('HN')),int(item.group('MN')),int(item.group('LN'))
    HN = int(item.group('HN'))
    MN = int(item.group('MN'))
    LN = int(item.group('LN'))

    #sort it 1,2,3
    if HN > MN:
        (HN,MN)=(MN,HN)
        
    if MN > LN:
        (MN,LN)=(LN,MN)
        
    if HN > MN:
        (HN,MN)=(MN,HN)

    
    for idx in range(0,len(codelist)):
        
        if  codelist[idx].number == HN*100+MN*10+LN:
            codelist[idx].times +=1
            if codelist[idx].miss == -1:
                codelist[idx].miss = cnt

            static_rate(cnt - codelist[idx].last_occur)
            
            if cnt - codelist[idx].last_occur > codelist[idx].max_missed_len:
                codelist[idx].max_missed_len = cnt - codelist[idx].last_occur
            codelist[idx].last_occur = cnt

            
                
            break
        #idx = codelist.index(item(HN*100+MN*10+LN))
    
    cnt += 1
    
    #codelist.append(HN*100+MN*10+LN)
    #Wprint codelist[idx].miss,codelist[idx].number

codelist.sort()

for code in codelist:
    
    print "number  %03d" %code.number, "  currunt  %4d" %code.miss ,"   ocurred %3d" %code.times,"  max missed %5d" %code.max_missed_len
    #print "miss rate %05f" %missrate(code.number,code.times,cnt)

print "total times",cnt

for H in range(0,3000):
    if s_t[H]> 0:
        print "%d," %H ,"%3d" %s_t[H]

 


        

