import picamera
import time
import os
import datetime as dt

from daemon.runner import DaemonRunner

_base_path = "/tmp/"

class DashCam:
    stdin_path = "/dev/null"
    stdout_path = os.path.join(_base_path, "dashcam.out") # Can also be /dev/null
    stderr_path =  os.path.join(_base_path, "dashcam.err") # Can also be /dev/null
    pidfile_path =  os.path.join(_base_path, "dashcam.pid")
    pidfile_timeout = 3

    def __init__(self):
        self.cam = None
        self.period = 30
        self.file_string = "/home/pi/cam_footage/%s.h264"

    def run(self):
        try:
            self.cam = picamera.PiCamera()
            self.cam.hflip = True
            self.cam.vflip = True
            self.cam.annotate_background = picamera.Color('black')
            self.cam.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            start_time = dt.datetime.now()
            self.cam.start_recording(self.file_string % start_time.strftime('%Y-%m-%d--%H:%M:%S'))
            while True:
                self.cam.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.cam.wait_recording(0.2)

                if (dt.datetime.now() - start_time).seconds > 5:
                    start_time = dt.datetime.now()
                    self.cam.split_recording(self.file_string % start_time.strftime('%Y-%m-%d--%H:%M:%S'))

        except(SystemExit, KeyboardInterrupt):
            pass
        except:
            raise
        finally:
            print("Shutting Down")


def main():
    """
          Call with arguments start/restart/stop
        """
    run = DaemonRunner(DashCam())
    run.do_action()

if __name__ == '__main__':
    main()
