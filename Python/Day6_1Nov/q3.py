import sys as s
f=open(s.argv[1],'w')
f.write(str([str(x)+'x'+s.argv[2]+'='+str(x*int(s.argv[2])) for x in range(1,11)]))
f.close()
