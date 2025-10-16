"""Sample program for the Text Simplifier project.

Author: CS149 Faculty
Version: 10/08/2025
"""

from analysis import summarize_text
from simplify import convert_to_easy_read

sample = """
THIS IS AN EXAMPLE paragraph that will commence our analysis to demonstrate
the potential benefits of the system. The process will UTILIZE advanced methods
to provide assistance to users; approximately across several departments.
"""


def main() -> None:
    """Demonstrate summarize_text() and convert_to_easy_read().

    This program analyzes and simplifies a sample text, printing statistics
    before and after simplification.
    """

    print("\nOriginal text:")
    print(sample.strip().replace("\n", " "))

    print("\nOriginal text statistics:")
    print(summarize_text(sample))

    print("\nSimplified text:")
    easy = convert_to_easy_read(sample)
    print(easy)

    print("\nSimplified text statistics:")
    print(summarize_text(easy))
    print()


if __name__ == "__main__":
    main()
