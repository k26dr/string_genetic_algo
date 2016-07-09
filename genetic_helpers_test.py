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

# breed
print("Breeding...")
parent1 = "hello mister sir"
parent2 = "go do more for m"
new_phrase = gh.breed(parent1, parent2)
assert(len(new_phrase) == len(parent1) == len(parent2))
for i in range(len(new_phrase)):
    assert(new_phrase[i] == parent1[i] or new_phrase[i] == parent2[i])
print("Parents:")
print(parent1)
print(parent2)
print("Child:", new_phrase)
print("breed passes tests")

# mutate
print("Mutating...")
phrase = new_phrase # from breed result
mutated = gh.mutate(phrase, 0)
assert(phrase == mutated)
mutated = gh.mutate(phrase, 1)
print("Original:", phrase)
print("Mutated: ", mutated)
assert(mutated != phrase, "Phrase did not mutate, WARNING: There is a 1/27 chance of this happeningordinarily. If you see this warning more often than that, this is a failed test")
different_letters = 0
for i in range(len(phrase)):
    if mutated[i] != phrase[i]:
        different_letters +=1 
assert(different_letters is 1, "Again, this will occur 1/27 times by random chance")
print("mutate passes tests")

# get_scores
generation = ["gello", "jo no"]
target = "hello"
assert(gh.get_scores(generation, target) == [.8,.2])
print("get scores passes tests")

#get_survivors
assert(gh.get_survivors(generation, target, 0.5) == ["gello"])
generation = ["goodbye", "goodboy", "joedbor"]
target = "goodbyf"
assert(gh.get_survivors(generation, target, 0.8) == ["goodbye", "goodboy"])
print("get_survivors passes tests")

# iterate_generation
old_generation = gh.random_generation(20,15)
target = gh.random_phrase(15)
new_generation = gh.iterate_generation(old_generation, target, 0.3, 0.01)
assert(len(new_generation) == len(old_generation))
for i in range(100):
    old_generation = new_generation
    new_generation = gh.iterate_generation(old_generation, target, 0.3, 0.01)
old_scores = gh.get_scores(old_generation, target)
new_scores = gh.get_scores(new_generation, target)
old_average = sum(old_scores) / len(old_scores)
new_average = sum(new_scores) / len(new_scores)
print(new_average, old_average)
assert(new_average > old_average)
