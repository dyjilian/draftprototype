from dataclasses import dataclass
from drafter import *

#dataclasses

@dataclass
class Move:
    name:str
    dmg:float
    status:str
    accuracy:float

@dataclass
class Character:
    name:str
    current_hp:int
    max_hp:int
    move1: Move
    move2: Move
@dataclass
class State:
    player_name:str
    roster: list[Character]
    active_player: Character
    enemy: Character
    battle_log:str






#routes
    #this is the protype and i just need the homescreen to work for now before i go into the complex combat.
@route
def index(state: State) -> Page:
    return Page(
        state,
        [Text("RPG game"),
         Button("Start Game", index)
         ])
    
    
if __name__ == "__main__":
    initial_state = State(
        player_name="",
        roster=[],
        active_player=Character("", 0, 0, Move("", 0.0, "", 0.0), Move("", 0.0, "", 0.0)),
        enemy=Character("", 0, 0, Move("", 0.0, "", 0.0), Move("", 0.0, "", 0.0)),
        battle_log=""
    )
    start_server(initial_state)

