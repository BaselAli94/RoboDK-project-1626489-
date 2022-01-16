


from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox

name_path = getOpenFile(r"C:\Users\alyaf\Desktop\myname.csv") #reading x, y &z from a csv file
name_list = LoadList(name_path) #storing the values in a matrix/list called (name_list)

RDK = Robolink()

robot = RDK.Item('',ITEM_TYPE_ROBOT)

home = RDK.Item('home') #Defining Home 
O_frame = RDK.Item('Object frame') #Defining a frame for the A4 object
start_eng = RDK.Item('Starting point')#Defining a tareget to start engraving
target_pose = start_eng.Pose()


robot.setPoseFrame(O_frame)


#Drawing the full name around the reference target
for i in range(len(name_list)):
    a = target_pose
    a.setPos(name_list[i])
    start_eng.setPose(a)
    
    if i == 0:
        robot.MoveJ(start_eng)
    else:
        robot.MoveL(start_eng)


        
        
#return back to home
robot.MoveJ(home)
