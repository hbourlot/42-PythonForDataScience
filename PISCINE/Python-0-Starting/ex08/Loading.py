from os import get_terminal_size, times


def grab_percent_gap(percent_value: int) -> str:
    length = len(str(percent_value))
    if length == 1:
        return " 0"
    elif length == 2:
        return " "
    return ""


def format_time(elapsed, eta) -> str:
    seconds_eta = int(eta)
    minutes_eta = (seconds_eta % 3600) // 60
    secs = seconds_eta % 60

    seconds_ela = int(elapsed)
    minutes_ela = (seconds_ela % 3600) // 60
    secs_ela = seconds_ela % 60
    return f"{minutes_ela:02d}:{secs_ela:02d}<{minutes_eta:02d}:{secs:02d}"


def format_its(rate) -> str:
    return f"{rate:.02f}it/s"


def ft_tqdm(lst: range):

    terminal_width = get_terminal_size().columns
    total = lst.stop
    start_time = times()[4]

    for i, ele in enumerate(lst, 1):
        now = times()[4]
        elapsed = now - start_time

        rate = i / elapsed if elapsed > 0 else 0
        remained_time = total - i
        eta = remained_time / rate if rate > 0 else 0

        total_width = terminal_width - len(str(terminal_width)) - 42
        filled = int((i / total) * total_width)
        bar = "=" * filled + " " * max(0, total_width - filled)

        percent_value = int((i / total) * 100)
        percent_slot = f"{grab_percent_gap(percent_value)}{percent_value}"
        yield print(
            f"\033[2K\r{percent_slot}%|[{bar}]| {i}/{total}",
            f"[{format_time(elapsed, eta)}, {format_its(rate)}]",
            end="",
            flush=True,
        )
