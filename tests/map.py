import folium
from geopy.distance import geodesic

# Tạo bản đồ với tâm là vị trí của Homestay Nera Garden Apartment, sử dụng CartoDB Positron
m = folium.Map(location=[16.4611, 107.5957], zoom_start=14, tiles="CartoDB Positron")

# Địa điểm gốc (đầu tiên) và danh sách các địa điểm khác
locations = [
    {"name": "Nhà Kim Long", "coords": [16.471157, 107.559260], "color": "red", "icon": "home", "is_home": True},
    {"name": "Bệnh viện Quân y 268", "coords": [16.486699627171586, 107.57116033830026], "color": "green", "icon": "plus-square"},
    {"name": "Bến xe phía bắc Huế", "coords": [16.486023416836655, 107.54644925587682], "color": "blue", "icon": "bus"},
    {"name": "Trường trung cấp nghề Huế", "coords": [16.469959795108313, 107.5609183962034], "color": "orange", "icon": "graduation-cap"},
    {"name": "Trường tiểu học Kim Long", "coords": [16.469007364818463, 107.56120706416202], "color": "blue", "icon": "school"},
    {"name": "Chợ Kim Long", "coords": [16.466214345689842, 107.56022412929747], "color": "purple", "icon": "shopping-cart"},
    {"name": "UBND phường Kim Long", "coords": [16.46261473540789, 107.55687566155457], "color": "darkred", "icon": "building"},
    {"name": "Trường THCS Nguyễn Hoàng", "coords": [16.462622235404474, 107.555886134148], "color": "green", "icon": "school"}
]

# Lấy tọa độ của địa điểm đầu tiên
home_coords = locations[0]["coords"]

# Tính khoảng cách và thêm các điểm vào bản đồ
for location in locations:
    # Tính khoảng cách từ địa điểm đầu tiên đến các địa điểm còn lại
    if not location.get("is_home", False):  # Không tính khoảng cách cho địa điểm gốc
        distance = geodesic(home_coords, location["coords"]).kilometers
        label = f"{location['name']} (Cách {distance:.1f} Km)"
    else:
        label = location["name"]

    # Thay đổi icon và kích thước cho từng loại địa điểm
    if location.get("is_home", False):
        icon_size = (50, 50)
        font_size = "20pt"
        font_weight = "bold"
        background_color = "rgba(0, 51, 102, 0)"  # Màu trong suốt cho nhãn
        text_color = "red"
    else:
        icon_size = (20, 20)
        font_size = "12pt"
        font_weight = "bold"
        background_color = "rgba(255, 255, 255, 0)"  # Nền trong suốt
        text_color = location["color"]

    # Thêm marker với biểu tượng icon và màu sắc phù hợp
    folium.Marker(
        location=location["coords"],
        popup=label,
        icon=folium.Icon(color=location["color"], icon=location["icon"], prefix="fa")
    ).add_to(m)

    # Kiểm tra nếu là Trường THCS Nguyễn Hoàng để điều chỉnh vị trí nhãn
    if location["name"] == "UBND phường Kim Long":
        offset = (20, -30)  # Di chuyển nhãn xuống dưới xa hơn
    elif location["name"] == "Nhà Kim Long":
        offset = (-80, -80)
    elif location["name"] == "Trường trung cấp nghề Huế":
        offset = (20, 0)
    else:
        offset = (0, 0)

    # Thêm nhãn với font chữ và định dạng đẹp hơn, hiển thị cả khoảng cách
    folium.map.Marker(
        location=location["coords"],
        icon=folium.DivIcon(
            html=f"""<div style="font-size: {font_size}; color: {text_color}; font-family: Arial, sans-serif;
                     font-weight: {font_weight}; background-color: {background_color}; padding: 6px; 
                     border-radius: 5px; box-shadow: 0px 0px 3px rgba(0,0,0,0); white-space: nowrap;
                     transform: translate({offset[0]}px, {offset[1]}px);">
                     {label}
                     </div>"""
        )
    ).add_to(m)

# Lưu bản đồ dưới dạng file HTML
m.save("nha_kim_long.html")
