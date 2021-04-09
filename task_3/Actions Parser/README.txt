1) Import libraries in a new filename.py

from actions_parser import imperative_parser

2) Call the function

imperative_parser("input_text")

"input text" could be a sentence or a list of sentences.

ex.

imperative_parser("I'm a single a sentence.")

imperative_parser(["I'm sentence 1.", "I'm sentence 2.", "I'm sentence 3."])
