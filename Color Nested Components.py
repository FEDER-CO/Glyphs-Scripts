#MenuTitle: Color Nested Components
# -*- coding: utf-8 -*-
__doc__="""
Creates a new tab with glyphs that have nested components and colors their layers.
"""

Font = Glyphs.font
tab = []

def showNestedComponents(glyph):
	glyphHasNestedComponents=False
	for idx, layer in enumerate(glyph.layers):
		for component in layer.components:
			component_name = component.componentName
			if component.componentLayer.components:
				layer.setColorIndex_(1)
				glyphHasNestedComponents=True
	return glyphHasNestedComponents

collectedGlyphs=[]
for glyph in Font.glyphs:
	if showNestedComponents(glyph):
		collectedGlyphs.append(glyph.name)

if collectedGlyphs:
	tabText="/"+"/".join(collectedGlyphs)
	Font.newTab(tabText)
	Glyphs.showNotification("Found %i nested components" % len(collectedGlyphs), "New tab is open in %s"%Font.familyName)
else:
	Glyphs.showNotification("Good to go!", "The font doesn't contain nested components.")