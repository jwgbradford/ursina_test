tup_string = "(1, 4, 1)"
print(f'{tup_string=}')
tup_tup = ()
for i in range(len(tup_string)):
    try: 
        int(tup_string[i])
        tup_tup = tup_tup + (int(tup_string[i]),)
    except:
        pass
print(f'{tup_tup=}')
tup_tup = tup_string
print(f'{tup_tup=}')