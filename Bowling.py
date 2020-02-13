class Frame:
    rolls = []

    def is_finished(self):
        return (len(self.rolls) == 2) or (self.rolls[0] == 10)

    def get_pins(self):
        pins = 0
        for roll in self.rolls:
            pins += roll
        return pins

    def translate_to_score(self, roll):
        if roll == "-":
            return 0
        return int(roll)

    def add_roll(self, roll):
        self.rolls.append(self.translate_to_score(roll))

frames = []

def compute_score(line):
    score = 0
    current_frame = 0
    frames.append(Frame())
    for roll in range(0,len(line)):
        frames[current_frame].add_roll(line[roll])
        if frames[current_frame].is_finished():
            current_frame = current_frame + 1
            frames.append(Frame())
    for frame in frames:
        score += frame.get_pins()
    return score