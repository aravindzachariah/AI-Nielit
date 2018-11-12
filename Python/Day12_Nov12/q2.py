import xml.dom.minidom as dm
dtree=dm.parse('book.xml')
rm=dtree.documentElement
for bm in rm.childNodes:
	if bm.nodeType==1:
		print "-----------------------"
		for k in bm.attributes.keys():
			print bm.attributes[k].name.title()," : ",bm.attributes[k].value.title()
	for tn in bm.childNodes:
		for tx in tn.childNodes:
			print tx.parentNode.nodeName.title()," : ",tx.nodeValue
