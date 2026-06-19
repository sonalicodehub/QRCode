# 📱 Student QR Code Generator

A simple and efficient QR Code Generator built using Python. This application allows users to generate QR codes containing student information such as name, roll number, and course. The generated QR code is saved as a PNG image and can be scanned to quickly access the stored details.

## ✨ Features

* 👨‍🎓 Store student information in a QR code
* 📱 Generate scannable QR codes instantly
* 💾 Save QR codes as PNG images
* ⚡ Fast and lightweight application
* 🐍 Built entirely with Python
* 🎓 Beginner-friendly project

## 🎮 Application Workflow

| Step | Action                    |
| ---- | ------------------------- |
| 1    | Enter Student Name        |
| 2    | Enter Roll Number         |
| 3    | Enter Course Name         |
| 4    | Generate QR Code          |
| 5    | Save QR Code as PNG Image |

## 🛠 Tech Stack

* Python 3.x
* qrcode Library
* Pillow (PIL)

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sonalicodehub/student-qr-code-generator.git
cd student-qr-code-generator
```

### 2️⃣ Install Required Libraries

```bash
pip install qrcode[pil]
```

### 3️⃣ Verify Installation

```bash
python --version
```

## ▶️ Run the Application

```bash
python qr_generator.py
```

## 🤖 How the Application Works

1. The user enters student details.
2. The program stores the information in a formatted string.
3. A QR code is generated using the qrcode library.
4. The QR code is saved as a PNG image using the student's roll number as the filename.
5. The generated QR code can be scanned to retrieve student information instantly.

## 📂 Project Structure

```text
student-qr-code-generator/
│
├── qr_generator.py
├── README.md
└── generated_qr_codes/
```

## 📸 Sample Input

```text
Enter Student Name: Rahul Kumar
Enter Roll No: 101
Enter Course: BCA
```

## 📄 Sample QR Data

```text
Student Name: Rahul Kumar
Roll No: 101
Course: BCA
```

## 🌟 Future Enhancements

* 🎨 Custom QR Code Colors
* 🖼 Add Student Photo Support
* 📊 Bulk QR Code Generation
* 📱 GUI Version Using Tkinter
* ☁ Export Student Data to CSV
* 🔒 Password-Protected Student Records

## 📜 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Sonali Gupta**

Python Developer | Technology Enthusiast | Aspiring Software Engineer 🚀

GitHub: https://github.com/sonalicodehub
