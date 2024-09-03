# Prompts

## Positive
```sh
# Prompt chung
instagram photo, masterpiece, cinematic shot, beautiful face, a pair of soulful eyes that smile, {custom}, {camera},

{pose},
{place},
{photography} {style} of a {age} {ethnicity} {sex},

{body_type},
{hair_style}, {hair_color},
{eyes_style}, {eyes_color},
{nose},
{lip_shape}, {lip_color},
{beard_style}, {beard_color},
{custom_2}

<lora:{ethnicity} {sex} face>,
```

### Giá trị mặc định
```sh
custom = ""
camera = ""
pose = "front shot"
place = "clean background"
photography = "professional portrait"
style = "photo"
age = "20"
ethnicity = "Asian"
sex = "girl"
body_type = ""
hair_style = ""
hair_color = ""
eyes_style = ""
eyes_color = ""
nose = ""
lip_shape = ""
lip_color = ""
beard_style = ""
beard_color = ""
custom_2 = ""
```


### photography
```sh
# Professional Portrait
photography = "professional portrait"

# semi-portrait 
photography = "full body semi-portrait"
pose = "front shot, standing pose"

# Full body
photography = "full body"
pose = "front shot, standing pose"
custom_2 = "is wearing high heels,"    # mặc định / hoặc nếu sex là nữ
custom_2 = "is wearing Oxford shoes,"  # nếu sex là nam

# Ha
photography = "Ha"

# Digicam
photography = "Digicam"

# Fashion
photography = "Fashion"

# Long Exposure
photography = "Long Exposure"

# Mid Shot
photography = "Mid Shot"

# Old Photo
photography = "Old Photo"

# Street
photography = "Street"
```


### Camera
```sh
# Thay tên vô là được
camera = "taken by {tên camera} camera"

## Ví dụ: taken by Canon camera
```


### Style


### Age
```sh
# Dưới 12 tuổi => Trừ 4 so với số tuổi người dùng nhập
age = "(8 y.o:1.4)"  # Ví dụ người dùng nhập 12 tuổi thì còn 8 tuổi

# Trên 12 dưới 18 tuổi => Trừ 2 so với số tuổi người dùng nhập
age = "(12 y.o:1.2)"  # Ví dụ 14 tuổi thì còn 12 tuổi

# Trên 18 dưới 50 tuổi => Giữ nguyên 
age = "20 y.o"   # Ví dụ 20 tuổi

# Trên 50 tuổi => 
custom = "wrinkled skin, elderly woman,"
age = "50 y.o"   # Ví dụ 50 tuổi

semi-portrait 

```


## Negative
```sh
(nsfw, naked, nude, deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime, mutated hands and fingers:1.4), (deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, disconnected limbs, mutation, mutated, ugly, disgusting, amputation, embedding:FastNegativeV2, embedding:negative_hand-neg, 
```



https://5579.mekongai.io/images/Walking.png

https://5579.mekongai.io/images/Sitting-chair.png

https://5579.mekongai.io/images/Sitting.png

https://5579.mekongai.io/images/Over the Shoulder.png

https://5579.mekongai.io/images/Lying Down.png

https://5579.mekongai.io/images/Leaning.png

https://5579.mekongai.io/images/Kneeling.png

https://5579.mekongai.io/images/Jumping.png

https://5579.mekongai.io/images/Hands on Hips.png

https://5579.mekongai.io/images/Crossed Arms.png


https://5579.mekongai.io/images/Portrait.png

https://5579.mekongai.io/images/Half.png

https://5579.mekongai.io/images/Full.png
