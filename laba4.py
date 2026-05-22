class MapLink:
    def __init__(self):
        self.map = {}

    def addlink(self, shortlink, link):
        if link in self.map.values():
            for key, value in self.map.items():
                if value == link:
                    print(f"Бро, уже есть короткий код на данную ссылку - {key}\n")
                    break
        else:
            self.map.setdefault(shortlink, link)
            print("Добавлено\n")

    def isSLink(self, shortlink):
        return shortlink in self.map

    def getLink(self, shortlink):
        return self.map.get(shortlink, None)
    
    def printShortLinks(self):
        for key in self.map.keys():
            print(f"{key} ")

if __name__ == "__main__":
    map = MapLink()
    print("Выберите, что хотите сделать с ссылками и их короткими кодами\n")
    print("1. Добавить ссылку и короткий код на нее\n")
    print("2. Проверить существует ли короткий код\n")
    print("3. Получить ссылку по короткому коду\n")
    print("4. Вывести все короткие коды\n")
    print("Все остальные значения - закончить работу с программой\n")
    A = True
    while A == True:
        vubor = input("")
        match vubor:
            case "1":
                print("Введите длинную ссылку\n")
                l = input("")
                print("Введите короткий код\n")
                sl = input("")
                
                map.addlink(sl, l)

            case "2":
                print("Введите короткий код\n")
                sl = input("")
                if map.isSLink(sl):
                    print("Есть в ассортименте\n")
                else:
                    print("Нет в наличии\n")

            case "3":
                print("Введите короткий код\n")
                sl = input("")
                l = map.getLink(sl)
                if l == None:
                    print("Нет такой\n")
                else:
                    print(f"Держите - {l}\n")

            case "4":
                map.printShortLinks()

            case _:
                print("Покедова")
                A = False
                