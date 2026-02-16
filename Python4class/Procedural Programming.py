hero_name = "용사"
hero_hp = 100
hero_power = 10

#캐릭터 2 슬라임

monster_name = "슬라임"
monster_hp = 30
monster_power =5

def attack(attacker_name, attacker_power, target_name, target_hp):
    print(f"[{attacker_name}]이(가) [{target_name}]을 공격! (데미지: {attacker_power})")
    target_hp -= attacker_power
    print(f"[{target_name}]의 남은 체력: {target_hp}")
    return target_hp

print("=== step1 전역변수를 사용해서 실행")
monster_hp = attack(hero_name,hero_power,monster_name,monster_hp)

##step2 딕셔너리 구조체(데이터 묶기)

hero = {"name" : "용사", "hp" : 100 ,"power" : 10}
monster = {"name" : "슬라임" , "hp" : 30 , "power" : 5}

def attack_dict(attacker,target):
    print(f"[{attacker['name']}]이(가) [{target['name']}을 공격! (데미지 : {attacker['power']}]")
    target['hp'] -= attacker['power']
    print(f"[{target['name']}의 남은 체력: {target['hp']}")
print("\n==== step2 딕셔너리를 사용해서 실행 ====")
attack_dict(hero,monster)


# step 3 클래스 객체지향 데이터랑 행위를 묶자

class Character:
    def __init__(self,name,hp,power):
        self.name = name
        self.hp = hp
        self.power =power

    # 내안에서 공격을 직접 처리한다

    def attack(self,target):
        print(f"[{self.name}]이(가) [{target.name}]을 공격! (데미지 :{self.power})")
        target.take_damage(self.power)

    def take_damage(self,power):
        if power < 0 :
            print(f"오류 : 잘못된 데미지 입니다. ({power}. 데이터 보호됨")
            return
        self.hp -= power
        print(f"{self.name}의 남은 체력 : {self.hp}")

print("\n==== step3 객체로 실행")

p1 = Character("용사",100,10)
m1 = Character("슬라임",30,5)

p1.attack(m1)

p1.power = -50
print("\n[Test] 잘못된 공격력으로 공격 시도")
p1.attack(m1)