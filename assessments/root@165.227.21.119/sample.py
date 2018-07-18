import csv
with open('namespace.txt') as f:
    import csv
    words = csv.reader(f)
    uniques = []
    for word in words:
        if word not in uniques:
            uniques.append(word)
    print(len(uniques))


import csv
with open('namespace.txt') as f:
    import csv
    words = csv.reader(f)
    for word in words:
        print(word[0] + '_')


# scp >>

# ssh root@IP_ADDRESS
# install flask sudo pip3 install flask
# mkdir mecha_example
# cd mecha_example
# cd tmp /
# mv run / ~
# nano run / wsgi.py
# change hostname from '127.0.0.1' to '0.0.0.0'
# cd to project folder
# python3 run / wsgi.py


# // from the project directory
# scp - r run username @ hostname: / tmp >> copies the directory to tmp
