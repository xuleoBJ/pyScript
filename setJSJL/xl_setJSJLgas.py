#!/usr/bin/env python
import simplestyle,inkex
class XLchangeFillColorEffect(inkex.Effect):
	def __init__(self):
		inkex.Effect.__init__(self)
	def effect(self):
		for id, node in self.selected.iteritems():
			if node.attrib.has_key('style'):
				styles = simplestyle.parseStyle(node.get('style'))
				this_color = '#%02x%02x%02x' % (255,153,0)
				styles['fill']=this_color
				node.set('style',simplestyle.formatStyle(styles))
e = XLchangeFillColorEffect()
e.affect()
