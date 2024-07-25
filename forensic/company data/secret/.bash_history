cat flag.txt
nano pass.txt
zip --password $(cat pass.txt | tr -d '\n') company_data.zip flag.txt
cat pass.txt
ls -lah
unzip company_data.zip
truncate -s -2 pass.txt
cat pass.txt
rm flag.txt
history -a


