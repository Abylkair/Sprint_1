time = '1h 45m,360s,25m,30m 120s,2h 60s'.split(',')

total_h = 0
total_m = 0
total_s = 0

for t in time:
    parts = t.split() 
    for p in parts:
        if 'h' in p:
            total_h += int(p.replace('h',''))
        elif 'm' in p:
            total_m += int(p.replace('m',''))
        elif 's' in p:
            total_s += int(p.replace('s',''))

# переводим всё в минуты
total_minutes = total_h*60 + total_m + total_s//60
print(total_minutes)
