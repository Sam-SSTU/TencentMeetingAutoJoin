import os
import pandas as pd
import pyautogui
import time
from datetime import datetime
from goto import with_goto
import sys
import os
import pyautogui
import time
import goto
from dominate.tags import label
import goto
from dominate.tags import label
import goto
from dominate.tags import label
from goto import with_goto
from goto import with_goto
import goto
from dominate.tags import label
from playsound import playsound
from goto import with_goto


def today1():
    global df,today
    today = datetime.now().weekday()
    
    if today ==0:
        df = pd.read_excel('timings.xlsx',index_col=False)
    elif today==1:
        df = pd.read_excel('timings1.xlsx',index_col=False)
    elif today==2:
        df = pd.read_excel('timings2.xlsx',index_col=False)
    elif today==3:
        df = pd.read_excel('timings3.xlsx',index_col=False)
        
    elif today==4:
        df = pd.read_excel('timings4.xlsx',index_col=False)
    else:
        df = pd.read_excel('timingsN.xlsx',index_col=False)




def mian():
    
    #To get current time
    now = datetime.now().strftime("%H:%M")
    
    if now in str(df['Timings']):
        today1()
        mylist=df["Timings"]
        mylist=[i.strftime("%H:%M") for i in mylist]
        c= [i for i in range(len(mylist)) if mylist[i]==now]
        row = df.loc[c] 
        meeting_id = str(row.iloc[0,1])  
        #password= str(row.iloc[0,2])  
        time.sleep(5)
        signIn(meeting_id)
        
        print('signed in')
        
        
        time.sleep(60)
        
        
    time.sleep(0.001)


        


def signIn(meeting_id):
    i=1
    if meeting_id=='114514':
        print('No Meeting Today')
        
    else:
        
        #Open's Zoom Application from the specified location
        os.startfile("D:\Program Files (x86)\Tencent\WeMeet\wemeetapp.exe")
        time.sleep(6)
        nojoin=pyautogui.locateCenterOnScreen("exit.png")
        if nojoin is not None:
            
            
            pyautogui.moveTo(nojoin)
            pyautogui.click()
            time.sleep(1)
        #Click's join button
        joinbtn=pyautogui.locateCenterOnScreen("joinameeting.png")
        pyautogui.moveTo(joinbtn)
        pyautogui.click()
        time.sleep(2)
        '''
        #Type the meeting id
        meetingidbtn=pyautogui.locateCenterOnScreen("meetingid.png")
        pyautogui.moveTo(meetingidbtn)
        pyautogui.write(meeting_id)
        time.sleep(2)
          '''
        '''
        #To turn of video and audio
        mediaBtn=pyautogui.locateAllOnScreen("media.png")
        for btn in mediaBtn:
            pyautogui.moveTo(btn)
            pyautogui.click()
            time.sleep(1)
            '''
        #To join
        nojoin=pyautogui.locateCenterOnScreen("exit.png")
        if nojoin is not None:
            
            
            pyautogui.moveTo(nojoin)
            pyautogui.click()
            time.sleep(1)
        pyautogui.write(meeting_id)
        time.sleep(1)
        join=pyautogui.locateCenterOnScreen("join.png")
        pyautogui.moveTo(join)
        pyautogui.click()
        time.sleep(1)
        join=pyautogui.locateCenterOnScreen("join.png")
        pyautogui.moveTo(join)
        
        pyautogui.click()
        playsound('succeessful.mp3')
        
        playsound('succeessful.mp3')
        
        playsound('succeessful.mp3')
        print('Join finished')

        '''
        #Enter's passcode to join meeting
        passcode=pyautogui.locateCenterOnScreen("meetingPasscode.png")
        pyautogui.moveTo(passcode)
        pyautogui.write(password)
        time.sleep(1)

        #Click's on join button
        joinmeeting=pyautogui.locateCenterOnScreen("joinmeeting.png")
        pyautogui.moveTo(joinmeeting)
        pyautogui.click()
        time.sleep(1)
        '''



today1()
while True:

    mian()
