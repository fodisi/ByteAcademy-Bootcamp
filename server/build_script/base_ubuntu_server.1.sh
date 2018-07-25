

# Server IP: 159.65.76.223
# Server Admin User: odisi
# Server Admin Password: abcdef123456.
# SSH Key Pair File Names: test_rsa


############### REMOTE ###############
ssh root@159.65.76.223

sh -c 'echo "set const" >> .nanorc'

sh -c 'echo "set tabsize 8" >> .nanorc'

sh -c 'echo "set tabstospaces" >> .nanorc'

adduser odisi --gecos "" odisi
#adduser --disabled-password --gecos "" odisi

usermod -aG sudo odisi

cp .nanorc /home/odisi/

#su - odisi

#mkdir ~/.ssh

#chmod 700 ~/.ssh

mkdir /etc/ssh/odisi

chown -R odisi:odisi /etc/ssh/odisi

chmod 755 /etc/ssh/odisi

exit

############### LOCAL ###########

sh -c 'echo "odisi:abcdef123456." > .credentials'

ssh-keygen -t rsa -N "" -f ~/.ssh/test_rsa

scp ~/.ssh/test_rsa.pub root@159.65.76.223:/etc/ssh/odisi/authorized_keys

scp .credentials root@159.65.76.223:/home/odisi/



############### REMOTE ###############

ssh root@159.65.76.223

chmod 644 /etc/ssh/odisi/authorized_keys

sed -i -e '/^#AuthorizedKeysFile/s/^.*$/AuthorizedKeysFile \/etc\/ssh\/odisi\/authorized_keys/' /etc/ssh/sshd_config

#sed -i -e '/^PermitRootLogin/s/^.*$/PermitRootLogin no/' /etc/ssh/sshd_config

sed -i -e '/^PasswordAuthentication/s/^.*$/PasswordAuthentication no/' /etc/ssh/sshd_config

sh -c 'echo "" >> /etc/ssh/sshd_config'

sh -c 'echo "" >> /etc/ssh/sshd_config'

sh -c 'echo "AllowUsers odisi" >> /etc/ssh/sshd_config'

sudo systemctl reload sshd
 
cat /home/odisi/.credentials | chpasswd

rm /home/odisi/.credentials




"sic transit gloria mundi"

Server


apt-get -y install firewalld
systemctl status firewalld

firewall-cmd --list-all

hostname -I >> gets the IP

firewall-cmd --add-port=80/tcp --permanent
firewall-cmd --add-port=5000/tcp --permanent

systemctl reload firewalld

install python, pip, flask, sqlite3


#upload and moderation picture with flask and python

socket private interface
port public interface

sudo reboot

