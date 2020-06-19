# blog-pwsz

Linux Debian 9

----------------Instalacja pythona------------------
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev curl libbz2-dev
curl -O https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz
tar -xf Python-3.7.3.tar.xz
cd Python-3.7.3
./configure --enable-optimizations
make -j 8
sudo make altinstall
python3.7 --version
-----------------------------------------------------
---------------------Instalacja pip-------------------
sudo apt update
sudo apt install python3-pip
pip3 --version

-------------Dodatki----------------------------------
pip3 install flask
pip3 install flask-login
pip3 install flask-sqlalchemy

cp appflask

--------------------------------------------
run.sh
flask run
--------------------------------------------
nano etc/systemd/python-blog-service.service
--------------------------------------------
[Unit]
Description=KZ PWSZ Blog
After=network.target

[Service]
WorkingDirectory=/home/zientek/aplikacjaflask
ExecStart = /bin/bash run.sh
Restart=always

[Install]
WantedBy=multi-user.target
--------------------------------------------

sudo systemctl daemon-reload
systemctl start python-blog-service.service

chown root /home/zientek/aplikacjaflask/myapp.py
chmod +x /home/zientek/aplikacjaflask/myapp.py
