# Инструкция по установке и настройке скриптов DevOps

## Установка Сygwin для Windows

1. Скачать инсталятор со [страницы cygwin](http://www.cygwin.com/)
1. Установить, путь для установки *cygwin* должен быть без пробелов.
1. Скопировать путь до папки **cygwin64\bin** в переменную среды окружения PATH `Свойства компьютера\Дополнительные параметры системы\Переменные среды:Системные переменные`

## Установка jq для Windows

1. Скачать исполняемый файл со [страницы jq](https://stedolan.github.io/jq/)
1. Сохранить по пути без пробелов и переименовать в **jq.exe**
1. Скопировать путь до папки с **jq.exe** в переменную среды окружения PATH `Свойства компьютера\Дополнительные параметры системы\Переменные среды:Системные переменные`

## Описание скриптов

> При возникновении проблем во время выплнения скриптов, убедитесь, что у вас для них выставлен Line Separator: **LF**

- **mvn-version-set-commit.sh** – изменяет версию приложения на введенную сразу после запуска скрипта. Если номер версии
заканчивается на `-` то к весрии будет добавлен суффикс *SNAPSHOT*. В *Working Directory* должна быть указана корневая папка проекта в котором требуется изменить версию. 
- **ssh-wget-autoDeploy.sh** – Деплой на сервер указанного приложения. В *Program arguments* необходимо указать аргументы в следующей последовательности: `stand-url project-key
 rchat-user-token rhcat-user-id`, 
В *Working Directory* должна быть указана корневая папка проекта **build** 
- **bamboo-run-builds.sh** - Запуск сборки на бамбу. В *Program arguments* необходимо указать аргументы в следующей последовательности: `bamboo-url bamboo-user-name bamboo-password
 bamboo-project-key
 bamboo-branch-key`

## Настройка запуска скриптов из Intellij IDEA

### Run/Debug Configurations

1. Установить плагин [BashSupport](https://plugins.jetbrains.com/plugin/4230-bashsupport) для Intellij IDEA: `Ctrl+Alt+S` раздел **Plugins**, 
выбрать *Marketplace* и в поиске написать *BashSupport*.
1. В поле **interpreter path** указать путь до *bash.exe*. Пример: `C:\tools\cygwin64\bin\bash.exe`

### External Tools

1. Вызвать **Settings** нажав сочетание клавиш `Ctrl+Alt+S`
1. Выбрать элемент **Tools/External Tools**

## Планы развития