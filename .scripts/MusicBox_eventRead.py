import subprocess
from evdev import InputDevice, ecodes

mpc_status = "mpc status".split()
mpc_random = "mpc random on".split()
mpc_clear = "mpc crop".split()
mpc_FUNK = "mpc add FUNK/".split()
mpc_JAZZ = "mpc add JAZZ/".split()
mpc_ROCK = "mpc add ROCK/".split()
mpc_ROCK_NOUV = "mpc add ROCK_NOUV/".split()
mpc_Play = "mpc play".split()
mpc_Pause = "mpc pause".split()
mpc_next = "mpc next".split()
mpc_prev = "mpc prev".split()
mpc_volUp = "mpc volume +5".split()
mpc_volDown = "mpc volume -5".split()

device = InputDevice("/dev/input/event17") # à changer plus tard

subprocess.call(mpc_random)

for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        # Lancement des playlists
        # FUNK KEY_NUMLOCK
        if event.code == 69:
            subprocess.call(mpc_clear)
            subprocess.call(mpc_FUNK)
            subprocess.call(mpc_Play)

        # JAZZ KEY_KPSLASH
        elif event.code == 98:
            subprocess.call(mpc_clear)
            subprocess.call(mpc_JAZZ)
            subprocess.call(mpc_Play)

        # ROCK KEY_KPASTERISK
        elif event.code == 55:
            subprocess.call(mpc_clear)
            subprocess.call(mpc_ROCK)
            subprocess.call(mpc_Play)

        # ROCK_NOUV KEY_KPMINUS
        elif event.code == 74:
            subprocess.call(mpc_clear)
            subprocess.call(mpc_ROCK_NOUV)
            subprocess.call(mpc_Play)

        # Raccourcis utiles
        # Play/Pause KEY.KP5
        elif event.code == 76:
            status_output = subprocess.check_output(mpc_status)
            if "[playing]" in status_output.decode() and event.value != 1 and event.value != 2:
                subprocess.call(mpc_Pause)
            elif event.value != 1 and event.value != 2:
                subprocess.call(mpc_Play)
        
        # Next KEY_KP6
        elif event.code == 77:
            subprocess.call(mpc_next)

        # Previous KEY_KP4
        elif event.code == 75:
            subprocess.call(mpc_prev)

        # Volume UP KEY_KP8
        elif event.code == 72:
            subprocess.call(mpc_volUp)
        
        # Volume DOWN KEY_KP2
        elif event.code == 80:
            subprocess.call(mpc_volDown)

        


