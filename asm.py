import sys
opcodes={"add":"10000","sub":"10001","mov":"10010",
        "mov2":"10011","ld":"10100","st":"10101",
        "mul":"10110","div":"10111","rs":"11000",
        "ls":"11001","xor":"11010","or":"11011",
        "and":"11100","not":"11101","cmp":"11110",
        "jmp":"11111","jlt":"01100","jgt":"01101",
        "je":"01111","hlt":"01010"}
registers={'R0': '000',
           'R1': '001',
           'R2': '010',
           'R3': '011',
           'R4': '100',
           'R5': '101',
           'R6': '110',
           'FLAGS': '111'
        }
typeA=["add","sub","mul","xor","or","and"]
typeB=["mov","rs","ls"]
typeC=["mov2","div","not","cmp"]
typeD=["ld","st"]
typeE=["jmp","jlt","jgt","je"]
typeF=["hlt"]
memoryadd={}
var={}
labels={}
indata=[]
duplicates={}
def binarycovert(n):
        num=int(n)
        binary=''
        temp=bin(num)
        temp=temp.replace('0b',"")
        binary+='0'*(8-len(temp))
        binary+=temp
        return binary
def hltcheck(state):
        #to check the state of the hlt command
        count=0
        for i in range(len(state)):
                if 'hlt' in state[i]:
                        count+=1
                if count > 1:
                        print("Error at line",indata.index(state[i])+1,"hlt instruction has been typed more than once!")
                        quit()
        if count==0:
                print("No hlt command int the given instuctions!")
                quit()
        for i in range(len(state)):
                if ":" in state[i][0]:
                        if state[i][1]=="hlt" and i!=len(state)-1:
                                print("Error at line",indata.index(state[i])+1,"hlt instruction is not the last instruction")
                                quit()
                else:
                        if state[i][0]=="hlt" and i!=len(state)-1:
                                print("Error at line",indata.index(state[i])+1,"hlt instruction is not the last instruction")
                                quit()
def varcount(state):
        #to count the number of vairables 
        count=0
        for i in range(len(state)):
                if state[i][0]=='var':
                        count+=1
                else:
                        break
        return count
def varcheck(state):
        #to check if all the variables have been declared in the start
        flag=0
        for i in range(len(state)):
                if state[i][0]!='var':
                        flag=1
                if flag==1 and state[i][0]=='var':
                        print("Error at line",indata.index(state[i])+1,"variable has been declared in between instructions")
                        quit()
def memorydict(state):
        idx=0
        for i in range(len(state)):
                if state[i][0]== 'var':
                        pass
                else:
                     memoryadd[tuple(state[i])]=idx
                     idx+=1
        for i in range(varcount(state)):
                memoryadd[tuple(state[i])]=idx
                idx+=1
def addvar(memeryadd):
        for i in memeryadd:
                if i[0]=='var' and i[1] not in var.keys():
                        var[i[1]]=memoryadd[i]
def addlabel(memoryadd):
        for i in memoryadd:
                if ':' in i[0]:
                        labels[i[0]]=memoryadd[i]
def insttypocheck(state):
        for i in range(len(state)):
                if state[i][0]!="":
                        if ":" in state[i][0]:
                                if state[i][1] not in opcodes.keys() and state[i][1] !='var' or state[i][1]=='mov2':
                                        print("Typo detected in line",indata.index(state[i])+1,"kindly check the list of intructions.")
                                        quit()
                        else:
                                if state[i][0] not in opcodes.keys() and state[i][0] !='var' or state[i][0]=='mov2':
                                        print("Typo detected in line",indata.index(state[i])+1,"kindly check the list of intructions.")
                                        quit()
def regtypocheck(state):
        for i in range(len(state)):
                if state[i][0]!="":
                        if ":" in state[i][0]:
                                if state[i][1] == 'mov' and "$" in state[i][3] and state[i][2] not in registers.keys():
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][1] == 'mov' and "$" not in state[i][3] and state[i][2] not in registers.keys():
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][1] in typeA and (state[i][2] not in registers.keys() or state[i][3] not in registers.keys() or state[i][4] not in registers.keys()):
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][1] in typeB and state[i][2] not in registers.keys():
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][1] in typeC and (state[i][2] not in registers.keys() or state[i][3] not in registers.keys()):
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][1] in typeD and state[i][2] not in registers.keys():
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                        else:   
                                if state[i][0] == 'mov' and "$" in state[i][2] and state[i][1] not in registers.keys():
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][0] == 'mov' and "$" not in state[i][2] and state[i][1] not in registers.keys():
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][0] in typeA and (state[i][1] not in registers.keys() or state[i][2] not in registers.keys() or state[i][3] not in registers.keys()):           
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][0] in typeB and state[i][1] not in registers.keys():
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][0] in typeC and (state[i][1] not in registers.keys() or state[i][2] not in registers.keys()):
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][0] in typeD and state[i][1] not in registers.keys():
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
def defvar(state):
        for i in range(len(state)):
                if state[i][0]!='':
                        if ":" not in state[i][0]:
                                if state[i][0] in typeD and (state[i][2] not in var.keys()and state[i][2]+":" not in labels.keys()):
                                        print("Error at line",indata.index(state[i])+1,"Use of undefined variable.")
                                        quit()
                        else:
                                if state[i][1] in typeD and (state[i][3] not in var.keys() and state[i][3]+":" not in labels.keys()):
                                        print("Error at line",indata.index(state[i])+1,"Use of undefined variable.")
                                        quit()
