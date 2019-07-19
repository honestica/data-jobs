#!/usr/bin/env python3
import random
from datetime import datetime, timedelta

START = datetime.strptime('2019-07-01 00:00:00', '%Y-%m-%d %H:%M:%S')
END = datetime.strptime('2019-08-01 00:00:00', '%Y-%m-%d %H:%M:%S')


def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)


def sample_communication(uuid):
  telecoms = random.choice(["paper", "mail", "lifen"])

  senders = random.choice(
    [
      {"name": "Jean Martin", "profession": "liberal"},
      {"name": "Michel Durant", "profession": "public_hospital"},
      {"name": "Herve Delatour", "profession": "liberal"},
      {"name": "Maurice Rolland", "profession": "liberal"},
      {"name": "Vincent Martinez", "profession": "private_hospital"}
    ]
  )

  return "|".join([
    f'id={uuid}',
    f'telecom={telecoms}',
    f'created_at={random_date(START, END).strftime("%Y-%m-%d %H:%M:%S")}',
    f'sender={senders}'
  ])
  