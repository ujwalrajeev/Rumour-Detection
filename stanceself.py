cmt = input("Enter the comment - ")
cmt= cmt.lower()

f = 0
a = 0
n = 0

favour = ["correct", "true", "support", "do believe", "favour", "support", "in favour of",
          "pro", "right"]

against = ["wrong", "not correct", "false", "against", "dont believe", "don't believe",
           "incorrect", "donot support", "fooling", "fooled", "oppose", "in opposition to",
           "at odds with", "con", "contrary", "will not", "fool"]

cmtsplit = cmt.split()

for c in cmtsplit:
    if c in favour:
        f = f + 1
    elif c in against:
        a = a + 1
    else:
        n = n + 1

print("a = " + str(a) + "\n")
print("f = " + str(f) + "\n")

if f > a:
    print("Favour")
elif a > f:
    print("Against")
else:
    print("None")
