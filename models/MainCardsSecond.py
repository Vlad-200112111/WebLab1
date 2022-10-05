from dataclasses import dataclass

from models import BaseModel


@dataclass
class MainCardsSecond(BaseModel):
    image_path: str
    name: str
    caption: str


if __name__ == '__main__':
    mainCardsSecond = MainCardsSecond(image_path='media/img/classes/class-1.jpg', name='BootCamp', id=None, caption='The Sopranos manages to address the biases<br /> and benefits of therapy')
    mainCardsSecond = MainCardsSecond(image_path='media/img/classes/class-2.jpg', name='Crossfit Level 1', id=None, caption='Strep throat is very common during the flu<br /> seasons and it can be preceded')
    mainCardsSecond = MainCardsSecond(image_path='media/img/classes/class-3.jpg', name='Energy Blast', id=None, caption='A Human Being’s right to life implies his right to<br /> have the free and unrestricted')
    mainCardsSecond = MainCardsSecond(image_path='media/img/classes/class-4.jpg', name='CLASSIC BODY BALANCE', id=None, caption='A Human Being’s right to life implies his right to<br /> have the free and unrestricted')
    mainCardsSecond._create_table()
    mainCardsSecond.save()
    print(mainCardsSecond)
    mainCards = MainCardsSecond.fetch_all()
    print(mainCards)