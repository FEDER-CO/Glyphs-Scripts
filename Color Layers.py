#MenuTitle: Color Layers
# -*- coding: utf-8 -*-
__doc__="""
Colors glyph layers to differentiate if they are Base Glyphs, Composites or Mixed Composites.
"""

Font = Glyphs.font
baseGlyphs = []
composites = []
mixedComposites = []

for glyph in Font.glyphs:
	for layer in glyph.layers:
		componentCount = len(layer.components)
		pathsCount = len(layer.paths)	
		if componentCount == 0:
			baseGlyphs.append(layer)
		else:
			if pathsCount == 0:
				composites.append(layer)
			else:
				mixedComposites.append(layer)			
#changes layer color						
for layer in baseGlyphs:
	layer.setColorIndex_(6)
for layer in composites:
	layer.setColorIndex_(10)
for layer in mixedComposites:
	layer.setColorIndex_(3)
	
