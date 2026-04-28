import sys

def progress_update(main_title, n, lenloop, compact_updates= False):
    curr_p = int((n / lenloop) * 20)
    prev_p = int(((n - 1) / lenloop) * 20)
    if compact_updates and curr_p == prev_p and n != lenloop:
        return
    n += 0
    center_len = 30
    longest_string = len(main_title)
    if longest_string > center_len:
        center_len = center_len - (center_len - longest_string)
    center_len += 4 
    main_title = " "*int(((center_len-len(main_title))/2) + 0.5)+ main_title + " "*int(((center_len-len(main_title))/2))

    p = int((n/lenloop)*20)
    bar = [
    f"╭────────────────────────╮",
    f"│α·{'#'*p+' '*(20-p)  }·ω│",
    f"╰────────────────────────╯",]
    detail = [
    f"╭{'─'*(len(str(abs(n)))+1+len(str(abs(lenloop))))}╮",
    f"│{n}/{lenloop}│",
    f"╰{'─'*(len(str(abs(n)))+1+len(str(abs(lenloop))))}╯",]

    print(bar[0] + "·"*center_len + detail[0])
    print(bar[1] + main_title + detail[1])
    print(bar[2] + "·"*center_len + detail[2])

if __name__ == "__main__":
    main_title = sys.argv[1]
    n = int(sys.argv[2])
    lenloop = int(sys.argv[3])
    compact_updates = sys.argv[4].strip().lower() in ("true", "1", "yes")

    progress_update(main_title, n, lenloop, compact_updates)