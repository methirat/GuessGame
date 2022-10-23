from random import randint
from sys import exit

class Intro:
    def __init__(self):
        print("ยินดีต้อนรับสู่เกมเดา!\n")
        self.username()

    def username(self):
        try:
            print("กรุณาบอกชื่อของคุณ!")
            self.username = input('> ')
            print("\n")
            #return self.username
        except KeyboardInterrupt:
            print("\nบายยย")
            exit()
        except Exception as e:
            print(e)

class Start(Intro):
    def proceed(self):
        try:
            print(f"คุณพร้อมหรือยัง, {self.username}?")
            self.user_input = input("[Y/N]> ")
            if self.user_input == 'Y' or self.user_input == 'y':
                print("\nเยี่ยม คุณพร้อมแล้ว!\n")
                return True
            elif self.user_input =='N' or self.user_input == 'n':
                print("ทำไมคุณถึงอยู่ที่นี่?")
                exit()
            else:
                print("\nเมื่อกี้คืออะไร?")
                raise ValueError
        except KeyboardInterrupt:
            print("\nไว้เจอกันใหม่ภายหลัง!")
            exit()
        except ValueError:
            print("\nโปรดเรียนรู้ที่จะพิมพ์!")
            self.proceed()
            

class Finish:
    def victory_message(self, number, guess):
        self.number = number
        self.guess = guess
        print("มันสุดยอดมาก!!!\n")
        print(f"เดาของคุณคือ {self.guess}.")
        print(f"หมายเลขลับคือ {self.number}.")
        exit()

    def defeat_message(self, number, guess):
        self.number = number
        self.guess = guess
        print("แย่มาก. เกือบได้แล้ว.\n")
        print(f"เดาของคุณคือ {self.guess}.")
        print(f"หมายเลขลับคือ {self.number}.")
        print("\nลองอีกครั้งในภายหลัง!")
        exit()

class In_game(Finish):
    def __init__(self):
        print("\n\"กฎของเกม\"\n")
        print("- คุณมีโอกาส 5 ครั้งในการเดา")
        print("- คุณจะได้รับคำใบ้สำหรับการเดาผิดทุกครั้ง")
        print("- ถ้าเดาถูกก็ชนะ ถ้าไม่อย่างนั้นก็ขาดทุน")
        print("- เกมจะจบลงเมื่อคุณเดาหมายเลขหรือหมดโอกาส")
         
        self.chances = 5
        self.number = randint(1,10)
        self.play()

    def play(self):
        try:
            while self.chances !=0:
                self.guess = int(input("เดาตัวเลขสิ : "))
                # print(self.number)
                self.chances -= 1
                if self.guess == self.number:
                    self.victory_message(self.number, self.guess)
                elif self.guess < self.number:
                    if self.number - self.guess >= 3:
                        print("\nนั่นมันเล็กเกินไป!")
                    else:
                        print("เฉียดฉิว! ใหญ่กว่านี้!")  
                elif self.guess > self.number:
                    if self.guess - self.number >= 3:
                        print("\nมันใหญ่เกินไป")
                    else:
                        print("เฉียดฉิว! เล็กลงหน่อย!")
                else:
                    print("เมื่อกี้คืออะไร? เราก็นับว่าเป็นโอกาสนะ!")
                print(f"คุณยังมี {self.chances} โอกาส\n")
            self.defeat_message(self.number, self.guess)
            exit()
        except KeyboardInterrupt:
            print("\nอืม อย่าเพิ่งยอมแพ้แบบนั้น!")
            print("แล้วเจอกันนะ!")
            exit()
        except ValueError:
            print("1-10 เท่านั้น! เราก็นับว่าเป็นโอกาส!")
            self.chances -= 1
            print(f"คุณยังมี {self.chances} โอกาส\n")
            self.play()


def main():
    # intro = Intro()
    try:
        start = Start()
        tmp = start.proceed()

        if tmp == True:
            finish = In_game()
    except KeyboardInterrupt:
        print("แล้วเจอกันนะ!!")
    except Exception as e:
        print(e)
    finally :
        print("\n\nCreated By 6504101373")

if __name__ == "__main__":
    main()



