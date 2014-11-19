# for generating training files from pos tagged file after manual annotation
import os,sys
fp= open(sys.argv[1],"r")
temp_path='../training_data/train_gazetteer'
temp_path_2 = '../training_data/train_crf'
# suffix length
slen=int(raw_input('Enter suffix length:'))
#prefix length
plen=int(raw_input('Enter prefix length:'))
fp1=open(temp_path,'w')
fp2=open(temp_path_2,'w')
count=1
id=1
flag=0
while(count==1):
    content = fp.readline()
    w=content.split('\t')
    for i in range (len(w)):
        w[i]=w[i].strip()
    l_ne=len(w[0])
    if(l_ne>0 and (w[0][-3:]=='NEM' or w[0][-3:]=='NEN' or w[0][-3:]=='ETI' or w[0][-3:]=='ETE')):
        w[0]='O'
    if(l_ne>0 and w[0][0]=='B'):
        flag=1
        ne=w[0][1:]
    if(l_ne>0 and w[0][0]=='E'):
        w[0]='I{0}'.format(ne)
        flag=0
    if(flag==1 and w[0]==''):
        w[0]='I{0}'.format(ne)
    if(flag==0 and w[0]==''):
        w[0]='O'
    if(l_ne>0 and flag==0  and w[0][0]=='N'):
        w[0]='B-'+w[0]
    l=len(w)
    if(l<4):
        if (content == ('\n')):
            continue
        elif(content == ('\t<Sentence id="1">\n')):
            fp1.write('\t<Sentence id="{0}">\n'.format(id))
            fp2.write('')
            id= id+1
        elif (content == ('\t</Sentence>\n')):
            fp1.write('\t</Sentence>\n')
            fp2.write('\n')
        elif(content==''):
            break
        
    else:
        fp1.write('{0}\t{1}\t{2}\t{3}\n'.format(w[1],w[2],w[3],w[0]))
        lw=len(w[2])
        if(lw>=max(slen,plen)):
            p=''
            s=''
            for i in range(0,(plen)):
                p= p+w[2][i]
            for i in range(-slen,0):
                s= s+w[2][i]
            fp2.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n'.format(w[2],w[3],lw,p,s,w[0]))
        else:
            p=w[2]
            s=w[2]
            fp2.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n'.format(w[2],w[3],lw,p,s,w[0]))
fp.close       
fp1.close
fp2.close
