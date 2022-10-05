from dataclasses import dataclass

from models import BaseModel


@dataclass
class MainCards(BaseModel):
    image_path: str
    name: str
    caption: str


if __name__ == '__main__':
    mainCard = MainCards(image_path='media/img/feature/feature-1.jpg', name='GROUP CLASSES', id=None, caption='The Sopranos manages to address the biases<br /> and benefits of therapy')
    mainCard = MainCards(image_path='media/img/feature/feature-2.jpg', name='PERSONAL TRAINING', id=None, caption='Strep throat is very common during the flu<br /> seasons and it can be preceded')
    mainCard = MainCards(image_path='media/img/feature/feature-3.jpg', name='Sports Nutrition', id=None, caption='A Human Being’s right to life implies his right to<br /> have the free and unrestricted')
    mainCard._create_table()
    mainCard.save()
    print(mainCard)
    mainCards = MainCards.fetch_all()
    print(mainCards)