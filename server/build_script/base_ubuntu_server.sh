

# Server IP: <server_ip>
# Server Admin User: <user>
# Server Admin Password: <pwd>
# SSH Key Pair File Names: <id_rsa>


############### REMOTE ###############
ssh root@<server_ip>

sh -c 'echo "set const" >> .nanorc'

sh -c 'echo "set tabsize 8" >> .nanorc'

sh -c 'echo "set tabstospaces" >> .nanorc'

#adduser <user>
adduser --disabled-password --gecos "" <user>

usermod -aG sudo <user>

cp .nanorc /home/<user>/

#su - <user>

#mkdir ~/.ssh

#chmod 700 ~/.ssh

mkdir /etc/ssh/<user>

chown -R <user>:<user> /etc/ssh/<user>

chmod 755 /etc/ssh/<user>

exit

############### LOCAL ###########

sh -c 'echo "<user>:<pwd>" > .credentials'

ssh-keygen -t rsa -N "" -f ~/.ssh/<id_rsa>

scp ~/.ssh/<id_rsa>.pub root@<server_ip>:/etc/ssh/<user>/authorized_keys

scp .credentials root@<server_ip>:/home/<user>/



############### REMOTE ###############

ssh root@<server_ip>

chmod 644 /etc/ssh/<user>/authorized_keys

sed -i -e '/^#AuthorizedKeysFile/s/^.*$/AuthorizedKeysFile \/etc\/ssh\/<user>\/authorized_keys/' /etc/ssh/sshd_config

sed -i -e '/^PermitRootLogin/s/^.*$/PermitRootLogin no/' /etc/ssh/sshd_config

sed -i -e '/^PasswordAuthentication/s/^.*$/PasswordAuthentication no/' /etc/ssh/sshd_config

sh -c 'echo "" >> /etc/ssh/sshd_config'

sh -c 'echo "" >> /etc/ssh/sshd_config'

sh -c 'echo "AllowUsers <user>" >> /etc/ssh/sshd_config'

systemctl reload sshd
 
cat /home/<user>/.credentials | chpasswd

rm /home/<user>/.credentials