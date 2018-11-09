import xml.sax

class ourhandler(xml.sax.ContentHandler):
    def __init__(self):
        self.title = ' '
        self.author = ' '
        self.year = ' '
        self.price = ' '
        self.currtag = ' '

    def startElement(self,tagname,attr):
        self.currtag = tagname
        if tagname == 'title':
            print '*********************'

    def characters(self,content):
        if self.currtag == 'title':
            self.title = content
        if self.currtag == 'author':
            self.author = content
        if self.currtag == 'year':
            self.year = content
        if self.currtag == 'price':
            self.price = content

    def endElement(self,tag):
        if tag=='title':
            print self.title
	if tag=='author':
	    print self.author
	if tag=='year':
	    print self.year
	if tag=='price':
	    print self.price

pobj = xml.sax.make_parser()
oho = ourhandler()
pobj.setContentHandler(oho)
pobj.parse('/home/ai3/Desktop/common/Python_Exercises/book.xml')
