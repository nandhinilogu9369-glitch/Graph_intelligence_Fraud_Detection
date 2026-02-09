import csv
import random
from data_generator.generate_entities import (
    generate_users,
    generate_devices,
    generate_ips,
)


def generate_events(path, n=200):
    users = generate_users()
    devices = generate_devices()
    ips = generate_ips()

    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["user", "device", "ip", "event"])

        for _ in range(n):
            writer.writerow(
                [
                    random.choice(users),
                    random.choice(devices),
                    random.choice(ips),
                    random.choice(["login", "payment", "access"]),
                ]
            )
