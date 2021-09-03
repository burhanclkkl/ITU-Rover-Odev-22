#!/usr/bin/env python

import rospy
from std_msgs.msg import String

# Alt Yurur Sistem 18 char
def callback(data):
    print(data.data)
    
    input = str(data.data)
    new_input = input[1:-1]
    
    x = new_input[0:4]
    y = new_input[4:8]
    z = new_input[8:12]
    t = new_input[12:16]

    ### x ###
    if x[0] == "0" :
        x1 = x[1:4]
        x2 =("-%s" % x1)   
        x2 = int(x2)
        
        if x2 < -255 : 
            son_x2 = -255  
        elif x2 > -100 and x2 <= -10:
            x2 = str(x2)
            x2 = x2[1:]
            x2 = "0" + str(x2)
            son_x2 = ("-%s" % x2)
        elif x2 > -10:
            x2 = str(x2)
            x2 = x2[1:]
            x2 = "00" + str(x2)
            son_x2 = ("-%s" % x2)
        elif x2 == 0:
            x2 = str(x2)
            x2 = x2[1:]
            x2 = "000" + str(x2)
            son_x2 = ("-%s" % x2)
        else:
          son_x2 = ("%s" % x2)
            
    if x[0] == "1" :
        x1 = x[1:4]
        x2 =x1
        x2 = int(x2)
        if x2 > 255 : 
             x2 = 255   
        elif x2 < 100 and x2 >= 10:
            x2 = "0" + str(x2)
        elif x2 < 10:
            x2 = "00" + str(x2)
        elif x == 0:
            x2 = "000" + str(x2)
        son_x2 = ("+%s" % x2)
    ### x ###
    
    ### y ###
    if y[0] == "0" :
        y1 = y[1:4]
        y2 =("-%s" % y1)   
        y2 = int(y2)
        
        if y2 < -255 : 
            son_y2 = -255  
        elif y2 > -100 and y2 <= -10:
            y2 = str(y2)
            y2 = y2[1:]
            y2 = "0" + str(y2)
            son_y2 = ("-%s" % y2)
        elif y2 > -10:
            y2 = str(y2)
            y2 = y2[1:]
            y2 = "00" + str(y2)
            son_y2 = ("-%s" % y2)
        elif y2 == 0:
            y2 = str(y2)
            y2 = y2[1:]
            y2 = "000" + str(y2)
            son_y2 = ("-%s" % y2)
        else:
          son_y2 = ("%s" % y2)
            
    if y[0] == "1" :
        y1 = y[1:4]
        y2 =y1
        y2 = int(y2)
        if y2 > 255 : 
             y2 = 255   
        elif y2 < 100 and y2 >= 10:
            y2 = "0" + str(y2)
        elif y2 < 10:
            y2 = "00" + str(y2)
        elif y == 0:
            y2 = "000" + str(y2)
        son_y2 = ("+%s" % y2)
    ### y ###
    
    ### z ###
    if z[0] == "0" :
        z1 = z[1:4]
        z2 =("-%s" % z1)   
        z2 = int(z2)
        
        if z2 < -255 : 
            son_z2 = -255  
        elif z2 > -100 and z2 <= -10:
            z2 = str(z2)
            z2 = z2[1:]
            z2 = "0" + str(z2)
            son_z2 = ("-%s" % z2)
        elif z2 > -10:
            z2 = str(z2)
            z2 = z2[1:]
            z2 = "00" + str(z2)
            son_z2 = ("-%s" % z2)
        elif z2 == 0:
            z2 = str(z2)
            z2 = z2[1:]
            z2 = "000" + str(z2)
            son_z2 = ("-%s" % z2)
        else:
          son_z2 = ("%s" % z2)
            
    if z[0] == "1" :
        z1 = z[1:4]
        z2 =z1
        z2 = int(z2)
        if z2 > 255 : 
             z2 = 255   
        elif z2 < 100 and z2 >= 10:
            z2 = "0" + str(z2)
        elif z2 < 10:
            z2 = "00" + str(z2)
        elif z == 0:
            z2 = "000" + str(z2)
        son_z2 = ("+%s" % z2)
    ### z ###
    
    ### t ###
    if t[0] == "0" :
        t1 = t[1:4]
        t2 =("-%s" % t1)   
        t2 = int(t2)
        
        if t2 < -255 : 
            son_t2 = -255  
        elif t2 > -100 and t2 <= -10:
            t2 = str(t2)
            t2 = t2[1:]
            t2 = "0" + str(t2)
            son_t2 = ("-%s" % t2)
        elif t2 > -10:
            t2 = str(t2)
            t2 = t2[1:]
            t2 = "00" + str(t2)
            son_t2 = ("-%s" % t2)
        elif t2 == 0:
            t2 = str(t2)
            t2 = t2[1:]
            t2 = "000" + str(t2)
            son_t2 = ("-%s" % t2)
        else:
          son_t2 = ("%s" % t2)
            
    if t[0] == "1" :
        t1 = t[1:4]
        t2 =t1
        t2 = int(t2)
        if t2 > 255 : 
             t2 = 255   
        elif t2 < 100 and t2 >= 10:
            t2 = "0" + str(t2)
        elif t2 < 10:
            t2 = "00" + str(t2)
        elif t == 0:
            t2 = "000" + str(t2)
        son_t2 = ("+%s" % t2)
    ### t ###
    
    output = str("{} {} {} {}"  .format(str(son_x2), str(son_y2), str(son_z2), str(son_t2))) 
    print(output)
    
    pub1 = rospy.Publisher('position/drive', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub1.publish(output)
        input = 0
        rate.sleep()
        break 
    
# Robotic Arm 26 char   
def callback2(data):
    print(data.data)
    
    input = str(data.data)
    new_input = input[1:-1]

    x = new_input[0:4]
    y = new_input[4:8]
    z = new_input[8:12]
    t = new_input[12:16]
    k = new_input[16:20]
    l = new_input[20:24]
    
    ### x ###
    if x[0] == "0" :
        x1 = x[1:4]
        x2 =("-%s" % x1)   
        x2 = int(x2)
        
        if x2 < -255 : 
            son_x2 = -255  
        elif x2 > -100 and x2 <= -10:
            x2 = str(x2)
            x2 = x2[1:]
            x2 = "0" + str(x2)
            son_x2 = ("-%s" % x2)
        elif x2 > -10:
            x2 = str(x2)
            x2 = x2[1:]
            x2 = "00" + str(x2)
            son_x2 = ("-%s" % x2)
        elif x2 == 0:
            x2 = str(x2)
            x2 = x2[1:]
            x2 = "000" + str(x2)
            son_x2 = ("-%s" % x2)
        else:
          son_x2 = ("%s" % x2)
            
    if x[0] == "1" :
        x1 = x[1:4]
        x2 =x1
        x2 = int(x2)
        if x2 > 255 : 
             x2 = 255   
        elif x2 < 100 and x2 >= 10:
            x2 = "0" + str(x2)
        elif x2 < 10:
            x2 = "00" + str(x2)
        elif x == 0:
            x2 = "000" + str(x2)
        son_x2 = ("+%s" % x2)
    ### x ###
    
    ### y ###
    if y[0] == "0" :
        y1 = y[1:4]
        y2 =("-%s" % y1)   
        y2 = int(y2)
        
        if y2 < -255 : 
            son_y2 = -255  
        elif y2 > -100 and y2 <= -10:
            y2 = str(y2)
            y2 = y2[1:]
            y2 = "0" + str(y2)
            son_y2 = ("-%s" % y2)
        elif y2 > -10:
            y2 = str(y2)
            y2 = y2[1:]
            y2 = "00" + str(y2)
            son_y2 = ("-%s" % y2)
        elif y2 == 0:
            y2 = str(y2)
            y2 = y2[1:]
            y2 = "000" + str(y2)
            son_y2 = ("-%s" % y2)
        else:
          son_y2 = ("%s" % y2)
            
    if y[0] == "1" :
        y1 = y[1:4]
        y2 =y1
        y2 = int(y2)
        if y2 > 255 : 
             y2 = 255   
        elif y2 < 100 and y2 >= 10:
            y2 = "0" + str(y2)
        elif y2 < 10:
            y2 = "00" + str(y2)
        elif y == 0:
            y2 = "000" + str(y2)
        son_y2 = ("+%s" % y2)
    ### y ###
    
    ### z ###
    if z[0] == "0" :
        z1 = z[1:4]
        z2 =("-%s" % z1)   
        z2 = int(z2)
        
        if z2 < -255 : 
            son_z2 = -255  
        elif z2 > -100 and z2 <= -10:
            z2 = str(z2)
            z2 = z2[1:]
            z2 = "0" + str(z2)
            son_z2 = ("-%s" % z2)
        elif z2 > -10:
            z2 = str(z2)
            z2 = z2[1:]
            z2 = "00" + str(z2)
            son_z2 = ("-%s" % z2)
        elif z2 == 0:
            z2 = str(z2)
            z2 = z2[1:]
            z2 = "000" + str(z2)
            son_z2 = ("-%s" % z2)
        else:
          son_z2 = ("%s" % z2)
            
    if z[0] == "1" :
        z1 = z[1:4]
        z2 =z1
        z2 = int(z2)
        if z2 > 255 : 
             z2 = 255   
        elif z2 < 100 and z2 >= 10:
            z2 = "0" + str(z2)
        elif z2 < 10:
            z2 = "00" + str(z2)
        elif z == 0:
            z2 = "000" + str(z2)
        son_z2 = ("+%s" % z2)
    ### z ###
    
    ### t ###
    if t[0] == "0" :
        t1 = t[1:4]
        t2 =("-%s" % t1)   
        t2 = int(t2)
        
        if t2 < -255 : 
            son_t2 = -255  
        elif t2 > -100 and t2 <= -10:
            t2 = str(t2)
            t2 = t2[1:]
            t2 = "0" + str(t2)
            son_t2 = ("-%s" % t2)
        elif t2 > -10:
            t2 = str(t2)
            t2 = t2[1:]
            t2 = "00" + str(t2)
            son_t2 = ("-%s" % t2)
        elif t2 == 0:
            t2 = str(t2)
            t2 = t2[1:]
            t2 = "000" + str(t2)
            son_t2 = ("-%s" % t2)
        else:
          son_t2 = ("%s" % t2)
            
    if t[0] == "1" :
        t1 = t[1:4]
        t2 =t1
        t2 = int(t2)
        if t2 > 255 : 
             t2 = 255   
        elif t2 < 100 and t2 >= 10:
            t2 = "0" + str(t2)
        elif t2 < 10:
            t2 = "00" + str(t2)
        elif t == 0:
            t2 = "000" + str(t2)
        son_t2 = ("+%s" % t2)
    ### t ###

    ### k ###
    if k[0] == "0" :
        k1 = k[1:4]
        k2 =("-%s" % k1)   
        k2 = int(k2)
        
        if k2 < -255 : 
            son_k2 = -255  
        elif k2 > -100 and k2 <= -10:
            k2 = str(k2)
            k2 = k2[1:]
            k2 = "0" + str(k2)
            son_k2 = ("-%s" % k2)
        elif k2 > -10:
            k2 = str(k2)
            k2 = k2[1:]
            k2 = "00" + str(k2)
            son_k2 = ("-%s" % k2)
        elif k2 == 0:
            k2 = str(k2)
            k2 = k2[1:]
            k2 = "000" + str(k2)
            son_k2 = ("-%s" % k2)
        else:
          son_k2 = ("%s" % k2)
            
    if k[0] == "1" :
        k1 = k[1:4]
        k2 =k1
        k2 = int(k2)
        if k2 > 255 : 
             k2 = 255   
        elif k2 < 100 and k2 >= 10:
            k2 = "0" + str(k2)
        elif k2 < 10:
            k2 = "00" + str(k2)
        elif k == 0:
            k2 = "000" + str(k2)
        son_k2 = ("+%s" % k2)
    ### k ###

    ### l ###
    if l[0] == "0" :
        l1 = l[1:4]
        l2 =("-%s" % l1)   
        l2 = int(l2)
        
        if l2 < -255 : 
            son_l2 = -255  
        elif l2 > -100 and l2 <= -10:
            l2 = str(l2)
            l2 = l2[1:]
            l2 = "0" + str(l2)
            son_l2 = ("-%s" % l2)
        elif l2 > -10:
            l2 = str(l2)
            l2 = l2[1:]
            l2 = "00" + str(l2)
            son_l2 = ("-%s" % l2)
        elif l2 == 0:
            l2 = str(l2)
            l2 = l2[1:]
            l2 = "000" + str(l2)
            son_l2 = ("-%s" % l2)
        else:
          son_l2 = ("%s" % l2)
            
    if l[0] == "1" :
        l1 = l[1:4]
        l2 =l1
        l2 = int(l2)
        if l2 > 255 : 
             l2 = 255   
        elif l2 < 100 and l2 >= 10:
            l2 = "0" + str(l2)
        elif l2 < 10:
            l2 = "00" + str(l2)
        elif l == 0:
            l2 = "000" + str(l2)
        son_l2 = ("+%s" % l2)
    ### l ###
    output2 = str("{} {} {} {} {} {}"  .format(str(son_x2), str(son_y2), str(son_z2), str(son_t2), str(son_k2), str(son_l2)))
    print(output2)

    pub = rospy.Publisher('position/robotic_arm', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(output2)
        input = 0
        rate.sleep()
        break

def listener():
    rospy.init_node('encoder_pub_node', anonymous=True)
    # Alt Yurur Sistem 18 char
    rospy.Subscriber("/serial/drive", String, callback) 
    # Robotic kol 26 char 
    rospy.Subscriber("/serial/robotic_arm", String, callback2) 
    rospy.spin()

if __name__ == '__main__':
    listener()
