"""Text analysis functions: sentence/word count, average word length.

Author: YOUR NAME
Version: THE DATE
"""


def count_sentences(text: str) -> int:
    """Count the number of sentences in the given text.

    A sentence is a sequence of words that ends with a period, question mark,
    or exclamation point. Every sentence except for the last sentence must be
    followed by a whitespace character as defined by str.isspace().

    If the text contains no such punctuation, the entire string is considered
    one sentence. However, a string that contains only whitespace characters
    is not considered a sentence.

    Args:
        text: The text to analyze.

    Returns:
        The number of sentences found.
    """


def count_words(text: str) -> int:
    """Count the number of words in the given text.

    Words are separated by whitespace and may include punctuation. For example,
    "Hello, world!" contains two words.

    Args:
        text: The text to analyze.

    Returns:
        The number of words found.
    """


def average_word_length(text: str) -> float:
    """Compute the average word length in the given text.

    Punctuation characters (as defined by string.punctuation) are stripped from
    each word before measuring its length. For example, "long-term" counts as 9
    characters, while "U.S.A." counts as 5 (because the end period is stripped).

    Args:
        text: The text to analyze.

    Returns:
        The average number of characters per word, or 0.0 if no words exist.
    """


def summarize_text(text: str) -> str:
    """Produce a formatted summary of text statistics.

    Includes the number of sentences, number of words, and average word length
    (formatted to one decimal place). Each line of the string begins with TWO
    spaces. The last line does NOT end with a newline character. For example:

    >>> summarize_text("Hi Mom!")
      Sentences: 1
      Words: 2
      Average word length: 2.5

    Args:
        text: The text to analyze.

    Returns:
        A formatted string summary of text statistics.
    """
