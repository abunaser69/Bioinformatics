#String and list problem
s = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain"

a = 22
b = 27
c = 97
d = 102

print(len(s))

print(s[a:b+1], s[c:d+1])

running_total = 0
for item in range(100, 200):
    if (item%2 == 1):
        running_total = running_total + item
        
print(running_total)

#Reading and Writing

ft = open("text.txt", mode="r", encoding="utf-8")
#print(ft.read())
text_list = ft.readlines()
for i in range(0,len(text_list)):
    if i%2 != 0:
        print(text_list[i])
s = "We tried list and we tried dicts also we tried Zen"

count = {}

for word in str.split(s):
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for key, value in dict.items(count):
    print(key)
    print(value)

#printing only repeated multiple times
for key in count:
    if count[key] > 1:
        print(key, count[key])
        
  #Counting Nucleotide
  #input string
s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

#convert into list
x = list(s)
#print(x)
#variable initialization (dictonary)
count = {}

for i in x:
    if i in count:
        count[i] +=1
    else: 
        count[i] = 1
    
#printing the dictonary and key
for key in count:
           print(key, count[key])


# replacing
t = "GATGGAACTTGACTACGTAAATT"

t.replace("T", "U")

#finding reverse complement:

s = "AAAACCCGGT"
inx =  len(s)
rev_s = []

while inx > 0:
    rev_s += s[inx-1]
    inx = inx-1

print(rev_s)
rev_s

#method 2 no need lenght of string (most efficient)
print(s[::-1])

#method 3
print(s[len(s)::-1])

#method 4 using join
rev_s2 =''.join(reversed(s))
print(rev_s2)

#method 5 
lis_s = list(s)
lis_s.reverse()
rev_s3 = ''.join(lis_s)
print(rev_s3)

#method 6 using recursion
def reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursion(s[1:]) + s[0]


rev_s4 = reverse_recursion(s)
print(rev_s4)

#rev_s2.replace("A", "T").replace("C", "G")

#Reverse complement
#joining letters with out putting anything is ''.join
#[] referes indices
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
#List Comprehension : [expression(what needs to be done) for value in collection(for loops)]
#List comprehension complex: [expr for val1 in coll1 and val2 in coll2] (if condn can also be used)
#revcompl = lambda x: ''.join([{'A':'T','C':'G','G':'C','T':'A'}[B] for B in x][::-1])
# x is argument that is string
#Base is the key here
revcompl = lambda x: ''.join([complement[Base] for Base in x][::-1])
print(revcompl(s))

def complement_base(base, material='DNA'):
    """Returns the Watson-Crick complement of a base."""
    
    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'
    
def reverse_complement(seq, material='DNA'):
    """Compute reverse complement of a sequence."""
    
    # Initialize reverse complement
    rev_seq = ''
    
    # Loop through and populate list with reverse complement
    for base in reversed(seq):
        rev_seq += complement_base(base, material=material)
        
    return rev_seq

def complement_base(base):
    """Returns the Watson-Crick complement of a base."""
    
    if base in 'Aa':
        return 'T'
    elif base in 'Tt':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'


def reverse_complement(seq):
    """Compute reverse complement of a sequence."""
    
    # Initialize reverse complement
    rev_seq = ''
    
    # Loop through and populate list with reverse complement
    for base in reversed(seq):
        rev_seq += complement_base(base)
        
    return rev_seq
  
  #Using library:
  #Counting nucleotide
  
  from Bio.Seq import Seq
my_seq =  Seq("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")

s = "ACGT"
for i in s:
    print(i, my_seq.count(i))
    
from Bio import ExPASy
from Bio import SwissProt

handle = ExPASy.get_sprot_raw('B5ZC00') #you can give several IDs separated by commas
record = SwissProt.read(handle) # use SwissProt.parse for multiple proteins
dir(record) # list of attributes for the obtained Swiss-Prot record
#record.cross_references[0] #.cross_references attribute of our record
#print(handle)

from Bio import Entrez
Entrez.email = "*****@gmail.com"
handle = Entrez.esearch(db="nucleotide", term='"Zea mays"[Organism] AND rbcL[Gene]')
record = Entrez.read(handle)
record["Count"]

