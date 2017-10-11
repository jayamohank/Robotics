import numpy as np
import time
# x Prevent the direct going into the rocks
# right wall crawling


def decision_step(Rover):

    if Rover.nav_angles is not None:
        if Rover.mode == 'forward':
            if len(Rover.nav_angles) >= Rover.stop_forward:
               if Rover.vel < 0.05:
                  if Rover.low_speed_state > 10:
                     Rover.low_speed_state = 0
                     Rover.brake = Rover.brake_set
                     Rover.throttle = 0
                     Rover.steer = 0
                     Rover.mode = 'stop'
                  else:
                     Rover.low_speed_state += 1
                     Rover.throttle = Rover.throttle_set 
                     Rover.brake = 0 
                     Rover.steer = np.clip(np.mean(Rover.nav_angles * 180/np.pi), -15, 15)
               elif Rover.vel > 1:
                  Rover.low_speed_state = 0
                  Rover.throttle = 0
                  Rover.brake = 0 
                  Rover.steer = np.clip(np.mean(Rover.nav_angles * 180/np.pi), -15, 15)
               else:
                  Rover.low_speed_state = 0
                  Rover.brake = 0 
                  Rover.throttle = Rover.throttle_set 
                  Rover.steer = np.clip(np.mean(Rover.nav_angles * 180/np.pi), -15, 15)
            else:
                 Rover.low_speed_state = 0
                 Rover.brake = Rover.brake_set
                 Rover.throttle = 0
                 Rover.steer = 0
                 Rover.mode = 'stop'
        elif Rover.mode == 'stop':
             if Rover.vel > 0.1:
                Rover.low_speed_state = 0
                Rover.brake = Rover.brake_set
                Rover.throttle = 0
             else:
                if len(Rover.nav_angles) >= 2 * Rover.stop_forward:
                   turn_off = np.clip(np.mean(Rover.nav_angles * 180/np.pi), -15, 15)
                   print("turn_off:", turn_off )
                   turn_off *= 100
                   turn_off = np.clip(turn_off, -5, 5)
                   Rover.steer = turn_off
                   Rover.throttle = 0
                   Rover.brake = 0 
                   Rover.mode = 'forward'
                else:
                   Rover.steer = -10 
                   Rover.throttle = 0 
                   Rover.brake = 0 

    return Rover

