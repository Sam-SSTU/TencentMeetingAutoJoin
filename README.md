# TencentMeetingAutoJoin-Describtion
根据星期几自入会（腾讯会议）。Auto join tencent meeting(VooV meeting) according to the day of week.


<a href="./readme/Englsih.md"><img alt="README in English" src="https://img.shields.io/badge/English-lightgrey"></a>
<a href="./readme/Chinese.md"><img alt="简体中文" src="https://img.shields.io/badge/简体中文-lightgrey"></a>

## License & Copyright

© 2020 <b>Sunil Aleti</b><br>
Licensed under <a href="https://github.com/aletisunil/Automating_Zoom/blob/master/LICENSE">MIT License</a>
Modified from:https://github.com/aletisunil/Automating_Zoom

## This repository is managed by:
<a href="https://github.com/Sam-SSTU/TencentMeetingAutoJoin/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Sam-SSTU/TencentMeetingAutoJoin" />
</a>

Made with [contrib.rocks](https://contrib.rocks).



Doesn't support password. Support mutiple time to join meeting



# Tencent meeting automation
A python script that automatically joins a tencent meeting based on your timetable.

## Prerequisites

Look at the code, enter the path
Install the libraries needed

## Behind the scenes

<ol>
<li>An infinite loop keeps checking the current time of the system using "datetime.now" funtion.</li>
<li>The zoom app is opened using "os.startfile()" funtion as soon as current time matches the time mentioned in "timings.xlsx".</li>
<li>"pyautogui.locateOnScreen()" function locates the image of join button on the screen and returns the position.</li>
<li>"pyautogui.moveTo()" moves the cursor to that location.</li>
<li>"pyautogui.click()" performs a click operation.</li>
<li>The meeting Id and Passcode are entered using the "pyautogui.write()" command.</li>
</ol>



Readme is still writing..
