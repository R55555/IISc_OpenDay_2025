import gym
import keyboard 
import time

# Initialize the environment
env = gym.make("PongNoFrameskip-v4", render_mode="human")
obs, info = env.reset()

# Define action mappings
# 0 = No Action, 2 = Move Up, 3 = Move Down

def get_manual_action():
    if keyboard.is_pressed("up"):
        return 4  # Move up
    elif keyboard.is_pressed("down"):
        return 5  # Move down
    elif keyboard.is_pressed("a"):
        return 4
    elif keyboard.is_pressed("s"):
        return 5
    elif keyboard.is_pressed("f"):
        return 1
    return 0  # No action

# Main loop
running = True
action=0
total_r_pos=0
total_r_neg=0

while running:
    
    
    obs, reward, terminated, truncated, info = env.step(action)
    env.render()
    if reward>0:
    	total_r_pos+=reward
    elif reward<0:
    	total_r_neg+=reward
    action = get_manual_action()
    if terminated or truncated or total_r_neg<=-5 or total_r_pos>=5:  # Reset if the episode ends
        obs, info = env.reset()
        total_r_neg=0
        total_r_pos=0

    time.sleep(0.01)  # Slow down for better control

env.close()
