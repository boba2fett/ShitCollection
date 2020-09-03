#!/usr/bin/env python3
import sys, os, random
text=input()
output=" ".join([word[0]+''.join(random.sample(word[1:-1],len(word[1:-1])))+word[-1] if len(word)>1 else word for word in text.split(" ")])
print(output)