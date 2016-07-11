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
assert(mutated != phrase)
different_letters = 0
for i in range(len(phrase)):
    if mutated[i] != phrase[i]:
        different_letters +=1 
assert(different_letters is 1)
print("mutate passes tests")

# get_scores
generation = ["gello", "jo no"]
target = "hello"
assert(gh.get_scores(generation, target) == [.8,.2])
print("get scores passes tests")

# get_survivors
assert(gh.get_survivors(generation, target, 0.5) == ["gello"])
generation = ["goodbye", "goodboy", "joedbor"]
target = "goodbyf"
assert(gh.get_survivors(generation, target, 0.8) == ["goodbye", "goodboy"])

target = gh.random_phrase(5)
generation = gh.random_generation(200, 5)
survivors = gh.get_survivors(generation, target, 0.1)
generation_scores = sorted(gh.get_scores(generation, target), reverse=True)
survivors_scores = sorted(gh.get_scores(survivors, target), reverse=True)
assert(generation_scores[0:20] == survivors_scores)
print("get_survivors passes tests")

# iterate_generation
survival_rate = 0.3
mutation_rate = 0.2
generations = 30
generation_size = 2000
phrase_size = 50

first_generation = gh.random_generation(generation_size, phrase_size)
target = gh.random_phrase(phrase_size)
new_generation = gh.iterate_generation(first_generation, target, survival_rate, mutation_rate)
assert(len(new_generation) == len(first_generation))

print("Starting full simulation")
print("Generations:", generations)
print("Generation Size:", generation_size)
print("Survival Rate:", survival_rate)
print("Mutation Rate:", mutation_rate)
print("Target:", target)
first_scores = gh.get_scores(first_generation, target)
first_average = sum(first_scores) / len(first_scores)
print("Generation 0 average:", first_average)
new_generation = gh.iterate_generation(first_generation, target, survival_rate, mutation_rate)
assert(len(new_generation) == len(first_generation))


for i in range(generations):
    old_generation = new_generation
    new_generation = gh.iterate_generation(old_generation, target, survival_rate, mutation_rate)
    new_scores = gh.get_scores(new_generation, target)
    new_average = sum(new_scores) / len(new_scores)
    print("Generation {0} average:".format(i+1), new_average)
assert(new_average > first_average)
