l1 = [[[1, 2.9], 8], "r", [3, 5], 4]
t1 = str(l1)
t1 = t1.replace("[", "")
t1 = t1.replace("]", "")
l2 = list(t1.split(", "))
#всі елементи списку тепер на одному рівні, але текстового типу
