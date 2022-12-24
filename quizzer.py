#program to have a test on networking full forms


def question_add(num):
    qst_add=open("questions.txt","a")
    ans_add=open("anss.txt","a")
    for i in range(num):
        q=input(f"[Q{i+1}] : ")
        a=input(f"[A{i+1}] : ")
        print("-----------------------")
        qst_add.write(q+",")
        ans_add.write(a+",")
    qst_add.close()
    ans_add.close()

print('''
###################################
## @@@@           //  @@         ##
## @  @          //  @  @        ##
## @@@@ UESTION //  @@@@@@ NSWER ##
##   @         //  @      @      ##
###################################
''')
ask=input("[+] want to add Question-answers? [y/n] : ")
topic = input("Quiz Topic : ")
if ask.lower() == "y" or ask.lower()=="yes":
    num=int(input("number of questions to add : "))
    question_add(num)
elif ask.lower() == "n" or ask.lower()=="no":
    pass
else:
    print("no reply :( ") 

f_q=open("questions.txt","a+")
f_q.seek(0)
count_qust=f_q.read().split(",")[:-1]
f_q.close()

f_a=open("anss.txt","a+")
f_a.seek(0)
count_ans=f_a.read().split(",")[:-1]
f_a.close()
print()

f_dbt=open("doubts.txt","a+")
f_dbt.close()
f_dbt=open("doubts.txt","r")
f_dbt_red=f_dbt.read().split(",")[:-1]
couner=1
print("[+] WEAK CONTENT : ")
for coc in f_dbt_red:
    print(f"{couner}] {coc}\t")
    couner+=1
f_dbt.close()

def smart(question,answer,limit):
    question=question.split()
    answer=answer.split()
    wrong=0
    for cont in range(len(question)):
        num=0
        for q_word in question[cont]:
            try:
                a_word=answer[cont][num]
            except IndexError:
                pass
            if a_word==q_word:
                pass
            else:
                wrong+=1
            num+=1
    if wrong>limit:
        wrong_ans=True
    else:
        wrong_ans=False
    return wrong_ans

d={}
for x in range(0,len(count_qust)):
    k=count_qust[x]
    v=count_ans[x]
    d[k]=v

q_l=[]
for kk in d:
    q_l.append(kk)

score=0
qn=0
an=""
print()
print("#### {} QUIZ ####".format(topic.upper()))
print("[+] TO EXIT TYPE 99 ")
print()
print("[=] SELECT ANY ONE CORRECTION LEVEL : \n\t1) HARD\t\t2) MEDIUM\t3) EASY")
limit_find=input("[-] your level : ").lower()
if limit_find in "hard1":
    limit=0
elif limit_find in "medium2":
    limit=5
elif limit_find in "easy3":
    limit=10
else:
    limit=3
print()
crt_marks = float(input('marks for correct answer : '))
wrong_marks = float(input('marks for wrong answer : '))

q_an_lst=[]
print()
try:
    while qn<=len(count_qust):
        q_an=d[q_l[qn]]
        qst=q_l[qn]
        print(f"[Q{qn+1}] {q_l[qn]} ?")
        an=input("answer : ")
        an.strip()
        ctr_ans=q_an.lower().strip()
        if an.isspace() or an== "" or an== None or len(an)==0:
            print(ctr_ans)
        else:
            eror=smart(ctr_ans,an,limit)
            if an.lower().strip()==ctr_ans or eror==False:
                score+=crt_marks
            elif an.lower()=="99":
                break
            else:
                score-=wrong_marks
                print(f"WRONG \nCORRECT : {ctr_ans}")
                q_an_lst.append(qst+",")
            if an.lower().strip()!=ctr_ans and eror==False:
                print(f"PARTIALLY WRONG \nCORRECT : {ctr_ans}")

        print("------------------------")
        print()
        qn+=1
except:
    print(f'''
    ######          ##
    #               ##
    ######                {score}
         # C O R E  ##
    ######          ##
    ''')
f_dbt=open("doubts.txt","w")
f_dbt.writelines(q_an_lst)
f_dbt.close()
ok=input(":")