def digital_root(num: int) -> int:
    if num < 10:
        return num
    return digital_root(sum(int(i) for i in str(num)))

print(digital_root(889987))