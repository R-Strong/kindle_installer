#welcome to my horrible script to install multiple apps to android based devices
#curently the script uses adb+ in order to install to multiple devices at once
#adb+ must be in the same directory as this script
#you must also have a folder called "apk" within the same directory as this script
#this folder should contain all the apps that you wish to install


import os
import time
import subprocess

#assert (os.path.isfile('adb+.bat')), "you must have the adb+ script in the same directory as this script in order for it to work"
assert (os.path.isdir('apk')), "you must have a folder containing your apps named \"apk\" in the same directory as this script"
#creates a list of apps to install

apkList = os.listdir('apk')



print("app list created, apps to be installed are\n")
print(apkList)

#creates a variable that is the number of apps to be installed
appCount=len(apkList)

print("total app count is - "+str(appCount))


print("Starting ADB")
#starts adb
os.system('adb kill-server')
os.system('adb start-server')
time.sleep(5)
print('you should have a prompt on all your devices that asks that you allow a device access to developer settings\nplease ensure that you have pressed \"ok\" or \"allow\" on all devices\n\n')
input('once you have pressed ok on all devices, press ENTER to continue\n\n')

#this is an effing mess, but it works to get the device IDs
os.system('adb devices > support/devList.txt')
devListUnfiltered=[""]
devListUnfiltered = open('support/devList.txt','r',encoding='utf8').readlines()
del devListUnfiltered[0]
#print(devListUnfiltered[0])
devList=[""]
tick=0
#print(str(len(devListUnfiltered)) + " lines")                #debug lines, left for later
#print(devListUnfiltered)
while tick < (len(devListUnfiltered)-1):
    devList.append(devListUnfiltered[tick][0:16])
    #print(str(tick) + "tick")
    tick+=1
    #print(devList[tick])

del devList[0]
#print(devList)
    
print("you have " + str(len(devList)) + " devices ready for apps, installing apps now/n/n")


doneCount=0

while doneCount<appCount:
    devNum=0
    while devNum < len(devList)
        print('installing app ' + apkList[doneCount] + 'on device' + devList[devNum])
        os.system('adb install /apk/' + apkList[doneCount] +' ' + devList[devNum])
        devNum+=1
    doneCount=doneCount+1
    print("Apps installed " + str(doneCount))
print("completed, " + str(appCount) + " apps installed on your devices")
print("please review the installation process to ensure that there were no failures.")




##############################################################################################################
