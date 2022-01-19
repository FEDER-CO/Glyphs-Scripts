#MenuTitle: Prepare for Pre-production
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
__doc__="""
Removes glyphOrder, guides, backup layers, annotations, background, images, color, unlocks glyphs.
"""

def prepareFontInfo( thisFont ):
	fontParameterList = ("glyphOrder",)
	for parameterName in fontParameterList:
		while thisFont.customParameters[parameterName]:
			del thisFont.customParameters[parameterName]
			print("🚫 %s" % parameterName)

def cleanUpMaster( thisMaster ):
	# delete global guides:
	if thisMaster.guides:
		print("🚫 Deleted %i global guides" % len(thisMaster.guides))
		thisMaster.guides = None

def cleanUpGlyph( thisGlyph ):
	# remove backup layers:
	delCount = 0
	for i in reversed(range(len(thisGlyph.layers))):
		thisLayer = thisGlyph.layers[i]
		if not thisLayer.isMasterLayer and not thisLayer.isSpecialLayer:
			del thisGlyph.layers[i]
			delCount += 1
	if delCount:
		print("  Deleted %i layers" % delCount)

	# clear layer stuff
	for thisLayer in thisGlyph.layers:
		if thisLayer.shapes:
			for thisShape in thisLayer.shapes:
				if type(thisShape) is GSPath:
					for thisNode in thisShape.nodes:
						thisNode.name = None
		if thisLayer.background:
			thisLayer.background = None
			# print("  %s: removed layer background" % thisLayer.name)
		if thisLayer.annotations:
			thisLayer.annotations = None
			print("  %s: removed layer annotations" % thisLayer.name)
		if thisLayer.guides:
			thisLayer.guides = None
			print("  %s: removed layer guides" % thisLayer.name)
		if thisLayer.backgroundImage:
			thisLayer.backgroundImage = None
			print("  %s: removed layer background image" % thisLayer.name)
		if thisLayer.color:
			thisLayer.color = None
			print("  %s: removed layer color" % thisLayer.name)
		if thisLayer.locked():
			thisLayer.setLocked_(0)
			print("  %s: Unlocked" % thisLayer.name)

	# clear glyph stuff
	if thisGlyph.note:
		thisGlyph.note = None
		print("  Removed glyph note")
	if thisGlyph.color:
		thisGlyph.color = None
		print("  Removed glyph color")
	if thisGlyph.locked:
		thisGlyph.locked = False
		print("  Unlocked glyph")

thisFont = Glyphs.font # frontmost font
Glyphs.clearLog() # clears log in Macro window
Glyphs.showMacroWindow()
print("Preparing for Preproduction: %s" % thisFont.familyName)
if thisFont.filepath:
	print("📄 %s" % thisFont.filepath)

thisFont.disableUpdateInterface() # suppresses UI updates in Font View
try:
	print("\nProcessing glyphs:")
	for thisGlyph in thisFont.glyphs:
		print("🔠 %s" % thisGlyph.name)
		thisGlyph.beginUndo() # begin undo grouping
		cleanUpGlyph( thisGlyph )
		thisGlyph.endUndo()   # end undo grouping

	print("\nProcessing Masters:")
	for thisMaster in thisFont.masters:
		print("🤴🏾 Master: %s" % thisMaster.name)
		cleanUpMaster(thisMaster)

	print("\nProcessing Font Info:")
	prepareFontInfo( thisFont )
	
	print("\n✅ Done.")
except Exception as e:
	Glyphs.showMacroWindow()
	print("\n⚠️ Error in script: Prepare for Pre-production\n")
	import traceback
	print(traceback.format_exc())
	print()
	raise e
finally:
	thisFont.enableUpdateInterface() # re-enables UI updates in Font View
