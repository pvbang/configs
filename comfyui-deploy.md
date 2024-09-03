### Insstall
```bash
git clone https://github.com/BennyKok/comfyui-deploy
cd comfyui-deploy/web

# bun install
curl -fsSL https://bun.sh/install | bash
source /root/.bashrc

bun i

# download docker
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
apt-cache policy docker-ce
sudo apt install docker-ce
# sudo systemctl status docker
# sudo systemctl start docker
# sudo systemctl restart docker
# sudo systemctl enable docker

cp .env.example .env.local
openssl rand -hex 32

# copy code - Repace JWT_SECRET with openssl rand -hex 32
nano .env.local
### .env.local
# POSTGRES_URL="postgres://postgres:postgres@localhost:5432/verceldb"
# NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_ZmluZXItcGlnZW9uLTQxLmNsZXJrLmFjY291bnRzLmRldiQ
# CLERK_SECRET_KEY=sk_test_ncoHgHcHsYCmJLXHRWla6oTPVwkEZtCcGtpeXo3kel
# JWT_SECRET=a9edb005a00cd6e1944ea8d413a16062978c12cc7dca2cc8915fc9978875dc25

createdb -U postgres -h localhost -p 5432 verceldb   
### dropdb -U postgres -h localhost -p 5432 verceldb --force

sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

#
bun run generate
bun run migrate-local

# mở 2 terminal cho 2 lệnh
bun run db-dev
bun dev
```

### Fix err
```bash
sudo apt update
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
source ~/.bashrc
nvm install 21
nvm use 21
npm install -g npm@latest
npm install -g bun

sudo reboot

nvm use 21
npm update
bun update
bun i
```

### Install Postgresql
```bash
sudo apt-get update
sudo apt-get install postgresql-16 postgresql-client-16

sudo netstat -plnt | grep postgres

# change password postgres
sudo su -
nano /etc/postgresql/16/main/pg_hba.conf ### Tìm dòng bắt đầu với local và peer. Thay đổi peer thành trust: local all all trust
systemctl restart postgresql
ALTER USER postgres WITH PASSWORD 'postgres';
nano /etc/postgresql/16/main/pg_hba.conf ### Tìm dòng bắt đầu với local và trust. Thay đổi trust thành peer: local all all peer
systemctl restart postgresql

createdb -U postgres -h localhost -p 5432 verceldb   
### dropdb -U postgres -h localhost -p 5432 verceldb --force

nano .env.local
POSTGRES_URL="postgres://postgres:postgres@localhost:5432/verceldb"

# fix
npm install --save-dev @types/node@latest
```


