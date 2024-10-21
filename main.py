from modules import database_manager
from modules import web_scrapper
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def menu():
    print()
    print('1) Check changes')
    print('2) Show products')
    print('3) Add product')
    print('4) Delete product')
    print('5) Edit product')
    print('6) Clear products list')
    print('q) Exit')

def print_updated_product(id, name, link, price):
    print(Fore.BLUE)
    print(f"\n{'-' * 50}")
    print(f'{Fore.RED}¡PRODUCTO ACTUALIZADO!{Fore.RESET}')
    print(f'{Style.BRIGHT}ID:{Style.NORMAL} {id}')
    print(f'{Style.BRIGHT}Name:{Style.NORMAL} {name}')
    print(f'{Style.BRIGHT}Link:{Style.NORMAL} {link}')
    print(f'{Style.BRIGHT}Price:{Style.NORMAL} {price}€')
    print(f"{'-' * 50}")
    print(Fore.RESET)

def check_changes():
    rows = db_manager.select_all_rows()
    for row in rows:
        db_id, db_name, db_link, db_price = row
        actual_price = scrapper.get_price(db_link)
        if actual_price != None:
            if actual_price != db_price:
                print_updated_product(db_id, db_name, db_link, actual_price)
                db_manager.edit_row(db_id, db_name, db_link, actual_price)

    scrapper.destruct_driver()

def show_products():
    rows = db_manager.select_all_rows()
    if len(rows) < 1:
        print('No hay  productos en la base de datos.')
        return
    for row in rows:
        db_id, db_name, db_link, db_price = row
        print(Fore.BLUE)
        print(f'\n{'-' * 50}')
        print(f'{Style.BRIGHT}ID:{Style.NORMAL} {db_id}')
        print(f'{Style.BRIGHT}Name:{Style.NORMAL} {db_name}')
        print(f'{Style.BRIGHT}Link:{Style.NORMAL} {db_link}')
        print(f'{Style.BRIGHT}Price:{Style.NORMAL} {db_price}€')
        print(f'{'-' * 50}')
        print(Fore.RESET)

def add_row():
    name = input('Product name: ')
    link = input('Product link: ')
    price = None
    while price == None:
        try:
            price = float(input('Product price: '))
        except ValueError:
            price = None

    db_manager.add_row(name, link, price)

    print('Row was succesfully added')

def delete_row():
    rows = db_manager.select_all_rows()
    if len(rows) < 1:
        print('No hay filas para eliminar.')
        return

    id_options = []

    for row in rows:
        db_id, db_name, db_link, db_price = row
        print(f'{db_id}) {db_name}')
        id_options.append(db_id)

    while True:
        try:
            id = int(input('ID de la fila que deseas eliminar: '))
            if id in id_options:
                break
            else:
                print('ID fuera de rango.')
        except ValueError:
            print('Por favor, introduce un número válido.')

    try:
        db_manager.delete_row(id)
        print('Fila eliminada con éxito.')
    except Exception as e:
        print(f'Error al eliminar la fila: {e}')

def edit_row():
    rows = db_manager.select_all_rows()
    if len(rows) < 1:
        print('No hay filas para editar.')
        return
    
    id_options = []

    for row in rows:
        db_id, db_name, db_link, db_price = row
        print(f'{db_id}) {db_name}')
        id_options.append(db_id)

    while True:
        try:
            id = int(input('ID de la fila que deseas editar: '))
            if id in id_options:
                break
            else:
                print('ID fuera de rango.')
        except ValueError:
            print('Por favor, introduce un número válido.')

    new_name = input('Nuevo nombre del producto: ')
    new_link = input('Nuevo enlace del producto: ')

    while True:
        try:
            new_price = float(input('Nuevo precio del producto: '))
            break
        except ValueError:
            print('Introduce un precio válido.')

    try:
        db_manager.edit_row(id, new_name, new_link, new_price)
        print('Fila editada con éxito.')
    except Exception as e:
        print(f'Error al editar la fila: {e}')

def clear_rows():
    answer = input('Are you sure? [y]es | [n]ot: ')
    while answer.lower() not in ['y', 'n']:
        answer = input('Are you sure? [Y]es | [N]ot')
    
    if answer.lower() == 'y':
        db_manager.clear_table()
        return
    else:
        return

def main():
    menu()

    answer = input('Elige qué quieres hacer: ')
    while answer not in ['1', '2', '3', '4', '5', '6', 'q']:
        answer = input('Elige qué quieres hacer: ')

    match answer:
        case '1':
            check_changes()
        case '2':
            show_products()
        case '3':
            add_row()
        case '4':
            delete_row()
        case '5':
            edit_row()
        case '6':
            clear_rows()
        case 'q':
            print('Saliendo del programa...')
            scrapper.destruct_driver()
            exit()

if __name__ == '__main__':
    # Scrapper
    scrapper = web_scrapper.web_scrapper()

    # DB manager
    db_manager = database_manager.database('products.db')
    db_manager.create_db()
    db_manager.create_table()

    while True:
        main()