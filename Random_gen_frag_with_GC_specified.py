import random

def gen_rand_DNA(N, L):
    dic = {} #put the genereated sequence in dictionary
    count = 0
    while count < N:
        dic[count]=[]
        DNA = [random.choice(list('ATGC')) for i in range(L)]
        DNA = ''.join(DNA) #joining list to string 
        if(DNA.count("G") + DNA.count("C"))/(float(len(DNA)))== 0.7:
            dic[count].append(DNA)
            count +=1
    return dic

a = gen_rand_DNA(5, 10)
