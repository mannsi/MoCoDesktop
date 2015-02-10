
import moCo.dropbox
import time


def run():
    while True:
        # with open('/home/mannsi/MoCo/output', 'a+') as f:
        #     f.write(str(datetime.datetime.now()) + "\n")
        _execute_commands()
        print("in run")
        time.sleep(5)


def _execute_commands():
    commands = moCo.dropbox.get_commands()
    for command in commands:
        command.execute()


if __name__ == "__main__":
    run()