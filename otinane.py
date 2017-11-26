import csv


with open('list.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    print(csv_file)

    with open('new_file.csv','w') as new_file:
        csv_writer = csv.writer(new_file,delimeter = '\t')

        for line in csv_reader:
            csv_writer.writerow(line)
            print(csv_writer.writerow(line))
