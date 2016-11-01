# the lib xlrd is at http://pypi.python.org/pypi/xlrd
#Versions of Excel supported:
#    2004, 2003, 2002, XP, 2000, 97, 95, 5.0, 4.0, 3.0.


import os
import turtle

#project='school' or 'production' # to run tests

timeCount=0.0
def tC():
    global timeCount
    timeCount=timeCount+0.000001
    return timeCount

try:
    import xlrd
except:
    w=open("WARNING.txt","r")
    for line in w:
        print line,
    w.close()
    os.sys.exit(1)

def flat(aList):
    a=""
    for i in range(len(aList)):
        if i==len(aList)-1: a+=aList[i]
        else:               a+=aList[i]+" "
    return a

def out_table(sh, book,f,rec): #!!!!!!!!!!
    #print "          start ", rec #test
    for r in range(sh.nrows):
      cols=sh.ncols
      if cols > 3: cols=3
      for c in range(cols):
          current=sh.cell_value(r,c)
          if c==0 and current=='': break
          if  current=='macro':
              #print '          macro ', sh.cell_value(r,c+1) #test
              if book.sheet_names().count(sh.cell_value(r,c+1))==0:
                  print "ERROR: sheet '"+sh.cell_value(r,c+1)+"' missing"
                  turtle.bye() # does not create problems if the graphic space is missing
                  os.sys.exit(1)
              sh_macro=book.sheet_by_index(book.sheet_names()\
                                      .index(sh.cell_value(r,c+1)))
              # open the macro sheet
              rec+=1 #!!!!!!!
              rec=out_table(sh_macro, book,f,rec)
              if r>0:
                  if sh.cell_value(r-1,0)=="#": #New
                    print >>f, "#",int(sh.cell_value(r-1,1))+tC() # a small addendum
                                                                  # to preserve order

                    #print "#",int(sh.cell_value(r-1,1)) #test

          else:
              if c==1 and sh.cell_value(r,0)=="#":
                  print >>f, int(current)+tC(), # a small addendum
                                               # to preserve order
              else:
                  print >>f, current,
          if current=='macro': break
      if current != 'macro' and c != 0:
          print >>f
          #print #test
    #print '          finish ', rec # test
    rec-=1 # measure of recursion, for tests
    return rec # measure of recursion, for test


files=os.listdir(project)
if "schedule.xls" in files:

 # translating
 f=open(project+"/schedule.txt","w")
 book = xlrd.open_workbook(project+"/schedule.xls")
 sh = book.sheet_by_index(0)
 if book.sheet_names()[0] != "schedule":
     print "Error, first sheet in schedule.txt has to be named 'schedule'"
     turtle.bye()
     os.sys.exit(1)
 out_table(sh,book,f,1)
 f.close()

 # post processing to order blocks, if necessary
 ll=[]
 lx=[]
 f=open(project+"/schedule.txt","r")
 for line in f:
     contents=line.split()
     #print contents

     if contents[0]=="#":
         if lx != []: ll.append(lx)
         lx=[]
         lx.append(float(contents[1]))
         if len(contents)==3:lx.append(int(float(contents[2])))

     else: lx.append(flat(contents))
 ll.append(lx)

 #print ll

 #print
 f.close()

 #print
 lll=0
 kk=len(ll)
 for i in range(kk):
     #print ll[i]
     if len(ll[i])>1:
         if isinstance(ll[i][1],int):
             i1=ll[i][0]+1; i2=ll[i][1]
             ll[i].pop(1)
             #print ll[i]
             del lll
             lll=ll[i][:]

             for k in range(int(i1),i2+1):
                 lll[0]=k+i1-int(i1)
                 ll.append(lll[:])
                 #print lll

 #print

 # managing repetitions (if isinstance(ll[i][1],int) is true)



 # sorting
 ll.sort(cmp=lambda x,y: cmp(x[0], y[0])) # so operating only on the first element print ll

 #for i in range(len(ll)):
 #    print ll[i]
 #print

 f=open(project+"/schedule.txt","w")
 sharp=0
 for i in range(len(ll)):
     ll[i][0]=int(ll[i][0])
     if ll[i][0]==sharp: pass
     else:
         sharp=ll[i][0]
         print >>f, '#', sharp

     for j in range(1,len(ll[i])):
         print >>f, ll[i][j]
 f.close()
