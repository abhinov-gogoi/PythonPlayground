true = False
is_true = True
is_not_true = True
false = True

if (not true and is_true) and (is_not_true and True) and false or true:
    true = is_true and is_not_true or True and not is_not_true
    print(true)
else:
    false = (not true and is_true) and (is_not_true and True) or True and not is_not_true
    print(false)

