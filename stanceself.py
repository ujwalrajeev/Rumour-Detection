import csv

def getstance():
    file = open('replies_clean.csv')
    csvreader = csv.reader(file)

    output_file = open('rumourdetails.txt', 'w')        

    total_favour = 0
    total_against = 0
    total_none = 0

    favour = ["correct", "true", "support", "do believe", "favour", "support", "in favour of",
          "pro", "right", "true rumour", "congratulations", "wow", "awesome", "great", "good", "nice", "yeah", "yes", "love this",
              "happy"]

    against = ["wrong", "not correct", "false", "against", "dont believe", "don't believe",
           "incorrect", "donot support", "fooling", "fooled", "oppose", "in opposition to",
           "at odds with", "con", "contrary", "will not", "fool", "fake", "rumour", "fake rumour", "no", "sad"]

    output_file.write("Rumour stance report generated by Scandal verifier\n\n")

    for i in csvreader:
        f = 0
        a = 0
        n = 0
        if i == [] or i == ['user','text']:
            continue
        else:
            cmt = i[1]
            cmtsplit = cmt.split()

            for c in cmtsplit:
                if c in favour:
                    f = f + 1
                elif c in against:
                    a = a + 1
                else:
                    n = n + 1

            #print("a = " + str(a) + "\n")
            #print("f = " + str(f) + "\n")

            if f > a:
                total_favour = total_favour + 1
                output_text = i[0] + " --- " + i[1] + " " + " --- Believed\n"
                output_file.write(output_text)
                #print("Favour")
            elif a > f:
                total_against = total_against + 1
                output_text = i[0] + " --- " + i[1] + " " + " --- Didn't believed\n"
                output_file.write(output_text)
                #print("Against")
            else:
                total_none = total_none + 1
                output_text = i[0] + " --- " + i[1] + " " + " --- None\n"
                output_file.write(output_text)
                #print("None")

            

    output_file.write("\n\n\nTotal people believed - " + str(total_favour) + "\n")
    output_file.write("Total people did'nt believed - " + str(total_against) + "\n")
    output_file.write("Total people niether believed or not - " + str(total_none) + "\n\n\n\n\n")

    output_file.write("Scandal Verification by Neural Networks created by Ujwal Rajeev, Vyshak A, Teena Poulose and Swaliha Abdul Salam")
    
    if total_favour > total_against:
        return 1
    elif total_against > total_favour:
        return 0
    else:
        return 2
                
