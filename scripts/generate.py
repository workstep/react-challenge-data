import json
import random

# https://www.randomlists.com/random-names?qty=20
names = [
    'Marissa Williamson',
    'Ireland Gillespie',
    'Amaris Escobar',
    'Judah Norman',
    'Amanda Avery',
    'Jovany Rose',
    'Natalia Sullivan',
    'Irene Hammond',
    'Tyrone Owen',
    'Freddy Maddox',
    'Simon Parker',
    'Dawson Davis',
    'Carmelo Green',
    'Dayana Good',
    'Jazmin Leonard',
    'Rigoberto Holder',
    'Blaine Reese',
    'Taylor Jenkins',
    'Rolando Daniels',
    'Clarence Robbins',
]


def get_random_string(length=24,
                      allowed_chars='abcdefghijklmnopqrstuvwxyz'
                                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    return ''.join(random.choice(allowed_chars) for _ in range(length))


domains = ['gmail.com', 'yahoo.com', 'hey.com', 'outlook.com', 'live.com', 'mailinator.com']
steps = [
    'New Candidate',
    'Invited to Interview',
    'Needs Feedback',
    'Moving Forward',
    'Hired',
]

data = []
for idx, name in enumerate(names):
    first, last = name.lower().split(' ')
    data.append({
        "id": idx + 1,
        "name": name,
        "phone": "555{}".format(get_random_string(7, '0123456789')),
        "email": "{}{}@{}".format(first, last, random.choice(domains)),
        "profile_url": "/resume/{}{}-{}".format(first[0], last, idx + 1),
        "step": random.choice(steps)
    })

print json.dumps(data, indent=2)
