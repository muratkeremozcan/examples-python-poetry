class Document:
		"""A class for text analysis
    
    :param text: string of text to be analyzed
    :ivar text: string of text to be analyzed; set by `text` parameter
    """
		def __init__(self, text):
			self.text = text