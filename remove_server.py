import os
from common import runparse, get_instance_by_name

from dotenv import load_dotenv

load_dotenv()

instance_name = os.getenv("INSTANCE_NAME")

instances = get_instance_by_name(instance_name)

for instance in instances:
    print(f"Removing instance {instance['id']}")
    output = runparse(["instance", "delete", instance["id"]])
    print(f"Instance {instance['id']} removed!")