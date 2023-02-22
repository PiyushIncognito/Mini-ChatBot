import random

R_EATING = "I like to eat data with some delicious malicious viruses!"



def unknown():
    response = ['Could you please re-phrase that?',
                "...",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]
    return response