from time import sleep


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class FakeCharLCDPlate(object):

    RED = "red"
    UP = "q"
    DOWN = "a"
    SELECT = "s"

    def __init__(self):
        self._getch = _GetchUnix()
        pass

    def clear(self):
        print "--LCD Cleared--"

    def message(self, msg):
        print msg

    def backlight(self, bl):
        print "Backlight %s" % str(bl)

    def fakeonly_getch(self):
        self._ch = self._getch()

    def buttonPressed(self, button):
        return self._ch == button



class TimelapseUi(object):

    def __init__(self):
       

    def update(self, text):
        print(text)

    def show_config(self, configs, current):
        config = configs[current]
        self.update("Timelapse\nT: %s ISO: %d" % (config[0], config[1]))

    def show_status(self, shot, configs, current):
        config = configs[current]
        self.update("Shot %d\nT: %s ISO: %d" % (shot, config[0], config[1]))

    def show_error(self, text):
        self.update(text[0:16] + "\n" + text[16:])
        

   


    def main(self, configs, current, network_status):
        
        self.update(network_status)
        
        ready = False
        while not ready:
            self.show_config(configs, current)

            
                
        return current 



