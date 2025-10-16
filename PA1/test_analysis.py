"""Unit tests for analysis functions.

Author: YOUR NAME
Version: THE DATE
"""

from analysis import count_sentences, count_words, average_word_length, summarize_text
from pytest import approx


# ---------------------------------------------------------------------------
# count_sentences()
# ---------------------------------------------------------------------------


def test_count_sentences_basic():
    """Test a short paragraph with two or more sentences."""


def test_count_sentences_mixed():
    """Test different sentences ending with ., ?, and !"""


def test_count_sentences_no_punctuation():
    """Test an incomplete sentence with no punctuation."""


def test_count_sentences_empty():
    """Test the empty string."""


def test_count_sentences_whitespace():
    """Test a string with only spaces and newlines."""


# ---------------------------------------------------------------------------
# count_words()
# ---------------------------------------------------------------------------


def test_count_words_basic():
    """Test sentences with several words."""


def test_count_words_extra_spaces():
    """Test sentences with multiple spaces between words."""


def test_count_words_punctuation():
    """Test sentences with words that include punctuation."""


def test_count_words_empty():
    """Test the empty string."""


def test_count_words_whitespace():
    """Test a string with only spaces and newlines."""


# ---------------------------------------------------------------------------
# average_word_length()
# ---------------------------------------------------------------------------

# NOTE Since average_word_length returns a float, be sure to use approx().


def test_average_word_length_basic():
    """Test sentences with several words."""


def test_average_word_length_with_punctuation():
    """Test sentences with words that include punctuation."""


def test_average_word_length_empty():
    """Test the empty string."""


def test_average_word_length_whitespace():
    """Test a string with only spaces and newlines."""


# ---------------------------------------------------------------------------
# summarize_text()
# ---------------------------------------------------------------------------


def test_summarize_text_basic():
    """Test a sentence with a few words."""


def test_summarize_text_no_words():
    """Test the empty string."""
