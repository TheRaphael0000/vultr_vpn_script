import subprocess
import json

def runparse(cmd):
    result = subprocess.run(["vultr-cli"] + cmd + ["-o", "json"], stdout=subprocess.PIPE)
    output = json.loads(result.stdout)
    return output


def get_instance_by_name(name):
    print(f"Getting instances with label='{name}'...")
    output = runparse(["instance", "list"])
    instances = output["instances"]
    instances = [i for i in instances if i["label"] == name]
    print(f"{len(instances)} instances found!")
    return instances


def get_regions():
    print(f"Getting regions...")
    output = runparse(["region", "list"])
    regions = output["regions"]
    print(f"{len(regions)} regions found!")
    return regions