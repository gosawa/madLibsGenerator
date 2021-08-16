class MadLibsGen:
    def __init__(self):
        self.theAnswers = []
        self.thePrompts = ["animal", "adjective", "adjective", "adjective", "noun"]

    def get_answers(self):

        for i in self.thePrompts:
            self.theAnswers.append(input(i))

    def print_my_lib(self):
        _myLib = f"""If you've ever met my {self.theAnswers[0]} Snoopy, then you know he's not your 
        average canine companion. Some kids might find it {self.theAnswers[1]} that their 
        beagle has such a/an {self.theAnswers[2]} imagination, but not me! All 
        I've ever wanted was a normal, {self.theAnswers[3]} dog. Why can't I have 
        a/an {self.theAnswers[4]} just like everyone else?"""
        print(_myLib)


if __name__ == '__main__':
    my_lib = MadLibsGen()
    my_lib.get_answers()
    my_lib.print_my_lib()
