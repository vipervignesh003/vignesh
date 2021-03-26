import random
import math
table=[]
monday=[]
tuesday=[]
wednesday=[]
thursday=[]
friday=[]
subj=[]
subjp=[]
subjpw=[]
days=["MONDAY   ","TUESDAY  ","WEDNESDAY","THURSDAY ","FRIDAY   "]
ans=1
#how many subjects for this sem
n=int(input("how many subjets"))

#input of all the subjects in the sem
for i in range(n):
    x=input("subjectname\n")
    subj.append(x)
print(subj)

#minimum periods of each subjects
for i in range(n):
    x=int(input("subjectperoids:\n"))
    subjp.append(x)
print(subjp)

#periods per week for each subjects
for i in range(n):
    x=math.ceil(subjp[i]/12)
    subjpw.append(x)
print(subjpw)

#allocating subjects randomly for monday
#while(ans==1):
for i in range(8):
    x=random.choice(subj)
    if x in monday:
        continue
    else:
        monday.append(x)
while len(monday)<n:
    for i in range(8):
        x=random.choice(subj)
        if x in monday:
            continue
        else:
            monday.append(x)
for i in range(8):
    x=random.choice(subj)
    if x in tuesday:
        continue
    else:
        tuesday.append(x)
while len(tuesday)<n:
    for i in range(8):
        x=random.choice(subj)
        if x in tuesday:
            continue
        else:
            tuesday.append(x)

for i in range(8):
    x=random.choice(subj)
    if x in wednesday:
        continue
    else:
        wednesday.append(x)
while len(wednesday)<n:
    for i in range(8):
        x=random.choice(subj)
        if x in wednesday:
            continue
        else:
            wednesday.append(x)

for i in range(8):
    x=random.choice(subj)
    if x in thursday:
        continue
    else:
        thursday.append(x)
while len(thursday)<n:
    for i in range(8):
        x=random.choice(subj)
        if x in thursday:
            continue
        else:
            thursday.append(x)

for i in range(8):
    x=random.choice(subj)
    if x in friday:
        continue
    else:
        friday.append(x)
while len(friday)<n:
    for i in range(8):
        x=random.choice(subj)
        if x in friday:
            continue
        else:
            friday.append(x)
table.append(monday)
table.append(tuesday)
table.append(wednesday)
table.append(thursday)
table.append(friday)
for i in range(5):
    print("\n",days[i],table[i])
    #ans=int(input("this table ok for you?\nyes means press 0 and no means press 1:"))
print("THANK YOU FOR CHOOSING OUR TIMETABLE SCHEDULER")
