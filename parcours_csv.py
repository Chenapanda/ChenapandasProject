import csv
import json
import pandas as pd
import openpyxl


def check_json(sherpa_name):
    f = open('sherpas.json')
    data = json.load(f)
    for i in data['sherpas']:
        first = i['firstname'].lower()
        first = first[0].upper() + first[1:]
        second = i['lastname'].lower()
        second = second[0].upper() + second[1:]
        name = first + second
        if name == sherpa_name:
            return i['email']

    return None
def read_json(name_of_the_file):

    f = open(name_of_the_file)

    data = json.load(f)
    names = []
    contacts = []
    campuss = []
    projects = []
    for i in data['sherpas']:
        first = i['firstname'].lower()
        first = first[0].upper() + first[1:]
        second = i['lastname'].lower()
        second = second[0].upper() + second[1:]
        name = first + second
        contact = i['email']
        campus = i['campus']
        project = i['project']
        projects.append(project)
        campuss.append(campus)
        contacts.append(contact)
        names.append(name)

    return names, contacts, campuss, projects


def read_file(name_of_the_file):
    with open(name_of_the_file, newline='',encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        header = next(reader, None)
        Project = []
        Leader = []
        Binome = []
        Leader_contact = []
        Binome_contact = []
        Leader_tel = []
        Binome_tel = []

        for row in reader:
            if row[0]:
                Project.append(row[0])
            else:
                Project.append("None")
            if row[1]:
                Leader.append(row[1])
            else:
                Leader.append("None")
            if row[2]:
                Binome.append(row[2])
            else:
                Binome.append("None")
            if row[3]:
                Leader_contact.append(row[3])
            else:
                Leader_contact.append("None")
            if row[4]:
                Binome_contact.append(row[4])
            else:
                Binome_contact.append("None")
            if row[5]:
                Leader_tel.append(row[5])
            else:
                Leader_tel.append("None")
            if row[6]:
                Binome_tel.append(row[6])
            else:
                Binome_tel.append("None")

        return Project, Leader, Binome, Leader_contact, Binome_contact, Leader_tel, Binome_tel

def read_effectif(campuss):
    wb_obj = openpyxl.load_workbook("EFFECTIFS_CAMPUS.xlsx",data_only=True)
    sheet = wb_obj[campuss]
    name = []
    promo = []
    contact = []
    equipe = []
    campus = []
    partenaire = []
    sherpa = []
    project = []
    for row in sheet.iter_rows(min_row=2):
        if (not row[0].value):
            break
        promo.append(row[1].value)

        project_name = row[6].value
        if (not project_name):
            project.append(project[len(project) - 1])
        else:
            project.append(project_name)

        first = str(row[2].value).lower()
        first = first[0].upper() + first[1:]
        second = str(row[3].value).lower()
        second = second[0].upper() + second[1:]
        name.append(first + " " + second)
        contact.append(row[4].value)
        equipe.append(row[5].value)
        partenaire.append(row[6].value)
        sherpa_name = row[8].value
        if (not sherpa_name):
            sherpa.append(first_sherpa + " " + second_sherpa)
        else:
            sherpa_list = sherpa_name.split()

            first_sherpa = sherpa_list[0].lower()
            first_sherpa = first_sherpa[0].upper() + first_sherpa[1:]
            second_sherpa = sherpa_list[1].lower()
            second_sherpa = second_sherpa[0].upper() + second_sherpa[1:]

            sherpa.append(first_sherpa + " " + second_sherpa)
        campus.append(campuss)


    return [promo, name, contact, equipe, campus, partenaire, sherpa, project]