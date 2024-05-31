import book
import user
import check
import storage
import logging
import models

# Main Menu
def main_menu():
    print("\nLibrary Management System")
    print("1. Manage Books")
    print("2. Manage Users")
    print("3. Checkout/Return Books")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

# Checkout/Return Menu
def checkout_menu():
    print("\nCheckout/Return Menu")
    print("1. Checkout Book")
    print("2. Return Book")
    print("3. Back to Main Menu")
    choice = input("Enter your choice: ")
    return choice

# Book Management Menu
def book_menu():
    print("\nBook Management")
    print("1. Add Book")
    print("2. List Books")
    print("3. Search Books")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Back to Main Menu")
    choice = input("Enter your choice: ")
    return choice

# User Management Menu
def user_menu():
    print("\nUser Management")
    print("1. Add User")
    print("2. List Users")
    print("3. Search Users")
    print("4. Update User")
    print("5. Delete User")
    print("6. Back to Main Menu")
    choice = input("Enter your choice: ")
    return choice

def main():
    # Load data from storage
    storage.load_data() 

    while True:
        choice = main_menu()
        if choice == '1':
            while True:
                book_choice = book_menu()
                if book_choice == '1':
                    title = input("Enter title: ")
                    author = input("Enter author: ")
                    isbn = input("Enter ISBN: ")
                    if not models.is_valid_isbn(isbn):
                        print("Invalid ISBN format. Please try again.")
                        continue
                    if storage.is_book_exists(isbn):
                        print("Book with this ISBN already exists.")
                        continue
                    new_book = book.Book(title, author, isbn)
                    storage.add_book(new_book) 
                    logging.info(f"Book added: {new_book}")
                    print("Book added.")
                elif book_choice == '2':
                    all_books = storage.get_all_books() 
                    if all_books:
                        for b in all_books:
                            print(b)
                    else:
                        print("No books in the library.")
                elif book_choice == '3':
                    search_term = input("Enter search term (title, author, or ISBN): ")
                    search_results = models.search_books(search_term)
                    if search_results:
                        for b in search_results:
                            print(b)
                    else:
                        print("No books found matching the search term.")
                elif book_choice == '4':
                    isbn = input("Enter ISBN of the book to update: ")
                    book_to_update = storage.get_book_by_isbn(isbn)
                    if book_to_update:
                        title = input(f"Enter new title (current: {book_to_update.title}): ")
                        author = input(f"Enter new author (current: {book_to_update.author}): ")
                        book_to_update.title = title
                        book_to_update.author = author
                        logging.info(f"Book updated: {book_to_update}")
                        print("Book updated.")
                    else:
                        print("Book not found.")
                elif book_choice == '5':
                    isbn = input("Enter ISBN of the book to delete: ")
                    if storage.delete_book_by_isbn(isbn):
                        logging.info(f"Book deleted: ISBN {isbn}")
                        print("Book deleted.")
                    else:
                        print("Book not found.")
                elif book_choice == '6':
                    break
                else:
                    print("Invalid choice, please try again.")

        elif choice == '2':
            while True:
                user_choice = user_menu()
                if user_choice == '1':
                    name = input("Enter user name: ")
                    user_id = input("Enter user ID: ")
                    if storage.is_user_exists(user_id):
                        print("User with this ID already exists.")
                        continue
                    new_user = user.User(name, user_id)
                    storage.add_user(new_user)
                    logging.info(f"User added: {new_user}")
                    print("User added.")
                elif user_choice == '2':
                    all_users = storage.get_all_users() 
                    if all_users:
                        for u in all_users:
                            print(u)
                    else:
                        print("No users in the library.")
                elif user_choice == '3':
                    search_term = input("Enter search term (name or user ID): ")
                    search_results = models.search_users(search_term)
                    if search_results:
                        for u in search_results:
                            print(u)
                    else:
                        print("No users found matching the search term.")
                elif user_choice == '4':
                    user_id = input("Enter User ID of the user to update: ")
                    user_to_update = storage.get_user_by_id(user_id)
                    if user_to_update:
                        name = input(f"Enter new name (current: {user_to_update.name}): ")
                        user_to_update.name = name
                        logging.info(f"User updated: {user_to_update}")
                        print("User updated.")
                    else:
                        print("User not found.")
                elif user_choice == '5':
                    user_id = input("Enter User ID of the user to delete: ")
                    if storage.delete_user_by_id(user_id):
                        logging.info(f"User deleted: ID {user_id}")
                        print("User deleted.")
                    else:
                        print("User not found.")
                elif user_choice == '6':
                    break
                else:
                    print("Invalid choice, please try again.")

        elif choice == '3':
            while True:
                checkout_choice = checkout_menu()
                if checkout_choice == '1':
                    user_id = input("Enter user ID: ")
                    book_title = input("Enter title of the book to checkout: ")
                    search_results = storage.search_books(book_title)
                    if search_results:
                        print("\nDo you mean one of these books?")
                        for i, b in enumerate(search_results):
                            print(f"{i+1}. {b.title}")
                        choice = input("Enter the number of the book (or 0 to cancel): ")
                        if choice.isdigit():
                            choice_index = int(choice) - 1
                            if 0 <= choice_index < len(search_results):
                                book_to_checkout = search_results[choice_index]
                                if book_to_checkout and book_to_checkout.is_available:
                                    new_checkout = check.Checkout(user_id, book_to_checkout.isbn)
                                    storage.add_checkout(new_checkout)
                                    book_to_checkout.mark_as_checked_out()  # Mark the book as unavailable
                                    storage.update_book(book_to_checkout)  # Update book in storage
                                    logging.info(f"Book checked out: {book_to_checkout} by User ID: {user_id}")
                                    print("Book checked out.")
                                else:
                                    print("Book is not available for checkout.")
                            else:
                                print("Invalid choice.")
                        else:
                            print("Invalid input.")
                    else:
                        print("No books found matching the title.")
                elif checkout_choice == '2':
                    user_id = input("Enter user ID: ")
                    isbn = input("Enter ISBN of the book to return: ")

                    book_to_return = storage.get_book_by_isbn(isbn)
                    checkout_record = storage.get_checkout_by_user_id_and_isbn(user_id, isbn)

                    if book_to_return and checkout_record:
                        book_to_return.mark_as_returned()  # Mark the book as available
                        storage.update_book(book_to_return)  # Update book in storage
                        storage.remove_checkout(checkout_record)
                        logging.info(f"Book returned: {book_to_return} by User ID: {user_id}")
                        print("Book returned successfully.")
                    else:
                        print("Book or checkout record not found.")
                elif checkout_choice == '3':
                    break
                else:
                    print("Invalid choice, please try again.")

        elif choice == '4':
            # Save data before exiting
            storage.save_data()
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()