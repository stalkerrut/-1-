define gg = Character("Макс")
define anna = Character("Аня")
define kir = Character("Кирилл")
define narrator = Character(None)

image anna normal = im.Scale("anna normal.png", 420, 700)
image anna happy = im.Scale("anna happy.png", 420, 700)
image anna sad = im.Scale("anna sad.png", 420, 700)

image kir normal = im.Scale("kir normal.png", 420, 700)
image kir angry = im.Scale("kir angry.png", 420, 700)
image kir smile = im.Scale("kir smile.png", 420, 700)

default courage = 0
default anna_trust = 0
default kir_trust = 0
default has_key = False

label start:

    scene black
    narrator "Глава 1. Странный вечер"

    scene bg room
    show anna normal at center

    gg "Где я?.."

    anna "Ты очнулся. Хорошо."

    gg "Кто ты?"

    show anna happy at center
    anna "Меня зовут Аня. Я нашла тебя возле старого дома."

    menu:
        "Как ответить Ане?"

        "Поблагодарить её":
            gg "Спасибо, что помогла мне."
            $ anna_trust += 1
            show anna happy at center
            anna "Не за что. Ты выглядел плохо."

        "Спросить грубо":
            gg "Откуда мне знать, что тебе можно доверять?"
            $ anna_trust -= 1
            show anna sad at center
            anna "Можешь не доверять. Но я всё равно помогла."

        "Промолчать":
            gg "..."
            show anna sad at center
            anna "Ладно. Видимо, тебе нужно время."

    show anna normal at center
    anna "Нам нужно решить, что делать дальше."

    menu:
        "Что сделать?"

        "Осмотреть комнату":
            jump inspect_room

        "Поговорить с Аней":
            jump talk_anna

        "Выйти наружу":
            jump outside


label inspect_room:

    scene bg room
    show anna normal at right

    narrator "Ты внимательно осматриваешь комнату."

    if not has_key:
        narrator "Под старой книгой ты находишь маленький ключ."
        $ has_key = True
        gg "Возможно, он пригодится."
        show anna happy at right
        anna "Отлично. Может, он откроет какой-нибудь проход."
    else:
        narrator "Ты уже всё здесь осмотрел."

    menu:
        "Что дальше?"

        "Поговорить с Аней":
            jump talk_anna

        "Выйти наружу":
            jump outside


label talk_anna:

    scene bg room
    show anna normal at center

    gg "Аня, что здесь происходит?"

    anna "Этот дом давно заброшен. Но ночью здесь появляются странные люди."

    menu:
        "Что спросить?"

        "Почему ты здесь?":
            gg "Почему ты сама здесь оказалась?"
            show anna sad at center
            anna "Я ищу своего брата."
            $ anna_trust += 1

        "Кто эти люди?":
            gg "Кто эти странные люди?"
            anna "Я не знаю. Но они явно что-то ищут."

        "Нам нужно уходить":
            gg "Хватит вопросов. Нам нужно уходить."
            $ courage += 1
            show anna happy at center
            anna "Согласна."

    jump outside


label outside:

    scene bg forest
    show anna normal at left
    show kir normal at right

    narrator "Вы выходите из дома. В лесу темно и холодно."

    kir "Стоять."

    gg "Кто ты?"

    show kir smile at right
    kir "Кирилл. Я тоже пытаюсь выбраться отсюда."

    menu:
        "Как поступить?"

        "Довериться Кириллу":
            gg "Ладно. Пойдём вместе."
            $ kir_trust += 1
            show kir smile at right
            kir "Разумное решение."

        "Не доверять ему":
            gg "Мы сами справимся."
            $ kir_trust -= 1
            show kir angry at right
            kir "Как знаешь."

        "Спросить, что он знает":
            gg "Что ты знаешь об этом месте?"
            show kir normal at right
            kir "Здесь есть подземный выход. Но дверь заперта."
            $ kir_trust += 1

    jump old_gate


label old_gate:

    scene bg gate
    show anna normal at left
    show kir normal at right

    narrator "Через несколько минут вы находите старые железные ворота."

    if has_key:
        gg "У меня есть ключ. Попробую открыть."
        narrator "Ключ подходит."
        show anna happy at left
        anna "Получилось!"
        jump underground
    else:
        narrator "Ворота заперты."
        gg "Нам нужен ключ."
        jump no_key_choice


label no_key_choice:

    scene bg gate
    show anna sad at left
    show kir normal at right

    menu:
        "Что делать?"

        "Вернуться в дом":
            jump inspect_room

        "Попытаться сломать ворота":
            $ courage += 1

            if courage >= 2:
                narrator "Ты с силой толкаешь ворота. Замок ломается."
                show kir smile at right
                kir "Неплохо."
                jump underground
            else:
                narrator "Ничего не выходит."
                jump bad_end


label underground:

    scene bg tunnel
    show anna sad at left
    show kir normal at right

    narrator "Вы спускаетесь в подземный тоннель."

    anna "Мне страшно."

    menu:
        "Что сказать?"

        "Поддержать Аню":
            gg "Мы справимся. Я рядом."
            $ anna_trust += 1
            show anna happy at left
            anna "Спасибо..."

        "Сказать идти быстрее":
            gg "Не время бояться. Идём."
            $ courage += 1
            show anna sad at left
            anna "Ладно..."

    show kir normal at right
    kir "Впереди развилка."

    menu:
        "Куда пойти?"

        "Налево":
            jump left_path

        "Направо":
            jump right_path


label left_path:

    scene bg tunnel
    show anna normal at left
    show kir normal at right

    narrator "Левый путь приводит к старой лестнице."

    if anna_trust >= 2:
        show anna happy at left
        anna "Подожди. Я слышу шум сверху. Лучше идти тихо."
        narrator "Благодаря Ане вы избегаете опасности."
        jump good_end
    else:
        show anna sad at left
        narrator "Вы поднимаетесь наверх, но вас замечают."
        jump bad_end


label right_path:

    scene bg tunnel
    show anna normal at left
    show kir normal at right

    narrator "Правый путь ведёт к закрытой двери."

    if kir_trust >= 1:
        show kir smile at right
        kir "Я знаю код от этой двери."
        narrator "Кирилл открывает дверь."
        jump secret_end
    else:
        show kir angry at right
        kir "Я не собираюсь рисковать ради людей, которые мне не доверяют."
        narrator "Дверь закрыта, а времени почти не осталось."
        jump bad_end


label good_end:

    scene bg sunrise
    show anna happy at center

    narrator "Вы выбираетесь из тоннеля и встречаете рассвет."

    anna "Мы выжили..."

    narrator "Хорошая концовка."
    return


label secret_end:

    scene bg lab
    show kir smile at center

    narrator "За дверью вы находите тайную лабораторию."

    kir "Теперь ты понимаешь, почему нас сюда привели?"

    narrator "Секретная концовка."
    return


label bad_end:

    scene black

    narrator "Вы не смогли выбраться."

    narrator "Плохая концовка."
    return