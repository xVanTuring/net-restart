from time import sleep
from ping3 import ping
import argparse
import os

parser = argparse.ArgumentParser(
    prog="NetRestart",
    description="Reboot computer if network is disconnect(why?)",
    epilog="xVanTuring",
)

parser.add_argument("ip_to_ping", help="Ip to ping")
parser.add_argument("-c", "--count", help="count to ping", default=4, type=int)
parser.add_argument("-t", "--timeout", help="timeout seconds", default=4, type=int)
parser.add_argument(
    "-m", "--max-reboot", help="max reboot count to shutdown", default=4, type=int
)
args = parser.parse_args()

print(args)


def ping_once(iter) -> bool:
    second = ping(args.ip_to_ping, timeout=args.timeout)
    if second is None:
        return False
    return True


def check_connection() -> bool:
    result = list(map(ping_once, range(args.count)))
    print(result)
    if True in result:
        return True
    return False


def inc_reboot_count():
    # TODO
    pass


def reset_reboot_count():
    # TODO
    pass


def get_reboot_count() -> int:
    return 0


def check_and_reboot():
    if not check_connection():
        # write reboot counts
        if get_reboot_count() > args.max_reboot:
            reset_reboot_count()
            print("After all reboots still can't connect. shutdown in 10s!")
            sleep(10)
            os.system("reboot")
            return
        inc_reboot_count()
        print("Failed to ping after all tries. Reboot in 10s")
        sleep(10)
        os.system("reboot")
    else:
        reset_reboot_count()
