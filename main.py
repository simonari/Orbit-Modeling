from datetime import datetime as dt

from numpy import set_printoptions

from visibility.visibility import visibility


def main():
    time_start = dt.now()
    print(f"[+] Output image resolution: {n}x{n} pixels.")

    visibility((n, n), cycle_number)

    print(f"[+] Exiting program.\n"
          f"[+] Execution took: {(dt.now() - time_start).total_seconds()}")


if __name__ == '__main__':
    set_printoptions(precision=3, suppress=True)
    n = 100
    cycle_number = 8
    main()
