#MenuTitle: Set Kerning Groups (Lat-Grk-Cyr)
# -*- coding: utf-8 -*-
from __future__ import print_function, division, unicode_literals
__doc__="""
(GUI) Sets kerning groups. Groups Latin Greek and Cyrillic together. I advise you use Split Cross-Script Kerning script later.
"""

import vanilla
import GlyphsApp
import re

class SetKernPairs ( object ):
	def __init__( self ):
		# Window 'self.w':
		textY  = 19
		spaceX = 10
		spaceY = 10
		buttonX = 90
		buttonY = 20
		windowWidth  = spaceX*4+buttonX*3
		windowHeight = spaceY*6+textY*2+buttonY
		self.w = vanilla.FloatingWindow(
			( windowWidth, windowHeight ), # default window size
			"Set Kerning Groups", # window title
		)
		self.w.textLower = vanilla.TextBox((spaceX, spaceY, 200, textY), "Lowercase style?", sizeStyle='regular')
		self.w.normalButton = vanilla.Button((spaceX, spaceY*2+textY, buttonX, buttonY), "Normal", sizeStyle='regular', callback=self.SetKernPairsMain )
		self.w.cursiveButton = vanilla.Button((spaceX*2+buttonX, spaceY*2+textY, buttonX, buttonY), "Cursive", sizeStyle='regular', callback=self.SetKernPairsMain )
		self.w.allcapButton = vanilla.Button((spaceX*3+buttonX*2, spaceY*2+textY, buttonX, buttonY), "All Cap", sizeStyle='regular', callback=self.SetKernPairsMain )

		self.w.line = vanilla.HorizontalLine((spaceX, spaceX*4+textY*2, -spaceX, 1))
		self.w.radioButton = vanilla.RadioGroup((spaceX, spaceY*5+textY*2, 300, textY), ["All Glyphs", "Selected Glyphs"], sizeStyle='regular', isVertical=False)

		# Open window and focus on it:
		self.w.open()
		self.w.radioButton.set(0)
		self.w.makeKey()
		


	def SetKernPairsMain( self, sender ):
		try:
			thisFont = Glyphs.font # frontmost font
			groupsUC = {
				"A" : ["UC_A", "UC_A"],
				"Aacute" : ["UC_A", "UC_A"],
				"Abreve" : ["UC_A", "UC_A"],
				"Acircumflex" : ["UC_A", "UC_A"],
				"Adieresis" : ["UC_A", "UC_A"],
				"Agrave" : ["UC_A", "UC_A"],
				"Amacron" : ["UC_A", "UC_A"],
				"Aogonek" : ["UC_A", "UC_A"],
				"Aring" : ["UC_A", "UC_A"],
				"Aringacute" : ["UC_A", "UC_A"],
				"Atilde" : ["UC_A", "UC_A"],
				"AE" : ["UC_AE", "UC_E"],
				"AEacute" : ["UC_AE", "UC_E"],
				"B" : ["UC_Stem", "UC_B"],
				"C" : ["UC_Round", "UC_C"],
				"Cacute" : ["UC_Round", "UC_C"],
				"Ccaron" : ["UC_Round", "UC_C"],
				"Ccedilla" : ["UC_Round", "UC_C"],
				"Ccircumflex" : ["UC_Round", "UC_C"],
				"Cdotaccent" : ["UC_Round", "UC_C"],
				"D" : ["UC_Stem", "UC_Round"],
				"Eth" : ["UC_Eth", "UC_Round"],
				"Dcaron" : ["UC_Stem", "UC_Round"],
				"Dcroat" : ["UC_Eth", "UC_Round"],
				"E" : ["UC_Stem", "UC_E"],
				"Eacute" : ["UC_Stem", "UC_E"],
				"Ebreve" : ["UC_Stem", "UC_E"],
				"Ecaron" : ["UC_Stem", "UC_E"],
				"Ecircumflex" : ["UC_Stem", "UC_E"],
				"Edieresis" : ["UC_Stem", "UC_E"],
				"Edotaccent" : ["UC_Stem", "UC_E"],
				"Egrave" : ["UC_Stem", "UC_E"],
				"Emacron" : ["UC_Stem", "UC_E"],
				"Eogonek" : ["UC_Stem", "UC_E"],
				"F" : ["UC_Stem", ""],
				"G" : ["UC_Round", "UC_G"],
				"Gbreve" : ["UC_Round", "UC_G"],
				"Gcircumflex" : ["UC_Round", "UC_G"],
				"Gcommaaccent" : ["UC_Round", "UC_G"],
				"Gcaron" : ["UC_Round", "UC_G"],
				"Gdotaccent" : ["UC_Round", "UC_G"],
				"H" : ["UC_Stem", "UC_Stem"],
				"Hbar" : ["UC_Stem", "UC_Stem"],
				"Hcircumflex" : ["UC_Stem", "UC_Stem"],
				"I" : ["UC_Stem", "UC_Stem"],
				"IJ" : ["UC_Stem", "UC_J"],
				"Iacute" : ["UC_Stem", "UC_Stem"],
				"Ibreve" : ["UC_Stem", "UC_Stem"],
				"Icircumflex" : ["UC_Stem", "UC_Stem"],
				"Idieresis" : ["UC_Stem", "UC_Stem"],
				"Idotaccent" : ["UC_Stem", "UC_Stem"],
				"Igrave" : ["UC_Stem", "UC_Stem"],
				"Imacron" : ["UC_Stem", "UC_Stem"],
				"Iogonek" : ["UC_Stem", "UC_Stem"],
				"Itilde" : ["UC_Stem", "UC_Stem"],
				"J" : ["UC_J", "UC_J"],
				"Jcircumflex" : ["UC_J", "UC_J"],
				"K" : ["UC_Stem", "UC_K"],
				"Kcommaaccent" : ["UC_Stem", "UC_K"],
				"L" : ["UC_Stem", "UC_L"],
				"Lacute" : ["UC_Stem", "UC_L"],
				"Lcaron" : ["UC_Stem", "UC_L"],
				"Lcommaaccent" : ["UC_Stem", "UC_L"],
				"Ldot" : ["UC_Stem", ""],
				"Lslash" : ["UC_Eth", "UC_L"],
				"M" : ["UC_Stem", "UC_Stem"],
				"N" : ["UC_Stem", "UC_Stem"],
				"Nacute" : ["UC_Stem", "UC_Stem"],
				"Ncaron" : ["UC_Stem", "UC_Stem"],
				"Ncommaaccent" : ["UC_Stem", "UC_Stem"],
				"Eng" : ["UC_Stem", ""],
				"Ntilde" : ["UC_Stem", "UC_Stem"],
				"O" : ["UC_Round", "UC_Round"],
				"Oacute" : ["UC_Round", "UC_Round"],
				"Obreve" : ["UC_Round", "UC_Round"],
				"Ocircumflex" : ["UC_Round", "UC_Round"],
				"Odieresis" : ["UC_Round", "UC_Round"],
				"Ograve" : ["UC_Round", "UC_Round"],
				"Ohungarumlaut" : ["UC_Round", "UC_Round"],
				"Omacron" : ["UC_Round", "UC_Round"],
				"Oslash" : ["UC_Round", "UC_Round"],
				"Oslashacute" : ["UC_Round", "UC_Round"],
				"Otilde" : ["UC_Round", "UC_Round"],
				"OE" : ["UC_Round", "UC_E"],
				"P" : ["UC_Stem", "UC_P"],
				"Thorn" : ["UC_Stem", ""],
				"Q" : ["UC_Round", ""],
				"R" : ["UC_Stem", "UC_R"],
				"Racute" : ["UC_Stem", "UC_R"],
				"Rcaron" : ["UC_Stem", "UC_R"],
				"Rcommaaccent" : ["UC_Stem", "UC_R"],
				"S" : ["UC_S", "UC_S"],
				"Sacute" : ["UC_S", "UC_S"],
				"Scaron" : ["UC_S", "UC_S"],
				"Scedilla" : ["UC_S", "UC_S"],
				"Scircumflex" : ["UC_S", "UC_S"],
				"Scommaaccent" : ["UC_S", "UC_S"],
				"T" : ["UC_T", "UC_T"],
				"Tbar" : ["UC_T", "UC_T"],
				"Tcaron" : ["UC_T", "UC_T"],
				"Tcedilla" : ["UC_T", "UC_T"],
				"Tcommaaccent" : ["UC_T", "UC_T"],
				"U" : ["UC_U", "UC_U"],
				"Uacute" : ["UC_U", "UC_U"],
				"Ubreve" : ["UC_U", "UC_U"],
				"Ucircumflex" : ["UC_U", "UC_U"],
				"Udieresis" : ["UC_U", "UC_U"],
				"Ugrave" : ["UC_U", "UC_U"],
				"Uhungarumlaut" : ["UC_U", "UC_U"],
				"Umacron" : ["UC_U", "UC_U"],
				"Uogonek" : ["UC_U", "UC_U"],
				"Uring" : ["UC_U", "UC_U"],
				"Utilde" : ["UC_U", "UC_U"],
				"W" : ["UC_W", "UC_W"],
				"Wacute" : ["UC_W", "UC_W"],
				"Wcircumflex" : ["UC_W", "UC_W"],
				"Wdieresis" : ["UC_W", "UC_W"],
				"Wgrave" : ["UC_W", "UC_W"],
				"X" : ["UC_X", "UC_X"],
				"Y" : ["UC_Y", "UC_Y"],
				"Yacute" : ["UC_Y", "UC_Y"],
				"Ycircumflex" : ["UC_Y", "UC_Y"],
				"Ydieresis" : ["UC_Y", "UC_Y"],
				"Ygrave" : ["UC_Y", "UC_Y"],
				"Z" : ["UC_Z", "UC_Z"],
				"Zacute" : ["UC_Z", "UC_Z"],
				"Zcaron" : ["UC_Z", "UC_Z"],
				"Zdotaccent" : ["UC_Z", "UC_Z"],
				"Schwa" : ["UC_Schwa", "UC_Round"],
				"A-cy" : ["UC_A", "UC_A"],
				"Be-cy" : ["UC_Stem", ""],
				"Ve-cy" : ["UC_Stem", "UC_B"],
				"Ge-cy" : ["UC_Stem", "UC_T"],
				"Gje-cy" : ["UC_Stem", "UC_T"],
				"Gheupturn-cy" : ["UC_Stem", "UC_T"],
				"De-cy" : ["", "UC_StemTooth"],
				"Ie-cy" : ["UC_Stem", "UC_E"],
				"Iegrave-cy" : ["UC_Stem", "UC_E"],
				"Io-cy" : ["UC_Stem", "UC_E"],
				"Zhe-cy" : ["UC_Zhe", "UC_K"],
				"Ze-cy" : ["UC_Ze", "UC_B"],
				"Ii-cy" : ["UC_Stem", "UC_Stem"],
				"Iishort-cy" : ["UC_Stem", "UC_Stem"],
				"Iigrave-cy" : ["UC_Stem", "UC_Stem"],
				"Ka-cy" : ["UC_Stem", "UC_K"],
				"Kje-cy" : ["UC_Stem", "UC_K"],
				"El-cy" : ["UC_El", "UC_Stem"],
				"Em-cy" : ["UC_Stem", "UC_Stem"],
				"En-cy" : ["UC_Stem", "UC_Stem"],
				"O-cy" : ["UC_Round", "UC_Round"],
				"Pe-cy" : ["UC_Stem", "UC_Stem"],
				"Er-cy" : ["UC_Stem", "UC_P"],
				"Es-cy" : ["UC_Round", "UC_C"],
				"Te-cy" : ["UC_T", "UC_T"],
				"U-cy" : ["UC_CyrU", "UC_CyrU"],
				"Ushort-cy" : ["UC_CyrU", "UC_CyrU"],
				"Ef-cy" : ["UC_Ef", "UC_Ef"],
				"Ha-cy" : ["UC_X", "UC_X"],
				"Che-cy" : ["UC_Che", "UC_Stem"],
				"Tse-cy" : ["UC_Stem", "UC_StemTooth"],
				"Sha-cy" : ["UC_Stem", "UC_Stem"],
				"Shcha-cy" : ["UC_Stem", "UC_StemTooth"],
				"Dzhe-cy" : ["UC_Stem", "UC_Stem"],
				"Ia-cy" : ["", "UC_Stem"],
				"Softsign-cy" : ["UC_Stem", "UC_Softsign"],
				"Hardsign-cy" : ["UC_T", "UC_Softsign"],
				"Yeru-cy" : ["UC_Stem", "UC_Stem"],
				"Lje-cy" : ["UC_El", "UC_Softsign"],
				"Nje-cy" : ["UC_Stem", "UC_Softsign"],
				"Dze-cy" : ["UC_S", "UC_S"],
				"E-cy" : ["UC_Round", "UC_C"],
				"Ereversed-cy" : ["UC_Ze", "UC_Round"],
				"I-cy" : ["UC_Stem", "UC_Stem"],
				"Yi-cy" : ["UC_Stem", "UC_Stem"],
				"Je-cy" : ["UC_J", "UC_J"],
				"Tshe-cy" : ["UC_T", "UC_Shha"],
				"Iu-cy" : ["UC_Stem", "UC_Round"],
				"Dje-cy" : ["UC_T", "UC_Softsign"],
				"Fita-cy" : ["UC_Round", "UC_Round"],
				"Izhitsa-cy" : ["UC_V", ""],
				"Ghestroke-cy" : ["UC_Eth", "UC_T"],
				"Ghemiddlehook-cy" : ["UC_Stem", ""],
				"Zhedescender-cy" : ["UC_Zhe", "UC_K"],
				"Zedescender-cy" : ["UC_Ze", "UC_B"],
				"Kadescender-cy" : ["UC_Stem", "UC_K"],
				"Kaverticalstroke-cy" : ["UC_Stem", "UC_K"],
				"Kastroke-cy" : ["UC_Stem", "UC_K"],
				"Kabashkir-cy" : ["UC_T", "UC_K"],
				"Endescender-cy" : ["UC_Stem", "UC_StemTooth"],
				"Pemiddlehook-cy" : ["UC_Stem", ""],
				"Haabkhasian-cy" : ["UC_Round", ""],
				"Esdescender-cy" : ["UC_Round", "UC_C"],
				"Tedescender-cy" : ["UC_T", "UC_T"],
				"Ustrait-cy" : ["UC_Y", "UC_Y"],
				"Ustraitstroke-cy" : ["UC_Y", "UC_Y"],
				"Hadescender-cy" : ["UC_X", "UC_X"],
				"Chedescender-cy" : ["UC_Che", "UC_StemTooth"],
				"Cheverticalstroke-cy" : ["UC_Che", "UC_Stem"],
				"Shha-cy" : ["UC_Stem", "UC_Shha"],
				"Cheabkhasian-cy" : ["UC_Cheabkhaz", "UC_Cheabkhaz"],
				"Chedescenderabkhasian-cy" : ["UC_Cheabkhaz", "UC_Cheabkhaz"],
				"Palochka-cy" : ["UC_Stem", "UC_Stem"],
				"Zhebreve-cy" : ["UC_Zhe", "UC_K"],
				"Kahook-cy" : ["UC_Stem", ""],
				"Eltail-cy" : ["UC_El", "UC_Stem"],
				"Enhook-cy" : ["UC_Stem", "UC_StemHook"],
				"Entail-cy" : ["UC_Stem", "UC_Stem"],
				"Chekhakassian-cy" : ["UC_Che", "UC_Stem"],
				"Emtail-cy" : ["UC_Stem", "UC_Stem"],
				"Abreve-cy" : ["UC_A", "UC_A"],
				"Adieresis-cy" : ["UC_A", "UC_A"],
				"Iebreve-cy" : ["UC_Stem", "UC_E"],
				"Schwa-cy" : ["UC_Schwa", "UC_Round"],
				"Schwadieresis-cy" : ["UC_Schwa", "UC_Round"],
				"Zhedieresis-cy" : ["UC_Zhe", "UC_K"],
				"Zedieresis-cy" : ["UC_Ze", "UC_B"],
				"Imacron-cy" : ["UC_Stem", "UC_Stem"],
				"Idieresis-cy" : ["UC_Stem", "UC_Stem"],
				"Odieresis-cy" : ["UC_Round", "UC_Round"],
				"Obarred-cy" : ["UC_Round", "UC_Round"],
				"Obarreddieresis-cy" : ["UC_Round", "UC_Round"],
				"Edieresis-cy" : ["UC_Ze", "UC_Round"],
				"Umacron-cy" : ["UC_CyrU", "UC_CyrU"],
				"Udieresis-cy" : ["UC_CyrU", "UC_CyrU"],
				"Uhungarumlaut-cy" : ["UC_CyrU", "UC_CyrU"],
				"Chedieresis-cy" : ["UC_Che", "UC_Stem"],
				"Ghedescender-cy" : ["UC_Stem", "UC_T"],
				"Yerudieresis-cy" : ["UC_Stem", "UC_Stem"],
				"Hahook-cy" : ["UC_X", "UC_X"],
				"Komide-cy" : ["", "UC_Stem"],
				"Elhook-cy" : ["UC_El", "UC_StemHook"],
				"Qa-cy" : ["UC_Round", "UC_Round"],
				"We-cy" : ["UC_W", ""],
				"Pedescender-cy" : ["UC_Stem", "UC_StemTooth"],
				"Shhadescender-cy" : ["UC_Stem", "UC_Shha"],
				"Ishorttail-cy" : ["UC_Stem", "UC_StemTooth"],
				"Enghe-cy" : ["UC_Stem", "UC_T"],
				"Tetse-cy" : ["UC_T", "UC_StemTooth"],
				"Ertick-cy" : ["UC_Stem","UC_P"],
				"Aie-cy" : ["", "UC_E"],
				"Alpha" : ["UC_A", "UC_A"],
				"Beta" : ["UC_Stem", "UC_B"],
				"Gamma" : ["UC_Stem", "UC_T"],
				"Delta" : ["UC_A", "UC_A"],
				"Epsilon" : ["UC_Stem", "UC_E"],
				"Zeta" : ["UC_Z", "UC_Z"],
				"Eta" : ["UC_Stem", "UC_Stem"],
				"Theta" : ["UC_Round", "UC_Round"],
				"Iota" : ["UC_Stem", "UC_Stem"],
				"Kappa" : ["UC_Stem", "UC_K"],
				"Lambda" : ["UC_A", "UC_A"],
				"Mu" : ["UC_Stem", "UC_Stem"],
				"Nu" : ["UC_Stem", "UC_Stem"],
				"Xi" : ["", "UC_E"],
				"Omicron" : ["UC_Round", "UC_Round"],
				"Pi" : ["UC_Stem", "UC_Stem"],
				"Rho" : ["UC_Stem", "UC_P"],
				"Sigma" : ["", "UC_E"],
				"Tau" : ["UC_T", "UC_T"],
				"Upsilon" : ["UC_Y", "UC_Y"],
				"Phi" : ["UC_Ef", "UC_Ef"],
				"Chi" : ["UC_X", "UC_X"],
				"Omega" : ["UC_Omega", "UC_Omega"],
				"Alphatonos" : ["", "UC_A"],
				"Epsilontonos" : ["UC_StemTonos", "UC_E"],
				"Etatonos" : ["UC_StemTonos", "UC_Stem"],
				"Iotatonos" : ["UC_StemTonos", "UC_Stem"],
				"Omicrontonos" : ["", "UC_Round"],
				"Upsilontonos" : ["", "UC_Y"],
				"Omegatonos" : ["", "UC_Omega"],
				"Iotadieresis" : ["UC_Stem", "UC_Stem"],
				"Upsilondieresis" : ["UC_Y", "UC_Y"]
			}

			groupsLCnormal = {
				"a" : ["lc_a", "lc_a"],
				"aacute" : ["lc_a", "lc_a"],
				"abreve" : ["lc_a", "lc_a"],
				"acircumflex" : ["lc_a", "lc_a"],
				"adieresis" : ["lc_a", "lc_a"],
				"agrave" : ["lc_a", "lc_a"],
				"amacron" : ["lc_a", "lc_a"],
				"aogonek" : ["lc_a", "lc_a"],
				"aring" : ["lc_a", "lc_a"],
				"aringacute" : ["lc_a", "lc_a"],
				"atilde" : ["lc_a", "lc_a"],
				"ae" : ["lc_a", "lc_e"],
				"aeacute" : ["lc_a", "lc_e"],
				"b" : ["lc_LongStem", "lc_Round"],
				"c" : ["lc_Round", "lc_c"],
				"cacute" : ["lc_Round", "lc_c"],
				"ccaron" : ["lc_Round", "lc_c"],
				"ccedilla" : ["lc_Round", "lc_c"],
				"ccircumflex" : ["lc_Round", "lc_c"],
				"cdotaccent" : ["lc_Round", "lc_c"],
				"d" : ["lc_Round", "lc_LongStem"],
				"eth" : ["lc_Round", ""],
				"dcaron" : ["lc_Round", "lc_Caron"],
				"dcroat" : ["lc_Round", "lc_LongStem"],
				"e" : ["lc_Round", "lc_e"],
				"eacute" : ["lc_Round", "lc_e"],
				"ebreve" : ["lc_Round", "lc_e"],
				"ecaron" : ["lc_Round", "lc_e"],
				"ecircumflex" : ["lc_Round", "lc_e"],
				"edieresis" : ["lc_Round", "lc_e"],
				"edotaccent" : ["lc_Round", "lc_e"],
				"egrave" : ["lc_Round", "lc_e"],
				"emacron" : ["lc_Round", "lc_e"],
				"eogonek" : ["lc_Round", "lc_e"],
				"f" : ["lc_f", "lc_f"],
				"g" : ["lc_g", "lc_g"],
				"gbreve" : ["lc_g", "lc_g"],
				"gcircumflex" : ["lc_g", "lc_g"],
				"gcommaaccent" : ["lc_g", "lc_g"],
				"gdotaccent" : ["lc_g", "lc_g"],
				"h" : ["lc_LongStem", "lc_Shoulder"],
				"hbar" : ["lc_LongStem", "lc_Shoulder"],
				"hcircumflex" : ["lc_LongStem", "lc_Shoulder"],
				"i" : ["lc_ShortStem", "lc_ShortStem"],
				"dotlessi" : ["lc_ShortStem", "lc_ShortStem"],
				"idotless" : ["lc_ShortStem", "lc_ShortStem"],
				"iacute" : ["lc_ShortStem", "lc_ShortStem"],
				"ibreve" : ["lc_ShortStem", "lc_ShortStem"],
				"icircumflex" : ["lc_ShortStem", "lc_ShortStem"],
				"idieresis" : ["lc_ShortStem", "lc_ShortStem"],
				"idotaccent" : ["lc_ShortStem", "lc_ShortStem"],
				"igrave" : ["lc_ShortStem", "lc_ShortStem"],
				"ij" : ["lc_ShortStem", "lc_j"],
				"imacron" : ["lc_ShortStem", "lc_ShortStem"],
				"iogonek" : ["lc_ShortStem", "lc_ShortStem"],
				"itilde" : ["lc_ShortStem", "lc_ShortStem"],
				"j" : ["lc_j", "lc_j"],
				"dotlessj" : ["lc_j", "lc_j"],
				"jdotless" : ["lc_j", "lc_j"],
				"jcircumflex" : ["lc_j", "lc_j"],
				"k" : ["lc_LongStem", "lc_k"],
				"kcommaaccent" : ["lc_LongStem", "lc_k"],
				"kgreenlandic" : ["lc_ShortStem", "lc_k"],
				"l" : ["lc_LongStem", "lc_LongStem"],
				"lacute" : ["lc_LongStem", "lc_LongStem"],
				"lcaron" : ["lc_LongStem", "lc_Caron"],
				"lcommaaccent" : ["lc_LongStem", "lc_LongStem"],
				"ldot" : ["lc_LongStem", ""],
				"lslash" : ["lc_lslash", "lc_lslash"],
				"m" : ["lc_ShortStem", "lc_Shoulder"],
				"n" : ["lc_ShortStem", "lc_Shoulder"],
				"nacute" : ["lc_ShortStem", "lc_Shoulder"],
				"napostrophe" : ["MSC_quoteright", "lc_Shoulder"],
				"ncaron" : ["lc_ShortStem", "lc_Shoulder"],
				"ncommaaccent" : ["lc_ShortStem", "lc_Shoulder"],
				"eng" : ["lc_ShortStem", "lc_Shoulder"],
				"ntilde" : ["lc_ShortStem", "lc_Shoulder"],
				"o" : ["lc_Round", "lc_Round"],
				"oacute" : ["lc_Round", "lc_Round"],
				"obreve" : ["lc_Round", "lc_Round"],
				"ocircumflex" : ["lc_Round", "lc_Round"],
				"odieresis" : ["lc_Round", "lc_Round"],
				"ograve" : ["lc_Round", "lc_Round"],
				"ohungarumlaut" : ["lc_Round", "lc_Round"],
				"omacron" : ["lc_Round", "lc_Round"],
				"oslash" : ["lc_Round", "lc_Round"],
				"oslashacute" : ["lc_Round", "lc_Round"],
				"otilde" : ["lc_Round", "lc_Round"],
				"oe" : ["lc_Round", "lc_e"],
				"p" : ["lc_p", "lc_Round"],
				"thorn" : ["lc_LongStem", "lc_Round"],
				"q" : ["lc_Round", ""],
				"r" : ["lc_ShortStem", "lc_r"],
				"racute" : ["lc_ShortStem", "lc_r"],
				"rcaron" : ["lc_ShortStem", "lc_r"],
				"rcommaaccent" : ["lc_ShortStem", "lc_r"],
				"s" : ["lc_s", "lc_s"],
				"sacute" : ["lc_s", "lc_s"],
				"scaron" : ["lc_s", "lc_s"],
				"scedilla" : ["lc_s", "lc_s"],
				"scircumflex" : ["lc_s", "lc_s"],
				"scommaaccent" : ["lc_s", "lc_s"],
				"t" : ["lc_t", "lc_t"],
				"tbar" : ["lc_t", ""],
				"tcaron" : ["lc_t", "lc_t"],
				"tcedilla" : ["lc_t", "lc_t"],
				"tcommaaccent" : ["lc_t", "lc_t"],
				"u" : ["lc_u", "lc_ShortStem"],
				"uacute" : ["lc_u", "lc_ShortStem"],
				"ubreve" : ["lc_u", "lc_ShortStem"],
				"ucircumflex" : ["lc_u", "lc_ShortStem"],
				"udieresis" : ["lc_u", "lc_ShortStem"],
				"ugrave" : ["lc_u", "lc_ShortStem"],
				"uhungarumlaut" : ["lc_u", "lc_ShortStem"],
				"umacron" : ["lc_u", "lc_ShortStem"],
				"uogonek" : ["lc_u", "lc_ShortStem"],
				"uring" : ["lc_u", "lc_ShortStem"],
				"utilde" : ["lc_u", "lc_ShortStem"],
				"v" : ["lc_vwy", "lc_vwy"],
				"w" : ["lc_vwy", "lc_vwy"],
				"wacute" : ["lc_vwy", "lc_vwy"],
				"wcircumflex" : ["lc_vwy", "lc_vwy"],
				"wdieresis" : ["lc_vwy", "lc_vwy"],
				"wgrave" : ["lc_vwy", "lc_vwy"],
				"x" : ["lc_x", "lc_x"],
				"y" : ["lc_vwy", "lc_vwy"],
				"yacute" : ["lc_vwy", "lc_vwy"],
				"ycircumflex" : ["lc_vwy", "lc_vwy"],
				"ydieresis" : ["lc_vwy", "lc_vwy"],
				"ygrave" : ["lc_vwy", "lc_vwy"],
				"z" : ["lc_z", "lc_z"],
				"zacute" : ["lc_z", "lc_z"],
				"zcaron" : ["lc_z", "lc_z"],
				"zdotaccent" : ["lc_z", "lc_z"],
				"schwa" : ["lc_schwa", "lc_Round"],
				"f_f" : ["lc_f", "lc_f"],
				"f_f_i" : ["lc_f", "lc_ShortStem"],
				"f_f_l" : ["lc_f", "lc_LongStem"],
				"f_i" : ["lc_f", "lc_ShortStem"],
				"f_l" : ["lc_f", "lc_LongStem"],
				"fi" : ["lc_f", "lc_ShortStem"],
				"fl" : ["lc_f", "lc_LongStem"],
				"a-cy" : ["lc_a", "lc_a"],
				"be-cy" : ["", "lc_Round"],
				"ve-cy" : ["lc_ShortStem", "lc_ze"],
				"ge-cy" : ["lc_ShortStem", "lc_te"],
				"gje-cy" : ["lc_ShortStem", "lc_te"],
				"gheupturn-cy" : ["lc_ShortStem", "lc_te"],
				"de-cy" : ["", "lc_StemTooth"],
				"ie-cy" : ["lc_Round", "lc_e"],
				"iegrave-cy" : ["lc_Round", "lc_e"],
				"io-cy" : ["lc_Round", "lc_e"],
				"zhe-cy" : ["lc_zhe", "lc_k"],
				"ze-cy" : ["lc_ze", "lc_ze"],
				"ii-cy" : ["lc_ShortStem", "lc_ShortStem"],
				"iishort-cy" : ["lc_ShortStem", "lc_ShortStem"],
				"iigrave-cy" : ["lc_ShortStem", "lc_ShortStem"],
				"ka-cy" : ["lc_ShortStem", "lc_k"],
				"kje-cy" : ["lc_ShortStem", "lc_k"],
				"el-cy" : ["lc_el", "lc_ShortStem"],
				"em-cy" : ["lc_ShortStem", "lc_ShortStem"],
				"en-cy" : ["lc_ShortStem", "lc_ShortStem"],
				"o-cy" : ["lc_Round", "lc_Round"],
				"pe-cy" : ["lc_ShortStem", "lc_ShortStem"],
				"er-cy" : ["lc_p", "lc_Round"],
				"es-cy" : ["lc_Round", "lc_c"],
				"te-cy" : ["lc_te", "lc_te"],
				"u-cy" : ["lc_vwy", "lc_vwy"],
				"ushort-cy" : ["lc_vwy", "lc_vwy"],
				"ef-cy" : ["lc_Round", "lc_Round"],
				"ha-cy" : ["lc_x", "lc_x"],
				"che-cy" : ["lc_che", "lc_ShortStem"],
				"tse-cy" : ["lc_ShortStem", "lc_StemTooth"],
				"sha-cy" : ["lc_ShortStem", "lc_ShortStem"],
				"shcha-cy" : ["lc_ShortStem", "lc_StemTooth"],
				"dzhe-cy" : ["lc_ShortStem", "lc_ShortStem"],
				"ia-cy" : ["", "lc_ShortStem"],
				"softsign-cy" : ["lc_ShortStem", "lc_softsign"],
				"hardsign-cy" : ["lc_te", "lc_softsign"],
				"yeru-cy" : ["lc_ShortStem", "lc_ShortStem"],
				"lje-cy" : ["lc_el", "lc_softsign"],
				"nje-cy" : ["lc_ShortStem", "lc_softsign"],
				"ereversed-cy" : ["lc_ze", "lc_Round"],
				"dze-cy" : ["lc_s", "lc_s"],
				"e-cy" : ["lc_Round", "lc_c"],
				"yi-cy" : ["lc_ShortStem", "lc_ShortStem"],
				"i-cy" : ["lc_ShortStem", "lc_ShortStem"],
				"je-cy" : ["lc_j", "lc_j"],
				"tshe-cy" : ["lc_LongStem", "lc_Shoulder"],
				"iu-cy" : ["lc_ShortStem", "lc_Round"],
				"dje-cy" : ["lc_LongStem", "lc_Shoulder"],
				"fita-cy" : ["lc_Round", "lc_Round"],
				"izhitsa-cy" : ["lc_vwy", ""],
				"ghestroke-cy" : ["lc_ShortStem", "lc_te"],
				"ghemiddlehook-cy" : ["lc_ShortStem", ""],
				"zhedescender-cy" : ["lc_zhe", "lc_k"],
				"zedescender-cy" : ["lc_ze", "lc_ze"],
				"kadescender-cy" : ["lc_ShortStem", "lc_k"],
				"kaverticalstroke-cy" : ["lc_ShortStem", "lc_k"],
				"kastroke-cy" : ["lc_LongStem", "lc_k"],
				"kabashkir-cy" : ["lc_te", "lc_k"],
				"endescender-cy" : ["lc_ShortStem", "lc_StemTooth"],
				"pemiddlehook-cy" : ["lc_ShortStem", ""],
				"haabkhasian-cy" : ["lc_Round", ""],
				"esdescender-cy" : ["lc_Round", "lc_c"],
				"tedescender-cy" : ["lc_te", "lc_te"],
				"ustrait-cy" : ["lc_vwy", "lc_vwy"],
				"hadescender-cy" : ["lc_x", "lc_x"],
				"chedescender-cy" : ["lc_che", "lc_StemTooth"],
				"cheverticalstroke-cy" : ["lc_che", "lc_ShortStem"],
				"shha-cy" : ["lc_LongStem", "lc_Shoulder"],
				"cheabkhasian-cy" : ["lc_cheabkhaz", "lc_e"],
				"chedescenderabkhasian-cy" : ["lc_cheabkhaz", "lc_e"],
				"palochka-cy" : ["lc_LongStem", "lc_LongStem"],
				"zhebreve-cy" : ["lc_zhe", "lc_k"],
				"kahook-cy" : ["lc_ShortStem", ""],
				"eltail-cy" : ["lc_el", "lc_StemTooth"],
				"enhook-cy" : ["lc_ShortStem", "lc_StemHook"],
				"entail-cy" : ["lc_ShortStem", "lc_StemTooth"],
				"chekhakassian-cy" : ["lc_che", "lc_ShortStem"],
				"emtail-cy" : ["lc_ShortStem", "lc_StemTooth"],
				"abreve-cy" : ["lc_a", "lc_a"],
				"adieresis-cy" : ["lc_a", "lc_a"],
				"iebreve-cy" : ["lc_Round", "lc_e"],
				"schwa-cy" : ["lc_schwa", "lc_Round"],
				"schwadieresis-cy" : ["lc_schwa", "lc_Round"],
				"zhedieresis-cy" : ["lc_zhe", "lc_k"],
				"zedieresis-cy" : ["lc_ze", "lc_ze"],
				"imacron-cy" : ["lc_ShortStem", "lc_ShortStem"],
				"idieresis-cy" : ["lc_ShortStem", "lc_ShortStem"],
				"odieresis-cy" : ["lc_Round", "lc_Round"],
				"obarred-cy" : ["lc_Round", "lc_Round"],
				"obarreddieresis-cy" : ["lc_Round", "lc_Round"],
				"edieresis-cy" : ["lc_ereversed", "lc_Round"],
				"umacron-cy" : ["lc_vwy", "lc_vwy"],
				"udieresis-cy" : ["lc_vwy", "lc_vwy"],
				"uhungarumlaut-cy" : ["lc_vwy", "lc_vwy"],
				"chedieresis-cy" : ["lc_che", "lc_ShortStem"],
				"ghedescender-cy" : ["lc_ShortStem", "lc_te"],
				"yerudieresis-cy" : ["lc_ShortStem", "lc_ShortStem"],
				"hahook-cy" : ["lc_x", "lc_x"],
				"komide-cy" : ["lc_Round", "lc_LongStem"],
				"elhook-cy" : ["lc_el", "lc_StemHook"],
				"we-cy" : ["lc_vwy", "lc_vwy"],
				"pedescender-cy" : ["lc_ShortStem", "lc_StemTooth"],
				"shhadescender-cy" : ["lc_LongStem", "lc_Shoulder"],
				"ishorttail-cy" : ["lc_ShortStem", "lc_StemTooth"],
				"ertick-cy" : ["lc_p", "p"],
				"enghe-cy" : ["lc_ShortStem", "lc_te"],
				"tetse-cy" : ["lc_te", "lc_StemTooth"],
				"aie-cy" : ["lc_a", "lc_e"],
				"alpha" : ["lc_Round", "lc_alpha"],
				"delta" : ["", "lc_Round"],
				"epsilon" : ["lc_epsilon", "lc_epsilon"],
				"eta" : ["lc_eta", "lc_eta"],
				"iota" : ["lc_iota", "lc_iota"],
				"mu" : ["lc_ShortStem", "lc_alpha"],
				"omicron" : ["lc_Round", "lc_Round"],
				"rho" : ["", "lc_Round"],
				"sigmafinal" : ["lc_Round", ""],
				"sigma" : ["lc_Round", ""],
				"upsilon" : ["lc_upsilon", "lc_upsilon"],
				"phi" : ["lc_Round", "lc_Round"],
				"psi" : ["", "lc_upsilon"],
				"omega" : ["lc_omega", "lc_upsilon"],
				"iotatonos" : ["lc_iota", "lc_iota"],
				"iotadieresis" : ["lc_iota", "lc_iota"],
				"iotadieresistonos" : ["lc_iota", "lc_iota"],
				"upsilontonos" : ["lc_upsilon", "lc_upsilon"],
				"upsilondieresis" : ["lc_upsilon", "lc_upsilon"],
				"upsilondieresistonos" : ["lc_upsilon", "lc_upsilon"],
				"omicrontonos" : ["lc_Round", "lc_Round"],
				"omegatonos" : ["lc_omega", "lc_upsilon"],
				"alphatonos" : ["lc_Round", "lc_alpha"],
				"epsilontonos" : ["lc_epsilon", "lc_epsilon"],
				"etatonos" : ["lc_eta", "lc_eta"]
			}

			groupsLCcursive = {
				"a" : ["lc_Round", "lc_ShortStem"],
				"aacute" : ["lc_Round", "lc_ShortStem"],
				"abreve" : ["lc_Round", "lc_ShortStem"],
				"acircumflex" : ["lc_Round", "lc_ShortStem"],
				"adieresis" : ["lc_Round", "lc_ShortStem"],
				"agrave" : ["lc_Round", "lc_ShortStem"],
				"amacron" : ["lc_Round", "lc_ShortStem"],
				"aogonek" : ["lc_Round", "lc_ShortStem"],
				"aring" : ["lc_Round", "lc_ShortStem"],
				"aringacute" : ["lc_Round", "lc_ShortStem"],
				"atilde" : ["lc_Round", "lc_ShortStem"],
				"ae" : ["lc_Round", "lc_e"],
				"aeacute" : ["lc_Round", "lc_e"],
				"b" : ["lc_LongStem1", "lc_Round"],
				"c" : ["lc_Round", "lc_c"],
				"cacute" : ["lc_Round", "lc_c"],
				"ccaron" : ["lc_Round", "lc_c"],
				"ccedilla" : ["lc_Round", "lc_c"],
				"ccircumflex" : ["lc_Round", "lc_c"],
				"cdotaccent" : ["lc_Round", "lc_c"],
				"d" : ["lc_Round", "lc_LongStem"],
				"eth" : ["lc_Round", ""],
				"dcaron" : ["lc_Round", "lc_Caron"],
				"dcroat" : ["lc_Round", "lc_LongStem"],
				"e" : ["lc_Round", "lc_e"],
				"eacute" : ["lc_Round", "lc_e"],
				"ebreve" : ["lc_Round", "lc_e"],
				"ecaron" : ["lc_Round", "lc_e"],
				"ecircumflex" : ["lc_Round", "lc_e"],
				"edieresis" : ["lc_Round", "lc_e"],
				"edotaccent" : ["lc_Round", "lc_e"],
				"egrave" : ["lc_Round", "lc_e"],
				"emacron" : ["lc_Round", "lc_e"],
				"eogonek" : ["lc_Round", "lc_e"],
				"f" : ["lc_f", "lc_f"],
				"g" : ["lc_g", "lc_g"],
				"gbreve" : ["lc_g", "lc_g"],
				"gcaron" : ["lc_g", "lc_g"],
				"gcircumflex" : ["lc_g", "lc_g"],
				"gcommaaccent" : ["lc_g", "lc_g"],
				"gdotaccent" : ["lc_g", "lc_g"],
				"h" : ["lc_LongStem2", "lc_Shoulder"],
				"hbar" : ["lc_LongStem2", "lc_Shoulder"],
				"hcircumflex" : ["lc_LongStem2", "lc_Shoulder"],
				"i" : ["lc_i", "lc_ShortStem"],
				"dotlessi" : ["lc_i", "lc_ShortStem"],
				"idotless" : ["lc_i", "lc_ShortStem"],
				"iacute" : ["lc_i", "lc_ShortStem"],
				"ibreve" : ["lc_i", "lc_ShortStem"],
				"icircumflex" : ["lc_i", "lc_ShortStem"],
				"idieresis" : ["lc_i", "lc_ShortStem"],
				"idotaccent" : ["lc_i", "lc_ShortStem"],
				"igrave" : ["lc_i", "lc_ShortStem"],
				"ij" : ["lc_i", "lc_j"],
				"imacron" : ["lc_i", "lc_ShortStem"],
				"iogonek" : ["lc_i", "lc_ShortStem"],
				"itilde" : ["lc_i", "lc_ShortStem"],
				"j" : ["lc_j", "lc_j"],
				"dotlessj" : ["lc_j", "lc_j"],
				"jdotless" : ["lc_j", "lc_j"],
				"jcircumflex" : ["lc_j", "lc_j"],
				"k" : ["lc_LongStem2", "lc_k"],
				"kcommaaccent" : ["lc_LongStem2", "lc_k"],
				"kgreenlandic" : ["lc_ShortStem", "lc_k"],
				"l" : ["lc_LongStem1", "lc_LongStem"],
				"lacute" : ["lc_LongStem1", "lc_LongStem"],
				"lcaron" : ["lc_LongStem1", "lc_Caron"],
				"lcommaaccent" : ["lc_LongStem1", "lc_LongStem"],
				"ldot" : ["lc_LongStem1", ""],
				"lslash" : ["lc_lslash", "lc_lslash"],
				"m" : ["lc_ShortStem", "lc_Shoulder"],
				"n" : ["lc_ShortStem", "lc_Shoulder"],
				"nacute" : ["lc_ShortStem", "lc_Shoulder"],
				"napostrophe" : ["MSC_quoteright", "lc_Shoulder"],
				"ncaron" : ["lc_ShortStem", "lc_Shoulder"],
				"ncommaaccent" : ["lc_ShortStem", "lc_Shoulder"],
				"eng" : ["lc_ShortStem", ""],
				"ntilde" : ["lc_ShortStem", "lc_Shoulder"],
				"o" : ["lc_Round", "lc_Round"],
				"oacute" : ["lc_Round", "lc_Round"],
				"obreve" : ["lc_Round", "lc_Round"],
				"ocircumflex" : ["lc_Round", "lc_Round"],
				"odieresis" : ["lc_Round", "lc_Round"],
				"ograve" : ["lc_Round", "lc_Round"],
				"ohungarumlaut" : ["lc_Round", "lc_Round"],
				"omacron" : ["lc_Round", "lc_Round"],
				"oslash" : ["lc_Round", "lc_Round"],
				"oslashacute" : ["lc_Round", "lc_Round"],
				"otilde" : ["lc_Round", "lc_Round"],
				"oe" : ["lc_Round", "lc_e"],
				"p" : ["lc_p", "lc_Round"],
				"thorn" : ["", "lc_Round"],
				"q" : ["lc_Round", ""],
				"r" : ["lc_ShortStem", "lc_r"],
				"racute" : ["lc_ShortStem", "lc_r"],
				"rcaron" : ["lc_ShortStem", "lc_r"],
				"rcommaaccent" : ["lc_ShortStem", "lc_r"],
				"s" : ["lc_s", "lc_s"],
				"sacute" : ["lc_s", "lc_s"],
				"scaron" : ["lc_s", "lc_s"],
				"scedilla" : ["lc_s", "lc_s"],
				"scircumflex" : ["lc_s", "lc_s"],
				"scommaaccent" : ["lc_s", "lc_s"],
				"t" : ["lc_t", "lc_t"],
				"tbar" : ["lc_t", "lc_t"],
				"tcaron" : ["lc_t", "lc_t"],
				"tcedilla" : ["lc_t", "lc_t"],
				"tcommaaccent" : ["lc_t", "lc_t"],
				"u" : ["lc_i", "lc_ShortStem"],
				"uacute" : ["lc_i", "lc_ShortStem"],
				"ubreve" : ["lc_i", "lc_ShortStem"],
				"ucircumflex" : ["lc_i", "lc_ShortStem"],
				"udieresis" : ["lc_i", "lc_ShortStem"],
				"ugrave" : ["lc_i", "lc_ShortStem"],
				"uhungarumlaut" : ["lc_i", "lc_ShortStem"],
				"umacron" : ["lc_i", "lc_ShortStem"],
				"uogonek" : ["lc_i", "lc_ShortStem"],
				"uring" : ["lc_i", "lc_ShortStem"],
				"utilde" : ["lc_i", "lc_ShortStem"],
				"v" : ["lc_vw", "lc_vw"],
				"w" : ["lc_vw", "lc_vw"],
				"wacute" : ["lc_vw", "lc_vw"],
				"wcircumflex" : ["lc_vw", "lc_vw"],
				"wdieresis" : ["lc_vw", "lc_vw"],
				"wgrave" : ["lc_vw", "lc_vw"],
				"x" : ["lc_x", "lc_x"],
				"y" : ["lc_y", "lc_y"],
				"yacute" : ["lc_y", "lc_y"],
				"ycircumflex" : ["lc_y", "lc_y"],
				"ydieresis" : ["lc_y", "lc_y"],
				"ygrave" : ["lc_y", "lc_y"],
				"z" : ["lc_z", "lc_z"],
				"zacute" : ["lc_z", "lc_z"],
				"zcaron" : ["lc_z", "lc_z"],
				"zdotaccent" : ["lc_z", "lc_z"],
				"schwa" : ["lc_schwa", "lc_Round"],
				"a-cy" : ["lc_Round", "lc_ShortStem"],
				"be-cy" : ["", "lc_Round"],
				"ve-cy" : ["lc_Round", "lc_ze"],
				"ge-cy" : ["lc_ge", "lc_ge"],
				"gje-cy" : ["lc_ge", "lc_ge"],
				"gheupturn-cy" : ["lc_ShortStem", ""],
				"de-cy" : ["lc_Round", ""],
				"ie-cy" : ["lc_Round", "lc_e"],
				"iegrave-cy" : ["lc_Round", "lc_e"],
				"io-cy" : ["lc_Round", "lc_e"],
				"zhe-cy" : ["lc_zhe", "lc_zhe"],
				"ze-cy" : ["lc_ze", "lc_ze"],
				"ii-cy" : ["lc_i", "lc_ShortStem"],
				"iishort-cy" : ["lc_i", "lc_ShortStem"],
				"iigrave-cy" : ["lc_i", "lc_ShortStem"],
				"ka-cy" : ["lc_ShortStem", "lc_k"],
				"kje-cy" : ["lc_ShortStem", "lc_k"],
				"el-cy" : ["lc_el", "lc_ShortStem"],
				"em-cy" : ["lc_el", "lc_ShortStem"],
				"en-cy" : ["lc_ShortStem", "lc_ShortStem"],
				"o-cy" : ["lc_Round", "lc_Round"],
				"pe-cy" : ["lc_ShortStem", "lc_Shoulder"],
				"er-cy" : ["lc_p", "lc_Round"],
				"es-cy" : ["lc_Round", "lc_c"],
				"te-cy" : ["lc_ShortStem", "lc_Shoulder"],
				"u-cy" : ["lc_y", "lc_y"],
				"ushort-cy" : ["lc_y", "lc_y"],
				"ef-cy" : ["lc_Round", "lc_Round"],
				"ha-cy" : ["lc_x", "lc_x"],
				"che-cy" : ["lc_che", "lc_ShortStem"],
				"tse-cy" : ["lc_i", "lc_StemTooth"],
				"sha-cy" : ["lc_i", "lc_ShortStem"],
				"shcha-cy" : ["lc_i", "lc_StemTooth"],
				"dzhe-cy" : ["lc_i", "lc_ShortStem"],
				"ia-cy" : ["", "lc_ShortStem"],
				"softsign-cy" : ["lc_i", "lc_softsign"],
				"hardsign-cy" : ["lc_hardsign", "lc_softsign"],
				"yeru-cy" : ["lc_i", "lc_ShortStem"],
				"lje-cy" : ["lc_el", "lc_softsign"],
				"nje-cy" : ["lc_ShortStem", "lc_softsign"],
				"dze-cy" : ["lc_s", "lc_s"],
				"ereversed-cy" : ["lc_ereversed", "lc_Round"],
				"e-cy" : ["lc_Round", "lc_c"],
				"yi-cy" : ["lc_i", "lc_ShortStem"],
				"je-cy" : ["lc_j", "lc_j"],
				"i-cy" : ["lc_i", "lc_ShortStem"],
				"tshe-cy" : ["lc_LongStem", "lc_Shoulder"],
				"iu-cy" : ["lc_ShortStem", "lc_Round"],
				"dje-cy" : ["lc_LongStem", ""],
				"yat-cy" : ["lc_ShortStem", "lc_softsign"],
				"fita-cy" : ["lc_Round", "lc_Round"],
				"izhitsa-cy" : ["lc_vwy", ""],
				"ghestroke-cy" : ["lc_ge", "lc_ge"],
				"ghemiddlehook-cy" : ["lc_ShortStem", ""],
				"zhedescender-cy" : ["lc_zhe", "lc_zhe"],
				"zedescender-cy" : ["lc_ze", "lc_ze"],
				"kadescender-cy" : ["lc_ShortStem", "lc_k"],
				"kaverticalstroke-cy" : ["lc_ShortStem", "lc_k"],
				"kastroke-cy" : ["lc_LongStem", "lc_k"],
				"kabashkir-cy" : ["lc_hardsign", "lc_k"],
				"endescender-cy" : ["lc_ShortStem", "lc_StemTooth"],
				"pemiddlehook-cy" : ["lc_ShortStem", ""],
				"haabkhasian-cy" : ["lc_Round", ""],
				"esdescender-cy" : ["lc_Round", "lc_c"],
				"tedescender-cy" : ["lc_ShortStem", "lc_ShoulderTooth"],
				"ustrait-cy" : ["lc_ustrait", "lc_ustrait"],
				"ustraitstroke-cy" : ["lc_ustrait", "lc_ustrait"],
				"hadescender-cy" : ["lc_x", "lc_x"],
				"chedescender-cy" : ["lc_che", "lc_StemTooth"],
				"cheverticalstroke-cy" : ["lc_che", "lc_ShortStem"],
				"shha-cy" : ["lc_LongStem", "lc_Shoulder"],
				"cheabkhasian-cy" : ["lc_cheabkhaz", "lc_e"],
				"chedescenderabkhasian-cy" : ["lc_cheabkhaz", "lc_e"],
				"palochka-cy" : ["lc_LongStem", "lc_LongStem"],
				"zhebreve-cy" : ["lc_zhe", "lc_zhe"],
				"kahook-cy" : ["lc_ShortStem", ""],
				"eltail-cy" : ["lc_el", "lc_StemTooth"],
				"enhook-cy" : ["lc_ShortStem", "lc_StemHook"],
				"entail-cy" : ["lc_ShortStem", "lc_StemTooth"],
				"chekhakassian-cy" : ["lc_che", "lc_ShortStem"],
				"emtail-cy" : ["lc_el", "lc_StemTooth"],
				"abreve-cy" : ["lc_Round", "lc_ShortStem"],
				"adieresis-cy" : ["lc_Round", "lc_ShortStem"],
				"iebreve-cy" : ["lc_Round", "lc_e"],
				"schwa-cy" : ["lc_schwa", "lc_Round"],
				"schwadieresis-cy" : ["lc_schwa", "lc_Round"],
				"zhedieresis-cy" : ["lc_zhe", "lc_zhe"],
				"zedieresis-cy" : ["lc_ze", "lc_ze"],
				"imacron-cy" : ["lc_i", "lc_ShortStem"],
				"idieresis-cy" : ["lc_i", "lc_ShortStem"],
				"odieresis-cy" : ["lc_Round", "lc_Round"],
				"obarred-cy" : ["lc_Round", "lc_Round"],
				"obarreddieresis-cy" : ["lc_Round", "lc_Round"],
				"edieresis-cy" : ["lc_ze", "lc_Round"],
				"umacron-cy" : ["lc_vwy", "lc_vwy"],
				"udieresis-cy" : ["lc_vwy", "lc_vwy"],
				"uhungarumlaut-cy" : ["lc_vwy", "lc_vwy"],
				"chedieresis-cy" : ["lc_che", "lc_ShortStem"],
				"ghedescender-cy" : ["lc_ge", "lc_ge"],
				"yerudieresis-cy" : ["lc_i", "lc_ShortStem"],
				"hahook-cy" : ["lc_x", "lc_x"],
				"komide-cy" : ["lc_Round", "lc_LongStem"],
				"reversedze-cy" : ["", "lc_c"],
				"elhook-cy" : ["lc_el", "lc_StemHook"],
				"we-cy" : ["lc_vwy", ""],
				"pedescender-cy" : ["lc_ShortStem", "lc_ShoulderTooth"],
				"shhadescender-cy" : ["lc_LongStem", "lc_ShoulderTooth"],
				"ishorttail-cy" : ["lc_i", "lc_StemTooth"],
				"ertick-cy" : ["lc_er", ""],
				"enghe-cy" : ["lc_ShortStem", ""],
				"tetse-cy" : ["lc_te", ""],
				"aie-cy" : ["lc_Round", "lc_e"]
			}
	
			groupsMS = {
				"colon" : ["MSC_colon", "MSC_colon"],
				"comma" : ["MSC_period", "MSC_period"],
				"ellipsis" : ["MSC_period", "MSC_period"],
				"period" : ["MSC_period", "MSC_period"],
				"exclam" : ["MSC_exclam", "MSC_exclam"],
				"exclamdouble" : ["MSC_exclam", "MSC_exclam"],
				"quotedbl" : ["MSC_VertQuote", "MSC_VertQuote"],
				"quotesingle" : ["MSC_VertQuote", "MSC_VertQuote"],
				"semicolon" : ["MSC_colon", "MSC_colon"],
				"slash" : ["MSC_slash", "MSC_slash"],
				"braceleft" : ["", "MSC_bracketleft"],
				"braceright" : ["MSC_bracketright", ""],
				"bracketleft" : ["", "MSC_bracketleft"],
				"bracketright" : ["MSC_bracketright", ""],
				"parenleft" : ["", "MSC_bracketleft"],
				"parenright" : ["MSC_bracketright", ""],
				"emdash" : ["MSC_dash", "MSC_dash"],
				"endash" : ["MSC_dash", "MSC_dash"],
				"hyphen" : ["MSC_dash", "MSC_dash"],
				"horizontalbar" : ["MSC_dash", "MSC_dash"],
				"hyphentwo" : ["MSC_dash", "MSC_dash"],
				"softhyphen" : ["MSC_dash", "MSC_dash"],
				"guillemetleft" : ["MSC_guillemetleft", "MSC_guillemetleft"],
				"guillemetright" : ["MSC_guillemetright", "MSC_guillemetright"],
				"guilsinglleft" : ["MSC_guillemetleft", "MSC_guillemetleft"],
				"guilsinglright" : ["MSC_guillemetright", "MSC_guillemetright"],
				"quotedblbase" : ["MSC_period", "MSC_period"],
				"quotedblleft" : ["MSC_quoteleft", "MSC_quoteleft"],
				"quotedblright" : ["MSC_quoteright", "MSC_quoteright"],
				"quoteleft" : ["MSC_quoteleft", "MSC_quoteleft"],
				"quoteright" : ["MSC_quoteright", "MSC_quoteright"],
				"quotesinglbase" : ["MSC_period", "MSC_period"],
				"questiongreek" : ["MSC_colon", "MSC_colon"],
				"space" : ["MSC_space", "MSC_space"],
				"nbspace" : ["MSC_space", "MSC_space"],
				"divide" : ["MSC_minus", "MSC_minus"],
				"equal" : ["MSC_equal", "MSC_equal"],
				"greater" : ["", "MSC_minus"],
				"less" : ["MSC_minus", ""],
				"minus" : ["MSC_minus", "MSC_minus"],
				"notequal" : ["MSC_equal", "MSC_equal"],
				"percent" : ["MSC_percent", ""],
				"perthousand" : ["MSC_percent", ""],
				"plus" : ["MSC_minus", "MSC_minus"]
			}
	
			thisFont.disableUpdateInterface() # suppresses UI updates in Font View
			isNeeded = {}
			for glyph in thisFont.glyphs:
				isNeeded[glyph.name] = False
			if self.w.radioButton.get() == 1:
				for layer in thisFont.selectedLayers:
					isNeeded[layer.parent.name] = True
			else:
				for glyph in thisFont.glyphs:
					isNeeded[glyph.name] = True

			for key in groupsUC:
				if thisFont.glyphs[key] and isNeeded[key]:
					thisFont.glyphs[key].setLeftKerningGroup_(groupsUC[key][0])
					thisFont.glyphs[key].setRightKerningGroup_(groupsUC[key][1])
				if thisFont.glyphs[key.lower()+".sc"] and isNeeded[key]:
					thisFont.glyphs[key.lower()+".sc"].setLeftKerningGroup_(re.sub("UC_", "SC_",groupsUC[key][0]))
					thisFont.glyphs[key.lower()+".sc"].setRightKerningGroup_(re.sub("UC_", "SC_",groupsUC[key][1]))
				elif thisFont.glyphs[key.lower()+".smcp"] and isNeeded[key]:
					thisFont.glyphs[key.lower()+".smcp"].setLeftKerningGroup_(re.sub("UC_", "SC_",groupsUC[key][0]))
					thisFont.glyphs[key.lower()+".smcp"].setRightKerningGroup_(re.sub("UC_", "SC_",groupsUC[key][1]))

				if sender == self.w.allcapButton:
					if thisFont.glyphs[key] and isNeeded[key]:
						try:
							thisFont.glyphs[key.lower()].setLeftKerningGroup_(groupsUC[key][0])
							thisFont.glyphs[key.lower()].setRightKerningGroup_(groupsUC[key][1])
						except:
							print(key.lower())

			for key in groupsMS:
				if thisFont.glyphs[key] and isNeeded[key]:
					thisFont.glyphs[key].setLeftKerningGroup_(groupsMS[key][0])
					thisFont.glyphs[key].setRightKerningGroup_(groupsMS[key][1])
				if (thisFont.glyphs[key.lower()+".case"] or thisFont.glyphs[key.lower()+".smcp"]) and isNeeded[key]:
					thisFont.glyphs[key].setLeftKerningGroup_(re.sub("MSC_", "MSC_UC_",groupsMS[key][0]))
					thisFont.glyphs[key].setRightKerningGroup_(re.sub("MSC_", "MSC_UC_",groupsMS[key][1]))
			
			if sender == self.w.normalButton:
				for key in groupsLCnormal:
					if thisFont.glyphs[key] and isNeeded[key]:
						thisFont.glyphs[key].setLeftKerningGroup_(groupsLCnormal[key][0])
						thisFont.glyphs[key].setRightKerningGroup_(groupsLCnormal[key][1])
			elif sender == self.w.cursiveButton:
				for key in groupsLCcursive:
					if thisFont.glyphs[key] and isNeeded[key]:
						thisFont.glyphs[key].setLeftKerningGroup_(groupsLCcursive[key][0])
						thisFont.glyphs[key].setRightKerningGroup_(groupsLCcursive[key][1])

			thisFont.enableUpdateInterface() # re-enables UI updates in Font View
					
			
			self.w.close() # delete if you want window to stay open
		except Exception as e:
			# brings macro window to front and reports error:
			Glyphs.showMacroWindow()
			print(" SetKernPairsMain Error: %s" % e)

SetKernPairs()