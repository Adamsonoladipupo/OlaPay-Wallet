import random

def generate_account_number():
    return "44" + str(random.randrange(00000000, 99999999))

def generate_reference_number():
    return "ref" + str(random.randrange(000000000000000, 999999999999999))