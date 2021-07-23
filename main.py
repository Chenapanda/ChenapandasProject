from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, StructuredRel)
from neo4j import GraphDatabase
import parcours_csv


class appli:
    """
    A class to modify the nodes for neo4j.

    ...

    Attributes
    ----------
    None
    Methods
    -------
    close():
        closes the driver connection
    reset():
        resets the driver connection
    create_relation(first_type, list_one, second_type, list_second, nature):
        creates relations between two lists of objects
    create_single_relation( first_type, list_one, second_type, list_second, nature):
        creates a relation between two objects
    """
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
    """
    A class to represent a project.

    ...

    Attributes
    ----------
    uid : id
        uid of the project
    name : str
        name of the project
    Methods
    -------
    None
    """
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)


class Lead(StructuredNode):
    """
    A class to represent the lead of a project.

    ...

    Attributes
    ----------
    uid : id
        uid of the person that leads the project
    name : str
        name of the person that leads the project
    contact : str
        email adress of the person that leads the project
    tel : str
        telephone number of the person that leads the project
    Methods
    -------
    None
    """
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    contact = StringProperty(unique_index=True)
    tel = StringProperty(unique_index=True)

class Student(StructuredNode):
    """
    A class to represent a student on a project.

    ...

    Attributes
    ----------
    uid : id
        uid of the student
    promo : str
        promotion of the student
    name : str
        name of the student
    contact : str
        email adress of the student
    equipe : int
        number of the student's team
    campus : str
        campus of the student
    Methods
    -------
    None
    """
    uid = UniqueIdProperty()
    promo = StringProperty(unique_index=True)
    name = StringProperty(unique_index=True)
    contact = StringProperty(unique_index=True)
    equipe = IntegerProperty(unique_index=True)
    campus = StringProperty(unique_index=True)



class Sherpa(StructuredNode):
    """
        A class to represent a Sherpa.

        ...

        Attributes
        ----------
        uid : id
            uid of the Sherpa
        name : str
            name of the Sherpa
        contact : str
            email adress of the Sherpa
        campus : str
            campus of the Sherpa
        Methods
        -------
        None
        """
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    contact = StringProperty(unique_index=True)
    campus = StringProperty(unique_index=True)


class Binome(StructuredNode):
    """
        A class to represent the second lead of a project, the second.

        ...

        Attributes
        ----------
        uid : id
            uid of the second
        name : str
            name of the second
        contact : str
            email adress of the second
        tel : str
            telephone number of the second
        Methods
        -------
        None
        """
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    contact = StringProperty(unique_index=True)
    tel = StringProperty(unique_index=True)


def create_student(promo_list,name_list,contact_list,equipe_list,campus_list):
    '''
    Creates objects of the Student class

            Parameters:
                    promo_list ([str]): List of the promotions of the student
                    name_list ([str]): List of the names of the student
                    contact_list ([str]): List of the email addresses of the student
                    equipe_list ([str]): List of the teams of the student
                    campus_list ([str]): List of the campus of the student

            Returns:
                    None
    '''
    for i in range(0, len(name_list), 1):
        toto = Student(promo=promo_list[i],name=name_list[i], contact=contact_list[i],equipe=equipe_list[i],campus=campus_list[i]).save()


def create_sherpa(name_list, contact_list, campus_list):
    '''
    Creates objects of the Sherpa class

            Parameters:
                    name_list ([str]): List of the names of the sherpas
                    contact_list ([str]): List of the email addresses of the sherpas
                    campus_list ([str]): List of the campus of the sherpas

            Returns:
                    None
    '''
    for i in range(0, len(name_list), 1):
        toto = Sherpa(name=name_list[i], contact=contact_list[i], campus=campus_list[i]).save()


def create_binome(name_list, contact_list, tel_list):
    '''
    Creates objects of the Binome class

            Parameters:
                    name_list ([str]): List of the names of the seconds
                    contact_list ([str]): List of the email addresses of the seconds
                    tel_list ([str]): List of the telephone numbers of the seconds

            Returns:
                    None
    '''
    for i in range(0, len(name_list), 1):
        toto = Binome(name=name_list[i], contact=contact_list[i], tel=tel_list[i]).save()


