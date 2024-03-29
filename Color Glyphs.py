#MenuTitle: Color Glyphs
# -*- coding: utf-8 -*-
__doc__="""
Colors glyphs to differentiate if they are Base Glyphs, Composites or Mixed Composites.
"""

Font.disableUpdateInterface()

Font = Glyphs.font
baseGlyphs = []
composites = []
mixedComposites = []

for glyph in Font.glyphs:
	for layer in glyph.layers:
		componentCount = len(layer.components)
		pathsCount = len(layer.paths)	
		if componentCount == 0:
			baseGlyphs.append(glyph)
		else:
			if pathsCount == 0:
				composites.append(glyph)
			else:
				mixedComposites.append(glyph)		
	
#changes glyph color						
for glyph in baseGlyphs:
	glyph.color = 6
for glyph in composites:
	glyph.color = 10
for glyph in mixedComposites:
	glyph.color = 3

Font.enableUpdateInterface()