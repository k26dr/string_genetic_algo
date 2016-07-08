#!/usr/bin/env python3
import genetic_helpers as gh

# random_phrase
phrase = gh.random_phrase(50)
assert(len(phrase) == 50)
print("Random Phrase:", phrase)

# random_generation
generation = gh.random_generation(50, 50)
assert(len(generation) == 50)
for phrase in generation:
    assert(len(phrase) == 50)
    assert(type(phrase) is str)
print("random_generation passes tests")

# match_score
assert(gh.match_score("get", "get") == 1)
assert(gh.match_score("Genie", "genie") == .8)
assert(gh.match_score("hello my name is bob", "hello my name is dan") == .85)
print("match_score passes tests")


