# цель проекта
tnm-rpg это text novel multiplayer role play game. задмука в том, что это максимально простой с точки зрения интерфейса проект, позволяющий создавать на своей основе по сути любую игру ограничиваясь лишь вашим креативом в разнообразии и подборки выборов для каждой сцены

вам будет доступно полная модификация и создание своей игры прямо из коробки. после запуска игры, вы сможете сами создавать свои варианты выбора и позвать друга для совместной ролевки или написания какой либо истории. вы так же можете самостоятельно модифицировать игру, я буду предоставлять максимально широкие возможности для этого

можно упомянуть что основными целями в принципе любого проекта могут быть: документируемость, доступность и реализация. этим целям следую и я


---
# используемые подходы
самое первое и основное что стоит отметить, так это инструмент схема, которая из другого проекта осознание (ссылочка будет позднее). в схеме есть такое понятие как регулярные выражения, так я мог сказать tnm-rpg и вы знаете о чем я сказал, так вот этот подход будет применён на всю разработку, поэтому если вы чего то не поняли, поищите где нибудь информацию об этом в схеме, скриптах, ридми или на крайний случай в интернете

используется [лицензия](LICENSE) gnu общая публичная второй версии. используйте мои наработки и распространяйте, я буду рад если этот проект не только позволит кому то разбавить досуг но и прийти к решению некоторых задач. можете посмотреть ещё один мой проект anthros-core по сути благодаря ему и deep-foundation у меня зарадилась мысль написать такую простую но обширную в возможностях игру, может даже это можно назвать интерактивной платформой для игр и их создания

система версий игры представлена в 3 основных понятиях и 2 числах. так ver a1.4 означает что это альфа версия, 1 ревизии и 4 выпуск этой ревизии в общее использование. альфа означает сырой не готовый продукт, бета означает уже выполняющий свои функции но недоработанный продукт, релиз означает что игра готова и должна работать стабильно. понятия "a", "b" и "r" могут менятся от ревизии к ревизии но не могут менятся на протяжении выхода новых версий ревизии (если только не найдётся большая проблема которая заставит откатить готовность продукта). по большому счету ядро очень базовое и такая система вероятно будет скорее описывать механники, не знаю пока, думаю

я буду использовать для написания чистый python. возможно в будущем я буду применять какие либо библиотеки для интерфейса или связи людей между друг другом по интернету (об этом позднее). в остальном я пишу для shell операционных систем, поэтому все запускается в консоли. добавлю ещё работу с github для удобства обновления и ведения разработки. другие языки программирования и средства пока использовать я не планирую


tnm-rpg как структура делится на комбинацию двух основных понятий, это механники и объекты. механники это реализованные кодом объекты (классы, функции, переменные), они как правило служат функции изменять объекты, автоматизировать игровой процесс и расширить его. написанны они могут быть на любом языке по своей сути, но полного выполнения этого принципа можно будет добиться только как то связав разные языки между собой (возможно с помощью deep или anthros-core)

в то же время объекты это по своей сути просто название объекта и его свойства, такие как описание, способности или колличество хп. некоторые свойства персонажей могут работать непосредственно от механник, такие свойства персонажа являются скрытыми, что бы ими нельзя было аперировать из игры и не сломать игровой процесс. так же сами по себе названия свойств объекта могут быть множественными а их описание само по себе может содержать другие объекты или их описание. писаться они будут на стандарте json (о их структуре позднее)

на данный момент будут использоваться механники:
- создания и удаления объектов
- сцены
- вывод информации о сцене и вариантах выбора
- ввод пользователя и обработка написанного по механникам

как писать свои механники на python? создайте модуль *.py в корне папки mechanics. в этом модуле может находится все что вам нужно, однако название модуля и того объекта что вы хотите внедрить в игру должно быть одноименное. так к примеру: "say_hello.py" должен содержать "def say_hello():" функцию. в противном случае ваша функция не будет исполнена а в корне программы появится log с ошибкой. так же ваша механника может не принимать не чего, или принимать один или более объектов (как аргументы функции или того объекта что вы задали, будет использоваться как вызов!)

если вы будете заниматься динамикой, то знайте, объекты динамичны и могут обнавлятся в реальном времени, а вот механики обнавляются только после перезапуска игры. так же ещё отмечу, что свойства есть как бы и механик (только это аттрибуты), так что вы можете использовать и их тоже. в папке механник и в папке объектов папки и их содержимое будет игнорироваться. пока что у core многовато полномочий, но я буду стараться сводить их к минимому со временем


---
# заметки по производству
тут будут пункты которые пришли мне на ум, они описывают то, что нужно сделать что бы достигнуть цели. основной целью является написание игры, все что описано ниже должно способствовать её написанию или использованию. названия списков символизируют вид деятельности, что будет дублироваться в коммитах на github


структура(frame):
- [x] создать README.md
- [x] выбрать лицензию и сохранить в корне проекта
- [x] задать главный скрипт core.py
- [x] описать схему производства
- [x] описать основные обьекты игры (так же будет использоваться для модификации)
- [ ] создать и прописать run.bat и run.sh для запуска и установки зависимостей на windows и termux (android)
- [ ] разработать систему модификаций
- [ ] реализовать и описать структуру игровых объектов


