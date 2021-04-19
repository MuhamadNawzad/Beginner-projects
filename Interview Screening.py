applicant_dict = {'anna': {'experience': 4, 'languages': ['python', 'c++', 'java'], 'project': False},
                  'jack': {'experience': 5, 'languages': ['python', 'c++', 'php'], 'project': True},
                  'john': {'experience': 8, 'languages': ['python', 'java', 'c++', 'c#'], 'project': True},
                  'smith': {'experience': 5, 'languages': ['python', 'java', 'c++', 'php'], 'project': False}}
min_experience = 4
languages_req = ['java', 'python']
project_supervision = True

for person, tasks in applicant_dict.items():
    if min_experience <= tasks['experience'] and \
            (set(languages_req).issubset(tasks['languages']) or tasks['project']):
        print(person)