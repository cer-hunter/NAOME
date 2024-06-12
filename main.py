from naome import *

ipaddress = "192.168.1.139"


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

    # Intro Loop
    while True:
        nao.update_msg("Hi my name is Sami, can you help me reed this story?")
        nao.free_tts()
        intro = raw_input("Type start to begin or press enter to use free tts: ")
        if intro == "start":
            nao.read_page()
            break
        else:
            nao.free_tts()

    # Outro Dialog
    raw_input("Press Enter to start outro dialog")
    nao.update_msg("Thank you for reading with me today, I learned a lot")
    nao.free_tts()
    while True:
        outro = raw_input("Type end to finish dialog or press enter to use free tts: ")
        if outro == "end":
            break
        else:
            nao.free_tts()


main()
