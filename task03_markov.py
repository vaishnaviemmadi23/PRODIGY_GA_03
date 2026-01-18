import random
from collections import defaultdict
text = """
Generative AI is a powerful technology that can create text, images, and code.
Markov Chains generate new text based on probability.
This program learns word patterns from the input text and produces new sentences.
Learning GitHub and Python step by step will help me improve my skills.
"""
words = text.split()
model = defaultdict(list)
for i in range(len(words)-1):
   current_word =words[i]
   next_word =words[i +1]
   model[current_word].append(next_word)
start_word = random.choice(words)
result = [start_word]

for _ in range(30):
 current_word= result[-1]
 if current_word not in model:
      break

result.append(random.choice(model[current_word])
             )
print("Generated Text:")
print(" ".join(result))
