import Repository.PersonRepository as PersonRepo

class PersonViewModel: 
    personRepo = PersonRepo.PersonRepo()
    title = ""

    def __init__(self):
        self.fetch_title_from_repo()

    def get_title(self):
        return self.title

    def fetch_title_from_repo(self):
        self.title = self.personRepo.fetch_title()