#MenuTitle: Lowercase Control Characters
# -*- coding: utf-8 -*-
__doc__="""
Creates a new tab with selected glyphs between lowercase control characters "n" and "o".
"""

font = Glyphs.font
tab = ''
for glyph in font.selection:
    tab += "/n/n/%s/n/o/%s/o/o\n" % (glyph.name, glyph.name)

# open new tab with text
font.newTab(tab)