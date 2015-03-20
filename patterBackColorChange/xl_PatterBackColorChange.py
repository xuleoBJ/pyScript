import simplestyle,inkex
		
class myEffect(inkex.Effect):
        def __init__(self):
                inkex.Effect.__init__(self)
                self.OptionParser.add_option("-t", "--to_color", action="store", type="string", dest="to_color", default="000000", help="By color")

	def effect(self):
                ## get user color
                toColor = "#"+self.options.to_color.strip('"').replace('#', '').lower()
##                inkex.debug(toColor)
                patternID=""
		for id, node in self.selected.iteritems():
                    if node.attrib.has_key('style'):
                        styles = simplestyle.parseStyle(node.get('style'))
                        patternID=styles['fill']

##                inkex.debug(patternID[5:-1])
                if patternID.startswith("url"):
                        defPatten =self.getElementById(patternID[5:-1])
##                inkex.debug(defPatten)
                        for node in defPatten.iterfind('{http://www.w3.org/2000/svg}rect'):
        ##                        inkex.debug(type(node))
                                if node.attrib.has_key('fill'):
                                        node.set('fill',toColor)
                                        node.set('stroke',toColor)
                                        break

e = myEffect()
e.affect()
