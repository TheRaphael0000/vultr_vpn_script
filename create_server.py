import os
from common import runparse, get_instance_by_name, get_regions
import subprocess
import time
import pick

from dotenv import load_dotenv

load_dotenv()

instance_name = os.getenv("INSTANCE_NAME")
ssh_key_id = os.getenv("SSH_KEY_ID")

instances = get_instance_by_name(instance_name)

if(len(instances) <= 0):

    regions = get_regions()

    menu_options = [(r["id"], f"{r['city']} ({r['country']})" ) for r in regions]
    menu_options = sorted(menu_options, key=lambda r: r[-1])

    option, index = pick.pick([o[-1] for o in menu_options], "Region :", indicator="->")
    region_id, region_name = menu_options[index]

    print(f"Creating new instance in {region_name}...")
    runparse(["instance", "create", f"--label={instance_name}", f"--region={region_id}", "--plan=vc2-1c-1gb", "--image=wireguard", f"--ssh-keys={ssh_key_id}"])


while True:
    instances = get_instance_by_name(instance_name)

    try:
        ip = instances[0]["main_ip"]
    except:
        print("No IP available yet, retrying in 5 seconds")
        time.sleep(5)
        continue
    
    print(f"Using instance with ip: {ip}")
    break


while True:
    print("Downloading wg0.conf...")
    output = subprocess.run(["scp", "-o", "StrictHostKeyChecking=no", "-o", "ConnectTimeout=5", f"root@{ip}:/var/www/html/wireguard_conf/wg0.conf", "."], stdout=subprocess.PIPE)
    if output.returncode == 0:
        break
    print("Couldn't download wg0.conf, retrying in 5 seconds")
    time.sleep(5)

print("wg0.conf downloaded!")
