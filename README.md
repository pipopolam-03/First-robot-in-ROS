# First-robot-in-ROS
This is sequence of my small works from univercity. It's about how to make robot in ROS from scratch and how to make it do some simple actions. Also it tells about how to implement trust and reputation algorithm via nodes.

# First steps
The first thing that I've done was a simple robot model with four wheels (you can do it using primary shaoes like cilinders and rectangle) and added joints between parts of robot to make it able to move. To make it look more friendly, I added some textures.
![image](https://github.com/pipopolam-03/First-robot-in-ROS/assets/69760973/63f0e61c-99d8-44a3-9510-6e074e0b5965)
![image](https://github.com/pipopolam-03/First-robot-in-ROS/assets/69760973/cd386fcf-baeb-459d-849b-6ad790a57650)
![image](https://github.com/pipopolam-03/First-robot-in-ROS/assets/69760973/6f705baa-a961-46a2-8732-5589e6b929b5)


# Teleop twist keyboard
After making the model I built some barriers for robot and installed "Teleop twist keyboard" package to make robot move via keys. My model wasn't able to move because I made it in sdf format, but this package suit to urdf models, so I had to found someone's urdf robot. 
![image](https://github.com/pipopolam-03/First-robot-in-ROS/assets/69760973/7cdb2f24-33c5-4a4e-90e4-dac61f0c041b)
![image](https://github.com/pipopolam-03/First-robot-in-ROS/assets/69760973/12c2b4a4-5ad9-459b-8450-20744e7484f7)
![Готово-overpass2](https://github.com/pipopolam-03/First-robot-in-ROS/assets/69760973/c0cd97e9-cd41-45c9-839a-c017570055d5)


# Using python sctipts
I added package for scripts in project and wrote the first one to make robot move to given coordinates. 
![image](https://github.com/pipopolam-03/First-robot-in-ROS/assets/69760973/6fe53067-830a-41be-b489-3334665d48c1)


After this I used lidar from this snatched model and made some big fences. My goal was made robot feel these walls and bypass them. So, I started use lidar readings. The point of my algorithm is: check barrier, do 90deg rotation and a few steps, and return. After this check barriers again and do this cycle untill robot leave the barrier zone. After this it can continue move to coordinates. The code of this script is in the file.
![image](https://github.com/pipopolam-03/First-robot-in-ROS/assets/69760973/a0a94016-cda3-4395-92a3-0673ca5584a0)
![Объезд_1](https://github.com/pipopolam-03/First-robot-in-ROS/assets/69760973/bc5b69ac-9c96-4e8d-abfc-d2eb0e0b28b4)

The last thind I did is trust and reputation model. I added one big truck as a barrier and made three robots standing in front of it. Two of them tell the truth about the barrier and one is lying. So, the point is to calculate reputation of every robot to understand which of them you can trust. The scripts (for impostor and for normal robots) isn't too complicated. I transfered information between them via their nodes and compared readings from lidar for each from each. So, this is what i got.

![image](https://github.com/pipopolam-03/First-robot-in-ROS/assets/69760973/a2c2c6ef-4207-4fee-b5dd-529b2d5abdeb)


