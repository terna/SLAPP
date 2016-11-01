"""

Typical complex rows (extension .txtx as extended txt) are:

1@3 1 2 &if n==1:v=100#else:v=10& 3

or (with the same effect)

1@3 1 2 &if n==1:v=100#if n>1:v=10& 3

or

1@3 &v=100*n& 3

or

1@3 1 2 3

; is quite complicated to be used with if, so we use #

n and v are mandatory names
  n is the value in first position of the record
  v is the result of the calculation in a formula

& starts and concludes a formula

we can have more than one formula in a row

"""


from txtxFunctions import *

fIn=open(project+"/"+fileName+".txtx","r")
fOu=open(project+"/"+fileName+".txt","w")

nrow=0
for line in fIn:
    nrow+=1
    line=fill(line) #to have formulas as blocks without spaces
    sline=splitUnfill(line) # split and restores spaces
    #print sline

    if len(sline)!=0: #skipping empty lines

     pos=sline[0].find("@")

     # found an @ sign
     if pos>=0:

        #the range of the first value
        n1=n2=0 #init. required
        try: n1=int(sline[0][0:pos])
        except:
            print "no digits or wrong characters on the left of @ in row",nrow,\
                  "\nexecution stopped in error."
            fIn.close()
            fOu.close()
            os.sys.exit(1)
        #print "*", n1

        try: n2=int(sline[0][pos+1:])
        except:
            print "no digits or wrong characters on the right of @ in row",nrow,\
                  "\nexecution stopped in error."
            fIn.close()
            fOu.close()
            os.sys.exit(1)
        #print "*", n2

     # not found an @ sign
     else:
        n1=n2=int(sline[0])

     # output, applying formulas

     for n in range(n1,n2+1):
        #print "%d " % n,
        print >> fOu, "%d " % n,
        for i in range(1,len(sline)):
        #check for the presence of a formula
            if sline[i].find("=") != -1:
                    #print "%s " % executeFormula(fIn,fOu,nrow,n,sline[i]),
                    print >> fOu, "%s " % executeFormula(fIn,fOu,nrow,n,sline[i]),
            else:
                    #print "%s " % sline[i],
                    print >> fOu, "%s " % sline[i],
        #print
        print >> fOu


fIn.close()
fOu.close()

print "File", fileName, "converted: .txtx => .txt\n"
