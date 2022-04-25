#MPRT new

import uniprot
import urllib.parse
import urllib.request
import os
import time
from urllib.request import urlopen
url = 'http://www.uniprot.org/uniprot'
id_list = ["A2Z669", "B5ZC00","P07204_TRBM_HUMAN", "P20840_SAG1_YEAST"]

for i in id_list:
    fasta = urlopen('http://www.uniprot.org/uniprot'+i+'.fasta')
    print (fasta)
    try:
        params = {
        'from' : 'ID',
        'to' : 'EMBL'
        'format' : 'tab'
        'guery' : id
        }
        data = urllib.parse.urlencode(params)
        data = data.encode('utf-8')
        req = urllib.request.Request(url,data)
        with urllib.request.urlopen(req) as f:
            response = f.read()

        output = response.decode('utf-8').split("\n")[1]



'''with open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_mprt_fasta.txt", "w") as output:
        print(f)
        fasta_sequence = SeqIO.parse(output, "fasta")
        record[fasta_sequence.id] = fasta_sequence.seq'''
    #response = r.post("http://www.uniprot.org/uniprot/"+i+".fasta")
    #cData = ''.join(response.text)
    #Seq = StringIO(cData)
    #for pSeq in SeqIO.parse(Seq, 'fasta'):
    #    record[i] = pSeq.seq
#print (record)
#print (open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_mprt.txt", "r"))
'''