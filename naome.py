import naoqi
import time


def no_error():
    page1 = {1: "Toad was sitting on his front porch",
             2: "Frog came along and said, what is the matter Toad?",
             3: "You are looking sad"}
    page2 = {1: "Yes said Toad",
             2: "This is my sad time of day",
             3: "It is the time when I wait for the mail to come",
             4: "It always makes me very unhappy",
             5: "Why is that? asked Frog",
             6: "Because I never get any mail, said Toad"}
    page3 = {1: "Not ever? asked Frog",
             2: "No never? said Toad",
             3: "No one has ever sent me a letter",
             4: "Every day my mailbox is empty",
             5: "That is why waiting for the mail is a sad time for me",
             6: "Frog and Toad sat on the porch, feeling sad together"}
    page4 = {1: "Then Frog said, I have to go home now Toad",
             2: "There is something I must do",
             3: "Frog hurried home",
             4: "He found a pencil and a piece of paper",
             5: "He wrote on the paper"}
    page5 = {1: "He put the paper in an envelope",
             2: "On the envelope he wrote, a letter for Toad",
             3: "Frog ran out of his house",
             4: "He saw a snail that he knew",
             5: "Snail, said Frog, please take this letter "
                "to Toad's house and put it in his mailbox",
             6: "Sure, said the snail, right away"}
    page6 = {1: "Then Frog ran back to Toad's house",
             2: "Toad was in bed, taking a nap.",
             3: "Toad, said Frog, "
                "I think you should get up and wait for the mail some more",
             4: "No, said Toad, I am tired of waiting for the mail"}
    page7 = {1: "Frog looked out of the window at Toad's mailbox",
             2: "The snail was not there yet",
             3: "Toad, said Frog, you never know when someone may send you a letter",
             4: "No, no, said Toad",
             5: "I do not think anyone will ever send me a letter"}
    page8 = {1: "Frog looked out of the window",
             2: "The snail was not there yet",
             3: "But Toad, said Frog, someone may send you a letter today",
             4: "Don't be silly, said Toad",
             5: "No one has ever sent me a letter before, and no one will send me a letter today"}
    page9 = {1: "Frog looked out of the window",
             2: "The snail was still not there",
             3: "Frog, why do you keep looking out of the window? asked Toad",
             4: "Because now I am waiting for the mail, said Frog",
             5: "But there will not be any, said Toad"}
    page10 = {1: "Oh, yes there will, said Frog, because I have sent you a letter",
              2: "You have? said Toad",
              3: "What did you write in the letter?",
              4: "Frog said, I wrote, "
                 "Dear Toad, I am glad that you are my best friend",
              5: "Your best friend, Frog"}
    page11 = {1: "Oh, said Toad, that makes a very good letter",
              2: "Then Frog and Toad went out "
                 "onto the front porch to wait for the mail",
              3: "They sat there, feeling happy together"}
    page12 = {1: "Frog and Toad waited a long time",
              2: "Four days later the snail got to "
                 "Toad's house and gave him the letter from Frog",
              3: "Toad was very pleased to have it"}
    story = {1: page1,
             2: page2,
             3: page3,
             4: page4,
             5: page5,
             6: page6,
             7: page7,
             8: page8,
             9: page9,
             10: page10,
             11: page11,
             12: page12}
    return story


