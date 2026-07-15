""" 20260715 KARAT interview (30 min)
You are running a classroom and suspect that some of your students are passing
around the answer to a multiple-choice question disguised as a random note.

Your task is to write a function that, given a list of words and a note,
finds and returns the word in the list that is scrambled inside the note,
if any exists. If none exist, it returns the result "-" as a string.
There will be at most one matching word. The letters don't need to be in order
or next to each other. The letters cannot be reused.

Example:  
words = ["baby", "referee", "cat", "dada", "dog", "bird", "ax", "baz", "bgb"]

note1 = "ctay"
find(words, note1) => "cat"   (the letters do not have to be in order)

note2 = "bcanihjsrrrferet"
find(words, note2) => "cat"   (the letters do not have to be together)

note3 = "tbaykkjlga"
find(words, note3) => "-"     (the letters cannot be reused)

note4 = "bbbblkkjbaby"
find(words, note4) => "baby"

note5 = "dad"
find(words, note5) => "-"

note6 = "breadmaking"
find(words, note6) => "bird"

note7 = "dadaa"
find(words, note7) => "dada"

Complexity analysis variables:
W = number of words in `words`  
S = maximal length of each word or of the note  
"""

def find_word_from_note(words: list, note: str) -> str:
    """ Algorithm
    For each word, look for each of its character in the note.
        If the character is not found, the word is not in the note
        If the character is found, remove the character from the note
        If there are no more of the word's characters to find, return word
    """
    for word in words:
        letters_remaining = len(word)
        note_copy = note
        for character in word:
            if character in note_copy:
                note_copy = note_copy.replace(character, "", 1)
                letters_remaining -= 1
            else:
                break
            if not letters_remaining:
                return word
    return '-'

def test_find_word_from_notes():
    words = ["baby", "referee", "cat", "dada", "dog", "bird", "ax", "baz", "bgb"]
    notes = ["ctay", "bcanihjsrrrferet", "tbaykkjlga","bbbblkkjbaby", "dad", "breadmaking", "dadaa"]
    expected = ["cat", "cat", "-", "baby", "-", "bird", "dada"]

    for count, note in enumerate(notes):
        print(f"\nSearching note: {note} for {len(words)} words")
        actual = find_word_from_note(words, note)
        print (f"FOUND: {actual}")
        assert expected[count] == actual

test_find_word_from_notes()
