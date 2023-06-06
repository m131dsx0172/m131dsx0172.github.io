import requests
import json

# Replace the following variables with your own values
repository_owner = "m131dsx0172"
repository_name = "m131dsx0172.github.io"
deploy_key_title = "Kunciku"
deploy_key_public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDYYRAbC0EiY6jDnVdNqA4a6OE8f34CxYqElh52TE1hRXhoxHwTqwbvdqlscp9BECqCvf9ldR0nxpmPhuj1QA88T9GGNGhVS/KzdvaNB/Ie+LDPF68cGdHCYIA17PghSI+txa/g810nLDdjVdwT/s+G4Ms26Va4BCieC/tSWpiOSXQypqJj4SmbBXO75zpAkCCjTTuI3MDEqapSqAiZfLgO781b00R4uagY8NS+C9zVap5R1QW3QWPHKV8bPiBA/7SC36ZY56J6+3IJg5Wor9xXNwpMwA9c0yfjCn265/qlOT1mQXgLRwGI+tB6NMfpfltR0nfSMYJdaskCgalJiyEokwdU1utOwS2F9KjGFNDtn35QuPD+YM/WRlz5PmZq+j+6EkNhlpg5BRT3IMYsCc1xykPVgpP9IpZYnuzKJSp4G1gvKhRApEe5nA2pYNKGxAHX1jdlh4wbZBvZ5rZzV331ALehdEAVp+UrYeOdL/rlEut4C4w/UR1odn0X5yGRKUiiLUEruLwD43/Ufm+hmY08sLf97J15jLE4bWgW688l6WFFki7yfhtr1hchnjym1+ZCMXpfBAnkT7FEx3SEiCSLA9Q5dBwmxMjKytqoL2JDUjolN7wMIlA00taZpnMinJeZThdpUtmLrKFK2Pk3jo1HAkF2UlezsMEUSx8qA8pAIQ== m131dsx0172@bangkit.academy"

# Generate a personal access token with the "repo" scope and replace with your own token
access_token = "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"

# Create the deploy key
url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/keys"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/vnd.github.v3+json"
}
data = {
    "title": deploy_key_title,
    "key": deploy_key_public_key,
    "read_only": False
}
response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 201:
    print("Deploy key created successfully.")
else:
    print("Failed to create deploy key.")
    print("Response:", response.json())