def rand_error():
    page1 = {1: "Toad was sitting on his front porch",
             2: "Frog came along and said, what is the matter Toad?",
             3: "You are looking sad"}
    page2 = {1: "Yes said Toad",
             2: "This is my sad time of day",
             3: "It is the time when I wait for the mail to come",
             4: "It always makes me very unhappy",
             5: "Why is that? asked Frog",
             6: "Because I never get any mail, said Toad"}
    page3 = {1: "Not ever? asked Frog",
             2: "No never? said Toad",
             3: "No one has ever sent me a letter",
             4: "Every day my mailbox is empty",
             5: "That is why waiting for the mail is a sad time for me",
             6: "Frog and Toad sat on the porch, feeling sad together"}
    page4 = {1: "Then Frog said, I have to go home now Toad",
             2: "There is something I must do",
             3: "Frog hurried home",
             4: "He found a pencil and a piece of paper",
             5: "He wrote on the paper"}
    page5 = {1: "He put the paper in an envelope",
             2: "On the envelope he wrote, a letter for Toad",
             3: "Frog ran out of his house",
             4: "He saw a snail that he knew",
             5: "Snail, said Frog, please take this letter "
                "to Toad's house and put it in his mailbox",
             6: "Sure, said the snail, right away"}
    page6 = {1: "Then Frog ran back to Toad's house",
             2: "Toad was in bed, taking a nap.",
             3: "Toad, said Frog, "
                "I think you should get up and wait for the mail some more",
             4: "No, said Toad, I am tired of waiting for the mail"}
    page7 = {1: "Frog looked out of the window at Toad's mailbox",
             2: "The snail was not there yet",
             3: "Toad, said Frog, you never know when someone may send you a letter",
             4: "No, no, said Toad",
             5: "I do not think anyone will ever send me a letter"}
    page8 = {1: "Frog looked out of the window",
             2: "The snail was not there yet",
             3: "But Toad, said Frog, someone may send you a letter today",
             4: "Don't be silly, said Toad",
             5: "No one has ever sent me a letter before, and no one will send me a letter today"}
    page9 = {1: "Frog looked out of the window",
             2: "The snail was still not there",
             3: "Frog, why do you keep looking out of the window? asked Toad",
             4: "Because now I am waiting for the mail, said Frog",
             5: "But there will not be any, said Toad"}
    page10 = {1: "Oh, yes there will, said Frog, because I have sent you a letter",
              2: "You have? said Toad",
              3: "What did you write in the letter?",
              4: "Frog said, I wrote, "
                 "Dear Toad, I am glad that you are my best friend",
              5: "Your best friend, Frog"}
    page11 = {1: "Oh, said Toad, that makes a very good letter",
              2: "Then Frog and Toad went out "
                 "onto the front porch to wait for the mail",
              3: "They sat there, feeling happy together"}
    page12 = {1: "Frog and Toad waited a long time",
              2: "Four days later the snail got to "
                 "Toad's house and gave him the letter from Frog",
              3: "Toad was very pleased to have it"}
    story = {1: page1,
             2: page2,
             3: page3,
             4: page4,
             5: page5,
             6: page6,
             7: page7,
             8: page8,
             9: page9,
             10: page10,
             11: page11,
             12: page12}
    return story


