from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
import numpy as np

def main():
    bot = InterbotixManipulatorXS(robot_model='px100',group_name='arm',gripper_name='gripper')

    bot.arm.go_to_home_pose()

    bot.arm.set_single_joint_position(joint_name='waist', position= (50*np.pi)/180, moving_time=2)

    bot.arm.set_single_joint_position(joint_name='shoulder', position=((30*np.pi)/180), moving_time=2)
    bot.gripper.grasp(2.0)

    bot.arm.set_single_joint_position(joint_name='shoulder', position=((-30*np.pi)/180))

    bot.arm.set_single_joint_position(joint_name='waist', position=((-50*np.pi)/180))

    bot.arm.set_single_joint_position(joint_name='shoulder', position=((30*np.pi)/180))
    bot.gripper.release(2.0)

    bot.arm.go_to_home_pose()
    bot.arm.go_to_sleep_pose()




if __name__ == '__main__':
    main()