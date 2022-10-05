from dataclasses import dataclass

from models import BaseModel


@dataclass
class Heros(BaseModel):
    image_path: str
    name: str
    caption: str


if __name__ == '__main__':
    hero = Heros(image_path='media/img/hero-slider/hero-1.jpg', name='FITNESS & SPORT', id=None, caption='Join Us Now')
    hero = Heros(image_path='media/img/hero-slider/hero-2.jpg', name='FITNESS & SPORT', id=None, caption='Join Us Now')
    hero = Heros(image_path='media/img/hero-slider/hero-3.jpg', name='FITNESS & SPORT', id=None, caption='Join Us Now')
    hero._create_table()
    hero.save()
    print(hero)