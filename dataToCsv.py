import csv

class NESA_CSV:
    
    #create the csv file, and write the info of all the advisors to it
    def writeFile(self, advList):
        fileName = 'NESA.csv'
        try:
            with open(fileName, 'w+', newline='') as csvfile:
                fieldnames = ['name','title' ,'location', 'email']
                thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                thewriter.writeheader()
                for adv in advList:
                    thewriter.writerow({'name': adv.name, 'title': adv.title, 'location': adv.location, 'email': adv.email})
            # csvfile = open('nesa.csv', 'a+', newline='')
            # writer = csv.writer(csvfile)
            # for adv in advList:
            #     writer.writerow({'name': adv.name, 'title': adv.title, 'location': adv.location, 'email': adv.email})
            csvfile.close()
            print(f"Writing {fileName} succeeded.")
        except:
            print(f"Writing {fileName} failed.")


class ISD_CSV:
    #create the csv file, and write the info of all the advisors to it
    def writeFile(self, schList):
        fileName = 'ISD.csv'
        try:
            with open(fileName, 'w+', newline='') as csvfile:
                fieldnames = ['location', 'name', 'curriculum' ,'language', 'ages', 'fees']
                thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                thewriter.writeheader()
                for sch in schList:
                    thewriter.writerow({'location': sch.location, 'name': sch.name, 'curriculum': sch.curriculum, 'language': sch.language, 'ages': sch.ages, 'fees': sch.fees})
                csvfile.close()
            print(f"Writing {fileName} succeeded.")
        except:
            print(f"Writing {fileName} failed.")