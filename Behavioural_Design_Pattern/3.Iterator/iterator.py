from __future__ import annotations
from dataclasses import dataclass

from typing import ClassVar, List, Protocol


@dataclass
class Profile:
    id: int
    email: str


@dataclass
class SocialNetwork(Protocol):
    platform: ClassVar[str]

    def create_friends_iterator(self, profile_id: int) -> ProfileIterator:
        ...

    def create_coworkers_iterator(self, profile_id: int) -> ProfileIterator:
        ...


@dataclass
class Facebook:
    platform: ClassVar[str] = "facebook"

    def create_friends_iterator(self, profile_id: int) -> ProfileIterator:
        return FacebookIterator(self, profile_id, "friends")

    def create_coworkers_iterator(self, profile_id: int) -> ProfileIterator:
        return FacebookIterator(self, profile_id, "coworkers")

    def social_graph_request(self, profile_id: int, type: str) -> List[Profile]:
        if type == "friends":
            return [
                Profile(1, "ram@friend.com"),
                Profile(2, "shyam@friend.com"),
                Profile(5, "hari@friend.com"),
            ]
        elif type == "coworkers":
            return [Profile(3, "sita@coworker.com"), Profile(4, "geeta@coworker.com")]
        return []


class ProfileIterator(Protocol):
    def get_next(self) -> Profile:
        ...

    def has_more(self) -> bool:
        ...


@dataclass
class FacebookIterator(ProfileIterator):
    facebook: Facebook
    profile_id: int
    type: str
    current_position: int = 0
    cache: List[Profile] = None

    def lazy_init(self):
        if self.cache is None:
            self.cache = self.facebook.social_graph_request(self.profile_id, self.type)

    def get_next(self):
        if self.has_more():
            profile = self.cache[self.current_position]
            self.current_position += 1
            return profile

    def has_more(self):
        self.lazy_init()
        return len(self.cache) > self.current_position


class SocialSpammer:
    def send(self, iterator: ProfileIterator, message: str):
        while iterator.has_more():
            profile = iterator.get_next()
            print(f"Emailing: {profile.email}: {message}")


@dataclass
class Application:
    network: SocialNetwork
    spammer: SocialSpammer

    def __init__(self, platform: str):
        self.config(platform)

    def config(self, platform: str):
        if platform == "facebook":
            self.network = Facebook()
        self.spammer = SocialSpammer()

    def send_spam_to_friends(self, profile_id: int, message: str = ""):
        iterator = self.network.create_friends_iterator(profile_id)
        self.spammer.send(iterator, message)

    def send_spam_to_coworkers(self, profile_id: int, message: str = ""):
        iterator = self.network.create_coworkers_iterator(profile_id)
        self.spammer.send(iterator, message)


"""
Iterator pattern provides a medium to iterator over bunch of
objects in a ordered fashion. Here we've used an example of
mass scammer that sends email to all friends or coworkers
at once. Here we created Iterator for all those categories.
In future, we can also add other Social Media Platform like
LinkedIn, etc.
"""


if __name__ == "__main__":
    app = Application("facebook")
    my_profile_id = 100
    app.send_spam_to_friends(my_profile_id, "Hello Friend")
    app.send_spam_to_coworkers(my_profile_id, "Hello coworker")
