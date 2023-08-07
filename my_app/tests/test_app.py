from my_app.app import main

def test_main():
    assert main() == 'User(name=John, age=35, email=john.doe@gmail.com)'

def test_main_with_args():
    assert main('Jane', 30, 'jane.doe@gmail.com') == 'User(name=Jane, age=30, email=jane.doe@gmail.com)'