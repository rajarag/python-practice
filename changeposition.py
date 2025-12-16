def muttable(string,position,character,):
    return string[:position]+character+string[position+1:]
string="rajaraja"
i,c=input().split()
ch=muttable(string,int(i),c)
print(ch)

