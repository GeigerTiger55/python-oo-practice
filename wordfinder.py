class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    # take a file path
    # makes attribute list of words
    # prints "[num-of-words-read] words read"
    # random() --> returns random word from list of words

    def __init__(self, file_path):
        """ Takes a file path.
            Calls function to create list attribute containing words in file.
            Calls function to print word count. 
        """
        self.file_path = file_path
        self.list_of_words = self.read_word_file()
        self.num_of_words = len(self.list_of_words)
        self.print_word_count()

    def __repr__(self):
        return f"<WordFinder file_path={self.file_path} list_of_words={self.list_of_words} num_of_words={self.num_of_words}"

    def read_word_file(self):
        """ Opens a file.
            Reads file line-by-line.
            Appends each line to a list of words.
            Returns the list.
        """
        file = open(self.file_path, "r")

        word_list = []

        for line in file:
            word_list.append(line)
        
        file.close()

        return word_list

    def print_word_count(self):
        """ Prints number of words read. """
        print (f"{self.num_of_words} words read.")