механники(mechanics):
- [ ] текстовый интерфейс
- [ ] механника создания объекта
- [ ] сцена (то что сейчас происходит, варианты выбора)
- [ ] обработки действий игрока
- [ ] написать механику update (для обновления игры)


объекты(objects):
- [ ] создать персонажа
- [ ] создать аниме (:3)
- [ ] создать комнату


написание(write):
- [x] создать реализацию создания log.txt при ошибках
- [x] '\\' символ указывает на конец объекта или механники а так же позволяет экранировать символ после себя
- [x] добавлен функционал перехода по пунткам по стрелочкам
- [x] теперь можно вернуться на сцену назад, введя 0
- [x] реализовать экранирование с помощью кавычек (в том числе и в скобочках)
- [x] реализована сеть через discord api (пока нет центрального сервера, это лучше чем нечего)
- [ ] описать правила установки и работы с tnm-rpg в README.md
- [ ] описать установку на windows и android


исправление(fix):
- [x] проблема возврата ")" в recusion устранена
- [x] проблема создания пунтка "???" устранена
- [x] проблема не верного синтаксиса при создании пункта в объекте
- [x] проблема появления доп пункта при $hook.back
- [x] проблема не рабочего object.remove()


тестирование(test):
- [x] проверить первый билд на termux (android)


второстепенные(secondary):
- [x] придумать реализацию версий и то из чего она строится
- [ ] написать автомаизированный скрипт для пуша новой версии и сборки *.exe
- [ ] написать или найти готовый конвертор из *.md в *.html
- [ ] описать систему форков как систему для распростронения своих механник и объектов
- [ ] придумать как описать последовательное исполнение игры
- [ ] возможно стоит добавить дампы для сохранения настроенных игр
- [ ] возможно стоит задать некоторые стандартные свойства объектов для удобства
- [ ] создать возможность просматривать все форки от этого проекта автоматизческий с помощью скрипта, так что бы если в объекте требуется механники которой нет у вас, эта механника могла с его согласия подгрузится автоматический и он мог бы продолжить игру не задумываясь об этом
- [ ] попробовать создать одно большую мега рп которую могут прописывать все люди и создавать ветки и свои механники в ней
- [ ] возможно стандартные схемы стоит перенести в core (для удобства обновления и надежности)
- [ ] сделать внешний loop
- [ ] возможно стоит переименновать loop во что то связанное с (дополнительно к каждому действию в цикле)
- [ ] разработать систему кастомного синтаксиса, так, что при обнуружении определённых подстрок, будет вызыватся определённая механника
- [ ] написать об необходимости писать class_name = class_name() что бы не было проблем с self и вызовом атрибутов (но это не касается таких классов, которые работают как object)
- [ ] написать объект обучения
- [ ] описать ??? как следствие ошибки. tnm-rpg будет стараться не ломаться при любом исходе, нобудет показывать ошибки визуально, что бы можно было понять, что нужно исправить
- [ ] если будет создан файл beckup.json, то он может быть перезаписан
- [ ] написать про структуру variables, в нем не может быть словарей (вложенности, мерности)
- [ ] о особенностях импорта механник
- [ ] решить проблему ушек (такие как \u007) в json(ах)
- [ ] показывать ошибку на 3 секунды после команды для удобства
- [ ] добавить встраивание времени удаления для removed
- [ ] добавить '' в синтаксис для экранирования в обычной команде а в скобочках так можно передавать аргументы
- [ ] описать особенности синтаксиса в документации
- [ ] сделать систему сохранений позиции поинт
- [ ] нельзя удалить корневой объект, исправить
- [ ] описать то, как делать механники и об особенностях совместимости с командами
- [ ] придумать использование для '_' как предыдущих переменных
- [ ] написать установищик для андроид ($ apt update, $ apt upgrade, $ y, $ y, $ apt install python python3, $ pip3 install discord) https://aktermux.in/install-pip-in-termux/
- [ ] реализовать систему для отправки объектов друг другу через discord   


---
# версии игры
тут я буду описывать все общие изменения игры, здесь вы сможете увидеть прогресс развития


версия alpha 0.1:
- реализованны первые основные для новеллы механники core, recursion, execution, object, variables
- реализованны дополнительные необходимые но изменяймые в будущем механники interface, get, hook
- добавленн основной запускаемый объект start
- создана основная система loop для core, последовательно выполняемые механники друг за другом
- реализованна система удаления и создания пунктов в объектах
- базовая отладка ошибок, в случае проблем, ошибки появляются в log.txt
- система вызова json как объектов
- система вызова py как механник
- общая работа над проектом, сборка всего вместе, общая законченость и работоспособность
- реализованно удаление, создается бекап в removed
- список изменений в scheme.md
- выбрана лицензия gnu public license version 2
- настроен запуск для windows по двойному нажатию по run.bat


версия alpha 0.2:
- исправлен баг некоректной обработки комнады в recursion
- переход по пунктам можно соверхать с помощью чисел, а предыдущая сцена доступна по 0
- экранирование для аргументов механник и для обычной команды


версия alpha 0.3:
- реализована сетевая состовляющая, теперь можно отправлять и считывать одну команду на сервере
- разработка и тестирование новых фич и идей которые будут в будущем
- небольшие улучшения в структуре и работе игры