from datetime import datetime


class CMD_Colors:

    # text color
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    ORANGE = '\033[38;5;208m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'

    # back ground
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_ORANGE = '\033[48;5;208m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # reset
    RESET = '\033[0m'

    # status
    INFO = 0
    ERROR = 1
    DANGER = 2
    RESULT = 3

    @staticmethod
    def user_log(status, log, category="", end='\n'):
        t_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if status == CMD_Colors.INFO:
            print(f'[{t_now}][{category}]{CMD_Colors.BG_GREEN}INFO{CMD_Colors.RESET}:{CMD_Colors.GREEN}{log}{CMD_Colors.RESET}',
                  end=end)
        elif status == CMD_Colors.ERROR:
            print(f'[{t_now}][{category}]{CMD_Colors.BG_YELLOW}ERROR{CMD_Colors.RESET}:{CMD_Colors.YELLOW}{log}{CMD_Colors.RESET}',
                  end=end)
        elif status == CMD_Colors.DANGER:
            print(f'[{t_now}][{category}]{CMD_Colors.BG_RED}DANGER{CMD_Colors.RESET}:{CMD_Colors.RED}{log}{CMD_Colors.RESET}',
                  end=end)
        elif status == CMD_Colors.RESULT:
            print(f'[{t_now}][{category}]{CMD_Colors.BG_BLUE}RESULT{CMD_Colors.RESET}:{CMD_Colors.BLUE}{log}{CMD_Colors.RESET}',
                  end=end)

    @staticmethod
    def printing(text, color):
        return f"{color}{text}{CMD_Colors.RESET}"