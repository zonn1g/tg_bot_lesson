from operator import index
from vk import vk
import pdfplumber
day = ""
pach = "../pdf.pdf"

def raspisanie(day, group):
    nomber = 0
    array = []

    mass_pach = vk()

    with pdfplumber.open(mass_pach[0]['name']) as pdf:
        page = pdf.pages[0]
        table = page.extract_table()
        for i in range(1, 50):
            if day in str(table[i][0]):
                nomber = i
        for i in range(len(table[1])):
            table[1][i] = table[1][i].replace("\n", " ").replace("\t", " ").strip()
        try:
            index_group = table[1].index(group)

            for j in range(1, 9):
                array.append(table[nomber+j][index_group])
        except:
            with pdfplumber.open(mass_pach[1]['name']) as pdf:
                page = pdf.pages[0]
                table = page.extract_table()
                for i in range(1, min(50, len(table))):
                    if day in str(table[i][0]):
                        nomber = i
                for i in range(len(table[1])):
                    table[1][i] = table[1][i].replace("\n", " ").replace("\t", " ").strip()
                #print(table[1])
                index_group = table[1].index(group)
                for j in range(1, 9):
                    array.append(table[nomber+j][index_group])

    return array
def teacher_search(text,day):
    mass_pach = vk()
    array=[]
    nomber = 0


    for masss in mass_pach:

        with pdfplumber.open(masss['name']) as pdf:
            for page_number, page in enumerate(pdf.pages, start=1):
                table = page.extract_table()
                #print(table[3])
                for i in range(3):
                    for value in table[3+(i*2)]:
                       # print(value)
                        value = str(value)
                        if text in value:
                            index_teacher = table[3+(i*2)].index(value)
                            #print(table[5])
                            array.append(f'{table[2+(i*2)][index_teacher]} {table[1][index_teacher]}')


    return array