from Bio import Entrez
geneName = "Anthoxanthum"
pubDateStart = "2003/7/25"
pubDateEnd = "2005/12/27"
searchTerm = f'({geneName}[Organism]) AND("{pubDateStart}"[Publication Date]: "{pubDateEnd}"[Publication Date])'
Entrez.email = "....@gmail.com"
handle = Entrez.esearch(db="nucleotide", term=searchTerm)
record = Entrez.read(handle)
record["Count"]

from Bio import Entrez
from Bio import SeqIO #To work with FASTA format
Entrez.email = "******@gmail.com"

#obtains plain text records in FASTA format from NCBI's [Nucleotide] database.
handle = Entrez.efetch(db="nucleotide", id=["FJ817486, JX069768, JX469983"], rettype="fasta")
#records = handle.read()
#print(records)

#Bio.SeqIO.parse() takes a handle and format name as parameters and returns entries as SeqRecords.
records = list(SeqIO.parse(handle, "fasta"))
print(records[0].id)  #first record id
print(len(records[-1].seq))  #length of the last record
 
 from Bio.Seq import Seq
from Bio import Entrez
from Bio import SeqIO #To work with FASTA format
from Bio.SeqIO.FastaIO import SimpleFastaParser


Entrez.email = "*****@gmail.com"

#obtains plain text records in FASTA format from NCBI's [Nucleotide] database.
handle = Entrez.efetch(db="nucleotide", id=["FJ817486, JX069768, JX469983"], rettype="fasta")
#records = handle.read()
#print(records)
records = list(SeqIO.parse(handle, "fasta"))
#print(len(records[2].seq))
#print(len(records))
#first_record = next(records)
#first_record.annotations["organism"]

#print(records[0].description)
records.sort(key = lambda r: len(r))

print(records[0].description)
print(records[0].seq)
#records.sort(key = lambda x,y: cmp(len(x),len(y)))
#SeqIO.write(records, "sorted_orchids.fasta", "fasta")
#The following approach good for large file
#Get the lengths and ids, and sort on length
#en_and_ids =

#len_and_ids = sorted((len(rec), rec.id) for rec in SeqIO.parse(handle,"fasta"))

#ids = reversed([id for (length, id) in len_and_ids])

#del len_and_ids #free this memory

#Bio.SeqIO.index() allows us to retrieve the records one by one
#required file not the handle len_and_ids
#record_index = SeqIO.index(len_and_ids, "fasta") 
#records = (record_index[id] for id in ids)
#SeqIO.write(records, "sorted.fasta", "fasta")

# Get the lengths and ids, and sort on length
#with open("ls_orchid.fasta") as in_handle:
#    len_and_ids = sorted(
 #       (len(seq), title.split(None, 1)[0])
#        for title, seq in SimpleFastaParser(in_handle)
 #   )
#ids = reversed([id for (length, id) in len_and_ids])
#del len_and_ids  # free this memory

#record_index = SeqIO.index("ls_orchid.fasta", "fasta")
#with open("sorted.fasta", "wb") as out_handle:
#    for id in ids:
#        out_handle.write(record_index.get_raw(id))

from Bio import SeqIO
from Bio import motifs


handle = list(SeqIO.parse("sample1.fasta", "fasta"))


#m = motifs.create(handle)
#records = motifs.parse(handle, "meme")

print(handle[0].seq)

from Bio import SeqIO

SeqIO.convert("sample2.fastq", "fastq", "sample2.fasta", "fasta")

from Bio.Seq import Seq
from Bio.Seq import translate

coding_dna = Seq("ATGGCCATGGCGCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA")

#translate(coding_dna)
#translate(coding_dna, stop_symbol="@")
#translate(coding_dna, to_stop=True)
#translate(coding_dna, table=2)
#translate(coding_dna, table=2, to_stop=True)

my_aa = coding_dna.translate(to_stop=True)

print(len(my_aa))

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#The IUPAC.unambiguous_dna() argument specifies that we are using the alphabet {A, C, G, T} and are not including the additional ambiguity symbols provided by IUPAC notation.

my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)

my_seq

#Seq('GATCGATGGGCCTATATAGGATCGAAAATCGC', IUPACUnambiguousDNA())

my_seq.complement()

#Seq('CTAGCTACCCGGATATATCCTAGCTTTTAGCG', IUPACUnambiguousDNA())

my_seq.reverse_complement()

#Seq('GCGATTTTCGATCCTATATAGGCCCATCGATC', IUPACUnambiguousDNA())

