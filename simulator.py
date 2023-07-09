from collections import OrderedDict
flags={"V":0,"L":0,"G":0,"E":0}
registers={"R0":{"address":"000","value":"00000000"},"R1":{"address":"001","value":"00000000"},"R2":{"address":"010","value":"00000000"},"R3":{"address":"011","value":"00000000"},"R4":{"address":"100","value":"00000000"},"R5":{"address":"101","value":"00000000"},"R6":{"address":"110","value":"00000000"},"FLAG":{"address":"111","value":"00000000"}}

memory={}
pc="00000000"


def change_flag_reg():
    string_temp=""
    string_temp="0"*4
    for i in flags:
        string_temp+=str(flags[i])
    registers["FLAG"]["value"]=string_temp

def printall(count):
    pc=binary(count)
    print(pc,end=" ")
    for x in registers:
        string_reg=registers[x]["value"]
        temp=""
        temp+="0"*(8)
        temp+=string_reg
        print(temp,end=" ")
    print("")



def binary(val):
    string=str(bin(val))
    string=string.replace("0b","")
    temp="0"*(8-len(string))
    temp+=string
    return temp

def check_overflow(a):
    if(a<=255):
        return 0
    else:
        return 1

def mov_imm(arr):
    for i in registers:
        if(arr[0]==registers[i]["address"]):
            registers[i]["value"]=arr[1]

def mov_reg(arr):
    for i in registers:
        if(arr[0]==registers[i]["address"]):
            value=registers[i]["value"]
            # print(value1)
    for i in registers:
        if(arr[1]==registers[i]["address"]):
            registers[i]["value"]=value

def add(arr):
    for i in registers:
        if(arr[0]==registers[i]["address"]):
            value_1=int(registers[i]["value"],2)
        if(arr[1]==registers[i]["address"]):
            value_2=int(registers[i]["value"],2)
        if(arr[2]==registers[i]["address"]):
            key=i
    ans=value_1+value_2
    if(check_overflow(ans)==0):
        registers[key]["value"]=binary(ans)
    elif (check_overflow(ans)==1):
        flags["V"]=1
        registers[key]["value"]=binary(255)

def subtract(arr):
    for i in registers:
        if(arr[0]==registers[i]["address"]):
            value_1=int(registers[i]["value"],2)
        if(arr[1]==registers[i]["address"]):
            value_2=int(registers[i]["value"],2)
        if(arr[2]==registers[i]["address"]):
            key=i
    ans=value_1-value_2
    if(value_1>=value_2):
        registers[key]["value"]=binary(ans)
    else:
        flags["V"]=binary(1)

def multi(arr):
    for i in registers:
        if(arr[0]==registers[i]["address"]):
            value_1=int(registers[i]["value"],2)
        if(arr[1]==registers[i]["address"]):
            value_2=int(registers[i]["value"],2)
        if(arr[2]==registers[i]["address"]):
            key=i
    ans=value_1*value_2
    if(ans<=255):
        registers[key]["value"]=binary(value_1*value_2)
    else:
        registers[key]["value"]=binary(255)
        flags["V"]=1

def divide(arr):
    for i in registers:
        if(arr[0]==registers[i]["address"]):
            value_1=int(registers[i]["value"],2)
        if(arr[1]==registers[i]["address"]):
            value_2=int(registers[i]["value"],2)
    ans=value_1/value_2
    rem=value_1%value_2
    registers["R0"]["value"]=(binary(int(ans)))
    registers["R1"]["value"]=(binary(int(rem)))
    
def XOR(arr):
    for i in registers:
        if(arr[0]==registers[i]["address"]):
            value_1=int(registers[i]["value"],2)
        if(arr[1]==registers[i]["address"]):
            value_2=int(registers[i]["value"],2)
        if(arr[2]==registers[i]["address"]):
            key=i
    registers[key]["value"]=binary(value_1^value_2)

def OR(arr):
    for i in registers:
        if(arr[0]==registers[i]["address"]):
            value_1=int(registers[i]["value"],2)
        if(arr[1]==registers[i]["address"]):
            value_2=int(registers[i]["value"],2)
        if(arr[2]==registers[i]["address"]):
            key=i
    registers[key]["value"]=(binary(value_1 | value_2))

def AND(arr):
    for i in registers:
        if(arr[0]==registers[i]["address"]):
            value_1=int(registers[i]["value"],2)
        if(arr[1]==registers[i]["address"]):
            value_2=int(registers[i]["value"],2)
        if(arr[2]==registers[i]["address"]):
            key=i
    registers[key]["value"]=(binary(value_1 & value_2))

def invert(arr):
    for i in registers:
        if(arr[0]==registers[i]["address"]):
            value=int(registers[i]["value"],2)
        # if(arr[1]==registers[i]["address"]):
        #     key=i
    string_invert=binary(value)
    string_invert=list(string_invert)
    str_in=""
    for i in range(len(string_invert)):
        if(string_invert[i])=="0":
            str_in+="1"
        if(string_invert[i]=="1"):
            str_in+="0"
    for i in registers:
        if(registers[i]["address"]==arr[1]):
            registers[i]["value"]=str_in

def compare(arr):
    for i in registers:
        if(arr[0]==registers[i]["address"]):
            value_1=int(registers[i]["value"],2)
        if(arr[1]==registers[i]["address"]):
            value_2=int(registers[i]["value"],2)
    # print(value_1,value_2)
    if(value_1>value_2):
        flags["G"]=1
        flags["E"]=0
        flags["L"]=0
    elif(value_1<value_2):
        flags["L"]=1
        flags["E"]=0
        flags["G"]=0
    elif(value_1==value_2):
        flags["E"]=1
        flags["G"]=0
        flags["L"]=0
    change_flag_reg()

