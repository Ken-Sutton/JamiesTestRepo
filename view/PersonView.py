import viewModel.PersonViewModel as VM

class PresonView: 
    personViewModel = None
    def __init__(self):
        self.personViewModel = VM.PersonViewModel()

    def __str__(self):
        return (self.personViewModel.get_title())