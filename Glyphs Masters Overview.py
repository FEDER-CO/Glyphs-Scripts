#MenuTitle: Glyphs Masters Overview
# -*- coding: utf-8 -*-
__doc__="""
Creates a new tab with rows of selected glyphs in all available masters. It ignores brace, bracket or a smart component layers. Useful for comparing the different weights of a typeface.
"""

font = Glyphs.font
font.newTab()
for glyph in font.selection:
	font.currentTab.layers.append(GSControlLayer(10))
	for layer in glyph.layers:
		if layer.isMasterLayer is True :
			font.currentTab.layers.append(layer)