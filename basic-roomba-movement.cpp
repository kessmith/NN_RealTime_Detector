#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "ca_msgs/Bumper.h"
#include "sensor_msgs/Joy.h"
#include <sstream>
#include "std_msgs/Int32.h"

int move = 0;
int color = 0;

geometry_msgs::Twist msg;

ros::Publisher pub;

int main(int argc, char **argv)

{

    ros::init(argc, argv, "example1_a");

    ros::NodeHandle n;

    pub = n.advertise<geometry_msgs::Twist>("cmd_vel", 1);

    ros::Rate loop_rate(10);

    while (ros::ok())

    {

        for (int i = 0; i < 8; i++)
        {
            if (i == 0)
            {
                msg.linear.x = 1;
                msg.angular.z = 0;
                pub.publish(msg);
                ros::spinOnce();
                loop_rate.sleep();
            }
            else if (i == 1)
            {
                msg.linear.x = 0;
                msg.angular.z = -1 pub.publish(msg);
                ros::spinOnce();
                loop_rate.sleep();
            }
            else if (i == 2)
            {
                msg.linear.x = 1;
                msg.angular.z = 0;
                pub.publish(msg);
                ros::spinOnce();
                loop_rate.sleep();
            }
            else if (i == 3)
            {
                msg.linear.x = 0;
                msg.angular.z = -1;
                pub.publish(msg);
                ros::spinOnce();
                loop_rate.sleep();
            }
        }
        /*
        if(move==0){

        msg.linear.x=1;

        msg.angular.z=0;

        pub.publish(msg);

        ros::spinOnce();

        loop_rate.sleep();

        ROS_INFO("move= [%d]", move);

        }

        if(move==1){

        for(int i=0;i<2;i++){

        msg.linear.x=0;

        msg.angular.z=-1;

        pub.publish(msg);

        ros::spinOnce();

        loop_rate.sleep();

        ros::Duration(2).sleep();

        ROS_INFO("move= [%d]", move);

        move=0;}

        }

        if(move==2){

        for(int i=0;i<2;i++){

        msg.linear.x=0;

        msg.angular.z=1;

        pub.publish(msg);

        ros::spinOnce();

        loop_rate.sleep();

        ros::Duration(2).sleep();

        move=0;}

        }
        /*
        if (color==1){
        msg.linear.x=0;
        msg.angular.z=0;
        pub.publish(msg);
        ros::spinOnce();
        loop_rate.sleep();
        ros::Duration(2).sleep();
        color=0;
        ROS_INFO("color= [%d]", color);

        }
        if (color==2){
        msg.linear.x=0;
        msg.angular.z=1;
        pub.publish(msg);
        ros::spinOnce();
        loop_rate.sleep();
        ros::Duration(2).sleep();
        color=0;
        ROS_INFO("color= [%d]", color);
        }
        if (color==3){
        msg.linear.x=1;
        msg.angular.z=0;
        pub.publish(msg);
        ros::spinOnce();
        loop_rate.sleep();
        color=0;
        ROS_INFO("color= [%d]", color);
        }
        */
    }
    return 0;
}
