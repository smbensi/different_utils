
#!/bin/sh 
echo x = $1;
# instruction to run in robot
aplay -D plughw:0,7 $1

# instruction to run when speaker connected in usb
# aplay -D plughw:2,0 $1