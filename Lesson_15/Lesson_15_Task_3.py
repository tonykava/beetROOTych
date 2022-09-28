CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels = channels

    def first_channel(self):
        self.cur_ch = CHANNELS[0]
        print(self.cur_ch)

    def last_channel(self):
        self.cur_ch = CHANNELS[-1]
        print(self.cur_ch)

    def current_channel(self):
        try:
            print(self.cur_ch)
        except AttributeError:
            print(CHANNELS[0])

    def turn_channel(self, number):
        self.number = number
        try:
            self.cur_ch = CHANNELS[number - 1]
            print(self.cur_ch)
        except IndexError:
            print('U should pick a proper number of channel')

    def next_channel(self):
        try:
            print(CHANNELS[CHANNELS.index(self.cur_ch) + 1])
            self.cur_ch = CHANNELS[CHANNELS.index(self.cur_ch) + 1]
        except IndexError:
            print(CHANNELS[0])
            self.cur_ch = CHANNELS[0]

    def previous_channel(self):
        try:
            print(CHANNELS[CHANNELS.index(self.cur_ch) - 1])
            self.cur_ch = CHANNELS[CHANNELS.index(self.cur_ch) - 1]
        except IndexError:
            print(CHANNELS[-1])
            self.cur_ch = CHANNELS[-1]

    def is_exist(self, ident):
        self.ident = ident
        if isinstance(self.ident, int):
            if self.ident in range(1, len(CHANNELS)):
                print('YES')
            else:
                print('NO')
        else:
            if ident in CHANNELS:
                print('YES')
            else:
                print('NO')


controller = TVController(CHANNELS)
controller.current_channel()
controller.first_channel()
controller.last_channel()
controller.turn_channel(2)
controller.next_channel()
controller.previous_channel()
controller.current_channel()
controller.is_exist(6)
controller.is_exist("BBC")



