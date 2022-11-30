# -*- coding: utf-8 -*-

def tree_segnemt_line(number_of_spaces = 10, number_of_twigs=10, twig_char = '*'):
	return "{spaces}{twigs}{twigs}{spaces}"\
				.format(spaces = number_of_spaces * ' ', 
						twigs = number_of_twigs * twig_char)


def tree_segment(hight = 10, width = 10, twig_char = '*', shift = 10):
	for i in range(hight):
		line = "{shift_segment}{tree_segment}"\
			.format(shift_segment = shift * ' ', 
					tree_segment = tree_segnemt_line(number_of_spaces = width-i-1, number_of_twigs=i+1) )
		print(line)
		


def christmas_tree(number_of_segments=3, first_segment_hight = 5):
	tree_segnemt_data = []
	shift = 0
	for segment_number in range(number_of_segments, 0, -1):
		width = hight = segment_number * first_segment_hight
		tree_segnemt_data[:0] = [{'shift': shift, 'width': width, 'hight': hight}]
		shift += first_segment_hight
	for segment in tree_segnemt_data:
		tree_segment(hight = segment['hight'], width = segment['width'], shift = segment['shift'])
		
		
		
if __name__ == '__main__':
	christmas_tree()
