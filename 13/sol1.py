def parse(rows):
    return [list(map(int, row.split(': '))) for row in rows]

def get_severity(scanners):
    def check_scanner(scanner):
        # the scanner returns back to 0 every 2*(r-1) steps,
        # and we will be there on step r
        return scanner[0] % (2*(scanner[1] - 1)) == 0

    return sum(s[0]*s[1] for s in scanners if check_scanner(s))

with open('input', 'r') as fp:
    scanners = parse(line.strip() for line in fp)
    print(get_severity(scanners))
