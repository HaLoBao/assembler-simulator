instruction_table ={
    #R-type
    'add':['0000000','rs2','rs1','000','rd','0110011'],
    'sub': ['0100000', 'rs2', 'rs1', '000', 'rd', '0110011'],
    'xor':['0000000','rs2','rs1','100','rd','0110011'],
    'or':['0000000','rs2','rs1','110','rd','0110011'],
    'and':['0000000','rs2','rs1','111','rd','0110011'],
    'sll':['0000000','rs2','rs1','001','rd','0110011'],
    'srl':['0000000','rs2','rs1','101','rd','0110011'],
    'sra':['0100000','rs2','rs1','101','rd','0110011'],
    'slt':['0000000','rs2','rs1','010','rd','0110011'],
    'sltu':['0000000','rs2','rs1','011','rd','0110011'],

    #I-type
    'addi': ['imm_11_0', 'rs1', '000', 'rd', '0010011'],
    'xori': ['imm_11_0', 'rs1', '100', 'rd', '0010011'],
    'ori': ['imm_11_0', 'rs1', '110', 'rd', '0010011'],
    'andi': ['imm_11_0', 'rs1', '111', 'rd', '0010011'],
    'slli': ['imm_0x00_0_4', 'rs1', '001', 'rd', '0010011'],
    'srli': ['imm_0x00_0_4', 'rs1', '101', 'rd', '0010011'],
    'srai': ['imm_0x20_0_4', 'rs1', '101', 'rd', '0010011'],
    'slti': ['imm_11_0', 'rs1', '010', 'rd', '0010011'],
    'sltiu': ['imm_11_0', 'rs1', '011', 'rd', '0010011'],
    'lb': ['imm_11_0', 'rs1', '000', 'rd', '0000011'],
    'lh':  ['imm_11_0', 'rs1', '001', 'rd', '0000011'],
    'lw':  ['imm_11_0', 'rs1', '010', 'rd', '0000011'],
    'lbu':  ['imm_11_0', 'rs1', '100', 'rd', '0000011'],
    'lhu':  ['imm_11_0', 'rs1', '101', 'rd', '0000011'],
    'jalr': ['imm_11_0', 'rs1', '000', 'rd', '1100111'],

    #S-type
    'sb': ['imm_11_5', 'rs2', 'rs1', '000', 'imm_4_0', '0100011'],
    'sh': ['imm_11_5', 'rs2', 'rs1', '001', 'imm_4_0', '0100011'],
    'sw': ['imm_11_5', 'rs2', 'rs1', '010', 'imm_4_0', '0100011'],

    #B-type
    'beq': ['imm_12|10_5', 'rs2', 'rs1', '000', 'imm_4_1|11', '1100011'],
    'bne': ['imm_12|10_5', 'rs2', 'rs1', '001', 'imm_4_1|11', '1100011'],
    'blt': ['imm_12|10_5', 'rs2', 'rs1', '100', 'imm_4_1|11', '1100011'],
    'bge': ['imm_12|10_5', 'rs2', 'rs1', '101', 'imm_4_1|11', '1100011'],
    'bltu': ['imm_12|10_5', 'rs2', 'rs1', '110', 'imm_4_1|11', '1100011'],
    'bgeu': ['imm_12|10_5', 'rs2', 'rs1', '111', 'imm_4_1|11', '1100011'],

    #J-type
    'jal': ['imm_20|10_1|11|19_12', 'rd',  '1101111'],
}