# Project Deployment and Usage Instructions

Note: Tencent meeting = VooV meeting, I'll just use tencent meeting below.

## 1. Deployment Steps

### 1.1 Clone the Project Locally

First, clone the project to your local machine. You can use the following command:

    git clone 

Or just download it from github.

### 1.2 Install Dependencies


`requirements.txt` file is not provided, manually install the following libraries:

    pip install pandas pyautogui dominate playsound

### 1.3 Modify Tencent Meeting Path

The script uses hardcoded paths to start the Tencent Meeting application. You need to modify this path according to your local installation. In the `signIn` function of the script, locate the following code:

    os.startfile("D:\Program Files (x86)\Tencent\WeMeet\wemeetapp.exe")

Replace the path with the actual path to your Tencent Meeting application.

### 1.4 Modify Excel Time and Meeting ID

The script relies on an Excel file to obtain meeting times and IDs. Modify the corresponding Excel file(s) (e.g., `timings.xlsx`, `timings1.xlsx`, etc.) according to your actual meeting schedule to ensure that the time and meeting ID are accurate. If your meetings are recurring, update the correct Excel file based on the day of the week.

## 2. Usage Instructions

Once you have completed the above steps, you can run the script in the command line (cmd) with the following command:

    python mian.py

The script will automatically match the current time with the meeting times in the Excel file and will launch Tencent Meeting to log in automatically.

### 2.1 How to Exit Meeting

The exit functionality was not written into the script. Instead, a scheduled task runs a `.cmd` script can execute the meeting. If you need to use this, you will need to modify the Tencent Meeting path in the `.cmd` file.

I use the following timer scripts: [52pojie.cn](https://www.52pojie.cn/thread-716138-1-1.html) or [onlinedown.net](https://www.onlinedown.net/soft/1217136.htm)

## 3. Known Issues / Future Updates

Tencent Meeting has been updated several times, so the click logic and reference images in this script may change due to these updates. If the script does not work correctly, please check and update the reference images or adjust the click logic.

Currently, the script does not support entering a meeting password automatically, as there has been no need for a password in my meetings. If you require this feature, you can uncomment the relevant code and make the necessary adjustments.

If you encounter any issues during usage or have feature requests, feel free to open an `Issue` or `PR` in the project's GitHub repository. We will follow up and improve the script promptly.