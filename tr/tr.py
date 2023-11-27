with open('./si.txt','rt',encoding='UTF-8') as f:
    lines=f.readlines()
txt=r'\begin{thebiblipgraphy}{99}'+'\n\n'
for i in range(len(lines)):
    re=lines[i].find('.')
    s=''.join(filter(None,lines[i][re+1:]))
    ind='ref'+str(i+1)
    txt+=fr'\bibitem'+'{'+ind+'}'+s
txt+='\n\n'+r'\end{thebiblipgraphy}'
with open('si_transed.txt','wt',encoding='UTF-8') as f:f.write(txt)