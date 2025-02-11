from vk import vk
import pdfplumber
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
                index_group = table[1].index(group)
                for j in range(1, 9):
                    array.append(table[nomber+j][index_group])
    return array

def teacher_search(text,day):
    mass_pach = vk()
    array=[]
    for masss in mass_pach:
        with pdfplumber.open(masss['name']) as pdf:
            for page_number, page in enumerate(pdf.pages, start=1):
                table = page.extract_table()
                for j in range(len(table)):
                    if 'понедельник' == day:
                        nomber_day=10
                        nomber_day_2=0
                    if 'вторник' == day:
                        nomber_day=20
                        nomber_day_2=10
                    if 'среда' == day:
                        nomber_day=30
                        nomber_day_2=20
                    if 'четверг' == day:
                        nomber_day=40
                        nomber_day_2=30
                    if 'пятница' == day:
                        nomber_day=50
                        nomber_day_2=40
                    if j <= nomber_day and j>=nomber_day_2:
                        for value in table[j]:
                            value = str(value)
                            if text in value:
                                index_teacher = table[j].index(value)
                                index_massiva = j
                                array.append(f'{table[index_massiva-1][index_teacher]} {table[1][index_teacher]}')

    return array
