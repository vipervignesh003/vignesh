import math
import random
global s
ans="y"
while(ans=="y"):
    r=int(input("enter your year"))
    if r==1:
        class firstyear:
            #global lab,subj,subjp,subjpw,staff,labsc,n,s,monday,tuesday,wednesday,thursday,friday
            monday1=["null","null","null","null","null","null","null","null"]
            tuesday1=["null","null","null","null","null","null","null","null"]
            wednesday1=["null","null","null","null","null","null","null","null"]
            thursday1=["null","null","null","null","null","null","null","null"]
            friday1=["null","null","null","null","null","null","null","null"]
            n=int(input("How many labs for firstyear"))
            s=int(input("how many subjets for firstyear"))
            lab1=[]
            subj1=[]
            subjp1=[]
            subjpw1=[]
            staff1=[]
            labsc1=[0,4]
            for i in range(n):
                    l=input("enter lab names:")
                    lab1.append(l)
            for i in range(s):
                    x=input("enter subject name\n")
                    subj1.append(x)
                    x1=input("enter staff name\n")
                    staff1.append(x1)
            for i in range(s):
                    x=int(input("entire total number peroids of each subject:\n"))
                    subjp1.append(x)
            for i in range(s):
                    x=math.ceil(subjp1[i]/12)
                    subjpw1.append(x)
            print("firstyear subjects:\n",subj1)
            print("Subjects Total periods:\n",subjp1)
            print("Subjects per week:\n",subjpw1)
            flag1=0
            flag2=0
            flag3=0
            flag4=0
            flag5=0
            for i in range(n):
                for j in range(8):
                    if monday1[j]=="null":
                            continue
                    else:
                            flag1=1
                            break
                for a in range(8):
                    if tuesday1[a]=="null":
                            continue
                    else:
                            flag2=1
                            break
                for b in range(8):
                    if wednesday1[b]=="null":
                            continue
                    else:
                            flag3=1
                            break
                for c in range(8):
                    if thursday1[c]=="null":
                            continue
                    else:
                            flag4=1
                            break
                for d in range(8):
                    if friday1[d]=="null":
                            continue
                    else:
                            flag5=1
                            break
            x=random.choice(labsc1)
            for v in range(5):
                        y=random.randint(0,4)
                        k=x
                        if y==0:
                            if flag1==0:
                                for j in range(4):
                                    monday1[k]=lab1[i]
                                    k=k+1
                                break
                            else:
                                continue
                        if y==1:
                            if flag2==0:
                                for j in range(4):
                                    tuesday1[k]=lab1[i]
                                    k=k+1
                                break
                            else:
                                continue
                        if y==2:
                            if flag3==0:
                                for j in range(4):
                                    wednesday1[k]=lab1[i]
                                    k=k+1
                                break
                            else:
                                continue
                        if y==3:
                            if flag4==0:
                                for j in range(4):
                                    thursday1[k]=lab1[i]
                                    k=k+1
                                break
                            else:
                                continue
                        if y==4:
                            if flag5==0:
                                for j in range(4):
                                    friday1[k]=lab1[i]
                                    k=k+1
                                break 
                            else:
                                continue
            for i in range(s):
                    p=subjpw1[i]
                    y=p
                    while(p>0):
                        for z in range(y):
                          if(p>0):
                            for c in range(40):
                                y=random.randint(0,7)
                                if z==0:
                                    if monday1[y]=="null":
                                        monday1[y]=subj1[i]
                                        p=p-1
                                        break
                                if z==1:
                                    if tuesday1[y]=="null":
                                        tuesday1[y]=subj1[i]
                                        p=p-1
                                        break
                                if z==2:
                                    if wednesday1[y]=="null":
                                        wednesday1[y]=subj1[i]
                                        p=p-1
                                        break
                                if z==3:
                                    if thursday1[y]=="null":
                                        thursday1[y]=subj1[i]
                                        p=p-1
                                        break
                                if z==4:
                                    if friday1[y]=="null":
                                        friday1[y]=subj1[i]
                                        p=p-1
                                        break
            print("**********************CLASS WISE TIME TABLE FOR FIRSTYEAR IS**********************")
            print(monday1)
            print(tuesday1)
            print(wednesday1)
            print(thursday1)
            print(friday1)
            sub1=list(subj1)
            print("\n")
            mon1=list(monday1)
            tue1=list(tuesday1)
            wed1=list(wednesday1)
            thurs1=list(thursday1)
            fri1=list(friday1)
            print("\n")
            #STAFF WISE TIMETABLE
            for i in range(s):
                for j in range(8):
                    if (sub1[i]==mon1[j]):
                        mon1[j]=staff1[i]
                    if (sub1[i]==tue1[j]):
                        tue1[j]=staff1[i]
                    if sub1[i]==wed1[j]:
                        wed1[j]=staff1[i]
                    if sub1[i]==thurs1[j]:
                        thurs1[j]=staff1[i]
                    if sub1[i]==fri1[j]:
                        fri1[j]=staff1[i]
            print("**********************STAFF WISE TIMETABLE**********************")
            print(mon1)
            print(tue1)
            print(wed1)
            print(thurs1)
            print(fri1)
            def process1(v):
                for i in range(s):
                    p=subjpw1[i]
                    y=p
                    while(p>0):
                        for z in range(y):
                          if(p>0):
                            for c in range(40):
                                y=random.randint(0,7)
                                if z==0:
                                    if monday1[y]=="null":
                                        monday1[y]=subj1[i]
                                        p=p-1
                                        break
                                if z==1:
                                    if tuesday1[y]=="null":
                                        tuesday1[y]=subj1[i]
                                        p=p-1
                                        break
                                if z==2:
                                    if wednesday1[y]=="null":
                                        wednesday1[y]=subj1[i]
                                        p=p-1
                                        break
                                if z==3:
                                    if thursday1[y]=="null":
                                        thursday1[y]=subj1[i]
                                        p=p-1
                                        break
                                if z==4:
                                    if friday1[y]=="null":
                                        friday1[y]=subj1[i]
                                        p=p-1
                                        break
                for i in range(s):
                    for j in range(8):
                        if (sub1[i]==mon1[j]):
                            mon1[j]=staff1[i]
                        if (sub1[i]==tue1[j]):
                            tue1[j]=staff1[i]
                        if sub1[i]==wed1[j]:
                            wed1[j]=staff1[i]
                        if sub1[i]==thurs1[j]:
                            thurs1[j]=staff1[i]
                        if sub1[i]==fri1[j]:
                            fri1[j]=staff1[i]
        obj1=firstyear()
    if r==2:
        class secondyear:
            global lab,subj,subjp,subjpw,staff,labsc,n,s,monday,tuesday,wednesday,thursday,friday
            monday2=["null","null","null","null","null","null","null","null"]
            tuesday2=["null","null","null","null","null","null","null","null"]
            wednesday2=["null","null","null","null","null","null","null","null"]
            thursday2=["null","null","null","null","null","null","null","null"]
            friday2=["null","null","null","null","null","null","null","null"]
            n=int(input("How many labs for secondyear"))
            s=int(input("how many subjets for secondyear"))
            lab2=[]
            subj2=[]
            subjp2=[]
            subjpw2=[]
            staff2=[]
            labsc2=[0,4]
            for i in range(n):
                    l=input("enter lab names:")
                    lab2.append(l)
            for i in range(s):
                    x=input("enter subject name\n")
                    subj2.append(x)
                    x1=input("enter staff name\n")
                    staff2.append(x1)
            for i in range(s):
                    x=int(input("entire total number peroids of each subject:\n"))
                    subjp2.append(x)
            for i in range(s):
                    x=math.ceil(subjp2[i]/12)
                    subjpw2.append(x)
            print("secondyear subjects:\n",subj2)
            print("Subjects Total periods:\n",subjp2)
            print("Subjects per week:\n",subjpw2)
            flag1=0
            flag2=0
            flag3=0
            flag4=0
            flag5=0
            for i in range(n):
                for j in range(8):
                    if monday2[j]=="null":
                            continue
                    else:
                            flag=1
                            break
                for a in range(8):
                    if tuesday2[a]=="null":
                            continue
                    else:
                            flag2=1
                            break
                for b in range(8):
                    if wednesday2[b]=="null":
                            continue
                    else:
                            flag3=1
                            break
                for c in range(8):
                    if thursday2[c]=="null":
                            continue
                    else:
                            flag4=1
                            break
                for d in range(8):
                    if friday2[d]=="null":
                            continue
                    else:
                            flag5=1
                            break
                x=random.choice(labsc2)
                for v in range(5):
                        y=random.randint(0,4)
                        k=x
                        if y==0:
                            if flag1==0:
                                for j in range(4):
                                    monday2[k]=lab2[i]
                                    k=k+1
                                break
                            else:
                                continue
                        if y==1:
                            if flag2==0:
                                for j in range(4):
                                    tuesday2[k]=lab2[i]
                                    k=k+1
                                break
                            else:
                                continue
                        if y==2:
                            if flag3==0:
                                for j in range(4):
                                    wednesday2[k]=lab2[i]
                                    k=k+1
                                break
                            else:
                                continue
                        if y==3:
                            if flag4==0:
                                for j in range(4):
                                    thursday2[k]=lab2[i]
                                    k=k+1
                                break
                            else:
                                continue
                        if y==4:
                            if flag5==0:
                                for j in range(4):
                                    friday2[k]=lab2[i]
                                    k=k+1
                                break 
                            else:
                                continue
            for i in range(s):
                    p=subjpw2[i]
                    y=p
                    while(p>0):
                        for z in range(y):
                          if(p>0):
                            for c in range(40):
                                y=random.randint(0,7)
                                if z==0:
                                    if monday2[y]=="null":
                                        monday2[y]=subj2[i]
                                        p=p-1
                                        break
                                if z==1:
                                    if tuesday2[y]=="null":
                                        tuesday2[y]=subj2[i]
                                        p=p-1
                                        break
                                if z==2:
                                    if wednesday2[y]=="null":
                                        wednesday2[y]=subj2[i]
                                        p=p-1
                                        break
                                if z==3:
                                    if thursday2[y]=="null":
                                        thursday2[y]=subj2[i]
                                        p=p-1
                                        break
                                if z==4:
                                    if friday2[y]=="null":
                                        friday2[y]=subj2[i]
                                        p=p-1
                                        break
            print("**********************CLASS WISE TIME TABLE FOR SECOND YEAR IS**********************")
            print(monday2)
            print(tuesday2)
            print(wednesday2)
            print(thursday2)
            print(friday2)
            sub2=list(subj2)
            print("\n")
            mon2=list(monday2)
            tue2=list(tuesday2)
            wed2=list(wednesday2)
            thurs2=list(thursday2)
            fri2=list(friday2)
            print("\n")
            #STAFF WISE TIMETABLE
            for i in range(s):
                for j in range(8):
                    if (sub2[i]==mon2[j]):
                        mon2[j]=staff2[i]
                    if (sub2[i]==tue2[j]):
                        tue2[j]=staff2[i]
                    if sub2[i]==wed2[j]:
                        wed2[j]=staff2[i]
                    if sub2[i]==thurs2[j]:
                        thurs2[j]=staff2[i]
                    if sub2[i]==fri2[j]:
                        fri2[j]=staff2[i]
            print("**********************STAFF WISE TIMETABLE**********************")
            print(mon2)
            print(tue2)
            print(wed2)
            print(thurs2)
            print(fri2)
            def process2(v):
                for i in range(s):
                    p=subjpw2[i]
                    y=p
                    while(p>0):
                        for z in range(y):
                          if(p>0):
                            for c in range(40):
                                y=random.randint(0,7)
                                if z==0:
                                    if monday2[y]=="null":
                                        monday2[y]=subj2[i]
                                        p=p-1
                                        break
                                if z==1:
                                    if tuesday2[y]=="null":
                                        tuesday2[y]=subj2[i]
                                        p=p-1
                                        break
                                if z==2:
                                    if wednesday2[y]=="null":
                                        wednesday2[y]=subj2[i]
                                        p=p-1
                                        break
                                if z==3:
                                    if thursday2[y]=="null":
                                        thursday2[y]=subj2[i]
                                        p=p-1
                                        break
                                if z==4:
                                    if friday2[y]=="null":
                                        friday2[y]=subj2[i]
                                        p=p-1
                                        break
                for i in range(s):
                    for j in range(8):
                        if (sub2[i]==mon2[j]):
                            mon2[j]=staff2[i]
                        if (sub2[i]==tue2[j]):
                            tue2[j]=staff2[i]
                        if sub2[i]==wed2[j]:
                            wed2[j]=staff2[i]
                        if sub2[i]==thurs2[j]:
                            thurs2[j]=staff2[i]
                        if sub2[i]==fri2[j]:
                            fri2[j]=staff2[i]
        obj2=secondyear()

    if r==3:
        class thirdyear:
            global lab,subj,subjp,subjpw,staff,labsc,n,s,monday,tuesday,wednesday,thursday,friday
            monday3=["null","null","null","null","null","null","null","null"]
            tuesday3=["null","null","null","null","null","null","null","null"]
            wednesday3=["null","null","null","null","null","null","null","null"]
            thursday3=["null","null","null","null","null","null","null","null"]
            friday3=["null","null","null","null","null","null","null","null"]
            n=int(input("How many labs for thirdyear"))
            s=int(input("how many subjets for thirdyear"))
            lab3=[]
            subj3=[]
            subjp3=[]
            subjpw3=[]
            staff3=[]
            labsc3=[0,4]
            for i in range(n):
                    l=input("enter lab names:")
                    lab3.append(l)
            for i in range(s):
                    x=input("enter subject name\n")
                    subj3.append(x)
                    x1=input("enter staff name\n")
                    staff3.append(x1)
            for i in range(s):
                    x=int(input("entire total number peroids of each subject:\n"))
                    subjp3.append(x)
            for i in range(s):
                    x=math.ceil(subjp3[i]/12)
                    subjpw3.append(x)
            print("thirdyear subjects:\n",subj3)
            print("Subjects Total periods:\n",subjp3)
            print("Subjects per week:\n",subjpw3)
            flag1=0
            flag2=0
            flag3=0
            flag4=0
            flag5=0
            for i in range(n):
                for j in range(8):
                    if monday3[j]=="null":
                            continue
                    else:
                            flag1=1
                            break
                for a in range(8):
                    if tuesday3[a]=="null":
                            continue
                    else:
                            flag2=1
                            break
                for b in range(8):
                    if wednesday3[b]=="null":
                            continue
                    else:
                            flag3=1
                            break
                for c in range(8):
                    if thursday3[c]=="null":
                            continue
                    else:
                            flag4=1
                            break
                for d in range(8):
                    if friday3[d]=="null":
                            continue
                    else:
                            flag5=1
                            break
            x=random.choice(labsc3)
            for v in range(5):
                        y=random.randint(0,4)
                        k=x
                        if y==0:
                            if flag1==0:
                                for j in range(4):
                                    monday3[k]=lab3[i]
                                    k=k+1
                                break
                            else:
                                continue
                        if y==1:
                            if flag2==0:
                                for j in range(4):
                                    tuesday3[k]=lab3[i]
                                    k=k+1
                                break
                            else:
                                continue
                        if y==2:
                            if flag3==0:
                                for j in range(4):
                                    wednesday3[k]=lab3[i]
                                    k=k+1
                                break
                            else:
                                continue
                        if y==3:
                            if flag4==0:
                                for j in range(4):
                                    thursday3[k]=lab3[i]
                                    k=k+1
                                break
                            else:
                                continue
                        if y==4:
                            if flag5==0:
                                for j in range(4):
                                    friday3[k]=lab3[i]
                                    k=k+1
                                break 
                            else:
                                continue
            for i in range(s):
                    p=subjpw3[i]
                    y=p
                    while(p>0):
                        for z in range(y):
                          if(p>0):
                            for c in range(40):
                                y=random.randint(0,7)
                                if z==0:
                                    if monday3[y]=="null":
                                        monday3[y]=subj3[i]
                                        p=p-1
                                        break
                                if z==1:
                                    if tuesday3[y]=="null":
                                        tuesday3[y]=subj3[i]
                                        p=p-1
                                        break
                                if z==2:
                                    if wednesday3[y]=="null":
                                        wednesday3[y]=subj3[i]
                                        p=p-1
                                        break
                                if z==3:
                                    if thursday3[y]=="null":
                                        thursday3[y]=subj3[i]
                                        p=p-1
                                        break
                                if z==4:
                                    if friday3[y]=="null":
                                        friday3[y]=subj3[i]
                                        p=p-1
                                        break
            print("**********************CLASS WISE TIME TABLE FOR THIRDYEAR IS**********************")
            print(monday3)
            print(tuesday3)
            print(wednesday3)
            print(thursday3)
            print(friday3)
            sub3=list(subj3)
            print("\n")
            mon3=list(monday3)
            tue3=list(tuesday3)
            wed3=list(wednesday3)
            thurs3=list(thursday3)
            fri3=list(friday3)
            print("\n")
            #STAFF WISE TIMETABLE
            for i in range(s):
                for j in range(8):
                    if (sub3[i]==mon3[j]):
                        mon3[j]=staff3[i]
                    if (sub3[i]==tue3[j]):
                        tue3[j]=staff3[i]
                    if sub3[i]==wed3[j]:
                        wed3[j]=staff3[i]
                    if sub3[i]==thurs3[j]:
                        thurs3[j]=staff3[i]
                    if sub3[i]==fri3[j]:
                        fri3[j]=staff3[i]
            print("**********************STAFF WISE TIMETABLE**********************")
            print(mon3)
            print(tue3)
            print(wed3)
            print(thurs3)
            print(fri3)
            def process3(v):
                for i in range(s):
                    p=subjpw3[i]
                    y=p
                    while(p>0):
                        for z in range(y):
                          if(p>0):
                            for c in range(40):
                                y=random.randint(0,7)
                                if z==0:
                                    if monday3[y]=="null":
                                        monday3[y]=subj3[i]
                                        p=p-1
                                        break
                                if z==1:
                                    if tuesday3[y]=="null":
                                        tuesday3[y]=subj3[i]
                                        p=p-1
                                        break
                                if z==2:
                                    if wednesday3[y]=="null":
                                        wednesday3[y]=subj3[i]
                                        p=p-1
                                        break
                                if z==3:
                                    if thursday3[y]=="null":
                                        thursday3[y]=subj3[i]
                                        p=p-1
                                        break
                                if z==4:
                                    if friday3[y]=="null":
                                        friday3[y]=subj3[i]
                                        p=p-1
                                        break
                for i in range(s):
                    for j in range(8):
                        if (sub3[i]==mon3[j]):
                            mon3[j]=staff3[i]
                        if (sub3[i]==tue3[j]):
                            tue3[j]=staff3[i]
                        if sub3[i]==wed3[j]:
                            wed3[j]=staff3[i]
                        if sub3[i]==thurs3[j]:
                            thurs3[j]=staff3[i]
                        if sub3[i]==fri3[j]:
                            fri3[j]=staff3[i]
        obj3=thirdyear()

    if r==4:
        class finalyear:
            global lab,subj,subjp,subjpw,staff,labsc,n,s,monday,tuesday,wednesday,thursday,friday
            monday4=["null","null","null","null","null","null","null","null"]
            tuesday4=["null","null","null","null","null","null","null","null"]
            wednesday4=["null","null","null","null","null","null","null","null"]
            thursday4=["null","null","null","null","null","null","null","null"]
            friday4=["null","null","null","null","null","null","null","null"]
            n=int(input("How many labs for finalyear"))
            s=int(input("how many subjets for finalyear"))
            lab4=[]
            subj4=[]
            subjp4=[]
            subjpw4=[]
            staff4=[]
            labsc4=[0,4]
            for i in range(n):
                    l=input("enter lab names:")
                    lab4.append(l)
            for i in range(s):
                    x=input("enter subject name\n")
                    subj4.append(x)
                    x1=input("enter staff name\n")
                    staff4.append(x1)
            for i in range(s):
                    x=int(input("entire total number peroids of each subject:\n"))
                    subjp4.append(x)
            for i in range(s):
                    x=math.ceil(subjp4[i]/12)
                    subjpw4.append(x)
            print("finalyear subjects:\n",subj4)
            print("Subjects Total periods:\n",subjp4)
            print("Subjects per week:\n",subjpw4)
            flag1=0
            flag2=0
            flag3=0
            flag4=0
            flag5=0
            for i in range(n):
                for j in range(8):
                    if monday4[j]=="null":
                            continue
                    else:
                            flag1=1
                            break
                for a in range(8):
                    if tuesday4[a]=="null":
                            continue
                    else:
                            flag2=1
                            break
                for b in range(8):
                    if wednesday4[b]=="null":
                            continue
                    else:
                            flag3=1
                            break
                for c in range(8):
                    if thursday4[c]=="null":
                            continue
                    else:
                            flag4=1
                            break
                for d in range(8):
                    if friday4[d]=="null":
                            continue
                    else:
                            flag5=1
                            break
            x=random.choice(labsc4)
            for v in range(5):
                        y=random.randint(0,4)
                        k=x
                        if y==0:
                            if flag1==0:
                                for j in range(4):
                                    monday4[k]=lab4[i]
                                    k=k+1
                                break
                            else:
                                continue
                        if y==1:
                            if flag2==0:
                                for j in range(4):
                                    tuesday4[k]=lab4[i]
                                    k=k+1
                                break
                            else:
                                continue
                        if y==2:
                            if flag3==0:
                                for j in range(4):
                                    wednesday4[k]=lab4[i]
                                    k=k+1
                                break
                            else:
                                continue
                        if y==3:
                            if flag4==0:
                                for j in range(4):
                                    thursday4[k]=lab4[i]
                                    k=k+1
                                break
                            else:
                                continue
                        if y==4:
                            if flag5==0:
                                for j in range(4):
                                    friday4[k]=lab4[i]
                                    k=k+1
                                break 
                            else:
                                continue
            for i in range(s):
                    p=subjpw4[i]
                    y=p
                    while(p>0):
                        for z in range(y):
                          if(p>0):
                            for c in range(40):
                                y=random.randint(0,7)
                                if z==0:
                                    if monday4[y]=="null":
                                        monday4[y]=subj4[i]
                                        p=p-1
                                        break
                                if z==1:
                                    if tuesday4[y]=="null":
                                        tuesday4[y]=subj4[i]
                                        p=p-1
                                        break
                                if z==2:
                                    if wednesday4[y]=="null":
                                        wednesday4[y]=subj4[i]
                                        p=p-1
                                        break
                                if z==3:
                                    if thursday4[y]=="null":
                                        thursday4[y]=subj4[i]
                                        p=p-1
                                        break
                                if z==4:
                                    if friday4[y]=="null":
                                        friday4[y]=subj4[i]
                                        p=p-1
                                        break
            print("**********************CLASS WISE TIME TABLE FOR FINALYEAR IS**********************")
            print(monday4)
            print(tuesday4)
            print(wednesday4)
            print(thursday4)
            print(friday4)
            sub4=list(subj4)
            print("\n")
            mon4=list(monday4)
            tue4=list(tuesday4)
            wed4=list(wednesday4)
            thurs4=list(thursday4)
            fri4=list(friday4)
            print("\n")
            #STAFF WISE TIMETABLE
            for i in range(s):
                for j in range(8):
                    if (sub4[i]==mon4[j]):
                        mon4[j]=staff4[i]
                    if (sub4[i]==tue4[j]):
                        tue4[j]=staff4[i]
                    if sub4[i]==wed4[j]:
                        wed4[j]=staff4[i]
                    if sub4[i]==thurs4[j]:
                        thurs4[j]=staff4[i]
                    if sub4[i]==fri4[j]:
                        fri4[j]=staff4[i]
            print("**********************STAFF WISE TIMETABLE**********************")
            print(mon4)
            print(tue4)
            print(wed4)
            print(thurs4)
            print(fri4)
            def process4(v):
                for i in range(s):
                    p=subjpw4[i]
                    y=p
                    while(p>0):
                        for z in range(y):
                          if(p>0):
                            for c in range(40):
                                y=random.randint(0,7)
                                if z==0:
                                    if monday4[y]=="null":
                                        monday4[y]=subj4[i]
                                        p=p-1
                                        break
                                if z==1:
                                    if tuesday4[y]=="null":
                                        tuesday4[y]=subj4[i]
                                        p=p-1
                                        break
                                if z==2:
                                    if wednesday4[y]=="null":
                                        wednesday4[y]=subj4[i]
                                        p=p-1
                                        break
                                if z==3:
                                    if thursday4[y]=="null":
                                        thursday4[y]=subj4[i]
                                        p=p-1
                                        break
                                if z==4:
                                    if friday4[y]=="null":
                                        friday4[y]=subj4[i]
                                        p=p-1
                                        break
                for i in range(s):
                    for j in range(8):
                        if (sub4[i]==mon4[j]):
                            mon4[j]=staff4[i]
                        if (sub4[i]==tue4[j]):
                            tue4[j]=staff4[i]
                        if sub4[i]==wed4[j]:
                            wed4[j]=staff4[i]
                        if sub4[i]==thurs4[j]:
                            thurs4[j]=staff4[i]
                        if sub4[i]==fri4[j]:
                            fri4[j]=staff4[i]
        obj4=finalyear()
    ans=input("\nPRESS Y TO ENTER OTHER YEAR DETAILS:\t")
