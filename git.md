## Use Git

### Login git (đăng nhập lúc mới tải git, sau này không cần nữa)
```bash
git config --global user.name "abc"                   # abc là tên tài khoản git, cần vào github để tạo tài khoản trước
git config --global user.email abc@gmail.com          # email dùng để đăng ký tài khoản trên
```

### Create new repository (tạo dự án mới, trưởng dự án tạo)
```bash
git init
git add .
git commit -m "messenger"
git branch -M main
git remote add origin https://github.com/ilyouu/save-public.git       # <<link repository>>.git
git push -u origin main

# ví dụ
# ```
echo "# unity2d-game-sieu-anh-hung" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/pvbang/unity2d-game-sieu-anh-hung.git
git push -u origin main
# ```
```

### Clone repository (Lấy repository về máy)
```bash
git clone https://github.com/ilyouu/save-public.git       # <<link repository>>.git
```

### Create new branch (Tạo nhánh mới)
```bash
git checkout -b nhanh1      # nhanh1 là tên nhánh, thường đặt tên của bản thân hoặc tính năng mới, ví dụ feature/cat-class
# or
git branch nhanh1
```

### Kiểm tra nhánh
```bash
git branch
```

### Đi đến nhánh khác
```bash
git checkout nhanh1     # nhanh1 là tên nhánh muốn đến
```

### Gộp nhánh
```bash
git checkout main
git merge nhanh1        # gộp nhanh1 vào nhánh main, tức là lưu thay đổi từ nhanh1 vào main
```

### Xoá nhánh
```bash
git checkout -d nhanh1
```

### Xem vị trí hiện tại và các nhánh khác
```bash
git log --oneline
```

### Cập nhật code từ máy lên github
```bash
git add .
git commit -m "note"       # -m "..." nơi viết ghi chú về điều mình vừa thực hiện, ví dụ: git commit -m "Fix: missing eat function" 
git push                   # or: git push origin nhanh1
```
### Cập nhật code từ github về máy
```bash
git pull                   # or: git pull origin main
```

### Phục hồi code từ commit cuối
```bash
git restore .
```

### Phục hồi từ commit bất kỳ
```bash
git checkout 000000 -- .      # 000000 là mã commit, sau -- có thể chọn file muốn phục hồi
```


### Cách gộp các lệnh lại làm 1 cho nhanh và tiện lợi
```bash
# ví dụ muốn gộp 3 câu lệnh: 
# git add . 
# git commit -m "..."
# git push

git config --global core.editor "code --wait"
git config --global --edit
# dưới [alias] thêm dòng sau 
up = "!f() { git add . && git commit -m \"$1\" && git push; }; f"

# [user]
# 	name = pvbang
# 	email = pvbang23092002@gmail.com
# [core]
# 	editor = code --wait
# [alias]
# 	up = "!f() { git add . && git commit -m \"$1\" && git push; }; f"

# sau này nếu muốn push một commit lên git thì chỉ cần
git up "message"
```

### Git LFS (github chỉ cho phép upload file <100mb nên nếu cần up file >100mb thì dùng cái này)
```bash
# document
https://git-lfs.com/

# dùng
git lfs install
git lfs track "*.psd"
git add .gitattributes

# ví dụ config trong .gitattributes
*.psd filter=lfs diff=lfs merge=lfs -text
*.psb filter=lfs diff=lfs merge=lfs -text
*.so filter=lfs diff=lfs merge=lfs -text
*.dll filter=lfs diff=lfs merge=lfs -text
*.dylib filter=lfs diff=lfs merge=lfs -text
*.aar filter=lfs diff=lfs merge=lfs -text
Library/PackageCache/com.unity.burst@1.8.7/.Runtime/hostmac/dsymutil filter=lfs diff=lfs merge=lfs -text
*dsymutil filter=lfs diff=lfs merge=lfs -text
```

### Fix lỗi
```bash
# lỗi push khi file quá lớn (ví dụ ở dưới là 12GB)
# nên chia ra và push nhiều lần 
git config --global http.postBuffer 12000000000
git config --global https.postBuffer 12000000000
```


### Login in Linux
```bash
git config --global user.name "pvbang"                   
git config --global user.email pvbang23092002@gmail.com 
git config --list
git remote set-url origin https://<token>@github.com/<repo>
```


### Xóa commit cuối
```sh
git reset --soft HEAD~1
```