def ideal_error():
    page1 = {1: "Toad was sitting on his front porch",
             2: "Frog came along and said, what is the matter Toad?",
             3: "You are looking sad"}
    page2 = {1: "Yes said Toad",
             2: "This is my sad time of day",
             3: "It is the time when I wait for the mail to come",
             4: "It always makes me very unhappy",
             5: "Why is that? asked Frog",
             6: "Because I never get any mail, said Toad"}
    page3 = {1: "Not ever? asked Frog",
             2: "No never? said Toad",
             3: "No one has ever sent me a letter",
             4: "Every day my mailbox is empty",
             5: "That is why waiting for the mail is a sad time for me",
             6: "Frog and Toad sat on the porch, feeling sad together"}
    page4 = {1: "Then Frog said, I have to go home now Toad",
             2: "There is something I must do",
             3: "Frog hurried home",
             4: "He found a pencil and a piece of paper",
             5: "He wrote on the paper"}
    page5 = {1: "He put the paper in an envelope",
             2: "On the envelope he wrote, a letter for Toad",
             3: "Frog ran out of his house",
             4: "He saw a snail that he knew",
             5: "Snail, said Frog, please take this letter "
                "to Toad's house and put it in his mailbox",
             6: "Sure, said the snail, right away"}
    page6 = {1: "Then Frog ran back to Toad's house",
             2: "Toad was in bed, taking a nap.",
             3: "Toad, said Frog, "
                "I think you should get up and wait for the mail some more",
             4: "No, said Toad, I am tired of waiting for the mail"}
    page7 = {1: "Frog looked out of the window at Toad's mailbox",
             2: "The snail was not there yet",
             3: "Toad, said Frog, you never know when someone may send you a letter",
             4: "No, no, said Toad",
             5: "I do not think anyone will ever send me a letter"}
    page8 = {1: "Frog looked out of the window",
             2: "The snail was not there yet",
             3: "But Toad, said Frog, someone may send you a letter today",
             4: "Don't be silly, said Toad",
             5: "No one has ever sent me a letter before, and no one will send me a letter today"}
    page9 = {1: "Frog looked out of the window",
             2: "The snail was still not there",
             3: "Frog, why do you keep looking out of the window? asked Toad",
             4: "Because now I am waiting for the mail, said Frog",
             5: "But there will not be any, said Toad"}
    page10 = {1: "Oh, yes there will, said Frog, because I have sent you a letter",
              2: "You have? said Toad",
              3: "What did you write in the letter?",
              4: "Frog said, I wrote, "
                 "Dear Toad, I am glad that you are my best friend",
              5: "Your best friend, Frog"}
    page11 = {1: "Oh, said Toad, that makes a very good letter",
              2: "Then Frog and Toad went out "
                 "onto the front porch to wait for the mail",
              3: "They sat there, feeling happy together"}
    page12 = {1: "Frog and Toad waited a long time",
              2: "Four days later the snail got to "
                 "Toad's house and gave him the letter from Frog",
              3: "Toad was very pleased to have it"}
    story = {1: page1,
             2: page2,
             3: page3,
             4: page4,
             5: page5,
             6: page6,
             7: page7,
             8: page8,
             9: page9,
             10: page10,
             11: page11,
             12: page12}
    return story


class Script:
    def __init__(self, cond, ip):
        self.text = cond()
        self.IP = ip
        self.page = 1
        self.sen = 1
        self.preset_msg = "None"

    def update_msg(self, msg):
        self.preset_msg = msg

    def free_tts(self):
        # tts = naoqi.ALProxy('ALTextToSpeech', self.IP, 9559)
        if self.preset_msg == "None":
            # tts.say(raw_input())
            # for testing without robot:
            print raw_input()
        else:
            # tts.say(self.preset_msg)
            # for testing without robot:
            print self.preset_msg
            self.preset_msg = "None"

    def read_page(self):
        sentences = len(self.text[self.page])  # number of sentences
        for i in range(sentences):
            try:
                self.update_msg(self.text[self.page][self.sen])
                self.free_tts()
                time.sleep(15)
                self.sen += 1
            except KeyboardInterrupt:
                dialog = raw_input("Type tts to enter free tts, otherwise "
                                   "default is mistake dialogue: ")
                if dialog == "tts":
                    self.free_tts()
                    self.update_msg(self.text[self.page][self.sen])
                    self.free_tts()
                    self.sen += 1
                else:
                    self.mistake_made()
                    self.update_msg(self.text[self.page][self.sen])
                    self.free_tts()
                    self.sen += 1
                continue
        self.update_msg("Okay should we continue to the next page, "
                        "or would you like for me to read this page again "
                        "to make sure I don't make any mistakes?")
        self.free_tts()
        decision = raw_input("Input 1 to re-read the page, default is next page: ")
        if decision == "1":
            self.reread_page()
        else:
            self.next_page()

    def next_page(self):
        self.sen = 1
        if self.page < 12:
            self.page = self.page + 1
            self.read_page()

    def reread_page(self):
        self.sen = 1
        self.read_page()

    def mistake_made(self):
        while True:
            self.update_msg("OK please tell me my mistake.")
            self.free_tts()
            new_sen = raw_input()
            self.text[self.page][self.sen] = new_sen
            self.update_msg(new_sen + ", is this correct?")
            self.free_tts()
            cont = raw_input("Press 1 to continue story or 0 to redo mistake dialog, default is redo dialog: ")
            if cont == "1":
                break
            else:
                continue
        self.update_msg("Okay I will continue reading now")
        self.free_tts()
