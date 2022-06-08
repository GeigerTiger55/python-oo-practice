from random import choice

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

            TODO: Open file directly in __init__, then call function, then close file
        """

        self.file = open(file_path, "r")
        self.list_of_words = self.read_word_file()
        self.file.close()
        self.num_of_words = len(self.list_of_words)
        self.print_word_count()

    def __repr__(self):
        return f"<WordFinder file={self.file} list_of_words={self.list_of_words} num_of_words={self.num_of_words}"

    def read_word_file(self):
        """ Reads file line-by-line.
            Appends each line to a list of words.
            Returns the list.
            TODO: Use method strip to remove white space from line
        """

        word_list = []

        for line in self.file:
            word_list.append(line.strip())

        return word_list

    def print_word_count(self):
        """ Prints number of words read. """
        print (f"{self.num_of_words} words read.")

    def random(self):
        """Returns a random word from the WordFinder list"""
        return choice(self.list_of_words)


class SpecialWordFinder(WordFinder):
    """Special Word Finder: ignores blank lines and lines that start with # when creating list of words"""

    def __repr__(self):
        return f"<SpecialWordFinder file_path={self.file_path} list_of_words={self.list_of_words} num_of_words={self.num_of_words}"

    def read_word_file(self):
        """ Uses parent method to get list of words
            Filters out items that start with # and that are empty"""
        word_list = super().read_word_file()

        updated_list = [line for line in word_list if not line.startswith("#") and len(line) > 0]
        return updated_list