print(sub1)
for i in range(8):
    if obj1.mon1 and obj2.mon2:
        if(obj1.mon1[i]==obj2.mon2[i]):
            obj1.process1()
        else:
            print("")
            continue
        if(obj1.tue1[i]==obj2.tue2[i]):
               obj1.process1()
        else:
               continue
        if(obj1.wed1[i]==obj2.wed2[i]):
               obj1.process1()
        else:
               continue
        if(obj1.thurs1[i]==obj2.thurs2[i]):
               obj1.process1()
        else:
               continue
        if(obj1.fri1[i]==obj2.fri2[i]):
               obj1.process1()
        else:
               continue
for i in range(8):
    if obj1.mon1 and obj3.mon3:
        if(obj1.mon1[i]==obj3.mon3[i]):
            obj1.process1()
        else:
           continue
        if(obj1.tue1[i]==obj3.tue3[i]):
            obj1.process1()
        else:
            continue
        if(obj1.wed1[i]==obj3.wed3[i]):
            obj1.process1()
        else:
               continue
        if(obj1.thurs1[i]==obj3.thurs3[i]):
            obj1.process1()
        else:
               continue
        if(obj1.fri1[i]==obj3.fri3[i]):
            obj1.process1()
        else:
               continue
for i in range(8):
    if obj1.mon1 and obj4.mon4:
        if(obj1.mon1[i]==obj4.mon4[i]):
            obj1.process1()
        else:
               continue
        if(obj1.tue1[i]==obj4.tue4[i]):
            obj1.process1()
        else:
               continue
        if(obj1.wed1[i]==obj4.wed4[i]):
            obj1.process1()
        else:
               continue
        if(obj1.thurs1[i]==obj4.thurs4[i]):
            obj1.process1()
        else:
               continue
        if(obj1.fri1[i]==obj4.fri4[i]):
            obj1.process1()
        else:
               continue
