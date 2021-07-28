class Country:

    name = "국가명"
    population = "인구"
    capital = "수도"

    def show(self):
        print("국가 클래스의 메소드입니다.")




class Korea(Country):

    def __init__(self,name,population,capital):
        self.name = name 
        self.population = population
        self.capital =capital

    def show(self):
        super().show()        #부모클래스의 'show()' 또한 실행하고 싶다면 이코드 넣어준다
        print(
            """
            국가의 이름은 {} 입니다.
            국가의 인구는 {} 입니다.
            국가의 수도는 {} 입니다.    
            """.format(self.name,self.population,self.capital)
        )

