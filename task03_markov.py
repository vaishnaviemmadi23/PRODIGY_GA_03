import random
from collections import defaultdict
text ="""
Generative AI is a powerful technology.
AI can generate text and images.
Morkov Chains generate text using probability.
"""
words = text.split()
model = defaultdict(list)
for i in range(len(words)-1):
   current_word =words[i]
   next_word =words[i +1]
   model[current_word].append(next_word)
start_word = random.choice(words)
result = [start_word]

for _in range(30):
 current_word= result[-1]
   if current_word not in model:
      break

result.append(random.choice(model[current_word])
             )
print("Generated Text:")
print("."join(result))
