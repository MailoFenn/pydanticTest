from pydantic import BaseModel


class Human(BaseModel):
    name: str
    age: int
    affairs: list


class Cat(BaseModel):
    name: str
    age: int
    affairs: list


class Test(BaseModel):
    human: Human
    cat: Cat


my_json = """{
    "human": {
        "name": "Peter",
        "age": "25",
        "affairs": ["walk", "work", "play", "eat", "sleep"]
    },
    "cat": {
        "name": "Garfield",
        "age": 4,
        "affairs": ["eat", "sleep"]
    }
}"""

test = Test.parse_raw(my_json)

print(test.human.name)
print(test.cat.affairs)
