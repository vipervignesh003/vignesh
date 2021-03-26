import math
import random
global r
r=int(input("enter your year to get the time table"))
if(r==1):
    class firstyear:
        global lab,subj,subjp,subjpw,staff,labsc,n,s,monday,tuesday,wednesday,thursday,friday
        monday=["null","null","null","null","null","null","null","null"]
        tuesday=["null","null","null","null","null","null","null","null"]
        wednesday=["null","null","null","null","null","null","null","null"]
        thursday=["null","null","null","null","null","null","null","null"]
        friday=["null","null","null","null","null","null","null","null"]
        n=int(input("How many labs for firstyear"))
        s=int(input("how many subjets for firstyear"))
        lab=[]
        subj=[]
        subjp=[]
        subjpw=[]
        staff=[]
        labsc=[0,4]
        def input1(q):
            for i in range(n):
                l=input("enter lab names:")
                lab.append(l)
            for i in range(s):
                x=input("enter subject name\n")
                subj.append(x)
                x1=input("enter staff name\n")
                staff.append(x1)
            for i in range(s):
                x=int(input("entire total number peroids of each subject:\n"))
                subjp.append(x)
            for i in range(s):
                x=math.ceil(subjp[i]/12)
                subjpw.append(x)
            print("first  year subjects:\n",subj)
            print("Subjects Total periods:\n",subjp)
            print("Subjects per week:\n",subjpw)
        def process1(q):
            flag1=0
            flag2=0
            flag3=0
            flag4=0
            flag5=0
            for i in range(n):
                for j in range(8):
                    if monday[j]=="null":
                        continue
                    else:
                        flag1=1
                break
        for a in range(8):
            if tuesday[a]=="null":
                continue
            else:
                flag2=1
                break
        for b in range(8):
            if wednesday[b]=="null":
                continue
            else:
                flag3=1
                break
        for c in range(8):
            if thursday[c]=="null":
                continue
            else:
                flag4=1
                break
        for d in range(8):
            if friday[d]=="null":
                continue
            else:
                flag5=1
                break
        x=random.choice(labsc)
        for v in range(5):
            y=random.randint(0,4)
            k=x
            if y==0:
                if flag1==0:
                    for j in range(4):
                        monday[k]=lab[i]
                        k=k+1
                    break
                else:
                    continue
            if y==1:
                if flag2==0:
                    for j in range(4):
                        tuesday[k]=lab[i]
                        k=k+1
                    break
                else:
                    continue
            if y==2:
                if flag3==0:
                    for j in range(4):
                        wednesday[k]=lab[i]
                        k=k+1
                    break
                else:
                    continue
            if y==3:
                if flag4==0:
                    for j in range(4):
                        thursday[k]=lab[i]
                        k=k+1
                    break
                else:
                    continue
            if y==4:
                if flag5==0:
                    for j in range(4):
                        friday[k]=lab[i]
                        k=k+1
                    break 
                else:
                    continue


    for i in range(s):
        p=subjpw[i]
        y=p
        while(p>0):
            for z in range(y):
              if(p>0):
                for c in range(40):
                    y=random.randint(0,7)
                    if z==0:
                        if monday[y]=="null":
                            monday[y]=subj[i]
                            p=p-1
                            break
                    if z==1:
                        if tuesday[y]=="null":
                            tuesday[y]=subj[i]
                            p=p-1
                            break
                    if z==2:
                        if wednesday[y]=="null":
                            wednesday[y]=subj[i]
                            p=p-1
                            break
                    if z==3:
                        if thursday[y]=="null":
                            thursday[y]=subj[i]
                            p=p-1
                            break
                    if z==4:
                        if friday[y]=="null":
                            friday[y]=subj[i]
                            p=p-1
                            break


    def print1(q):
            print("**********************TIME TABLE FOR FIRSTYEAR IS**********************")
            print(monday)
            print(tuesday)
            print(wednesday)
            print(thursday)
            print(friday)


