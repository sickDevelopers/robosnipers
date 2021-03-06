
TARGET_COLLISION_GROUP = 10

## AGENT

AGENT_HEIGHT = 27
AGENT_WIDTH = 12

REAR_TIRE_JOINT_X = 6.5
REAR_TIRE_JOINT_Y = 4
FRONT_TIRE_JOINT_X = 6.5
FRONT_TIRE_JOINT_Y = 23

DEFAULT_STARTING_POSITION = (100, 100)


## WORLD

# --- constants ---
# Box2D deals with meters, but we want to display pixels,
# so define a conversion factor:
PPM = 1 # PIXEL PER METER
TARGET_FPS = 60
TIME_STEP = 1.0 / TARGET_FPS

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 500
ZOOM = 1