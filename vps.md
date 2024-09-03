## Host server (linux):

### Truy cập server thông qua Password
```bash
ssh root@11.111.11.111      # host example 11.111.11.111
password123                 # password
```

### Truy cập server thông qua pem file
```bash
chmod 600 file.pem
ssh -i file.pem root@111.111.111.111        # host
```

### Cách duy trì host dù đã tắt terminal (screen)
```bash
# duy trì màn hình này, tắt cửa sổ thì lệnh vẫn chạy
screen

# xem tất cả screen
screen -ls

# xóa screen
screen -XS <session-id> quit

# bình thường dùng
screen -ls
screen -XS chatbot quit
screen -S chatbot
```

### Run server python trên host
```bash
# file fast api ở trong app.py 
uvicorn app:app --host 111.111.111.111 --port 1000
```

### Install Apache2
```bash
# link
https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-22-04

sudo apt update
sudo apt install apache2
sudo ufw allow 'Apache'

sudo nano /etc/apache2/sites-available/example.conf
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    ServerName example
    ServerAlias www.example
    DocumentRoot /var/www/html
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

sudo a2ensite example.conf
sudo a2dissite 000-default.conf
sudo apache2ctl configtest
sudo systemctl restart apache2
```

### Host server using apache2
```bash
# link
https://galaxyz.net/cach-su-dung-che-do-doc-lap-cua-certbot-de-lay-chung-chi-ssl-ma-hoa-tren-ubuntu-1604.3113.anews

# nhớ thay example.com thành tên domain

# cài certbot
sudo add-apt-repository ppa:certbot/certbot 
sudo apt-get update 
sudo apt-get install certbot

sudo ufw allow 80
sudo service apache2 stop

# nhận chứng chỉ
sudo certbot certonly --standalone --preferred-challenges http -d example.com 

# cấu hình trong nano /etc/apache2/sites-available/example.com.conf
<VirtualHost *:80>
    ServerAdmin webmaster@example.com
    ServerName example.com
    Redirect / https://example.com/
    ServerAlias www.example.com
    DocumentRoot /var/www/html
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

<VirtualHost *:443>
   ServerName example.com
   DocumentRoot /var/www/html

   SSLEngine on
   SSLCertificateFile /etc/letsencrypt/live/example.com/fullchain.pem
   SSLCertificateKeyFile /etc/letsencrypt/live/example.com/privkey.pem
</VirtualHost>

# kích hoạt cấu hình example.conf
sudo a2ensite example.conf
sudo a2dissite 000-default.conf

# reset apache2
sudo systemctl restart apache2

# bước cuối cùng: cầu nguyện cho nó không gặp lỗi nào :v
```


### Renew (Let's Encrypt certificate expiration notice for domain)
```bash
sudo systemctl stop apache2
sudo certbot renew

# check
sudo certbot renew --dry-run
```


### Cấu hình cho python
```bash
# ví dụ cấu hình python
screen -ls
screen -XS chatbot quit
screen -S chatbot
cd mekongai-chatbot/
pip install -r requirements.txt
uvicorn app:app --host 45.90.108.32 --port 1002


# nano /etc/apache2/sites-available/example.com.conf
<VirtualHost *:80>
    ServerAdmin webmaster@example.com
    ServerName example.com
    Redirect / https://example.com/
    ServerAlias www.example.com
    DocumentRoot /var/www/html
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

<VirtualHost *:443>
   ServerName example.com
   DocumentRoot /var/www/html

   SSLEngine on
   SSLCertificateFile /etc/letsencrypt/live/example.com/fullchain.pem
   SSLCertificateKeyFile /etc/letsencrypt/live/example.com/privkey.pem     
   
   ProxyPass /mekongai-chatbot/ http://45.90.108.32:1002/
   ProxyPassReverse /mekongai-chatbot/ http://45.90.108.32:1002/
</VirtualHost>

#
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo systemctl restart apache2
```


### Nvidia
```bash
sudo add-apt-repository ppa:graphics-drivers/ppa
ubuntu-drivers devices
sudo ubuntu-drivers autoinstall
sudo reboot
```

### Permission denied 
```bash
sudo chown -R ubuntu.ubuntu /folder-name
```

### AWS
```bash
https://stackoverflow.com/questions/57765350/how-to-copy-multiple-file-from-local-to-s3

# local to aws
aws s3 cp C:\pvbang s3://therhome-video --recursive

# aws to local
aws s3 cp s3://therhome-video C:\pvbang --recursive     ## aws s3 cp s3://therhome-video/models /tmp2/pvbang/ComfyUI/models --recursive
```


### Tạo remote desktop cho vps
```bash
sudo apt update
sudo apt install ubuntu-desktop -y
sudo apt install xrdp -y
sudo adduser xrdp ssl-cert

sudo systemctl restart xrdp
sudo passwd ubuntu
sudo reboot
```

### Mở rộng disk
```bash
df -h
lsblk

# xem ổ nào đang dư
sudo growpart /dev/xvda 1
sudo resize2fs /dev/xvda1
```

### Zip
```bash
sudo apt-get update
sudo apt-get install zip

zip -r tên_tệp.zip tên_thư_mục
```


### Unzip
```bash
# Cài đặt unzip trên Ubuntu/Debian
sudo apt-get update
sudo apt-get install unzip

# Giải nén tệp zip vào thư mục hiện tại
unzip file.zip
```


### GPU
```bash
# chỉ xem GPU đang được sử dụng trên linux
watch -n 1 nvidia-smi --format=csv,noheader,nounits --query-gpu=index,name,utilization.gpu

# fix nvidia-smi
# kill hết
nvidia-smi | grep 'python' | awk '{ print $5 }' | xargs -n1 kill -9
# kill một gpu chỉ định
nvidia-smi -i <id_gpu> | grep 'python' | awk '{ print $5 }' | xargs -n1 kill -9
```
