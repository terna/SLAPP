import os



def executeFormula(fIn,fOu,nrow,n,s):
    #v=0 #init. not required; it can interfere with the try/except structure

    pos=s.find("v")
    if pos == -1:
        print "missing 'v' in formula, row", nrow, "\nexecution stopped in error"
        fIn.close()
        fOu.close()
        os.sys.exit(1)

    pos=s.find("=")
    if pos == -1:
        print "missing '=' in formula, row", nrow, "\nexecution stopped in error"
        fIn.close()
        fOu.close()
        os.sys.exit(1)

    try:
        while s[0]==' ':
            if s[0]==' ': s=s[1:]
        pos=s.find('\n') #eliminating spaces after \n (formerly #) if any
        if pos != -1:
            while s[pos+1]==' ':
                s=s[:pos+1]+s[pos+2:]

        #print "[",n, s,"]",
        exec(s)
        return str(v)
    except:
        print "error in formula, row", nrow, "\nexecution stopped in error"
        fIn.close()
        fOu.close()
        os.sys.exit(1)
        
def fill(s):

    s=list(s)
    if s=="": return s

    change=False

    s=list(s)

    for i in range(len(s)):
        if s[i]=='&':
            if not change: change=True
            else:          change=False 
        if s[i]==' '  and change: s[i]='&'
        
    return "".join(s)

def splitUnfill(s):
    if s=="": return s

    #print s
    s=s.split()
    #print s

    for i in range(len(s)):
        s_tmp=list(s[i])
        #print s_tmp, len(s_tmp)
        for j in range(len(s_tmp)):
            if s_tmp[j] == "&": s_tmp[j]=' '
            if s_tmp[j] == "#": s_tmp[j]='\n' # inserting \n sign
        #print s_tmp
        s[i]="".join(s_tmp)

    return s    
