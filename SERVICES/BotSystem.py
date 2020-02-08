import sys ,os ,time

class start:
    def __init__(self,bot):
        self.bot = bot
        try:
            if sys.argv[1].strip(' ') == '--background':
                self.run_bot_background()
            elif sys.argv[1].strip(' ') == '-BG':
                self.run_bot()
            elif sys.argv[1].strip(' ') == '--start':
                print('\033[1;32m[*] bot started... [Ctrl + C] * 2')
                self.run_bot()
            else:
                print('\033[1;31m[!] Not Found...')
        except IndexError:
            print('\033[1;32m[*] bot started... [Ctrl + C] * 2')
            self.run_bot()

    def run_bot(self):
        try:
            while True:
                try:
                    self.bot.polling(none_stop=True)
                except:
                    pass
                finally:
                    time.sleep(15)
        except KeyboardInterrupt:
            exit()

    def run_bot_background(self):
        print('\033[1;32m[*] bot started...')
        os.popen('nohup python3 bot.py -BG &>/dev/null&')
