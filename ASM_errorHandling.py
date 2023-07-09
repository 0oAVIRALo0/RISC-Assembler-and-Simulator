typeA=["add","sub","mul","xor","or","or"]
typeB=["mov","rs","ls"]
typeC=["mov2","div","not","cmp"]
typeD=["ld","st"]
typeE=["jmp","jlt","jgt","je"]
typeF=["hlt"]

opcodes={"add":"10000","sub":"10001","mov":"10010",
        "mov2":"10011","ld":"10100","st":"10101",
        "mul":"10110","div":"10111","rs":"11000",
        "ls":"11001","xor":"11010","or":"11011",
        "or":"11100","not":"11101","cmp":"11110",
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

def typosinInstruction(data):
    for i in range(len(data)):
        if ':' in data[i][0]:
            count = 0
            for j in range(i+1, len(data[i])):
                count += 1
                if data[i][1] in typeA and count+1 != 5:
                        print(f"ISA instruction syntax is wrong in line {i+1}.")
                        quit()
                elif data[i][1] in typeB and count+1 != 4:
                        print(f"ISA instruction syntax is wrong in line {i+1}.")
                        quit()
                elif data[i][1] in typeC and count+1 != 4:
                        print(f"ISA instruction syntax is wrong in line {i+1}.")
                        quit()
                elif data[i][1] in typeD and count+1 != 4:
                        print(f"ISA instruction syntax is wrong in line {i+1}.")
                        quit()
                elif data[i][1] in typeE and count+1 != 3:
                        print(f"ISA instruction syntax is wrong in line {i+1}.")
                        quit()
                elif data[i][1] in typeF and count+1 != 2:
                        print(f"ISA instruction syntax is wrong in line {i+1}.")
                        quit()

        if data[i][0] == 'var' and len(data[i]) != 2:
            print(f"ISA instruction syntax is wrong in line {i+1}.")
            quit()
        elif data[i][0] in typeA and len(data[i]) != 4:
            print(f"ISA instruction syntax is wrong in line {i+1}.")
            quit()
        elif data[i][0] in typeB and len(data[i]) != 3:
            print(f"ISA instruction syntax is wrong in line {i+1}.")
            quit()
        elif data[i][0] in typeC and len(data[i]) != 3:
            print(f"ISA instruction syntax is wrong in line {i+1}.")
            quit()
        elif data[i][0] in typeD and len(data[i]) != 3:
            print(f"ISA instruction syntax is wrong in line {i+1}.")
            quit()
        elif data[i][0] in typeE and len(data[i]) != 2:
            print(f"ISA instruction syntax is wrong in line {i+1}.")
            quit()
        elif data[i][0] in typeF and len(data[i]) != 1:
            print(f"ISA instruction syntax is wrong in line {i+1}.")
            quit()


def flagError(data):
    for i in range(len(data)):
        if data[i][0] in opcodes.keys():
            if 'FLAGS' in data[i][1: len(data[i])]:
                print(f"Illegal use of FLAGS register in line {i+1}.")
                quit()


def immediatevaluesError(data):
    for i in range(len(data)):
        if data[i][0] == typeB[0] and data[i][2] not in registers.keys():
            if int(data[i][-1]) < 0 or int(data[i][-1]) > 255:
                print(f"Illegal use of Immediate value in line {i+1}.")
                quit()
        
        if data[i][0] == typeB[1] or data[i][0] == typeB[2]:
            if int(data[i][-1]) < 0 or int(data[i][-1]) > 255:
                print(f"Illegal use of Immediate value in line {i+1}.")
                quit()

data = [['var', 'x'], ['mov', 'R1', '255'], ['mov', 'R2', '100'], ['mul', 'R3', 'R1', 'R2'], ['label:', 'add', 'R0', 'R1', 'R3'], ['st', 'R3', 'x'], ['hlt']]
typosinInstruction(data)
flagError(data)
immediatevaluesError(data)
