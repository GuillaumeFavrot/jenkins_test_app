from models.user import User


def main(first_name: str = 'John', age: int = 35, email: str = 'john.doe@gmail.com') -> str:
    user = User(first_name, age, email)

    print(user.__repr__())
            
    return user.__repr__()

if __name__ == '__main__':
    main()