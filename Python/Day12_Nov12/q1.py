import xml.dom.minidom as dm
dtree=dm.parse('book.xml')
rm=dtree.documentElement
f=open('book1.txt','w')
c=0
for bm in rm.childNodes:
	if bm.nodeType==1:
		for k in bm.attributes.keys():
			tm= bm.attributes[k].name.title()
			tmname=bm.attributes[k].value.title()
	for tn in bm.childNodes:
		for tx in tn.childNodes:
			a=tx.parentNode.nodeName.title()
			if a=="Title":
				title=tx.nodeValue.title()
			if a=="Author":
                                author=tx.nodeValue.title()
			if a=="Year":
                                year=tx.nodeValue.title()
			if a=="Price":
				c+=1 
                                price=tx.nodeValue.title()
				f.writelines("%d.The book %s belongs to %s category and is witten by %s.\n" % (c,title,tmname,author))  
                                f.writelines("   This book is published in the year %s with a price of %s.\n" % (year,price))			
