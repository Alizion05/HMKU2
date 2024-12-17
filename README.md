Задание №2
Разработать инструмент командной строки для визуализации графа
зависимостей, включая транзитивные зависимости. Сторонние средства для
получения зависимостей использовать нельзя.
Зависимости определяются для git-репозитория. Для описания графа
зависимостей используется представление Mermaid. Визуализатор должен
выводить результат в виде сообщения об успешном выполнении и сохранять граф
в файле формата png.
45
Построить граф зависимостей для коммитов, в узлах которого находятся
списки файлов и папок. Граф необходимо строить только для коммитов ранее
заданной даты.
Конфигурационный файл имеет формат xml и содержит:
• Путь к программе для визуализации графов.
• Путь к анализируемому репозиторию.
• Путь к файлу с изображением графа зависимостей.
• Дата коммитов в репозитории.
Все функции визуализатора зависимостей должны быть покрыты тестами.
