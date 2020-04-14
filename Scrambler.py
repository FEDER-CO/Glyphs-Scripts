#MenuTitle: Scrambler
# -*- coding: utf-8 -*-
__doc__="""
Creates a new tab with a generated random sequence of selected glyphs.
"""

import random
random.seed()

font = Glyphs.font
currentLayers = font.selectedLayers
printableLayers = []
tab = []
if currentLayers is None:
	for glyph in font.glyphs:
		printableLayers.append('/'+ glyph.name)
	for i in range(500):
		tab.append(random.choice(printableLayers))
	font.newTab(''.join(tab))
else:
	for eachLayer in currentLayers:
		printableLayers.append('/'+ eachLayer.parent.name)
	for i in range(500):
		tab.append(random.choice(printableLayers))
	font.newTab(''.join(tab))