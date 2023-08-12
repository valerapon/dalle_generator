class Category():
    ID_SET = set()
    ID_TO_NAME = dict()
    ID_TO_PROMPT = dict()
    ID_TO_PARENT_ID = dict()
    ID_TO_OBJ = dict()

    def __init__(self, name, id, parent_id, prompt):
        self.name = name
        self.id = id
        self.parent_id = parent_id
        self.prompt = prompt

        if id in self.ID_SET:
            raise Exception('id {} has been all ready created'.format(id))
        
        self.ID_SET.add(id)
        self.ID_TO_NAME[id] = name
        self.ID_TO_PROMPT[id] = prompt
        self.ID_TO_PARENT_ID[id] = parent_id
        self.ID_TO_OBJ[id] = self
        self.parent = self.ID_TO_OBJ[parent_id]

def make_hierachy():
    Category(name='Категория', id=0, parent_id=0, prompt='\"see you\" title, early 3D computer art')
    Category(name='Спорт', id=1, parent_id=0 , prompt='some sport, marble sculpture')
    Category(name='Игры', id=2, parent_id=0, prompt='a some computer game, made from glowing multicolored luminescent particles, digital art')
    Category(name='Концерты', id=3, parent_id=0 , prompt='a piano, digital art, op art')
    Category(name='Активный отдых', id=4, parent_id=0 , prompt='an astronaut, by Stephan Martiniere')
    Category(name='Мастер классы', id=5, parent_id=0 , prompt='the discovery of gravity, painting from the 17th century')
    Category(name='Искусство', id=6, parent_id=0 , prompt='a horse,  in the topiary shape')

    Category(name='Футбол', id=7, parent_id=1 , prompt='A man kicks a penalty at the goal where the goalkeeper stands during a football match, high quality image, Cinematic Lighting, 85mm, Polaroid')
    Category(name='Баскетбол', id=8, parent_id=1 , prompt='Basketball player doing a slam dunk, high quality image, Cinematic Lighting, Art Deco print')
    Category(name='Легкая атлетика', id=9, parent_id=1 , prompt='Man running around the stadium, dressed in sports clothes, sneakers on his feet, high quality image, Autochrome, 85mm, Studio Lighting, Studio Lighting')
