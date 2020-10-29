# Working out which intersection was not processed by the voxelizer

TRIANGLES = [
	# [ [ 1.67494, 27.6985 ], [ 1.67753, 27.7249 ], [ 1.64396, 27.7001 ], ], # 0 [ 3552246, 3589987, 3589971 ] - miss
	# [ [ 1.61697, 27.6816 ], [ 1.64396, 27.7001 ], [ 1.64114, 27.7124 ], ], # 1 [ 1627988, 3589971, 3589972 ] - miss
	# [ [ 1.64396, 27.7001 ], [ 1.67753, 27.7249 ], [ 1.67085, 27.7377 ], ], # 2 [ 3589971, 3589987, 548205 ] - miss
	[ [ 1.64396, 27.7001 ], [ 1.67085, 27.7377 ], [ 1.64114, 27.7124 ], ], # 3 [ 3589971, 548205, 3589972 ] - hit
	# [ [ 1.61697, 27.6816 ], [ 1.64114, 27.7124 ], [ 1.6182, 27.6929 ], ], # 4 [ 1627988, 3589972, 4597829 ] - miss
	# [ [ 1.6182, 27.6929 ], [ 1.64114, 27.7124 ], [ 1.64457, 27.7235 ], ], # 5 [ 4597829, 3589972, 548207 ] - miss
	# [ [ 1.64114, 27.7124 ], [ 1.67085, 27.7377 ], [ 1.64457, 27.7235 ], ], # 6 [ 3589972, 548205, 548207 ] - miss
	# [ [ 1.6182, 27.6929 ], [ 1.64457, 27.7235 ], [ 1.61624, 27.6973 ], ], # 7 [ 4597829, 548207, 4928721 ] - miss
	# [ [ 1.64457, 27.7235 ], [ 1.65405, 27.7347 ], [ 1.61624, 27.6973 ], ], # 8 [ 548207, 1483296, 4928721 ] - miss
	# [ [ 1.61624, 27.6973 ], [ 1.65405, 27.7347 ], [ 1.6008, 27.6853 ], ], # 9 [ 4928721, 1483296, 1483295 ] - miss
	# [ [ 1.6008, 27.6853 ], [ 1.65405, 27.7347 ], [ 1.65742, 27.7392 ], ], # 10 [ 1483295, 1483296, 1483297 ] - miss
	# [ [ 1.6008, 27.6853 ], [ 1.64765, 27.7244 ], [ 1.59656, 27.6755 ], ], # 11 [ 1483295, 1483298, 2797748 ] - miss
	# [ [ 1.65742, 27.7392 ], [ 1.64765, 27.7244 ], [ 1.6008, 27.6853 ], ], # 12 [ 1483297, 1483298, 1483295 ] - miss
	# [ [ 1.64765, 27.7244 ], [ 1.63279, 27.7065 ], [ 1.59656, 27.6755 ], ], # 13 [ 1483298, 3791831, 2797748 ] - miss
	# [ [ 1.64765, 27.7244 ], [ 1.64448, 27.7148 ], [ 1.63279, 27.7065 ], ], # 14 [ 1483298, 693162, 3791831 ] - miss
	[ [ 1.64765, 27.7244 ], [ 1.6658, 27.7329 ], [ 1.64448, 27.7148 ], ], # 15 [ 1483298, 1483299, 693162 ] - hit
	# [ [ 1.63279, 27.7065 ], [ 1.64448, 27.7148 ], [ 1.60662, 27.6799 ], ], # 16 [ 3791831, 693162, 4785893 ] - miss
	[ [ 1.64448, 27.7148 ], [ 1.60047, 27.6744 ], [ 1.60662, 27.6799 ], ], # 17 [ 693162, 693161, 4785893 ] - hit ??
	# [ [ 1.6658, 27.7329 ], [ 1.63963, 27.7063 ], [ 1.64448, 27.7148 ], ], # 18 [ 1483299, 283633, 693162 ] - miss
	# [ [ 1.63963, 27.7063 ], [ 1.60047, 27.6744 ], [ 1.64448, 27.7148 ], ], # 19 [ 283633, 693161, 693162 ] - miss ??
	# [ [ 1.60047, 27.6744 ], [ 1.63963, 27.7063 ], [ 1.57748, 27.651 ], ], # 20 [ 693161, 283633, 283635 ] - miss
	# [ [ 1.6658, 27.7329 ], [ 1.66477, 27.7292 ], [ 1.63963, 27.7063 ], ], # 21 [ 1483299, 2630390, 283633 ] - miss
	# [ [ 1.63963, 27.7063 ], [ 1.53947, 27.6177 ], [ 1.57748, 27.651 ], ], # 22 [ 283633, 283634, 283635 ] - miss
	# [ [ 1.63963, 27.7063 ], [ 1.60304, 27.6763 ], [ 1.53947, 27.6177 ], ], # 23 [ 283633, 2630392, 283634 ] - miss
	# [ [ 1.66477, 27.7292 ], [ 1.60304, 27.6763 ], [ 1.63963, 27.7063 ], ], # 24 [ 2630390, 2630392, 283633 ] - miss
	# [ [ 1.66477, 27.7292 ], [ 1.67055, 27.7313 ], [ 1.60304, 27.6763 ], ], # 25 [ 2630390, 2630391, 2630392 ] - miss
	# [ [ 1.67055, 27.7313 ], [ 1.60518, 27.6798 ], [ 1.60304, 27.6763 ], ], # 26 [ 2630391, 2630394, 2630392 ] - miss
	# [ [ 1.67055, 27.7313 ], [ 1.68628, 27.7428 ], [ 1.60518, 27.6798 ], ], # 27 [ 2630391, 3737874, 2630394 ] - miss
	# [ [ 1.60648, 27.6762 ], [ 1.60518, 27.6798 ], [ 1.65014, 27.7092 ], ], # 28 [ 2630393, 2630394, 1925083 ] - miss
	# [ [ 1.60518, 27.6798 ], [ 1.68628, 27.7428 ], [ 1.65014, 27.7092 ], ], # 29 [ 2630394, 3737874, 1925083 ] - miss
	# [ [ 1.6266, 27.6905 ], [ 1.60648, 27.6762 ], [ 1.65014, 27.7092 ], ], # 30 [ 4155495, 2630393, 1925083 ] - miss
	# [ [ 1.63708, 27.6895 ], [ 1.65014, 27.7092 ], [ 1.66425, 27.7144 ], ], # 31 [ 1096317, 1925083, 1925084 ] - miss
	# [ [ 1.63708, 27.6895 ], [ 1.6266, 27.6905 ], [ 1.65014, 27.7092 ], ], # 32 [ 1096317, 4155495, 1925083 ] - miss
	# [ [ 1.63708, 27.6895 ], [ 1.66425, 27.7144 ], [ 1.6704, 27.7168 ], ], # 33 [ 1096317, 1925084, 4155516 ] - miss
	# [ [ 1.62683, 27.6819 ], [ 1.63708, 27.6895 ], [ 1.6704, 27.7168 ], ], # 34 [ 1096315, 1096317, 4155516 ] - miss
	# [ [ 1.62683, 27.6819 ], [ 1.6704, 27.7168 ], [ 1.67815, 27.7252 ], ], # 35 [ 1096315, 4155516, 1195 ] - miss
	# [ [ 1.62116, 27.68 ], [ 1.67815, 27.7252 ], [ 1.6396, 27.6967 ], ], # 36 [ 2907616, 1195, 1194 ] - miss
	# [ [ 1.6396, 27.6967 ], [ 1.67815, 27.7252 ], [ 1.67244, 27.7311 ], ], # 37 [ 1194, 1195, 1196 ] - miss
	# [ [ 1.62116, 27.68 ], [ 1.62683, 27.6819 ], [ 1.67815, 27.7252 ], ], # 38 [ 2907616, 1096315, 1195 ] - miss
	# [ [ 1.6396, 27.6967 ], [ 1.67244, 27.7311 ], [ 1.64277, 27.7014 ], ], # 39 [ 1194, 1196, 4731008 ] - miss
	# [ [ 1.66065, 27.7178 ], [ 1.64277, 27.7014 ], [ 1.67244, 27.7311 ], ], # 40 [ 4731006, 4731008, 1196 ] - miss
	# [ [ 1.62952, 27.6906 ], [ 1.64277, 27.7014 ], [ 1.66065, 27.7178 ], ], # 41 [ 2907617, 4731008, 4731006 ] - miss
	# [ [ 1.62952, 27.6906 ], [ 1.66065, 27.7178 ], [ 1.67307, 27.7409 ], ], # 42 [ 2907617, 4731006, 4731007 ] - miss
	# [ [ 1.63508, 27.705 ], [ 1.62952, 27.6906 ], [ 1.67307, 27.7409 ], ], # 43 [ 3225755, 2907617, 4731007 ] - miss
	# [ [ 1.59843, 27.6589 ], [ 1.62952, 27.6906 ], [ 1.63508, 27.705 ], ], # 44 [ 3699875, 2907617, 3225755 ] - miss
	# [ [ 1.583, 27.6501 ], [ 1.59843, 27.6589 ], [ 1.63508, 27.705 ], ], # 45 [ 3699874, 3699875, 3225755 ] - miss
	[ [ 1.66242, 27.7358 ], [ 1.63508, 27.705 ], [ 1.67307, 27.7409 ], ], # 46 [ 3225756, 3225755, 4731007 ] - hit
	# [ [ 1.58769, 27.6566 ], [ 1.583, 27.6501 ], [ 1.63508, 27.705 ], ], # 47 [ 1096265, 3699874, 3225755 ] - miss
	# [ [ 1.58769, 27.6566 ], [ 1.63508, 27.705 ], [ 1.66242, 27.7358 ], ], # 48 [ 1096265, 3225755, 3225756 ] - miss
	# [ [ 1.57071, 27.6395 ], [ 1.58769, 27.6566 ], [ 1.64595, 27.7183 ], ], # 49 [ 1096264, 1096265, 1096266 ] - miss
	# [ [ 1.64595, 27.7183 ], [ 1.58769, 27.6566 ], [ 1.66242, 27.7358 ], ], # 50 [ 1096266, 1096265, 3225756 ] - miss
	# [ [ 1.64595, 27.7183 ], [ 1.66242, 27.7358 ], [ 1.65637, 27.7279 ], ], # 51 [ 1096266, 3225756, 1874443 ] - miss
	# [ [ 1.57238, 27.6382 ], [ 1.57071, 27.6395 ], [ 1.64595, 27.7183 ], ], # 52 [ 1520130, 1096264, 1096266 ] - miss
	[ [ 1.57238, 27.6382 ], [ 1.64595, 27.7183 ], [ 1.64087, 27.7025 ], ], # 53 [ 1520130, 1096266, 283681 ] - hit
	# [ [ 1.64087, 27.7025 ], [ 1.64595, 27.7183 ], [ 1.65637, 27.7279 ], ], # 54 [ 283681, 1096266, 1874443 ] - miss
	# [ [ 1.64087, 27.7025 ], [ 1.65637, 27.7279 ], [ 1.65895, 27.7254 ], ], # 55 [ 283681, 1874443, 1874445 ] - miss
	# [ [ 1.64087, 27.7025 ], [ 1.65895, 27.7254 ], [ 1.66558, 27.7252 ], ], # 56 [ 283681, 1874445, 3911844 ] - miss
	# [ [ 1.64087, 27.7025 ], [ 1.66558, 27.7252 ], [ 1.63493, 27.6851 ], ], # 57 [ 283681, 3911844, 3911845 ] - miss
	# [ [ 1.63493, 27.6851 ], [ 1.66558, 27.7252 ], [ 1.65281, 27.7063 ], ], # 58 [ 3911845, 3911844, 2132111 ] - miss
	# [ [ 1.63493, 27.6851 ], [ 1.65281, 27.7063 ], [ 1.63739, 27.6842 ], ], # 59 [ 3911845, 2132111, 3911860 ] - miss
	# [ [ 1.65281, 27.7063 ], [ 1.69541, 27.7453 ], [ 1.63739, 27.6842 ], ], # 60 [ 2132111, 2132113, 3911860 ] - miss
	# [ [ 1.63312, 27.6765 ], [ 1.63739, 27.6842 ], [ 1.67563, 27.7151 ], ], # 61 [ 5152671, 3911860, 3911861 ] - miss
	# [ [ 1.63739, 27.6842 ], [ 1.69541, 27.7453 ], [ 1.67563, 27.7151 ], ], # 62 [ 3911860, 2132113, 3911861 ] - miss
	# [ [ 1.63312, 27.6765 ], [ 1.67563, 27.7151 ], [ 1.65481, 27.6952 ], ], # 63 [ 5152671, 3911861, 5152672 ] - miss
	# [ [ 1.64046, 27.6851 ], [ 1.65481, 27.6952 ], [ 1.71114, 27.7484 ], ], # 64 [ 3911859, 5152672, 4856882 ] - miss
	# [ [ 1.64046, 27.6851 ], [ 1.71114, 27.7484 ], [ 1.71086, 27.7492 ], ], # 65 [ 3911859, 4856882, 4856881 ] - miss
	# [ [ 1.6585, 27.7064 ], [ 1.64046, 27.6851 ], [ 1.71086, 27.7492 ], ], # 66 [ 2943109, 3911859, 4856881 ] - miss
	# [ [ 1.64046, 27.6851 ], [ 1.6585, 27.7064 ], [ 1.62319, 27.68 ], ], # 67 [ 3911859, 2943109, 1408164 ] - miss
	# [ [ 1.6585, 27.7064 ], [ 1.68873, 27.7389 ], [ 1.64359, 27.7057 ], ], # 68 [ 2943109, 1963413, 1408165 ] - miss
	# [ [ 1.62319, 27.68 ], [ 1.6585, 27.7064 ], [ 1.64359, 27.7057 ], ], # 69 [ 1408164, 2943109, 1408165 ] - miss
	# [ [ 1.64359, 27.7057 ], [ 1.68873, 27.7389 ], [ 1.68513, 27.7474 ], ], # 70 [ 1408165, 1963413, 1963412 ] - miss
	# [ [ 1.62319, 27.68 ], [ 1.64359, 27.7057 ], [ 1.62508, 27.6832 ], ], # 71 [ 1408164, 1408165, 1408166 ] - miss
	# [ [ 1.66872, 27.7339 ], [ 1.64359, 27.7057 ], [ 1.68513, 27.7474 ], ], # 72 [ 3911874, 1408165, 1963412 ] - miss
	# [ [ 1.64359, 27.7057 ], [ 1.66872, 27.7339 ], [ 1.62508, 27.6832 ], ], # 73 [ 1408165, 3911874, 1408166 ] - miss
	# [ [ 1.62508, 27.6832 ], [ 1.66872, 27.7339 ], [ 1.65146, 27.7136 ], ], # 74 [ 1408166, 3911874, 3911873 ] - miss
	# [ [ 1.62508, 27.6832 ], [ 1.65146, 27.7136 ], [ 1.62479, 27.6842 ], ], # 75 [ 1408166, 3911873, 4644501 ] - miss
	# [ [ 1.62479, 27.6842 ], [ 1.64377, 27.7085 ], [ 1.6137, 27.6812 ], ], # 76 [ 4644501, 5465143, 2955328 ] - miss
	# [ [ 1.62479, 27.6842 ], [ 1.65146, 27.7136 ], [ 1.64377, 27.7085 ], ], # 77 [ 4644501, 3911873, 5465143 ] - miss
	# [ [ 1.65146, 27.7136 ], [ 1.66287, 27.7243 ], [ 1.64377, 27.7085 ], ], # 78 [ 3911873, 3679195, 5465143 ] - miss
	# [ [ 1.64377, 27.7085 ], [ 1.66287, 27.7243 ], [ 1.64841, 27.7122 ], ], # 79 [ 5465143, 3679195, 5215970 ] - miss
	# [ [ 1.6137, 27.6812 ], [ 1.64377, 27.7085 ], [ 1.64841, 27.7122 ], ], # 80 [ 2955328, 5465143, 5215970 ] - miss
	# [ [ 1.6137, 27.6812 ], [ 1.64841, 27.7122 ], [ 1.62636, 27.6949 ], ], # 81 [ 2955328, 5215970, 3943893 ] - miss
	# [ [ 1.64841, 27.7122 ], [ 1.66287, 27.7243 ], [ 1.68203, 27.7452 ], ], # 82 [ 5215970, 3679195, 3679197 ] - miss
	# [ [ 1.64841, 27.7122 ], [ 1.68203, 27.7452 ], [ 1.6718, 27.7399 ], ], # 83 [ 5215970, 3679197, 717408 ] - miss
	# [ [ 1.64841, 27.7122 ], [ 1.6364, 27.7027 ], [ 1.61656, 27.687 ], ], # 84 [ 5215970, 4131726, 1745688 ] - miss
	# [ [ 1.64841, 27.7122 ], [ 1.65752, 27.7239 ], [ 1.6364, 27.7027 ], ], # 85 [ 5215970, 3679194, 4131726 ] - miss
	# [ [ 1.64841, 27.7122 ], [ 1.6718, 27.7399 ], [ 1.65752, 27.7239 ], ], # 86 [ 5215970, 717408, 3679194 ] - miss
	# [ [ 1.64841, 27.7122 ], [ 1.61656, 27.687 ], [ 1.62636, 27.6949 ], ], # 87 [ 5215970, 1745688, 3943893 ] - miss
	# [ [ 1.65752, 27.7239 ], [ 1.65432, 27.7224 ], [ 1.6364, 27.7027 ], ], # 88 [ 3679194, 914469, 4131726 ] - miss
	# [ [ 1.6364, 27.7027 ], [ 1.65432, 27.7224 ], [ 1.63001, 27.6925 ], ], # 89 [ 4131726, 914469, 4131727 ] - miss
	# [ [ 1.65432, 27.7224 ], [ 1.65432, 27.7317 ], [ 1.64115, 27.7081 ], ], # 90 [ 914469, 914470, 914471 ] - miss
	# [ [ 1.65432, 27.7224 ], [ 1.64115, 27.7081 ], [ 1.63001, 27.6925 ], ], # 91 [ 914469, 914471, 4131727 ] - miss
	# [ [ 1.63001, 27.6925 ], [ 1.64115, 27.7081 ], [ 1.60527, 27.6748 ], ], # 92 [ 4131727, 914471, 5133857 ] - miss
	# [ [ 1.64115, 27.7081 ], [ 1.62533, 27.7102 ], [ 1.6036, 27.6937 ], ], # 93 [ 914471, 5242244, 914466 ] - miss
	[ [ 1.65432, 27.7317 ], [ 1.62533, 27.7102 ], [ 1.64115, 27.7081 ], ], # 94 [ 914470, 5242244, 914471 ] - hit
	# [ [ 1.64115, 27.7081 ], [ 1.6036, 27.6937 ], [ 1.60321, 27.6795 ], ], # 95 [ 914471, 914466, 914468 ] - miss
	# [ [ 1.64115, 27.7081 ], [ 1.60321, 27.6795 ], [ 1.60527, 27.6748 ], ], # 96 [ 914471, 914468, 5133857 ] - miss
	# [ [ 1.65432, 27.7317 ], [ 1.64622, 27.7289 ], [ 1.62533, 27.7102 ], ], # 97 [ 914470, 4464006, 5242244 ] - miss
	# [ [ 1.64622, 27.7289 ], [ 1.60713, 27.7043 ], [ 1.62533, 27.7102 ], ], # 98 [ 4464006, 1957526, 5242244 ] - miss
	# [ [ 1.64622, 27.7289 ], [ 1.65974, 27.7454 ], [ 1.60713, 27.7043 ], ], # 99 [ 4464006, 1957525, 1957526 ] - miss
	# [ [ 1.65974, 27.7454 ], [ 1.64381, 27.7345 ], [ 1.60713, 27.7043 ], ], # 100 [ 1957525, 351210, 1957526 ] - miss
	# [ [ 1.60713, 27.7043 ], [ 1.64381, 27.7345 ], [ 1.58469, 27.6859 ], ], # 101 [ 1957526, 351210, 351212 ] - miss
	# [ [ 1.64381, 27.7345 ], [ 1.61439, 27.706 ], [ 1.58469, 27.6859 ], ], # 102 [ 351210, 351211, 351212 ] - miss
	# [ [ 1.6446, 27.733 ], [ 1.61439, 27.706 ], [ 1.64381, 27.7345 ], ], # 103 [ 4431152, 351211, 351210 ] - miss
	# [ [ 1.6446, 27.733 ], [ 1.62226, 27.7023 ], [ 1.61439, 27.706 ], ], # 104 [ 4431152, 2375101, 351211 ] - miss
	# [ [ 1.6446, 27.733 ], [ 1.65557, 27.7333 ], [ 1.62226, 27.7023 ], ], # 105 [ 4431152, 4431151, 2375101 ] - miss
	# [ [ 1.65557, 27.7333 ], [ 1.63401, 27.7077 ], [ 1.62226, 27.7023 ], ], # 106 [ 4431151, 2375102, 2375101 ] - miss
	# [ [ 1.65557, 27.7333 ], [ 1.66364, 27.7344 ], [ 1.63401, 27.7077 ], ], # 107 [ 4431151, 4711216, 2375102 ] - miss
	# [ [ 1.62226, 27.7023 ], [ 1.63401, 27.7077 ], [ 1.58927, 27.6774 ], ], # 108 [ 2375101, 2375102, 2375103 ] - miss
	# [ [ 1.63713, 27.7042 ], [ 1.60629, 27.6791 ], [ 1.58927, 27.6774 ], ], # 109 [ 2812215, 2812216, 2375103 ] - miss
	# [ [ 1.63401, 27.7077 ], [ 1.63713, 27.7042 ], [ 1.58927, 27.6774 ], ], # 110 [ 2375102, 2812215, 2375103 ] - miss
	[ [ 1.66364, 27.7344 ], [ 1.63713, 27.7042 ], [ 1.63401, 27.7077 ], ], # 111 [ 4711216, 2812215, 2375102 ] - hit
	# [ [ 1.66364, 27.7344 ], [ 1.68492, 27.7432 ], [ 1.63713, 27.7042 ], ], # 112 [ 4711216, 4711215, 2812215 ] - miss
	# [ [ 1.68492, 27.7432 ], [ 1.66949, 27.7247 ], [ 1.63713, 27.7042 ], ], # 113 [ 4711215, 4711214, 2812215 ] - miss
	# [ [ 1.63713, 27.7042 ], [ 1.64013, 27.7004 ], [ 1.60629, 27.6791 ], ], # 114 [ 2812215, 2019537, 2812216 ] - miss
	# [ [ 1.66949, 27.7247 ], [ 1.64013, 27.7004 ], [ 1.63713, 27.7042 ], ], # 115 [ 4711214, 2019537, 2812215 ] - miss
	# [ [ 1.66949, 27.7247 ], [ 1.70329, 27.7487 ], [ 1.64013, 27.7004 ], ], # 116 [ 4711214, 2019538, 2019537 ] - miss
	# [ [ 1.64013, 27.7004 ], [ 1.70329, 27.7487 ], [ 1.67621, 27.7258 ], ], # 117 [ 2019537, 2019538, 2019539 ] - miss
	# [ [ 1.64013, 27.7004 ], [ 1.67621, 27.7258 ], [ 1.66014, 27.7132 ], ], # 118 [ 2019537, 2019539, 2375100 ] - miss
	# [ [ 1.64013, 27.7004 ], [ 1.66014, 27.7132 ], [ 1.62139, 27.6808 ], ], # 119 [ 2019537, 2375100, 1324629 ] - miss
	# [ [ 1.62139, 27.6808 ], [ 1.66014, 27.7132 ], [ 1.66832, 27.7095 ], ], # 120 [ 1324629, 2375100, 1324630 ] - miss
	# [ [ 1.58864, 27.6136 ], [ 1.62139, 27.6808 ], [ 1.66832, 27.7095 ], ], # 121 [ 1324628, 1324629, 1324630 ] - miss
	# [ [ 1.58864, 27.6136 ], [ 1.66832, 27.7095 ], [ 1.65443, 27.6792 ], ], # 122 [ 1324628, 1324630, 4253399 ] - miss
	# [ [ 1.63562, 27.6565 ], [ 1.65443, 27.6792 ], [ 1.68064, 27.7041 ], ], # 123 [ 2375079, 4253399, 2375080 ] - miss
	# [ [ 1.63562, 27.6565 ], [ 1.68064, 27.7041 ], [ 1.66933, 27.6885 ], ], # 124 [ 2375079, 2375080, 2375081 ] - miss
	# [ [ 1.58793, 27.6087 ], [ 1.65796, 27.6764 ], [ 1.68605, 27.7089 ], ], # 125 [ 327836, 327837, 327838 ] - miss
	# [ [ 1.70794, 27.7314 ], [ 1.58793, 27.6087 ], [ 1.68605, 27.7089 ], ], # 126 [ 1268467, 327836, 327838 ] - miss
	# [ [ 1.62967, 27.651 ], [ 1.58793, 27.6087 ], [ 1.70794, 27.7314 ], ], # 127 [ 1268466, 327836, 1268467 ] - miss
	# [ [ 1.64491, 27.6663 ], [ 1.70794, 27.7314 ], [ 1.70004, 27.721 ], ], # 128 [ 368850, 1268467, 3958762 ] - miss
	# [ [ 1.62967, 27.651 ], [ 1.70794, 27.7314 ], [ 1.64491, 27.6663 ], ], # 129[ 1268466, 1268467, 368850 ] - miss
	# [ [ 1.64813, 27.6674 ], [ 1.64491, 27.6663 ], [ 1.70004, 27.721 ], ], # [ 3588205, 368850, 3958762 ] - miss
	# [ [ 1.64813, 27.6674 ], [ 1.70004, 27.721 ], [ 1.6945, 27.7102 ], ], # [ 3588205, 3958762, 3958761 ] - miss
	# [ [ 1.66966, 27.6804 ], [ 1.64813, 27.6674 ], [ 1.6945, 27.7102 ], ], # [ 3588206, 3588205, 3958761 ] - miss
]

def sign(a: [float], b: [float], c: [float]):
    # looks like cross
	return (a[0 ] - c[0 ]) * (b[1 ] - c[1 ]) - (b[0 ] - c[0 ]) * (a[1 ] - c[1 ])

def dot(a: [float], b: [float]):
	return a[0 ] * b[0 ] + a[1 ] * b[1 ]

def edge(begin: [float], end: [float]):
	return [end[0 ] - begin[0 ], end[1 ] - begin[1 ]]

def barycentric_check(point: [float], triangle: [[float]]):
	d1 = sign(point, triangle[0 ], triangle[1 ])
	d2 = sign(point, triangle[1 ], triangle[2 ])
	d3 = sign(point, triangle[2 ], triangle[0 ])

	neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
	pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
	return not (neg and pos)

def check_against_triangles(point: [float]):
	hits = 0

	index = 0
	for triangle in TRIANGLES:
		if barycentric_check(point, triangle):
			print("Barycentric (" + str(index) + ") " + str(triangle))
			hits += 1
		index += 1
	
	print("Hit " + str(hits) + " triangles")

def problem():
	check_against_triangles([ 1 + 82.5/128, 27 + 91.5/128 ])
