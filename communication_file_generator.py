#!/usr/bin/env python3
"""
Script used to generate 1000 random communication.
"""
import os
import uuid

from lib.communication_generator import sample_communication

for _ in range(1000):
    communication_id = uuid.uuid4()

    filename = f"./communications/communication-{communication_id}.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as file:
        com = sample_communication(communication_id)
        file.write(sample_communication(communication_id))
