import subprocess

def get_passwords(amount=None, config=None):
    cmd = "hsxkpasswd" if amount is None else "hsxkpasswd {}".format(amount)
    cmd = cmd if config is None else "{} --config-file {}".format(cmd, config)
    cmd = "{} -w NONE".format(cmd)

    try:
        result_string = subprocess.check_output(
            cmd,
            stderr=subprocess.STDOUT,
            shell=True)

    except:
        return ""

    pw_list = result_string.split('\n')

    return pw_list[:-1]

def main():
    print(get_passwords())

if __name__ == "__main__":
    main()
