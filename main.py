from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, StructuredRel)
from neo4j import GraphDatabase
import parcours_csv


class appli:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    def reset(self):
        with self.driver.session() as session:
            node_id = session.write_transaction(reset_tx)

    def create_relation(self, first_type, list_one, second_type, list_second, nature):
        with self.driver.session() as session:
            node_id = session.write_transaction(create_relation_tx, first_type, list_one, second_type, list_second, nature)

    def create_single_relation(self, first_type, list_one, second_type, list_second, nature):
        with self.driver.session() as session:
            node_id = session.write_transaction(create_single_relation_tx, first_type, list_one, second_type, list_second, nature)

def create_single_relation_tx(tx, first_type,list_one, second_type, list_second, nature):
    create_relation(tx,first_type,list_one,second_type,list_second,nature)

def create_relation_tx(tx, first_type,list_one, second_type, list_second, nature):
    for i in range(0,len(list_one),1):
        create_relation(tx, first_type, list_one[i], second_type, list_second[i], nature)


def create_relation(tx, first_type, first, second_type, second, nature):
        toto = "match (a:%s{name: $project_name }) match (b:%s{name: $lead_name}) create( (b)-[r:%s]->(a))RETURN r" % (first_type, second_type, nature)
        tx.run(toto, project_name=first, lead_name=second)


def reset_tx(tx):
    result = tx.run("MATCH (n) DETACH DELETE n")


class Project(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)


class Lead(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    contact = StringProperty(unique_index=True)
    tel = StringProperty(unique_index=True)

class Student(StructuredNode):
    uid = UniqueIdProperty()
    promo = StringProperty(unique_index=True)
    name = StringProperty(unique_index=True)
    contact = StringProperty(unique_index=True)
    equipe = IntegerProperty(unique_index=True)
    campus = StringProperty(unique_index=True)



class Sherpa(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    contact = StringProperty(unique_index=True)
    campus = StringProperty(unique_index=True)


class Binome(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    contact = StringProperty(unique_index=True)
    tel = StringProperty(unique_index=True)


def create_student(promo_list,name_list,contact_list,equipe_list,campus_list):
    for i in range(0, len(name_list), 1):
        toto = Student(promo=promo_list[i],name=name_list[i], contact=contact_list[i],equipe=equipe_list[i],campus=campus_list[i]).save()


def create_sherpa(name_list, contact_list, campus_list):
    for i in range(0, len(name_list), 1):
        toto = Sherpa(name=name_list[i], contact=contact_list[i], campus=campus_list[i]).save()


def create_binome(name_list, contact_list, tel_list):
    for i in range(0, len(name_list), 1):
        toto = Binome(name=name_list[i], contact=contact_list[i], tel=tel_list[i]).save()


def create_project(name_list):
    for p in name_list:
        toto = Project(name = p).save()


def create_lead(name_list, contact_list, tel_list):
    for i in range(0,len(name_list),1):
        toto = Lead(name=name_list[i],contact=contact_list[i],tel=tel_list[i]).save()


def collect_infos_leads(file_name):
    a, b, c, d, e, f, g = parcours_csv.read_file(file_name)
    infos = [a, b, c, d, e, f, g]
    value = ["Project", "Lead", "Binome", "Lead_contact", "Binome_contact", "Lead_tel", "Binome_tel"]
    return infos, value


def collect_infos_sherpa(file_name):
    a, b, c, d = parcours_csv.read_json(file_name)
    infos = [a,b,c,d]
    value = ["Sherpa", "Contact", "Campus", "Project"]
    return infos, value

def create_teams_and_relation(name_list, equipe_list, sherpa_list,project_liste,app):
    lead = []
    others = []
    current_team = 0
    current_lead = "bz"
    for i in range(len(name_list)):

        if current_team == equipe_list[i] :
            app.create_single_relation("Student",current_lead,"Student",name_list[i],"LEAD_BY")

            others.append(name_list[i])
            lead.append(current_lead)

        else:
            app.create_single_relation( "Sherpa", sherpa_list[i],"Student", current_lead, "SUPERVISED_BY")
            app.create_single_relation( "Project", project_liste[i],"Student", current_lead, "WORKING_ON")
            current_team = current_team + 1
            current_lead = name_list[i]
            lead.append(current_lead)
            others.append(current_lead)
    return lead, others



def formate_sherpa(sherpa_name_liste,camp):
    campus = []
    sherpa_fin_name = []
    contact = []
    cur_name = " "
    for i in sherpa_name_liste:
        if cur_name != i:
            sherpa_fin_name.append(i)
            cur_name = i

    for i in sherpa_fin_name:
        campus.append(camp)

    for i in sherpa_fin_name:
        stock = parcours_csv.check_json(i)
        if stock:
            contact.append(stock)
        else:
            toto = i.split()
            first = toto[0]
            second = toto[1]
            contact.append(first + '.' + second + '@isg.fr')

    create_sherpa(sherpa_fin_name,contact,campus)
    return sherpa_fin_name


def formate_project(project_name_liste):
    project_fin_name = []
    cur_name = " "
    for i in project_name_liste:
        if cur_name != i:
            project_fin_name.append(i)
            cur_name = i


    create_project(project_fin_name)
    return project_fin_name





def import_files(app):

    #FIRST CSV
    #infos, val = collect_infos_leads("liste_leads.csv")

    #create_project(infos[0])
    #create_lead(infos[1], infos[3], infos[5])
    #create_binome(infos[2], infos[4], infos[6])
    #app.create_relation("Project", infos[0], "Lead", infos[1], "WORKED_ON")

    #app.create_relation("Lead", infos[1], "Binome", infos[2], "WORKED_WITH")

    #SECOND Json
    #infos, val = collect_infos_sherpa("sherpas.json")
    #create_sherpa(infos[0], infos[1], infos[2])

    #THIRD Effectifs campus by campus
    val_Lille = parcours_csv.read_effectif("ISG_Lille")


    formate_sherpa(val_Lille[6],'Lille')
    formate_project(val_Lille[5])
    create_student(val_Lille[0],val_Lille[1],val_Lille[2],val_Lille[3],val_Lille[4])

    create_teams_and_relation(val_Lille[1],val_Lille[3],val_Lille[6],val_Lille[5],app)

    print(val_Lille[7])
    val_Lyon = parcours_csv.read_effectif("ISG_Lyon")

    formate_sherpa(val_Lyon[6], 'Lyon')
    formate_project(val_Lyon[5])
    create_student(val_Lyon[0], val_Lyon[1], val_Lyon[2], val_Lyon[3], val_Lyon[4])

    create_teams_and_relation(val_Lyon[1], val_Lyon[3], val_Lyon[6],val_Lyon[5], app)





def anyhow():
    test = appli("bolt://localhost:7687", "neo4j", "1234")
    test.reset()
    config.DATABASE_URL = 'bolt://neo4j:1234@localhost:7687'
    import_files(test)

    test.close()

if __name__ == "__main__":
    anyhow()