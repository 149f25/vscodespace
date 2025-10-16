"""Simplify and normalize text for easier reading.

Author: YOUR NAME
Version: THE DATE
"""

replacements = {
    "approximately": "about",
    "assistance": "help",
    "commence": "begin",
    "comprehend": "understand",
    "consequently": "so",
    "demonstrate": "show",
    "endeavor": "try",
    "fortunate": "lucky",
    "indicate": "show",
    "individuals": "people",
    "inform": "tell",
    "modify": "change",
    "nevertheless": "but",
    "numerous": "many",
    "obtain": "get",
    "prior": "before",
    "purchase": "buy",
    "regarding": "about",
    "requirement": "need",
    "reside": "live",
    "respond": "answer",
    "subsequent": "next",
    "terminate": "end",
    "therefore": "so",
    "utilize": "use",
}


def normalize_text(text: str) -> str:
    """Clean up whitespace and punctuation spacing.

    - Removes leading/trailing spaces
    - Replaces newlines with single spaces
    - Collapses multiple spaces into one space
    - Removes spaces before periods and commas

    Example:
        "  Hello ,   world! " → "Hello, world!"

    Args:
        text: The text to normalize.

    Returns:
        A normalized string.
    """


def simplify_case(text: str) -> str:
    """Convert ALL CAPS words to all lowercase.

    You may assume that the first word of a sentence will not be in ALL CAPS.
    (This makes the assignment easier, because you won't have to go back and
    capitalize the first word of every sentence.) Some words might end with
    punctuation, as shown in the example below. The personal pronoun "I" must
    not be made lowercase.

    Example:
        "That's WHAT I SAID!" → "That's what I said!"

    Args:
        text: The text to adjust.

    Returns:
        A string with ALL CAPS words made lowercase.
    """


def replace_complex_words(text: str) -> str:
    """Replace difficult or academic words with simpler synonyms.

    All words found in `replacements` (the global variable) are replaced in
    the text. Capitalized words remain capitalized (Ex: "Utilize" → "Use").

    Args:
        text: The text to simplify.

    Returns:
        A string with complex words replaced by easier ones.
    """


def shorten_sentences(text: str) -> str:
    """Split sentences that contain semicolons.

    Sentences with one or more semicolons are split into two or more sentences.
    The first word of each new sentence must be capitalized, for example:
    "Today is Friday; this is nice." → "Today is Friday. This is nice."

    Args:
        text: The text to process.

    Returns:
        The text with sentences shortened.
    """


def convert_to_easy_read(text: str) -> str:
    """Run all simplification steps on the given text.

    Steps:
        1. Normalize text
        2. Simplify case
        3. Replace complex words
        4. Shorten sentences

    Args:
        text: The text to simplify.

    Returns:
        A simplified version of the text.
    """
