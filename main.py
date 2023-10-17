import cv2
import matplotlib.pyplot as plt

# Định nghĩa hàm xử lý sự kiện khi click chuột vào ảnh
def on_click(event):
    global current_scale
    if event.inaxes:
        ax = event.inaxes
        if event.button == 'up':
            # Phó to ảnh khi cuộn lên
            current_scale *= 1.1
        elif event.button == 'down':
            # Thu nhỏ ảnh khi cuộn xuống
            current_scale /= 1.1
        # Hiển thị ảnh với tỷ lệ mới
        ax.images[0].set_data(cv2.resize(img, dsize=None, fx=current_scale, fy=current_scale))

        ax.set_title(f'Scale: {current_scale:.2f}')
        plt.draw()

img = cv2.imread('img.png', cv2.IMREAD_COLOR)  # Đọc ảnh full màu

current_scale = 1.0  # Tỷ lệ ban đầu

half = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)
bigger = cv2.resize(img, (1050, 1610))
stretch_near = cv2.resize(img, (780, 540), interpolation=cv2.INTER_LINEAR)

Titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]
images = [img, half, bigger, stretch_near]
count = 4

for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  # Chuyển đổi BGR sang RGB
    plt.axis('off')  # Tắt trục

# Đăng ký sự kiện click chuột
plt.connect('button_press_event', on_click)

plt.show()