def create_project(name_list):
    '''
    Creates objects of the Project class

            Parameters:
                    name_list ([str]): List of the names of the projects

            Returns:
                    None
    '''
    for p in name_list:
        toto = Project(name = p).save()


def create_lead(name_list, contact_list, tel_list):
    '''
    Creates objects of the Lead class

            Parameters:
                    name_list ([str]): List of the names of the lead
                    contact_list ([str]): List of the email addresses of the lead
                    tel_list ([str]): List of the telephone numbers of the lead

            Returns:
                    None
    '''
    for i in range(0,len(name_list),1):
        toto = Lead(name=name_list[i],contact=contact_list[i],tel=tel_list[i]).save()


def collect_infos_leads(file_name):
    '''
    Collects information on the read file

            Parameters:
                    file_name (str): name of the file to collect lead infos from

            Returns:
                    infos ([str]): informations about the lead
                    value ([str]): titles of the informations
    '''
    a, b, c, d, e, f, g = parcours_csv.read_file(file_name)
    infos = [a, b, c, d, e, f, g]
    value = ["Project", "Lead", "Binome", "Lead_contact", "Binome_contact", "Lead_tel", "Binome_tel"]
    return infos, value

def create_teams_and_relation(name_list, equipe_list, sherpa_list,project_liste,app):
    '''
    Creates teams and relations between the lead, the second, the sherpas, the students and the project

            Parameters:
                    name_list ([str]): names of the students
                    equipe_list ([str]): names of the teams
                    sherpa_list ([str]): names of the sherpas
                    project_liste ([str]): names of the projects
                    app (appli): object of the appli class

            Returns:
                    lead ([str]): names of the leads
                    others ([str]): names o other people working on the project
    '''
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
    '''
    Normalises the names of the sherpas from the files

            Parameters:
                    sherpa_name_liste ([str]): names of the sherpas
                    camp (str): campus

            Returns:
                    sherpa_fin_name ([str]): fixed names of the sherpas
    '''
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
    '''
    Normalises the names of the projects from the files

            Parameters:
                    project_name_liste ([str]): names of the projects

            Returns:
                    project_fin_name ([str]): fixed names of the projects
    '''
    project_fin_name = []
    cur_name = " "
    for i in project_name_liste:
        if cur_name != i and i:
            toto = Project.nodes.first_or_none(name= i)
            if not toto:
                project_fin_name.append(i)
                cur_name = i


    create_project(project_fin_name)
    return project_fin_name

def import_files(app):
    '''
    Reads the files and creates nodes, also creates relations between the nodes.

            Parameters:
                    app (appli): application for neo4j

            Returns:
                    None
    '''
    #FIRST CSV
    infos, val = collect_infos_leads("liste_leads.csv")

    create_lead(infos[1], infos[3], infos[5])
    create_binome(infos[2], infos[4], infos[6])
    app.create_relation("Lead", infos[1], "Binome", infos[2], "WORKED_WITH")

    #Effectifs campus by campus
    cities = ["Lille", "Lyon", "Bordeaux", "Paris", "Strasbourg", "Toulouse"]

    for city in cities:
        val = parcours_csv.read_effectif("ISG_" + city)
        formate_sherpa(val[6], city)
        formate_project(val[5])
        create_student(val[0],val[1],val[2],val[3],val[4])
        create_teams_and_relation(val[1],val[3],val[6],val[5],app)

    app.create_relation("Project", infos[0], "Lead", infos[1], "WORKED_ON")

def anyhow():
    '''
    Resets and launches the application for neo4j and launches the project

            Parameters:
                    None

            Returns:
                    None
    '''
    test = appli("bolt://localhost:7687", "neo4j", "1234")
    test.reset()
    config.DATABASE_URL = 'bolt://neo4j:1234@localhost:7687'
    import_files(test)

    test.close()

if __name__ == "__main__":
    anyhow()