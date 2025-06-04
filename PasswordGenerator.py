import random
import string

def generate_password(
    length=12,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_symbols=True,
    exclude_similar=True,
    require_each_type=True
):
    
    similar_chars = 'il1Lo0O'
    uppercase = ''.join(c for c in string.ascii_uppercase if c not in similar_chars) if exclude_similar else string.ascii_uppercase
    lowercase = ''.join(c for c in string.ascii_lowercase if c not in similar_chars) if exclude_similar else string.ascii_lowercase
    digits = ''.join(c for c in string.digits if c not in similar_chars) if exclude_similar else string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/~"

    pool = ''
    guaranteed = []

    if use_uppercase:
        pool += uppercase
        if require_each_type:
            guaranteed.append(random.choice(uppercase))
    if use_lowercase:
        pool += lowercase
        if require_each_type:
            guaranteed.append(random.choice(lowercase))
    if use_digits:
        pool += digits
        if require_each_type:
            guaranteed.append(random.choice(digits))
    if use_symbols:
        pool += symbols
        if require_each_type:
            guaranteed.append(random.choice(symbols))

    if not pool:
        raise ValueError("No character types selected!")

 
    remaining_length = length - len(guaranteed)
    password = guaranteed + random.choices(pool, k=remaining_length)
    random.shuffle(password)
    
    return ''.join(password)


print(generate_password(length=4, use_uppercase=False, use_lowercase=False, use_digits=True, use_symbols=False)) 
# To test different scenarios, all you need to do is change the arguments you pass to the generate_password() function.

