#MenuTitle: Uppercase Control Characters
# -*- coding: utf-8 -*-
__doc__="""
Creates a new tab with selected glyphs between uppercase control characters "H" and "O".
"""

font = Glyphs.font
tab = ''
for glyph in font.selection:
    tab += "/H/H/%s/H/O/%s/O/O\n" % (glyph.name, glyph.name)

# open new tab with text
font.newTab(tab)