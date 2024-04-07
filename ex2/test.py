import naval_battle


naval_battle.NavalBattle.playing_field = [
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
]

player_1 = naval_battle.NavalBattle('📍')
player_2 = naval_battle.NavalBattle('📎')

naval_battle.NavalBattle.show()
player_1.shot(1, 1)
naval_battle.NavalBattle.show()
player_2.shot(4, 2)
naval_battle.NavalBattle.show()
