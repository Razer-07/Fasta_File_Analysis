from columnar import columnar

"""
final(string) :: function takes a sequence_id as string and returns  TOTAL_SCORE. 

"""

def final(string):
    t=0
    for i in range(len(string)):

        if(string[i]=="A"):
            t=t+10
        elif(string[i]=="R"):
            t=t+9
        elif(string[i]=="N"):
            t=t+8
        elif(string[i]=="D"):
            t=t+7
        elif(string[i]=="C"):
            t=t+6
        elif(string[i]=="Q"):
            t=t+5
        elif(string[i]=="E"):
            t=t+4
        elif(string[i]=="G"):
            t=t+3
        elif(string[i]=="H"):
            t=t+2   
        elif(string[i]=="I"):
            t=t+1
        elif(string[i]=="L"):
            t=t-1
        elif(string[i]=="K"):
            t=t-2
        elif(string[i]=="M"):
            t=t-3
        elif(string[i]=="F"):
            t=t-4
        elif(string[i]=="P"):
            t=t-5
        elif(string[i]=="S"):
            t=t-6
        elif(string[i]=="T"):
            t=t-7
        elif(string[i]=="W"):
            t=t-8
        elif(string[i]=="Y"):
            t=t-9
        elif(string[i]=="V"):
            t=t-10    
        elif(string[i]=="X"):
            t=t+0       
    return(t)    
    
"""
Add a ">" character to the end of file manually or 
by code . 
This character will help to break the while loop at the end of file 

example code is:

filename = "db.fasta"

with open(filename, "r") as file:
    contents = file.read()

if contents[-1] != ">":
    with open(filename, "a") as file:
        file.write(">")
        print("'>' added at the end of file")
else:
	print(" '>' already present at the end of file")
file.close()


so that while loop can close at the end of file.

"""

filename = "db.fasta"

with open(filename, "r") as file:
    contents = file.read()

if contents[-1] != ">":
    with open(filename, "a") as file:
        file.write(">")
        print(" The character '>'is added at the END of file ")
else:
	print(" '>' already present at the end of file")
file.close()


g=open("db.fasta",'r')
with g as line:
    p=line.readlines()

id_seq_dictionary = dict()


"""
The for loop will go through each line of file and if this '>' character found in first character of line the we get an SEQ_ID.
And using while loop we make a string of sequence and while loop will break if the '>' character present.
And make a dictionary of SEQ_ID and Sequence 

the for loop will run again. 
 
"""

for i in range(len(p)-2):

    if(p[i][0]==">"):
        l=p[i]
        ID=l[1:24]
        k=1
        seq=""
        while(p[i+k][0] != ">"):
            #print(p[i+k])
            p[i+k]=p[i+k].replace("\n","")
            seq=seq+p[i+k]
            k=k+1

        id_seq_dictionary.update({ID:seq})




headers =["Seq_ID", "Seq_Length" ,"Total_Score","Mean_Score"]
col=[]

for i,k in id_seq_dictionary.items():
    Total_Score=final(k)
    Mean_Score=Total_Score/len(k)
    lis=[str(i),str(len(k)),str(Total_Score),'%.6f' % Mean_Score]
    col.append(lis)    


"""

Inorder to sort according to the Mean_Score use lambda function for the nested list of col . 
Mean_Score have negative values too, so for negative value sorting we don't use reverse=True in sorting 

"""

Mean_Score_negative=[]
Mean_Score_positive=[]
for i in col:
	if(float(i[3])< 0):
		Mean_Score_negative.append(i)
	else:
		Mean_Score_positive.append(i)
		
Mean_Score_negative_sorted = sorted(Mean_Score_negative, key=lambda x: x[3])
Mean_Score_positive_sorted = sorted(Mean_Score_positive, key=lambda x: x[3],reverse=True)
Mean_Score_sorted= Mean_Score_positive_sorted + Mean_Score_negative_sorted


table = columnar(Mean_Score_sorted, headers, no_borders=True)
with open("final_output.txt", 'w') as f:
    f.writelines(table)
g.close()   		

print("Success")			
    
