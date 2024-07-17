from naome import *

ipaddress = "192.168.1.112"


def main():

    mode = raw_input("Type ideal, random or none to select study condition: ")
    if mode == "ideal":
        nao = Script(ideal_error, ipaddress)
    elif mode == "random":
        nao = Script(rand_error, ipaddress)
    elif mode == "none":
        nao = Script(no_error, ipaddress)
    else:
        return

    # turn off artificial life
    nao.al_off()

    # for testing motion
    # while True:
        # body = raw_input("sit, stand: ")
        # nao.posture(body)
        # pos = raw_input("wave, read, reset: ")
        # nao.move_arms(pos)
        # if pos == "break":
            # break

    # Setup loop
    nao.posture("sit")
    nao.move_head("book")
    nao.posture("rest")
    prog = raw_input("0 for demo, 1 for study: ")

    if prog == "0":
        nao.update_msg("Hi")
        raw_input("Enter to continue")
        nao.posture("sit")
        nao.free_tts()
        nao.move_arms("wave")
        nao.move_arms("reset")
        nao.posture("rest")
        raw_input("Enter to continue")
        while True:
            demo = raw_input("Enter wave to wave, end to end, enter to tts: ")
            if demo == "wave":
                nao.posture("sit")
                nao.move_arms("wave")
                nao.move_arms("reset")
                nao.posture("rest")
            elif demo == "end":
                break
            else:
                nao.posture("sit")
                nao.free_tts()
                nao.move_arms("rest")

    elif prog == "1":
        while True:
            raw_input("Press enter to start: ")
            break
        # Intro Loop
        nao.posture("stand")
        nao.move_head("child")
        raw_input("Enter to continue")
        nao.update_msg("Hi")
        nao.free_tts()
        nao.move_arms("wave")
        nao.posture("stand")
        nao.move_head("child")
        raw_input("Enter to continue")
        nao.update_msg("Can you help me reed this story? If I make a mistake, please let me know!")
        nao.free_tts()
        raw_input("Enter to continue")
        nao.update_msg("Also, I will ask you, if you want me to ree-reed any page, if you're not sure...")
        nao.free_tts()
        raw_input("Enter to continue")
        nao.posture("sit")
        nao.move_head("child")
        nao.update_msg("Okay, should we start reading?")
        nao.free_tts()
        raw_input("Enter to continue")
        while True:
            intro = raw_input("Type start to begin or press enter to use free tts: ")
            if intro == "start":
                nao.move_head("book")
                nao.read_page()
                break
            if intro == "end":
                nao.end_early()
                break
            else:
                nao.free_tts()

        # Outro Dialog
        nao.move_head("child")
        raw_input("Press Enter to start outro dialog")
        nao.update_msg("Thank you for reading with me today, I learned a lot.")
        nao.free_tts()
        raw_input("Press Enter to continue outro")
        nao.update_msg("Bye")
        nao.free_tts()
        nao.move_arms("wave")
        nao.move_arms("reset")

        while True:
            outro = raw_input("Type end to finish dialog or press enter to use free tts: ")
            if outro == "end":
                nao.move_head("book")
                nao.posture("rest")
                break
            else:
                nao.free_tts()


main()
