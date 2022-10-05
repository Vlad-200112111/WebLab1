from dataclasses import dataclass

from models import BaseModel


@dataclass
class Trainers(BaseModel):
    image_path: str
    name: str
    caption: str


if __name__ == '__main__':
    # trainer = Trainers(image_path='media/img/trainer/trainer-1.jpg', name='Becky Taylor', id=None, caption='Gymer')
    # trainer = Trainers(image_path='media/img/trainer/trainer-2.jpg', name='Noah Leonard', id=None, caption='Trainer')
    # trainer = Trainers(image_path='media/img/trainer/trainer-3.jpg', name='Evelyn Fields', id=None, caption='Gymer')
    # trainer = Trainers(image_path='media/img/trainer/trainer-4.jpg', name='Leroy Guzman', id=None, caption='Manager')
    # trainer._create_table()
    # trainer.save()
    # print(trainer)
    trainers = Trainers.fetch_all()
    print(trainers)