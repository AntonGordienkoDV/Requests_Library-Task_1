import requests


class Hero:
    host = 'https://superheroapi.com/api/2619421814940190'

    def _get_id(self):
        url = f'{self.host}/search/{self.name}'
        response = requests.get(url)
        for hero in response.json()['results']:
            if self.name == hero['name']:
                return hero['id']

    def _get_intelligence(self):
        url = f'{self.host}/{self.id}/powerstats'
        response = requests.get(url)
        return int(response.json()['intelligence'])

    def __init__(self, name: str):
        self.name = name
        self.id = self._get_id()
        self.intelligence = self._get_intelligence()


def get_most_intelligent_hero(*heroes: Hero):
    intelligence_rating = sorted(heroes, key=lambda _hero: _hero.intelligence, reverse=True)
    for hero in heroes:
        print(f'{hero.name}, id: {hero.id}, intelligence: {hero.intelligence}')
    print(f'\nThe most intelligence hero is {intelligence_rating[0].name}')


def main():
    hulk = Hero('Hulk')
    ca = Hero('Captain America')
    thanos = Hero('Thanos')
    get_most_intelligent_hero(hulk, ca, thanos)


if __name__ == '__main__':
    main()
