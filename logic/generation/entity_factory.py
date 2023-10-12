from model.entity import Entity

player = Entity(char='@', color=(255, 255, 51), name='Player', blocks_movement=True)

orc = Entity(char='o', color=(102, 51, 0), name='Orc', blocks_movement=True)
troll = Entity(char='T', color=(0, 51, 0), name='Troll', blocks_movement=True)