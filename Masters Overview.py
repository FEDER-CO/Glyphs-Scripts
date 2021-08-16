#MenuTitle: Masters Overview
# -*- coding: utf-8 -*-
__doc__="""
Creates a new tab with rows of selected glyphs in all available master layers. Useful for comparing the different weights of a typeface.
"""

Font = Glyphs.font
Font.newTab()
for glyph in Font.selection:
	Font.currentTab.layers.append(GSControlLayer(10))
	for layer in glyph.layers:
		if layer.isMasterLayer is True :
			Font.currentTab.layers.append(layer)
