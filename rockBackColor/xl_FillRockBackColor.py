import simplestyle,inkex
		
class myEffect(inkex.Effect):
        def __init__(self):
                inkex.Effect.__init__(self)
                self.OptionParser.add_option("-t", "--rockColor", action="store", type="string", dest="rockColor", default="255,255,255", help="By color")
	def effect(self):
                ## get user color
                rgb=self.options.rockColor.lower().split(',')
##                inkex.debug(rgb)
                toColor = '#%02x%02x%02x' % (int(rgb[0]),int(rgb[1]),int(rgb[2]))
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
