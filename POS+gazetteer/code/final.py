import os,sys
fml=open('../output/crf','r')
fgaz=open('../output/gazetteer','r')
#ffinal=open('../output/final','w')
while(1):
    crf=fml.readline()
    gaz=fgaz.readline()
    if(crf==''):
        break
    if(crf=='\n'):
        print ''
        crf=fml.readline()
        gaz=fgaz.readline()
    wcrf=crf.split('\t')
    wgaz=gaz.split('\t')
    for i in range (len(wcrf)):
        wcrf[i]=wcrf[i].strip()
    for i in range (len(wgaz)):
        wgaz[i]=wgaz[i].strip()
    if(wgaz[-1]!='O'):
        NE=wgaz[-1]
    if(wgaz[-1]=='O' and wcrf[-1]!='O'):
        NE=wcrf[-1]
    if(wgaz[-1]=='O' and wcrf[-1]=='O'):
        NE='O'
    print'{0}\t{1}'.format(wcrf[0],NE)
fml.close()
fgaz.close()
#ffinal.close()