def labelcheck(state):
        for i in range(len(state)):
                if state[i][0]!="":
                        if ":" in state[i][0]:
                                if state[i][1] in typeE and state[i][2]+":" not in labels.keys() and state[i][2] not in var.keys():
                                        print("Error at line",indata.index(state[i])+1,"USe of undefined label.")
                                        quit()
                        else:
                                if state[i][0] in typeE and state[i][1]+":" not in labels.keys() and state[i][1] not in var.keys():
                                        print("Error at line",indata.index(state[i])+1,"Use of undefined label.")
                                        quit()
def flagcheck(state):
        for i in range(len(state)):
                if state[i][0]!="":
                        if ":" in state[i][0]:
                                if (state[i][1]=="mov" and "$" in state[i][3]) and state[i][2]=="FLAGS":
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif (state[i][1]=="mov" and "$"  not in state[i][3]) and state[i][3]=="FLAGS":
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif state[i][1] in typeA and "FLAGS" in state[i]:
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif state[i][1] in typeB and state[i][2]=="FLAGS":
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif state[i][1] in typeC and (state[i][2]=="FLAGS" or state[i][3]=="FLAGS"):
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif state[i][1] in typeD and state[i][2]=="FLAGS":
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                        else: 
                                if (state[i][0]=="mov" and "$" in state[i][2]) and state[i][1]=="FLAGS":
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif (state[i][0]=="mov" and "$"  not in state[i][2]) and  state[i][2]=="FLAGS":
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif state[i][0] in typeA and "FLAGS" in state[i]:
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif state[i][0] in typeB and state[i][1]=="FLAGS":
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif state[i][0] in typeC and (state[i][1]=="FLAGS" or state[i][2]=="FLAGS"):
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif state[i][0] in typeD and state[i][1]=="FLAGS":
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
def immvalue(state):
        for i in range(len(state)):
                if state[i][0]!="":
                        if ":" in state[i][0]:
                                if state[i][1] in typeB and "$" in state[i][3] and (float(state[i][3][1:])<0 or float(state[i][3][1:])>255 or float(state[i][3][1:])%1!=0 or state[i][3][1:].isalpha()):
                                        print("Error at line",indata.index(state[i])+1,"Illegal Immediate Value.")
                                        quit()
                        else:
                                if state[i][0] in typeB and "$" in state[i][2] and (float(state[i][2][1:])<0 or float(state[i][2][1:])>255 or float(state[i][2][1:])%1!=0 or state[i][2][1:].isalpha()):
                                        print("Error at line",indata.index(state[i])+1,"Illegal Immediate Value.")
                                        quit()
def instsyntax(state):
        for i in range(len(state)):
                if state[i][0]!="":
                        if ":" in state[i][0]:
                                if (state[i][1]=="mov" and "$" in state[i][3]) and len(state[i])!=4:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif (state[i][1]=="mov" and "$"  not in state[i][3]) and len(state[i])!=4:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][1] in typeA and len(state[i])!=5:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][1] in typeB and len(state[i])!=4:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][1] in typeC and len(state[i])!=4:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][1] in typeD and len(state[i])!=4:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][1] in typeE and len(state[i])!=3:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][1] in typeF and len(state[i])!=2:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                        else: 
                                if (state[i][0]=="mov" and "$" in state[i][2]) and len(state[i])!=3:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif (state[i][0]=="mov" and "$"  not in state[i][2]) and len(state[i])!=3:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][0] in typeA and len(state[i])!=4:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][0] in typeB and len(state[i])!=3:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][0] in typeC and len(state[i])!=3:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][0] in typeD and len(state[i])!=3:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][0] in typeE and len(state[i])!=2:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][0] in typeF and len(state[i])!=1:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
