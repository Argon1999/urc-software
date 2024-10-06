from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("walli_arm_v2_block", package_name="walli_arm_v2_block_moveit_config").to_moveit_configs()
    return generate_demo_launch(moveit_config)