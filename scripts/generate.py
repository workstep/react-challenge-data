import json
import random
from datetime import datetime, timedelta


MOMENT_ISO8601_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'

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


def get_random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + timedelta(days=random_number_of_days)


domains = ['gmail.com', 'yahoo.com', 'hey.com', 'outlook.com', 'live.com', 'mailinator.com']
steps = [
    '',
    'Paperwork',
    'Background Check',
    'Drug Test',
]

start_date = datetime.now() - timedelta(days=30)
end_date = datetime.now()

data = []
for idx, name in enumerate(names):
    first, last = name.lower().split(' ')
    data.append({
        "id": idx + 1,
        "name": name,
        "phone": "555{}".format(get_random_string(7, '0123456789')),
        "email": "{}{}@{}".format(first, last, random.choice(domains)),
        "profile_url": "/resume/{}{}-{}".format(first[0], last, idx + 1),
        "time_interview": get_random_date(start_date, end_date).strftime(MOMENT_ISO8601_FORMAT),
        "step": random.choice(steps)
    })

print json.dumps(data, indent=2)