def emptylabel(state):
        for i in range(len(state)):
                if ":" in state[i][0] and len(state[i])==1:
                        print("Error at line",indata.index(state[i])+1,"Empty Label.")
def duplicatevar(state):
        for i in range(len(state)):
                if state[i][0]=='var':
                        if state[i][1] not in duplicates.keys():
                                duplicates[state[i][1]]=1
                        else:
                                duplicates[state[i][1]]+=1
                        if duplicates[state[i][1]] > 1:
                                print("Error at line",indata.index(state[i])+1,"Same variable defined twice.")
                                quit()
def labelinlabel(state):
        for i in range(len(state)):
                if ":" in state[i][0] and ":" in state[i][1]:
                        print("Error at line",indata.index(state[i])+1,"Nested Labels not allowed")

def output(inst):
        if ':' in inst[0]:
                if inst[1] == 'mov' :
                        if "$" in inst[3]:
                                print(opcodes['mov']+registers[inst[2]]+binarycovert(inst[3][1:]))
                        else: 
                                print(opcodes['mov2']+'0'*5+registers[inst[2]]+registers[inst[3]])
                elif inst[1] in typeA:
                        print(opcodes[inst[1]]+'0'*2+registers[inst[2]]+registers[inst[3]]+registers[inst[4]])
                elif inst[1] in typeB:
                        print(opcodes[inst[1]]+registers[inst[2]]+binarycovert(inst[3][1:]))
                elif inst[1] in typeC:
                        print(opcodes[inst[1]]+'0'*5+registers[inst[2]]+registers[inst[3]])
                elif inst[1] in typeD:
                        print(opcodes[inst[1]]+registers[inst[2]]+binarycovert(var[inst[3]]))
                elif inst[1] in typeE:
                        print(opcodes[inst[1]]+'0'*3+binarycovert(labels[inst[2]+":"]))
                elif inst[1] in typeF:
                        print(opcodes[inst[1]]+'0'*11)
        else: 
                if inst[0] == 'mov' :
                        if "$" in inst[2]:
                                print(opcodes['mov']+registers[inst[1]]+binarycovert(inst[2][1:]))
                        else: 
                                print(opcodes['mov2']+'0'*5+registers[inst[1]]+registers[inst[2]])
                elif inst[0] in typeA:
                        print(opcodes[inst[0]]+'0'*2+registers[inst[1]]+registers[inst[2]]+registers[inst[3]])
                elif inst[0] in typeB:
                        print(opcodes[inst[0]]+registers[inst[1]]+binarycovert(inst[2][1:]))
                elif inst[0] in typeC:
                        print(opcodes[inst[0]]+'0'*5+registers[inst[1]]+registers[inst[2]])
                elif inst[0] in typeD:
                        print(opcodes[inst[0]]+registers[inst[1]]+binarycovert(var[inst[2]]))
                elif inst[0] in typeE:
                        print(opcodes[inst[0]]+'0'*3+binarycovert(labels[inst[1]+":"]))
                elif inst[0] in typeF:
                        print(opcodes[inst[0]]+'0'*11)
def labelsandvar(state):
        for i in range(len(state)):
                if state[i][0]!='':
                        if ":" not in state[i][0]:
                                if state[i][0] in typeD and (state[i][2] not in var.keys() and state[i][2]+":" in labels.keys()):
                                        print("Error at line",indata.index(state[i])+1,"Label has been used a variable.")
                                        quit()
                                if state[i][0] in typeE and (state[i][1] in var.keys() and state[i][1]+":" not in labels.keys()):
                                        print("Error at line",indata.index(state[i])+1,"Variable has been used a label.")
                                        quit()
                        else:
                                if state[i][1] in typeD and (state[i][3] not in var.keys() and state[i][3]+":" in labels.keys()):
                                        print("Error at line",indata.index(state[i])+1,"Label has been used a variable.")
                                        quit()
                                if state[i][1] in typeE and (state[i][2] in var.keys() and state[i][2]+":" not in labels.keys()):
                                        print("Error at line",indata.index(state[i])+1,"Variable has been used a label.")
                                        quit()
def main():
        for line in sys.stdin:
                if ''==line:
                        break
                indata.append((line.strip()).split())
        data=[i for i in indata if i !=[]]
        memorydict(data)
        addvar(memoryadd)
        addlabel(memoryadd)
        hltcheck(data)
        varcheck(data)
        labelinlabel(data)
        duplicatevar(data)
        emptylabel(data)
        instsyntax(data)
        insttypocheck(data)
        defvar(data)
        flagcheck(data)
        immvalue(data)
        labelsandvar(data)
        regtypocheck(data)
        labelcheck(data)
        for i in data:
                output(i)
if __name__=="__main__":
        main()