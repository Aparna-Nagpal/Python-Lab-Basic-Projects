"""
fixed length, At least 12 characters long is recommended, 8 at the minimum. The 
combination of both upper- and lower-case letters, numbers, and symbols. Random enough that 
they do not contain any predictable sequence
"""
import random
import string
t=''
l=random.randint(8,12)
H=string.digits
q=string.ascii_lowercase
r=string.ascii_uppercase
s=string.punctuation
t=H+q+r+s+t
k=l-4
p=random.choices(t,k=k)
p.append(random.choice(H))
p.append(random.choice(q))
p.append(random.choice(r))
p.append(random.choice(s))
random.shuffle(p)
print("PASSWORD =",''.join(p))
