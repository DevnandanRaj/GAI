employees=[
    {"name":"Jhon","skills":["Python","Database"],"current_project":None},
    {"name":"Emma","skills":["Java","Testing"],"current_project":None},
    {"name":"Kelly","skills":["Python","Java"],"current_project":None}
]

projects=[
    {"name":"Project A","required_skills":["Python","Database"]},
    {"name":"Project B","required_skills":["Java","Testing"]},
    {"name":"Project C","required_skills":["Python","Java"]}
]

def allocate_projects(employees, projects):
    alocatedPrjects=[]
    for project in projects:
        project_name=project["name"]
        required_skils=set(project["required_skills"])
        for employee in employees:
            if employee["current_project"]is None and required_skils.issubset(set(employee["skills"])):
                employee["current_project"]=project_name
                alocatedPrjects.append({"employee":employee["name"],"project":project_name})
                break
    return alocatedPrjects        
res=allocate_projects(employees,projects);
print(res)