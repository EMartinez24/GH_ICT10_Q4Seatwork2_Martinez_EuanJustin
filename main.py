from pyscript import display, document


class Classmate:
    def __init__(self, name, section, fav_subject):
        self.name = name
        self.section = section
        self.fav_subject = fav_subject

    def introduce(self):
        display(f'Hi! I am {self.name} from {self.section}. My favorite subject is {self.fav_subject}.')


classmates_list = [
    Classmate('Kelsey Medina', 'Sapphire', 'Physical Education'),
    Classmate('Alijah Lagman', 'Sapphire', 'Math'),
    Classmate('Adrianna Garces', 'Sapphire', 'TLE'),
    Classmate('Harvey Dolor', 'Sapphire', 'Science'),
    Classmate('Aaron Dee', 'Sapphire', 'English'),
]


def create_classmate(e):
    name = document.getElementById('name1').value
    section = document.getElementById('section1').value
    subject = document.getElementById('subject1').value

    if name and section and subject:
        new_classmate = Classmate(name, section, subject)
        classmates_list.append(new_classmate)

    document.getElementById('name1').value = ''
    document.getElementById('section1').value = ''
    document.getElementById('subject1').value = ''

    display(f'Classmate added successfully!', target='output')


def display_all(e):
    document.getElementById('output').innerHTML = ' '

    for classmate in classmates_list:
        classmate.introduce()
