def change(str):
    snk = [str[0].lower()]
    for c in str[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            snk.append('_')
            snk.append(c.lower())
        else:
            snk.append(c)

    return ''.join(snk)



str = "InsightsWorkshops"
print(change(str))
