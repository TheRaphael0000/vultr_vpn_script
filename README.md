# vultr_vpn_script

the goal of these script are to quickly create a vps with Wireguard on Vultr and download the tunnel file.

requirements (accessible in the PATH):
- vultr-cli: https://github.com/vultr/vultr-cli
- scp

## Config

```bash
cp .env_sample .env
vim .env
```

- `API_KEY=` Generate an API key on, add access control if you want: https://my.vultr.com/settings/#settingsapi
- `SSH_KEY_ID=` Add you public ssh key to: https://my.vultr.com/settings/#settingssshkeys, click on it, you'll see the key id in the url
- `INSTANCE_NAME=` Any name that you don't use yet on Vultr, for example `vpn`

## Install

```
pip install -r requirements.txt
```

## Usage

```bash
python create_server.py # will create the server on Vultr and get the tunnel key from it
python remove_server.py # will remove it
```