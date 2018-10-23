import subprocess
cmdpipe = subprocess.Popen("sudo arp-scan --interface=en0 --localnet", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
result = {}

for row in cmdpipe.stdout.readline():
    if '. ' in row:
        key, value = row.split(' ')
        result[key.strip(' ')] = value.strip()

print(result)
print(result['A (Host) Record'])
