#MenuTitle: Reinterpolate Current Layer
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
__doc__="""
Reinterpolates currently selected layer.
"""

from copy import copy as deepcopy

def process( thisLayer ):
	backupLayer = deepcopy(thisLayer)
	thisLayer.reinterpolate()
	if len(thisLayer.shapes)==0 and len(backupLayer.shapes) > 0:
		thisLayer.shapes = backupLayer.shapes
	thisLayer.selection = None

thisFont = Glyphs.font # frontmost font
selectedLayers = thisFont.selectedLayers # active layers of selected glyphs
Glyphs.clearLog() # clears log in Macro window

thisFont.disableUpdateInterface() # suppresses UI updates in Font View
try:
	for thisLayer in selectedLayers:
		thisGlyph = thisLayer.parent
		print("Processing %s" % thisGlyph.name)
		thisGlyph.beginUndo() # begin undo grouping
		process( thisLayer )
		thisGlyph.endUndo()   # end undo grouping
except Exception as e:
	Glyphs.showMacroWindow()
	print("\n⚠️ Error in script: Reinterpolate Current Layer\n")
	import traceback
	print(traceback.format_exc())
	print()
	raise e
finally:
	thisFont.enableUpdateInterface() # re-enables UI updates in Font View
