#!/usr/bin/env python3
import os
import uuid
from lib.communication_generator import sample_communication

for _ in range(1000):
	id = uuid.uuid4()

	filename = f'./communications/communication-{id}.json'
	os.makedirs(os.path.dirname(filename), exist_ok=True)

	with open(filename, 'w') as file:
		com = sample_communication(id)
		file.write(sample_communication(id))



