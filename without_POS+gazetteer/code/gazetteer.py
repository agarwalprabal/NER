import os,sys
fp=open('../test_data/test_gazetteer','r')
fp.readline()
pre=fp.readline()
pres=fp.readline()
se=0
flag=0
while(1):
    wpre=pre.split('\t')
    wpres=pres.split('\t')
    for i in range (len(wpre)):
        wpre[i]=wpre[i].strip()
        wpres[i]=wpres[i].strip()
    fp1=open('../gazetteers/NEO','r')
    while(1):
        NE='O'
        content=fp1.readline()
        if(content==''):
            break
        ne=content.strip()
        if(wpre[1].lower()==ne.lower()):
            NE='B-NEO'
            break
    fp2=open('../gazetteers/NEB','r')
    while(1):
        e=0
        content=fp2.readline()
        if(content==''):
            if(flag==1):
                flag=0
            break
        ne=content.split(' ')
        for i in range (len(ne)):
            ne[i] = ne[i].strip()
        if((len(ne)==2) and (ne[0].lower() == wpre[1].lower())):
            NE = 'B-NEB'
            flag=1
            break
        for i in range ((len(ne)-1)):
            b=0
            if((len(ne) == 2) and (ne[i].lower() == wpre[1].lower())):
                print 'here'
                NE = 'B-NEB'
                flag=1
                e=1
                break
            if((wpre[1].lower()== ne[i].lower()) and ((len(ne))!=2)):
                while(1):
                    if(len(ne)>2):
                        for i in range (len(ne)):
                            ne[i]=ne[i].strip()
                        for i in range (len(ne)-2):
                            if(wpre[1].lower()==ne[i].lower() and wpres[1].lower()==ne[i+1].lower()):
                                if((NE=='O' or NE=='B-NEO') and flag==0):
                                    NE='B-NEB'
                                    flag=1
                                    break
                                if(NE=='O' and flag==1):
                                    NE='I-NEB'
                                    break
                    if(NE=='B-NEB' or NE=='I-NEB'):
                        b=2
                        break
                    content=fp2.readline()
                    if(content==''):
                        if(flag==1 and NE!='B-NEO'):
                            NE='I-NEB'
                        flag=0
                        b=1
                        break
                    ne=content.split(' ')
                if(flag==0 and NE=='O'):
                    fp3=open('../gazetteers/NEB','r')
                    while(1):
                        content1=fp3.readline()
                        if(content1==''):
                            break
                        nes=content1.split(' ')
                        for i in range (len(nes)):
                            nes[i]=nes[i].strip()
                        if(len(nes)==2 and wpre[1].lower()==nes[0].lower()):
                            NE='B-NEB'
                            flag=1
                            b=3
                            break
                    fp3.close()
            if(b==1 or b==2 or b==3):
                e=1
                break
        if(e==1):
            break
    fp2.close()
    fp1.close()
    print '{0}\t{1}'.format(wpre[1],NE)
    pre=pres
    pres=fp.readline()
# for line gap at senetnce ending
    if(se==1):
        print ''
        se=0
    if(pres=='\t</Sentence>\n'):
        se=1
        pres=fp.readline()
        pres=fp.readline()
        if(pres==''):
            print '.\tO'
            break
fp.close()
