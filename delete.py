import glob
import os
from plyer import notification  #this is the module of toast notification

folder_path = "../../ビデオ/test"  #Put the path of folder.
folder_list = folder_path.split("/")   #splitting folder's strings
folder = folder_list[len(folder_list)-1]  #picking last folder's strings

videos = glob.glob("{}/*".format(folder_path))  #picking all files of the folder
target = max(videos, key=os.path.getctime)  #getting the last created file using the key
os.remove(target)

notification.notify(
    title = "{}内の最新ファイルを削除しました。".format(folder),
    message = "削除されたファイル：{}".format(target),
    app_name = "Deleter",
    timeout = 5
)