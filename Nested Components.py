#MenuTitle: Nested Components
# -*- coding: utf-8 -*-
__doc__="""
Creates a new tab with glyphs that have nested components.
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
				tab.append('/'+ glyph.name)
				print("Glyph %s has nested Components" % glyph.name)


for glyph in Font.glyphs:
	showNestedComponents(glyph)

# open new tab with nested components
Font.newTab(''.join(tab))