for i in range(8):
    if mon2 and mon3:
        if(obj2.mon2[i]==obj3.mon3[i]):
            obj2.process2()
        else:
               continue
        if(obj2.tue2[i]==obj3.tue3[i]):
            obj2.process2()
        else:
               continue
        if(obj2.wed2[i]==obj3.wed3[i]):
            obj2.process2()
        else:
               continue
        if(obj2.thurs2[i]==obj3.thurs3[i]):
            obj2.process2()
        else:
               continue
        if(obj2.fri2[i]==obj3.fri3[i]):
            obj2.process2()
        else:
               continue
for i in range(8):
    if mon2 and mon4:
        if(obj2.mon2[i]==obj4.mon4[i]):
            obj2.process2()
        else:
               continue
        if(obj2.tue2[i]==obj4.tue4[i]):
            obj2.process2()
        else:
               continue
        if(obj2.wed2[i]==obj4.wed4[i]):
            obj2.process2()
        else:
               continue
        if(obj2.thurs2[i]==obj4.thurs4[i]):
            obj2.process2()
        else:
               continue
        if(obj2.fri2[i]==obj4.fri4[i]):
            obj2.process2()
        else:
               continue
for i in range(8):
    if mon3 and mon4:
        if(obj3.mon3[i]==obj4.mon4[i]):
            obj3.process3()
        else:
               continue
        if(obj3.tue3[i]==obj4.tue4[i]):
            obj3.process3()
        else:
               continue
        if(obj3.wed3[i]==obj4.wed4[i]):
            obj3.process3()
        else:
               continue
        if(obj3.thurs3[i]==obj4.thurs4[i]):
            obj3.process3()
        else:
               continue
        if(obj3.fri3[i]==obj4.fri4[i]):
            obj3.process3()
        else:
               continue
print(monday1)
print(tuesday1)
print(wednesday1)
print(thursday1)
print(friday1)
print("\n",monday2)
print(tuesday2)
print(wednesday2)
print(thursday2)
print(friday2)
print("\n",monday3)
print(tuesday3)
print(wednesday3)
print(thursday3)
print(friday3)
print("\n",monday4)
print(tuesday4)
print(wednesday4)
print(thursday4)
print(friday4)
print("*************************THANK YOU FOR CHOOSING OUR SCHEDULER*************************")
#obj5=comparision()
#obj5.comp()"""
