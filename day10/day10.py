import os

def get_codon_dict(text_path):
    """把codon.txt里的内容读出来，放到一个字典里，后面翻译要用"""
    codon_dict = {}
    with open(text_path, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            line = line.strip()
            codon, amino = line.split(' ')
            codon_dict[codon] = amino # 键是密码子，值是氨基酸
    return codon_dict


def get_seq_dict(text_path):
    """把seq.fa的内容读出来，并存到一个字典里"""
    seq_dict = {}
    with open(text_path, 'r') as file:
        lines = file.readlines()
        id = 1
        for line in lines[1::2]:
            seq_dict[f'seq{id}'] = line
            id += 1
    return seq_dict

def transcript(dna: str) -> str:
    """把DNA序列翻译成mRNA序列"""
    return dna.replace('T', 'U')

def translate(dna: str) -> dict:
    """把DNA序列最终转化为氨基酸序列"""
    mrna = transcript(dna)
    
    start = 0 #用来判断有没有遇到起始密码子
    result = ''
    for i in range(0, len(mrna), 3):
        cur_rna = mrna[i : i + 3] #3位3位地读取
        if codon_dict[cur_rna] == 'stop': #遇到终止密码子，则跳出循环。这个的优先级应该最高
            break
        if start == 0: #然后就是判断有没有遇到过起始密码子
            if cur_rna != 'AUG':
                continue
            else:
                start = 1 #这是第一次遇到起始密码子，但是还是要正常翻译
        cur_amino = codon_dict[cur_rna] #最后才是正常翻译
        result += cur_amino
    return result

codon_dict = get_codon_dict('第十天附加材料/codon.txt')
seq_dict = get_seq_dict('第十天附加材料/seq.fa') #此处第十天附近材料前面不应该再加/，因为/表示从根目录开始找，而此时要
#的是相对路径
protein_dict = {}
for name, dna_str in seq_dict.items():
    protein_dict[name] = translate(dna_str)

with open('第十天附加材料/protein.txt', 'a') as file:
    file.write('\n以下是结果：')
    for name, protein in protein_dict.items():
        file.write('\n' + name)
        file.write('\n' + protein)
print(protein_dict)