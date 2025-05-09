# _ means private method

import re
from collections import Counter

class Document:
	"""A class for text analysis
	
	:param text: string of text to be analyzed
	:ivar text: string of text to be analyzed; set by `text` parameter
	"""
	def __init__(self, text):
		self.text = text
		self.tokens = self._tokenize()
		self.word_counts = self._count_words()
	
	# converts text to lowercase and uses regex to find all alphanumeric "words"
	def _tokenize(self):
		return re.findall(r'\b\w+\b', self.text.lower())
		
	def _count_words(self):
		return Counter(self.tokens)