class secondyear:
 global lab,subj,subjp,subjpw,staff,labsc,n,s,monday,tuesday,wednesday,thursday,friday
 monday=["null","null","null","null","null","null","null","null"]
 tuesday=["null","null","null","null","null","null","null","null"]
 wednesday=["null","null","null","null","null","null","null","null"]
 thursday=["null","null","null","null","null","null","null","null"]
 friday=["null","null","null","null","null","null","null","null"]
 n=int(input("How many labs for secondyear"))
 s=int(input("How many subjets for secondyear"))
 lab=[]
 subj=[]
 subjp=[]
 subjpw=[]
 staff=[]
 labsc=[0,4]
 def input2(q):
    
    for i in range(n):
        l=input("enter lab names:")
        lab.append(l)
    
    for i in range(s):
        x=input("enter subject name\n")
        subj.append(x)
        x1=input("enter staff name\n")
        staff.append(x1)
    for i in range(s):
        x=int(input("entire total number peroids of each subject:\n"))
        subjp.append(x)
    for i in range(s):
        x=math.ceil(subjp[i]/12)
        subjpw.append(x)
    print("second year subjects:\n",subj)
    print("Subjects Total periods:\n",subjp)
    print("Subjects per week:\n",subjpw)
 def process2(q):
    flag1=0
    flag2=0
    flag3=0
    flag4=0
    flag5=0
    for i in range(n):
        for j in range(8):
            if monday[j]=="null":
                continue
            else:
                flag1=1
                break
        for a in range(8):
            if tuesday[a]=="null":
                continue
            else:
                flag2=1
                break
        for b in range(8):
            if wednesday[b]=="null":
                continue
            else:
                flag3=1
                break
        for c in range(8):
            if thursday[c]=="null":
                continue
            else:
                flag4=1
                break
        for d in range(8):
            if friday[d]=="null":
                continue
            else:
                flag5=1
                break
        x=random.choice(labsc)
        for v in range(5):
            y=random.randint(0,4)
            k=x
            if y==0:
                if flag1==0:
                    for j in range(4):
                        monday[k]=lab[i]
                        k=k+1
                    break
                else:
                    continue
            if y==1:
                if flag2==0:
                    for j in range(4):
                        tuesday[k]=lab[i]
                        k=k+1
                    break
                else:
                    continue
            if y==2:
                if flag3==0:
                    for j in range(4):
                        wednesday[k]=lab[i]
                        k=k+1
                    break
                else:
                    continue
            if y==3:
                if flag4==0:
                    for j in range(4):
                        thursday[k]=lab[i]
                        k=k+1
                    break
                else:
                    continue
            if y==4:
                if flag5==0:
                    for j in range(4):
                        friday[k]=lab[i]
                        k=k+1
                    break 
                else:
                    continue


    for i in range(s):
        p=subjpw[i]
        y=p
        while(p>0):
            for z in range(y):
              if(p>0):
                for c in range(40):
                    y=random.randint(0,7)
                    if z==0:
                        if monday[y]=="null":
                            monday[y]=subj[i]
                            p=p-1
                            break
                    if z==1:
                        if tuesday[y]=="null":
                            tuesday[y]=subj[i]
                            p=p-1
                            break
                    if z==2:
                        if wednesday[y]=="null":
                            wednesday[y]=subj[i]
                            p=p-1
                            break
                    if z==3:
                        if thursday[y]=="null":
                            thursday[y]=subj[i]
                            p=p-1
                            break
                    if z==4:
                        if friday[y]=="null":
                            friday[y]=subj[i]
                            p=p-1
                            break
    
 def print2(q):
    print("********************************TIME TABLE FOR SECONDYEAR IS********************************")
    print(monday)
    print(tuesday)
    print(wednesday)
    print(thursday)
    print(friday)


