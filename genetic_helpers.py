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
        phrase[random.randint(0, len(phrase)-1)] = random.choice(lowercase)
    return phrase

def get_scores(generation, target):
    return [match_score(phrase, target) for phrase in generation]

def get_survivors(generation, target, survival_rate):
    survivor_count = int(len(generation)*survival_rate)
    scores_with_index = list(enumerate(get_scores(generation, target)))
    sorted_scores_with_index = sorted(scores_with_index, key=lambda x: x[0])
    return sorted_scores_with_index[0:survivor_count]
    
def iterate_generation(old_generation, survival_rate, mutation_rate):
    new_generation = []
    survivors = get_survivors(old_generation)
    while len(new_generation) < 20:
        phrase1 = random.choice(old_generation)
        phrase2 = random.choice(new_generation)
        new_generation.append(mutate(breed(phrase1, phrase2)))
    return new_generation
    
