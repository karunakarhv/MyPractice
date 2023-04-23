# Scheduling Commands
# Problem
# We need to schedule commands for execution at certain times

import time, os, sys, sched
schedule = sched.scheduler(time.time, time.sleep)

def perform_cmd(cmd, inc):
    schedule.enter(inc, 0, perform_cmd, (cmd, inc))
    os.system(cmd)

def main(cmd, inc=60):
    schedule.enter(0, 0, perform_cmd, (cmd, inc))
    schedule.run()

if __name__ == '__main__':
    main('dir')