#MenuTitle: Color Nested Components
# -*- coding: utf-8 -*-
__doc__="""
Colors layers that have nested components.
"""

Font = Glyphs.font
tab = []

def showNestedComponents(glyph):
	for idx, layer in enumerate(glyph.layers):
		if not layer.components:
			continue
		for component in layer.components:
			component_name = component.componentName
			font = glyph.parent
			component_glyph = font.glyphs[component_name]
			if component_glyph.layers[idx].components:
				layer.setColorIndex_(1)

for glyph in Font.glyphs:
	showNestedComponents(glyph)