class thirdyear:
 global lab,subj,subjp,subjpw,staff,labsc,n,s,monday,tuesday,wednesday,thursday,friday
 monday=["null","null","null","null","null","null","null","null"]
 tuesday=["null","null","null","null","null","null","null","null"]
 wednesday=["null","null","null","null","null","null","null","null"]
 thursday=["null","null","null","null","null","null","null","null"]
 friday=["null","null","null","null","null","null","null","null"]
 n=int(input("How many labs for thirdyear"))
 s=int(input("How many subjets for thirdyear"))
 lab=[]
 subj=[]
 subjp=[]
 subjpw=[]
 staff=[]
 labsc=[0,4]
 def input3(q):
    
    for i in range(n):
        l=input("enter lab names:")
        lab.append(l)
    
    for i in range(s):
        x=input("enter subject name\n")
        subj.append(x)
        x1=input("enter staff name\n")
        staff.append(x1)
    for i in range(s):
        x=int(input("entire total number peroids of each subject:\n"))
        subjp.append(x)
    for i in range(s):
        x=math.ceil(subjp[i]/12)
        subjpw.append(x)
    print("third year subjects:\n",subj)
    print("Subjects Total periods:\n",subjp)
    print("Subjects per week:\n",subjpw)
 def process3(q):
    flag1=0
    flag2=0
    flag3=0
    flag4=0
    flag5=0
    for i in range(n):
        for j in range(8):
            if monday[j]=="null":
                continue
            else:
                flag1=1
                break
        for a in range(8):
            if tuesday[a]=="null":
                continue
            else:
                flag2=1
                break
        for b in range(8):
            if wednesday[b]=="null":
                continue
            else:
                flag3=1
                break
        for c in range(8):
            if thursday[c]=="null":
                continue
            else:
                flag4=1
                break
        for d in range(8):
            if friday[d]=="null":
                continue
            else:
                flag5=1
                break
        x=random.choice(labsc)
        for v in range(5):
            y=random.randint(0,4)
            k=x
            if y==0:
                if flag1==0:
                    for j in range(4):
                        monday[k]=lab[i]
                        k=k+1
                    break
                else:
                    continue
            if y==1:
                if flag2==0:
                    for j in range(4):
                        tuesday[k]=lab[i]
                        k=k+1
                    break
                else:
                    continue
            if y==2:
                if flag3==0:
                    for j in range(4):
                        wednesday[k]=lab[i]
                        k=k+1
                    break
                else:
                    continue
            if y==3:
                if flag4==0:
                    for j in range(4):
                        thursday[k]=lab[i]
                        k=k+1
                    break
                else:
                    continue
            if y==4:
                if flag5==0:
                    for j in range(4):
                        friday[k]=lab[i]
                        k=k+1
                    break 
                else:
                    continue


    for i in range(s):
        p=subjpw[i]
        y=p
        while(p>0):
            for z in range(y):
              if(p>0):
                for c in range(40):
                    y=random.randint(0,7)
                    if z==0:
                        if monday[y]=="null":
                            monday[y]=subj[i]
                            p=p-1
                            break
                    if z==1:
                        if tuesday[y]=="null":
                            tuesday[y]=subj[i]
                            p=p-1
                            break
                    if z==2:
                        if wednesday[y]=="null":
                            wednesday[y]=subj[i]
                            p=p-1
                            break
                    if z==3:
                        if thursday[y]=="null":
                            thursday[y]=subj[i]
                            p=p-1
                            break
                    if z==4:
                        if friday[y]=="null":
                            friday[y]=subj[i]
                            p=p-1
                            break
    
 def print3(q):
    print("********************************TIME TABLE FOR THIRDYEAR IS********************************")
    print(monday)
    print(tuesday)
    print(wednesday)
    print(thursday)
    print(friday)




