from Bio import SeqIO
import requests

file = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_mprt.txt", "r")
ID = file.read().split()
file.close()
#ID = ["A2Z669", "B5ZC00","P07204_TRBM_HUMAN", "P20840_SAG1_YEAST"]
#ID = ["A2Z669", "B5ZC00"]
record = {}
#print (ID)

for i in ID:   
    response = requests.get("http://www.uniprot.org/uniprot/"+i+".fasta")
    fastaform = response.text
    front, back  = fastaform.find('\n'), fastaform.rfind('\n')
    record[i] = fastaform[front+1:back].replace("\n","")


def N_gly_motif(sequence):
    global result
    result = []
    for i in range(0, len(sequence)-3):
        short = sequence[i:i+4]
        if (short[0]=="N") and (short[2] == "S" or short[2] == "T") and (short[1] !="P") and (short[3] != "P"):
            result.append(i+1)

for key, value in record.items():
    N_gly_motif (value)
    if not result:
        continue
    else:
        print(key)
        strresult = str(result)[1:-1]
        print(strresult.replace(',', ''))

#print (record)


'''
motifpos = {}
for id in ID:
    for spemotif in range(len(motif)):
        for pos, char in enumerate(record[id]):
            if (char == motif[spemotif]):
                motifpos[id] = pos
'''
#print (motifpos)