
from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
z=[]
for row in contacts_list:
    r = row[0].split()
    if len(r) == 2:
        row[1]=r[1]
        row[0]=r[0]
    elif len(r) == 3:
        row[2] = r[2]
        row[1] = r[1]
        row[0] = r[0]
    ro=row[1].split()
    if len(ro) == 2:
        row[2]=ro[1]
        row[1]=ro[0]
    z.append(row)
    #print(row)
#print(z)

with open("itog.csv", "w", encoding="utf-8",newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(z)

with open( "itog.csv", encoding="utf8") as f:
    text = f.read()
    pattern_phone = r'(\+7|8)?\s*\(?(\d{3})\)?[\s*-]?(\d{3})[\s*-]?(\d{2})[\s*-]?(\d{2})(\s*)\(?(доб\.?)?\s*(\d*)?\)?'
    fixed_phones = re.sub(pattern_phone, r'+7(\2)\3-\4-\5\6\7\8', text)
    #print(fixed_phones)
    with open("itog.csv", 'w+', encoding="utf8") as f:
        text = f.write(fixed_phones)

with open( "itog.csv", encoding="utf8") as f:
    text = f.read()[:-1]
    Dct={}
    for st in text.split("\n"):
        #print(st.split(','))
        sp=st.split(',')
        key=sp[0]+" "+sp[1]
        value=sp
        if key not in Dct:
            Dct[key]=value
        else:
            for key0,val0 in Dct.items():
                if key == key0:
                    VAL = []
                    for w in range(len(value)):
                        if value[w] != "":
                            VAL.append(value[w])
                        elif val0[w] != "":
                            VAL.append(val0[w])
                        else:
                            VAL.append("")
                    Dct[key] = VAL
    ITOG_list=[]
    for key0, val0 in Dct.items():
        ITOG_list.append(val0)
    print(ITOG_list)

with open("itog.csv", "w", encoding="utf-8",newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(ITOG_list)