class finalyear:
 global lab,subj,subjp,subjpw,staff,labsc,n,s,monday,tuesday,wednesday,thursday,friday
 monday=["null","null","null","null","null","null","null","null"]
 tuesday=["null","null","null","null","null","null","null","null"]
 wednesday=["null","null","null","null","null","null","null","null"]
 thursday=["null","null","null","null","null","null","null","null"]
 friday=["null","null","null","null","null","null","null","null"]
 n=int(input("How many labs for finalyear"))
 s=int(input("How many subjets for finalyear"))
 lab=[]
 subj=[]
 subjp=[]
 subjpw=[]
 staff=[]
 labsc=[0,4]
 def input4(q):
    
    for i in range(n):
        l=input("enter lab names:")
        lab.append(l)
    
    for i in range(s):
        x=input("enter subject name\n")
        subj.append(x)
        x1=input("enter staff name\n")
        staff.append(x1)
    for i in range(s):
        x=int(input("entire total number peroids of each subject:\n"))
        subjp.append(x)
    for i in range(s):
        x=math.ceil(subjp[i]/12)
        subjpw.append(x)
    print("final year subjects:\n",subj)
    print("Subjects Total periods:\n",subjp)
    print("Subjects per week:\n",subjpw)
 def process4(q):
    flag1=0
    flag2=0
    flag3=0
    flag4=0
    flag5=0
    for i in range(n):
        for j in range(8):
            if monday[j]=="null":
                continue
            else:
                flag1=1
                break
        for a in range(8):
            if tuesday[a]=="null":
                continue
            else:
                flag2=1
                break
        for b in range(8):
            if wednesday[b]=="null":
                continue
            else:
                flag3=1
                break
        for c in range(8):
            if thursday[c]=="null":
                continue
            else:
                flag4=1
                break
        for d in range(8):
            if friday[d]=="null":
                continue
            else:
                flag5=1
                break
        x=random.choice(labsc)
        for v in range(5):
            y=random.randint(0,4)
            k=x
            if y==0:
                if flag1==0:
                    for j in range(4):
                        monday[k]=lab[i]
                        k=k+1
                    break
                else:
                    continue
            if y==1:
                if flag2==0:
                    for j in range(4):
                        tuesday[k]=lab[i]
                        k=k+1
                    break
                else:
                    continue
            if y==2:
                if flag3==0:
                    for j in range(4):
                        wednesday[k]=lab[i]
                        k=k+1
                    break
                else:
                    continue
            if y==3:
                if flag4==0:
                    for j in range(4):
                        thursday[k]=lab[i]
                        k=k+1
                    break
                else:
                    continue
            if y==4:
                if flag5==0:
                    for j in range(4):
                        friday[k]=lab[i]
                        k=k+1
                    break 
                else:
                    continue


    for i in range(s):
        p=subjpw[i]
        y=p
        while(p>0):
            for z in range(y):
              if(p>0):
                for c in range(40):
                    y=random.randint(0,7)
                    if z==0:
                        if monday[y]=="null":
                            monday[y]=subj[i]
                            p=p-1
                            break
                    if z==1:
                        if tuesday[y]=="null":
                            tuesday[y]=subj[i]
                            p=p-1
                            break
                    if z==2:
                        if wednesday[y]=="null":
                            wednesday[y]=subj[i]
                            p=p-1
                            break
                    if z==3:
                        if thursday[y]=="null":
                            thursday[y]=subj[i]
                            p=p-1
                            break
                    if z==4:
                        if friday[y]=="null":
                            friday[y]=subj[i]
                            p=p-1
                            break
    
 def print4(q):
    print("********************************TIME TABLE FOR FINALYEAR IS********************************")
    print(monday)
    print(tuesday)
    print(wednesday)
    print(thursday)
    print(friday)

if(r==1):
    obj1=firstyear()
    obj1.input1()
    obj1.process1()
    obj1.print1()
if(r==2):
    obj2=secondyear()
    obj2.input2()
    obj2.process2()
    obj2.print2()
if(r==3):
    obj3=thirdyear()
    obj3.input3()
    obj3.process3()
    obj3.print3()
if(r==4):
    obj4=finalyear()
    obj4.input4()
    obj4.process4()
    obj4.print4()
