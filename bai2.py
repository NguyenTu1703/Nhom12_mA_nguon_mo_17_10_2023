import cv2
import numpy as np
import tkinter as tk
from tkinter import simpledialog
from matplotlib import pyplot as plt

# Hàm quay ảnh
def rotate_image(image, angle):
    center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)

# Tạo cửa sổ Tkinter để nhập góc quay
root = tk.Tk()
root.withdraw()

# Đọc ảnh và khởi tạo biến góc quay
img = cv2.imread('img.png', cv2.IMREAD_COLOR)
rotation_angle = 0.0

# Hiển thị ảnh ban đầu
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis('off')
plt.show()

# Nhập góc quay từ người dùng
rotation_angle = simpledialog.askfloat("Enter Rotation Angle", "Enter the rotation angle (in degrees):", parent=root)

if rotation_angle is not None:
    # Quay ảnh theo góc và hiển thị
    rotated_img = rotate_image(img, rotation_angle)
    plt.imshow(cv2.cvtColor(rotated_img, cv2.COLOR_BGR2RGB))
    plt.title(f"Rotated Image (Angle: {rotation_angle} degrees)")
    plt.axis('off')
    plt.show()
