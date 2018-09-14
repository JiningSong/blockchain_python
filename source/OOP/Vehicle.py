class Vehicle:
    def __init__(self, starting_top_speed=100):
        self.top_speed = starting_top_speed
        self.__warning = []

    def drive(self):
        print('I am driving but certainly not faster than {}'.format(self.top_speed))

    def __repr__(self):
        print('Printing...')
        return 'Top Speed: {}, Warnings: {}'.format(self.top_speed, len(self.__warning))

    def get_warning(self):
        return self.__warning

    def add_warning(self, warning_text):
        if len(warning_text) > 0:
            self.__warning.append(warning_text)
