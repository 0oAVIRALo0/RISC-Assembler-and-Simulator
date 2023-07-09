def undefined_var(l):
    varlist=[]
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][0]=="var":
                varlist.append(l[i][1])
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][0]=="ld" or l[i][0]=="st": 
                if l[i][2] not in varlist:
                    print("USE OF UNDEFIEND VARIABLE IN LINE:",i+1)
                    quit()

def var_label(arr):
    varlist=[]
    label_list=[]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][0]=="var":
                varlist.append(arr[i][1])
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][0]=="jmp" or arr[i][0]=="jlt" or arr[i][0]=="jgt" or arr[i][0]=="je":
                label_list.append(arr[i][1])
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][0]=="jmp" or arr[i][0]=="jlt" or arr[i][0]=="jgt" or arr[i][0]=="je" and arr[i][1] in varlist : 
                print("MISUSE OF VARIABLE IN LABEL in line",i+1)      
            if arr[i][0]=="var" and arr[i][1] in label_list:
                print("MISUSE OF VAR IN LABEL IN LINE:",i+1)
                quit()

def varbw(arr):

    flag=0 
    for i in range(len(arr)):
        if(arr[i][0]!="var"):
            flag=1
        if(flag==1 and arr[i][0]=="var"):
            print("USE OF VARIABLE INBETWEEN IN LINE:",i+1)

def varcount(state):
        #to count the number of vairables 
        count=0
        for i in range(len(state)):
                if state[i][0]=='var':
                        count+=1
                else:
                        break
        return count

def hltcheck(state):
    #to check the state of the hlt command
    count=0
    for i in range(len(state)):
            if state[i][0]=='hlt':
                    count+=1
            if count > 1:
                    print("Error at line",i+1,"hlt instruction has been typed more than once!")
                    quit()
    if count==0:
            print("No hlt command int the given instuctions!")
            quit()
    for i in range(len(state)):
            if state[i][0]=="hlt" and i!=len(state)-1:
                    print("Error at line",i+1,"hlt instruction is not the last instruction")
                    quit()


lenght=int(input("ENTER LENGHT"))
l1=[]
for i in range(lenght):
    string=[str(i) for i in input().split(" ")]
    l1.append(string)
# undefined_var(l1,lenght)
# var_label(l1,lenght)
# varbw(l1)
# print(varcount(l1))


