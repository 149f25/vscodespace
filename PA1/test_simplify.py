"""Unit tests for simplify functions.

Author: YOUR NAME
Version: THE DATE
"""

from simplify import (
    normalize_text,
    simplify_case,
    replace_complex_words,
    shorten_sentences,
    convert_to_easy_read,
)


# ---------------------------------------------------------------------------
# normalize_text()
# ---------------------------------------------------------------------------


def test_normalize_text_lead_trail():
    """Test sentence with spaces before and after."""


def test_normalize_text_newlines():
    """Test paragraph with newline characters."""


def test_normalize_text_extra_spaces():
    """Test multiple spaces between words."""


def test_normalize_text_space_before():
    """Test spaces before periods and commas."""


# ---------------------------------------------------------------------------
# simplify_case()
# ---------------------------------------------------------------------------


def test_simplify_case_all_caps():
    """Test a sentence with all words in ALL CAPS."""


def test_simplify_case_lowercase():
    """Test a sentence with all lowercase letters."""


def test_simplify_case_with_i():
    """Test a sentence that includes the personal pronoun I."""


def test_simplify_case_punctuation():
    """Test sentences that include punctuation, including after I."""


# ---------------------------------------------------------------------------
# replace_complex_words()
# ---------------------------------------------------------------------------


def test_replace_complex_words_basic():
    """Test sentences with one or more complex words."""


def test_replace_complex_words_capitalized():
    """Test sentences with capitalized complex words."""


def test_replace_complex_words_no_match():
    """Test a sentence with no complex words."""


# ---------------------------------------------------------------------------
# shorten_sentences()
# ---------------------------------------------------------------------------


def test_shorten_sentences_basic():
    """Test a simple example with one semicolon."""


def test_shorten_sentences_multiple():
    """Test an example with two or more semicolons."""


def test_shorten_sentences_none():
    """Test an example with no semicolons."""


# ---------------------------------------------------------------------------
# convert_to_easy_read()
# ---------------------------------------------------------------------------


def test_convert_to_easy_read_all4():
    """Test a paragraph that needs all four simplification steps."""


def test_convert_to_easy_read_only2():
    """Test a paragraph that needs only two simplification steps."""
