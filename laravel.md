### Install laravel:
```bash
composer create-project laravel/laravel name-project-laravel --prefer-dist
cp .env.example .env
composer update
php artisan key:generate
```

### Start laravel:
```
php artisan serve
```

### Authentication laravel 8:
```
php artisan migrate
composer require laravel/jetstream
php artisan jetstream:install livewire
npm install
npm run dev
php artisan migrate:fresh
```

### Check version:
```
php artisan -v
```

### Database:
```
php artisan config:cache
```

### Migration:
```bash
php artisan migrate		# up
php artisan migrate:rollback	# down
php artisan migrate:fresh
php artisan migrate:fresh --seed
```

### Create migration:
```
php artisan make:migration create_name_table
```

### Create model:
```
php artisan make:model Name
```

### Create controller:
```bash
php artisan make:controller NameController 
# php artisan make:controller NameController --resource
```

### Create Seeder:
```
php artisan make:seeder NameSeeder 
```

### Clone project:
```bash
git clone ...
composer install	
# or: composer install --ignore-platform-reqs
# or: composer update 
# or: composer update --ignore-platform-reqs 
npm install
npm run dev
cp .env.example .env
# create database
php artisan storage:link
php artisan migrate
php artisan key:generate
php artisan db:seed
php artisan serve
```
	
### Multiple Project:
```bash
php artisan serve --port=8080
# php artisan serve --port=...
```
