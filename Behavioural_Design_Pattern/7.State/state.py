from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class State(ABC):
    player: AudioPlayer

    @abstractmethod
    def click_lock(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def click_play(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def click_next(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def click_previous(self) -> None:
        raise NotImplementedError


class LockedState(State):
    def click_lock(self) -> None:
        if self.player.playing:
            self.player.change_state(PlayingState(self.player))
        else:
            self.player.change_state(ReadyState(self.player))

    def click_play(self) -> None:
        return NotImplemented

    def click_next(self) -> None:
        return NotImplemented

    def click_previous(self) -> None:
        return NotImplemented


class ReadyState(State):
    def click_lock(self) -> None:
        self.player.change_state(LockedState(self.player))

    def click_play(self) -> None:
        self.player.start_playback()
        self.player.change_state(PlayingState(self.player))

    def click_next(self) -> None:
        self.player.next_song()

    def click_previous(self) -> None:
        self.player.previous_song()


class PlayingState(State):
    def click_lock(self) -> None:
        self.player.change_state(LockedState(self.player))

    def click_play(self) -> None:
        self.player.stop_playback()
        self.player.change_state(ReadyState(self.player))

    def click_next(self) -> None:
        self.player.next_song()

    def click_previous(self) -> None:
        self.player.previous_song()


@dataclass
class AudioPlayer:
    state: State = None
    playlist: List[str] = field(default_factory=list)
    current_song: str = None
    playing: bool = False
    index: int = 0

    def initialize(self, playlist: List[str] = []) -> AudioPlayer:
        self.state = ReadyState(self)
        self.playlist = playlist
        return self

    def change_state(self, state: State) -> None:
        self.state = state

    def start_playback(self) -> None:
        if not self.current_song:
            self.current_song = self.playlist[self.index]
        self.playing = True

    def stop_playback(self) -> None:
        self.playing = False

    def next_song(self) -> None:
        if self.index >= len(self.playlist) - 1:
            raise ValueError("No next song")
        self.index += 1
        self.current_song = self.playlist[self.index]

    def previous_song(self) -> None:
        if self.index <= 0:
            raise ValueError("No previous song")
        self.index -= 1
        self.current_song = self.playlist[self.index]


"""
In State pattern, the overall behaviour of object changes
as the state changes. The action of the objects depend directly
on the state of the object. The state does know about other states
and can transfer the state of Context from one to another.
"""


if __name__ == "__main__":
    player = AudioPlayer().initialize(playlist=["adele", "arjun", "aryan"])
    while True:
        choice = input(f"{player} [L/P/n/p]: ")
        if choice == "L":
            player.state.click_lock()
        elif choice == "P":
            player.state.click_play()
        elif choice == "n":
            player.state.click_next()
        elif choice == "p":
            player.state.click_previous()
        else:
            print("Closing Player")
            break
