import random
import re

from copy import deepcopy
no = 0
def wordInString(word, string_value):
    return True if re.search(r'\b' + word + r'\b', string_value) else False
def find_test_cases(s):
    positive_result = {}
    Negative_result = {}
    Corner_result = {}
    if "&&" not in s:
        if wordInString("/",s) :
            res1 = s.split("/")
            if "==" in res1[1]:
                res2 = res1[1].split("==")
                if (res2[0].isdigit() and res2[1].isdigit()):
                    positive_result[res1[0]] = int(res2[0]) * int(res2[1])
                    Negative_result[res1[0]] = int(res2[0]) * int(res2[1]) - 1
                else :
                    positive_result[res1[0]] = int(res2[1])
                    positive_result[res2[0]] = 1
                    Negative_result[res1[0]] = int(res2[1]) -1
                    Negative_result[res2[0]] = 1
                    Corner_result[res2[0]] = 0
            elif "!=" in res1[1]:
                res2 = res1[1].split("!=")
                if (res2[0].isdigit() and res2[1].isdigit()):
                    positive_result[res1[0]] = int(res2[0]) * int(res2[1]) -1
                    Negative_result[res1[0]] = int(res2[0]) * int(res2[1])
                else :
                    positive_result[res1[0]] = int(res2[1]) -1
                    positive_result[res2[0]] = 1
                    Negative_result[res1[0]] = int(res2[1])
                    Negative_result[res2[0]] = 1
                    Corner_result[res2[0]] = 0
            #return positive_result, Negative_result, Corner_result
        elif wordInString(">=",s)   or wordInString("<=",s):
            if ">=" in s:
              res = s.split(">=")
            else:
              res = s.split("<=")
            if(res[1].isdigit()):
                positive_result[res[0]]=int(res[1])
                Negative_result[res[0]] = int(res[1]) -1
            else:
                positive_result[res[0]] = random.randint(1,20)
                positive_result[res[1]] = positive_result[res[0]]
                Negative_result[res[0]] = random.randint(1, 20)
                if(wordInString(">=",s)):
                    Negative_result[res[1]] = Negative_result[res[0]] + 1
                else:
                    Negative_result[res[1]] = Negative_result[res[0]] - 1


        elif wordInString("%",s):
            res1 = s.split("%")
            if "==0" in res1[1]:
                res2 = res1[1].split("==")
                if(res2[0].isdigit()):
                    positive_result[res1[0]] = int(res2[0]) * int(res2[0])
                else:
                    positive_result[res2[0]] = random.randint(1,5)
                    positive_result[res1[0]] = positive_result[res2[0]] *positive_result[res2[0]]
                    Negative_result[res1[0]] = random.randint(1,5)
                    Negative_result[res2[0]] = Negative_result[res1[0]] +5
            elif "!=0" in res1[1]:
                res2 = res1[1].split("!=")
                if (res2[0].isdigit()):
                    positive_result[res1[0]] = int(res2[0]) * int(res2[0]) + 1
        elif wordInString(">",s):
            res = s.split(">")
            if (res[1].isdigit()):
                positive_result[res[0]] = int(res[1]) - 1
                Negative_result[res[0]] = int(res[1])
            else:
                positive_result[res[0]] = random.randint(1, 20)
                positive_result[res[1]] = positive_result[res[0]] -1
                Negative_result[res[0]] = positive_result[res[0]]
                Negative_result[res[1]] = positive_result[res[0]]
        elif wordInString("!=",s):
            res = s.split("!=")
            if (res[1].isdigit()):
                positive_result[res[0]] = int(res[1]) - 1
                Negative_result[res[0]] = int(res[1])
            else:
                positive_result[res[0]] = random.randint(1, 20)
                positive_result[res[1]] = positive_result[res[0]] - 1
                Negative_result[res[0]] = positive_result[res[0]]
                Negative_result[res[1]] = positive_result[res[0]]
        elif wordInString("==",s):
            res = s.split("==")
            if (res[1].isdigit()):
                positive_result[res[0]] = int(res[1])
                Negative_result[res[0]] = int(res[1]) -1
            else:
                positive_result[res[0]] = random.randint(1, 20)
                positive_result[res[1]] = positive_result[res[0]]
                Negative_result[res[0]] = positive_result[res[0]]
                Negative_result[res[1]] = positive_result[res[0]] -1
        elif wordInString("<",s):
            res = s.split("<")
            if (res[1].isdigit()):
                positive_result[res[0]] = int(res[1]) + 1
                Negative_result[res[0]] = int(res[1])
            else:
                positive_result[res[0]] = random.randint(1, 20)
                positive_result[res[1]] = positive_result[res[0]] + 1
                Negative_result[res[0]] = positive_result[res[0]]
                Negative_result[res[1]] = positive_result[res[0]]

    return positive_result ,Negative_result ,Corner_result




