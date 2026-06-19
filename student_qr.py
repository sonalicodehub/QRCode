import qrcode

name = input("Enter Student Name: ")
roll_no = input("Enter Roll No: ")
course = input("Enter Course: ")

data = f"""
Student Name: {name}
Roll No: {roll_no}
Course: {course}
"""

qr = qrcode.make(data)

file_name = f"{roll_no}_student_qr.png"
qr.save(file_name)

print(f"QR Code generated successfully and saved as {file_name}")