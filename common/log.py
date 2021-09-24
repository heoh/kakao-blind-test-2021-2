import os

log_file = None


def set_log_filename(filename):
    global log_file
    log_file = open(filename, 'a')


def get_next_log_filename(path):
    log_filenames = list(
        filter(lambda s: s.endswith('.log'), os.listdir(path)))
    log_numbers = [int(s[:-4]) for s in log_filenames]
    log_numbers = sorted(log_numbers)

    next_number = 0
    if log_numbers:
        next_number = log_numbers[-1] + 1

    return f"{next_number}.log"


def set_log_filename_auto(path):
    filename = get_next_log_filename(path)
    set_log_filename(f'{path}/{filename}')


def print_log(*args, **kwargs):
    _print(*args, **kwargs)
    if log_file:
        _print(*args, **kwargs, file=log_file, flush=True)


def override_print_globally():
    __builtins__['print'] = print_log


_print = __builtins__['print']