def right_shift(arr):
    for i in registers:
        if(arr[0]==registers[i]["address"]):
            key=i
    shifting_number=int(arr[1],2)
    number=int(registers[key]["value"],2)
    ans=number>>shifting_number
    registers[key]["value"]=(binary(ans))

def left_shift(arr):
    for i in registers:
        if(arr[0]==registers[i]["address"]):
            key=i
    shifting_number=int(arr[1],2)
    number=int(registers[key]["value"],2)
    ans=number<<shifting_number
    registers[key]["value"]=(binary(ans))

def load(arr):
    flag=0
    for i in memory:
        if(i==arr[1]):
            data=memory[i]
            flag=1
    if(flag==0):
        data="00000000"
    for i in registers:
        if(registers[i]["address"]==arr[0]):
            registers[i]["value"]=data;

def store(arr):
    
    for i in registers:
        if(arr[0]==registers[i]["address"]):
            data=registers[i]["value"]
    memory[arr[1]]=data

def flag_reset():
    for i in flags:
        flags[i]=0
    
l1=[]
input_list=(str(input()))
l1.append(input_list)
while(input_list!="0101000000000000"):
    input_list=str(input())
    l1.append(input_list)

flag_temp=0
flag_temp2=0
i=0  
count=0
while(i<len(l1)):
    opcode=l1[i][0:5]
    # Immediate value with register
    if(opcode=="10010"):
        input_list=[l1[i][5:8],l1[i][8:16]]
        mov_imm(input_list)
    if(opcode=="11000"):
        input_list=[l1[i][5:8],l1[i][8:16]]
        right_shift(input_list)
    if(opcode=="11001"):
        input_list=[l1[i][5:8],l1[i][8:16]]
        left_shift(input_list)
    # two register type
    if(opcode=="10011"):
        input_list=[l1[i][10:13],l1[i][13:16]]
        mov_reg(input_list)
    if(opcode=="10111"):
        input_list=[l1[i][10:13],l1[i][13:16]]
        divide(input_list)
    if(opcode=="11110"):
        input_list=[l1[i][10:13],l1[i][13:16]]
        compare(input_list)
        flag_temp=1
        flag_temp2=0
    if(opcode=="11101"):
        input_list=[l1[i][10:13],l1[i][13:16]]
        invert(input_list)
    # three type register
    if(opcode=="10000"):
        input_list=[l1[i][7:10],l1[i][10:13],l1[i][13:16]]
        add(input_list)
    if(opcode=="10001"):
        input_list=[l1[i][7:10],l1[i][10:13],l1[i][13:16]]
        subtract(input_list)
    if(opcode=="10110"):
        input_list=[l1[i][7:10],l1[i][10:13],l1[i][13:16]]
        multi(input_list)
    if(opcode=="11010"):
        input_list=[l1[i][7:10],l1[i][10:13],l1[i][13:16]]
        XOR(input_list)
    if(opcode=="11011"):
        input_list=[l1[i][7:10],l1[i][10:13],l1[i][13:16]]
        OR(input_list)
    if(opcode=="11100"):
        input_list=[l1[i][7:10],l1[i][10:13],l1[i][13:16]]
        AND(input_list)
    #register and memory addresss
    if(opcode=="10100"):
        input_list=[l1[i][5:8],l1[i][8:16]]
        load(input_list)
    if(opcode=="10101"):
        input_list=[l1[i][5:8],l1[i][8:16]]
        store(input_list)

    if(opcode=="01100"):
        input=l1[i][8:16]
        if(flags["L"]==1):
            jump=int(input,2)
            if(flag_temp2==1 and flag_temp==1):
                flag_reset()
                flag_temp=0
            if(flag_temp==1 and flag_temp2==0):
                flag_temp2=1
            change_flag_reg()
            printall(i)
            count+=1
            i=jump
            continue
    if(opcode=="01101"):
        input=l1[i][8:16]
        if(flags["G"]==1):
            jump=int(input,2)
            if(flag_temp2==1 and flag_temp==1):
                flag_reset()
                flag_temp=0
            if(flag_temp==1 and flag_temp2==0):
                flag_temp2=1
            change_flag_reg()
            printall(i)
            count+=1
            i=jump
            continue
    if(opcode=="01111"):
        input=l1[i][8:16]
        if(flags["E"]==1):
            jump=int(input,2)
            if(flag_temp2==1 and flag_temp==1):
                flag_reset()
                flag_temp=0
            if(flag_temp==1 and flag_temp2==0):
                flag_temp2=1
            change_flag_reg()
            printall(i)
            i=jump
            count+=1
            continue
    if(opcode=="11111"):
        input=l1[i][8:16]
        jump=int(input,2)
        if(flag_temp2==1 and flag_temp==1):
                flag_reset()
                flag_temp=0
        if(flag_temp==1 and flag_temp2==0):
            flag_temp2=1
        change_flag_reg()
        printall(i)
        i=jump
        count+=1
        continue
    
    if(flag_temp2==1 and flag_temp==1):
        flag_reset()
        flag_temp=0
    if(flag_temp==1 and flag_temp2==0):
        flag_temp2=1

    change_flag_reg()
    printall(i)
    i+=1
    count+=1
    if(opcode=="01010"):
        break

for i in range(len(l1)):
    print(l1[i])

res =dict(reversed(list(memory.items())))
for i in res:
    string_reg1=res[i]
    temp1=""
    temp1+="0"*(8)
    temp1+=string_reg1
    print(temp1)
for i in range(256-len(l1)-len(memory)):
    print("0000000000000000")
# list=[]

