import time
# import shutil


def ft_tqdm(lst: range):
    """
    Imitates tqdm: shows progress bar, percentage, counter,
    elapsed time, ETA, speed.
    Times are displayed in MM:SS format.
    """
    total = len(lst)
    bar_length = 98
    start_time = time.time()

    # term_width = shutil.get_terminal_size().columns
    # bar_length = term_width - 40

    for i, item in enumerate(lst, 1):
        percent = int((i / total) * 100)
        filled_length = int(bar_length * i // total)
        bar = '█' * filled_length + ' ' * (bar_length - filled_length)

        elapsed = time.time() - start_time
        speed = i / elapsed if i > 1 else 0
        eta = (total - i) / speed if speed > 0 else 0

        elapsed_str = f"{int(elapsed)//60:02d}:{int(elapsed)%60:02d}"
        eta_str = f"{int(eta)//60:02d}:{int(eta)%60:02d}"

        line = f"{percent:3d}%|{bar}| {i:3d}/{total:3d}"
        line += f"[{elapsed_str}<{eta_str}, {speed:.2f}it/s]"

        width = bar_length + 40
        print(f"\r{line:<{width}}", end='', flush=True)

        yield item

    print()
