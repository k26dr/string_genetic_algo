import random
from string import ascii_lowercase as lowercase

# add space characer to lowercase for random letter generation
lowercase += ' '

def random_phrase(size):
    return ''.join(random.choice(lowercase) for i in range(size))

def random_generation(generation_size, phrase_size):
    generation = []
    for i in range(generation_size):
        generation.append(random_phrase(phrase_size))
    return generation

def match_score(phrase, target):
    score = 0
    for i in range(len(phrase)):
        if target[i] == phrase[i]:
            score += 1
    return score / len(phrase)

def breed(phrase1, phrase2):
    new_phrase = ""
    for i in range(len(phrase1)):
        if random.random() < 0.5:
            new_phrase += phrase1[i]
        else:
            new_phrase += phrase2[i]
    return new_phrase

def mutate(phrase, mutation_rate):
    if random.random() < mutation_rate:
        index = random.randint(0, len(phrase)-1)
        phrase = phrase[0:index] + random.choice(lowercase) + phrase[index+1:]
    return phrase

def get_scores(generation, target):
    return [match_score(phrase, target) for phrase in generation]

def get_survivors(generation, target, survival_rate):
    survivor_count = int(len(generation)*survival_rate)
    scores_with_index = list(enumerate(get_scores(generation, target)))
    sorted_scores_with_index = sorted(scores_with_index, key=lambda x: x[1], reverse=True)
    survivors = []
    for t in sorted_scores_with_index[0:survivor_count]:
        survivors.append(generation[t[0]])
    return survivors
    
def iterate_generation(old_generation, target, survival_rate=0.3, mutation_rate=0.01):
    new_generation = []
    survivors = get_survivors(old_generation, target, survival_rate)
    while len(new_generation) < len(old_generation):
        parent1 = random.choice(survivors)
        parent2 = random.choice(survivors)
        child = mutate(breed(parent1, parent2), mutation_rate)
        new_generation.append(child)
    return new_generation
    
