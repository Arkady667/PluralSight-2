# coding=utf-8
"""
The with statement clarifies code that previously would use try...finally blocks to ensure that clean-up code is executed.
In this section, I’ll discuss the statement as it will commonly be used. In the next section, I’ll examine the implementation
details and show how to write objects for use with this statement.

The with statement is a control-flow structure whose basic structure is:

with expression [as variable]:
    with-block

The expression is evaluated, and it should result in an object that supports the context management protocol
(that is, has __enter__() and __exit__() methods).

with jest uzywane do pracy z niezarzadzanymi zasobami np. strumienie plikow
pozwala na upewnienie sie ze zrodlo jest "wyczyszczone" kiedy kod zaczyna dzialac
"""
import sys
from urllib import urlopen


def fetch_words(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words()  
    print_items(words)


if __name__ == "__main__":
    main(sys.argv[1])
