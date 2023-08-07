from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str
    
    def __repr__(self):
        return f'User(name={self.name}, age={self.age}, email={self.email})'
