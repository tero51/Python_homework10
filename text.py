main_menu = ['Main menu',
             'Open file',
             'Save file',
             'Show contact',
             'Create contact',
             'Find contact',
             'Change contact',
             'Delete contact',
             'Exit']

main_menu_choice = 'Choice menu: '
load_successful = 'Phonebook is successfully loaded'
epmty_phone_book = 'Empty'
save_successful = 'Save successful!'

new_contact = ['Enter name: ',
               'Enter phone number: ',
               'Enter comment: ']

def new_contact_added_successful(name: str) -> str:
    return f'Contact {name} successful added!'

input_search_word = 'Enter searching word: '

def contacts_not_found(word: str) -> str:
    return f'Contacts containing {word} not found!'

input_id_change_contact = 'Enter ID contact you wanna change: '

change_contact = ['Input new name or ENTER if you dont wanna change: ',
                'Input new phone number name or Enter if you dont wanna change: ',
                'Input new comment name or Enter if you dont wanna change: ']

def contact_changed_seccessful(name: str) -> str:
    return f'Contact {name} successful changed!'

input_id_delete_contact = 'Enter ID contact you wanna delete: '

def contact_deleted_seccessful(name: str) -> str:
    return f'Contact {name} successful deleted!'

good_bye = 'See you later, dirty python'