q=""
temp = tuple()
temp = ("if","endif")
#list = ["if","elif","for","while"]
list = []
list.append(temp)
temp = ("elif","endif")
list.append(temp)
temp = ("for","endfor")
list.append(temp)
temp = ("while","endwhile")
list.append(temp)


ret_val = []



def CheckForMe(list,s):
    if (wordInString(list[0][0],s)):
        return True , list[0]
    elif (wordInString(list[1][0],s)):
        return True, list[1]
    elif (wordInString(list[2][0],s)):
        return True, list[2]
    elif (wordInString(list[3][0],s)):
        return True, list[3]
    else :
        return False ,None
    #return True if (wordInString(list[0][0],s) or wordInString(list[1][0],s) or
     #               wordInString(list[2][0],s) or wordInString(list[3][0],s)) else False
no = 1
with open('mido.txt', 'r') as file:
    data = file.readlines()
cor = []
def Compinations(data,lineNo,val):
    global ret_val
    dontPrint = False
    if lineNo == 0:
        dontPrint = True
    q=""
    for l in range(lineNo,len(data)):
        if "#" in data[l] and dontPrint is False:
            global no
            with open('test' + str(no) + '.txt', 'w') as file:
                file.writelines(data)
            no += 1
            te = deepcopy(val)
            ret_val.append(te)
            val.clear()
            return
        check, tem = CheckForMe(list, data[l])
        if (check):
            var = []
            sub_var = tuple()
            for i in range(len(data[l])):
                if (data[l][i] == '('):
                    for j in range(i + 1, len(data[l])):
                        if data[l][j] == ')':
                            break
                        if (data[l][j].isalpha()):
                            sub_var = (data[l][j], j)
                            var.append(sub_var)
                        q += data[l][j]
                    x_p, x_n, x_c = find_test_cases(q)
                    t = tuple()
                    t = (x_p,x_n)
                    v_p = deepcopy(val)
                    v_n = deepcopy(val)
                    v_p.append(x_p)
                    v_n.append(x_n)
                    if (len(x_c)!=0):
                        global cor
                        cor.append(x_c)
                    newP = deepcopy(data)
                    newN = deepcopy(data)

                    #print(data)
                    for key in x_p.keys():
                        for item in var:
                            # print(key)
                            if (key == item[0]):
                                for a in range (len(newP[l])):
                                   if(newP[l][a]==item[0]):
                                        newP[l] = (newP[l].replace(newP[l][a], str(x_p[key])))
                                        break
                    for key in x_n.keys():
                        for item in var:
                            # print(key)
                            if (key == item[0]):
                                #newN = data
                                for a in range(len(newN[l])):
                                    if(newN[l][a]==item[0]):
                                        newN[l] = (newN[l].replace(newN[l][a], str(x_n[key])))
                                        break
                                #print(newN)
                                # print(line)


                    Compinations(newP,l+1,v_p)
                    Compinations(newN,l+1,v_n)
                    return
val = []
Compinations(data,0,val)
for itr in  range(len(ret_val)):
    with open("MetaData.txt", "a") as myfile:
     myfile.write("input for test case "+str(itr+1)+" "+str(ret_val[itr]) + "\n")
if(cor!=None):
    for i in cor:
        with open("MetaData.txt", "a") as myfile:
            myfile.write("input for Courner test case " + str(itr + 1) + " " + str(i) + "\n")

