# KivyMD шпаргалка (Powered by gruger)
да, скозлил шпаргалку

## Оглавление 

1. [Установка KivyMD](#установка-kivymd)
2. [Установка поддержки синтаксиса kivy language в PyCharm](#установка-поддержки-синтаксиса-kivy-language-в-pycharm)
3. [Конфигурационные файлы](#конфигурационные-файлы)
4. [Основные свойства](#основные-свойства)
5. [Темы](#указание-темы-приложения-и-цветовой-схемы)
6. [Макеты](#макеты-layout)
7. [Кнопки](#кнопки-button)
8. [Текстовые поля](#текстовое-поле-text-field)
9. [Label](#label)
10. [Менеджер экранов](#менеджер-экранов-screenmanager)
11. [Список и прокрутка](#список-и-прокрутка)
12. [Контроль выбора SelectionControls](#контроль-выбора-selectioncontrols)
13. [Верхний бар приложения TopAppBar](#верхний-бар-приложения-topappbar)
13. [Нижний бар приложения BottomAppBar](#нижний-бар-приложения-bottomappbar)
14. [Сборка APK](#сборка-apk)

## Установка KivyMD

1. Установите последнюю версию KivyMD
   ```
   py -m pip install https://github.com/kivymd/KivyMD/archive/master.zip
   ```

## Установка поддержки синтаксиса kivy language в PyCharm

1. Перейдите по ссылке https://github.com/noembryo/KV4Jetbrains/releases.
2. Скачайте последнюю версию. Скачивать надо `.jar` файл.
3. Откройте любой проект в PyCharm `File` -> `Manage IDE Settings` -> `Import Settings`.
4. Выберите скачанный файл `jar` и нажмите `ОK`.

## Основная структура проекта с использованием kv language файла

Если вы намерены использовать `kivy language` файл, то фаш проект будет иметь 
минимум два файла:
* `ui.kv` - файла kivy language
* `main.py` - исполняемый файл python

Рассмотрим пример проекта:

* `ui.kv`  
   Интерфейс на языке `kivy language` представляет собой структуру вложенных друг в друга 
   виджетов и их свойств. На нулевом уровне (относительно табуляции) у нас всегда может 
   быть только один элемент, который является корневым.  
   Объявив необходимый нам элемент мы проваливаемся на уровень в него и по необходимости
   указываем его свойства, а только потом помещаем внутрь дочерние элементы.
   ```kv
   MDScreen:  # Корневой элемент, единственный на 0 уровне
       md_bg_color: self.theme_cls.primaryColor  # Свойство элемента MDScreen
       MDTopAppBar:  # Элемент находящийся внутри MDScreen
           type:'small'  # Свойство элемента MDTopAppBar
           pos_hint: {'top':1}  # Свойство элемента MDTopAppBar
           MDTopAppBarTitle:  # Элемент находящийся внутри MDTopAppBar
               id: appbar_title  # Идентификатор элемента MDTopAppBarTitle
               text:'Не нажимай кнопку'  # Свойство элемента MDTopAppBarTitle
       MDButton:  # Элемент находящийся внутри MDScreen
           style: 'tonal' # Свойство элемента MDButton
           pos_hint: {'center_x': .5,'center_y':.5}  # Свойство элемента MDButton
           on_press: app.red_button(self)  # Событие элемента MDButton
           MDButtonText:
               id: btn1_text  # Идентификатор элемента MDTopAppBarTitle
               text: 'Жми сюда!'  # Свойство элемента MDButtonText
   ```
  
  
* `main.py`  
   Исполняемый файл проекта. В нем создается класс приложения который мы в дальнейшем запустим.
   У наименования класса приложения есть одна особенность. Если вы не укажите у приложения свойство
   `title`, то по умолчанию за название возьмется имя класса приложение, но если в имени в конце есть
   фрагмент `App`, то за название возьмется только правая часть названия до него.  
   Ещё стоит обратить внимание, что собранный интерфейс желательно сохранить в атрибут класса для него
   обычно для удобства берут название `root` или `screen`. Данный атрибут нам поможет в дальнейшем с удобством
   обращаться к элементам интерфейса. В примере ниже видно как для поиска используется метода `ids` который
   возвращает элемент с указанным `id`. 
   ```python
   from kivymd.app import MDApp  # Импортируем класс приложения KivyMD
   from kivy.lang import Builder  # Импортируем конструктор интерфейса с kivy language
   
   class HelloApp(MDApp):
       screen = None
       def build(self):
           self.theme_cls.primary_palette = 'Coral'  # Цветовая палитра приложения
           self.theme_cls.theme_style = 'Light'  # Тема приложения Светлая/Темная
           self.title = 'KivyMD'  # Название окна приложения
           self.screen = Builder.load_file('ui.kv')  # Собираем интерфейс из нашего kv файла и сохраняем в атрибут screen
           return self.screen  # Передаем собранный интерфейс в корень приложения
   
       def red_button(self, btn):  # Создаем функцию, которую вызовем через кнопку
           self.screen.ids.btn1_text.text = 'Не жми сюда!'  # Меняем текст кнопки через поиск по идентификатору кнопки
           self.screen.ids.appbar_title.text = 'А я говорил!'  # Меняем текст верхней панели поиском по идентификатору
           btn.disabled = True  # Отключаем нажатую кнопку
   HelloApp().run()  # Запускаем приложение
   ```
  
## Конфигурационные файлы

* `main.py`
    from kivymd.app import MDApp
    from kivy.lang import Builder
    
    
    class TestApp(MDApp):
        def build_config(self, config):
            config.setdefaults('DISPLAY',{
                'theme_style': 'Dark',
                'primary_palette':'Blue'
            }) # Устанавливаем дефолтную структуру конфиг файла
            config.setdefaults('SESSION', {
                'login':None,
                'token': None
            }) # Устанавливаем дефолтную структуру конфиг файла
    
    
        def build(self):
            self.root = Builder.load_file('ui.kv')
            self.theme_cls.theme_style = self.config.get('DISPLAY',"theme_style")  # Считать значение в конфиге
            self.theme_cls.primary_palette = self.config.get('DISPLAY',"primary_palette")  # Считать значение в конфиге
            self.config.set('SESSION','token','278392738yeudy2dyy281yd89su1298edu21')  # Установить значение в конфиге
            self.config.write()  # Записать конфиг в файл
            return self.root
    
    
    
    
    TestApp().run()

    ```
* Содержимое файла ini
    ```ini
    [DISPLAY]
    theme_style = Dark
    primary_palette = Blue
    
    [SESSION]
    login = None
    token = 278392738yeudy2dyy281yd89su1298edu21
    ```

## Основные свойства

### Расположение элемента

> Важно знать что ось координат верстки интерфейса находиться в нижнем левом углу  
> ![img.png](src/main_attr/img_axis.png)

* `pos` - позиция элемента относительного его родительского элемента в пикселях, принимает два значения x, y
    * `kv.ui`
        ```
        MDScreen:
            MDButton:
                style:'elevated'
                pos: [50,50]
                MDButtonText:
                    text:'Тестовая кнопка'
        ```
    * Интерфейс  
        ![img.png](src/main_attr/img111.png)
    
* `pos_hint` - позиция виджета относительного его родительского элемента в процентном соотношении
    > Процент задается в следующем формате: `1` - 100%, `0.5` - 50%, `0` - 0% и т.д.
    * `x` - расположение элемента (начало его координат) относительно оси x
        * `kv.ui`
            ```
            MDScreen:
                MDButton:
                    style:'elevated'
                    pos_hint: {'x':.5}
                    MDButtonText:
                        text:'Тестовая кнопка'
            ```
        * Интерфейс  
            ![img.png](src/main_attr/img.png)
    * `y` - расположение элемента (начало его координат) относительно оси y
        * `kv.ui`
            ```
            MDScreen:
                MDButton:
                    style:'elevated'
                    pos_hint: {'y':.5}
                    MDButtonText:
                        text:'Тестовая кнопка'
            ```
        * Интерфейс  
            ![img_1.png](src/main_attr/img_1.png)
    * `right` - расположение правой части элемента (при значении 1 ставит элемент в плотную справа)
        * `kv.ui`
            ```
            MDScreen:
                MDButton:
                    style:'elevated'
                    pos_hint: {'right':.9}
                    MDButtonText:
                        text:'Тестовая кнопка'
            ```
        * Интерфейс  
            ![img_2.png](src/main_attr/img_2.png)
    * `top` - расположение верхней части элемента (при значении 1 ставит элемент в плотную сверху)
        * `kv.ui`
            ```
            MDScreen:
                MDButton:
                    style:'elevated'
                    pos_hint: {'top':.9}
                    MDButtonText:
                        text:'Тестовая кнопка'
            ```
        * Интерфейс  
            ![img_3.png](src/main_attr/img_3.png)
    * `center_x` - расположение центра элемента относительно оси x
        * `kv.ui`
            ```
            MDScreen:
                MDButton:
                    style:'elevated'
                    pos_hint: {'center_x':.5}
                    MDButtonText:
                        text:'Тестовая кнопка'
            ```
        * Интерфейс  
            ![img_4.png](src/main_attr/img_4.png)
    * `center_y` - расположение центра элемента относительно оси y
        * `kv.ui`
            ```
            MDScreen:
                MDButton:
                    style:'elevated'
                    pos_hint: {'center_y':.5}
                    MDButtonText:
                        text:'Тестовая кнопка'
            ```
        * Интерфейс  
            ![img_5.png](src/main_attr/img_5.png)

### Размер элемента

* `size` - размер элемента в пикселях (ширина/высота)
    * `kv.ui`
        ```
        MDScreen:
            MDButton:
                style:'elevated'
                size:[500,500]
                MDButtonText:
                    text:'Тестовая кнопка
        ```
    * Интерфейс  
        ![img.png](src/main_attr/img6.png)

* `size_hint` - размер элемента в процентах относительно родительского элемента (ширина/высота)

### Отображение элемента

* `disabled` - булево значение определяющее активен ли элемент (ширина/высота)
    * `kv.ui`
        ```
        MDScreen:
            MDFloatLayout:
                MDButton:
                    style:'elevated'
                    pos_hint:{'center_x':.5,'center_y':.5}
                    disabled: True
                    MDButtonText:
                        text:'Тестовая кнопка'
        ```
    * Интерфейс  
        ![img_1.png](src/main_attr/img7.png)


* `opacity` - свойство определяет непрозрачность виджета, принимая значение от 0 (полностью прозрачный) до 1 (полностью непрозрачный).
    * `kv.ui`
        ```
        MDScreen:
            MDFloatLayout:
                MDButton:
                    style:'elevated'
                    pos_hint:{'center_x':.5,'center_y':.5}
                    opacity: .5
                    MDButtonText:
                        text:'Тестовая кнопка'
        ```
    * Интерфейс  
        ![img_2.png](src/main_attr/img8.png)


### Кастомизация размеров у фиксированных элементов

Чтобы снять фиксированный размер элемента нужно указать один или несколько след. атрибутов:

* `theme_height: 'Custom'` - открывает изменение высоту размера эл-та
* `theme_width: 'Custom'` - открывает изменение высоту размера эл-та

### Включение авторазмера по содержимому

* `adaptive_size : True` - открывает изменение всего размера эл-та
* `adaptice_width: True` - открывает изменение высоту размера эл-та
* `adaptive_height: True` - открывает изменение высоту размера эл-та


## Оформление

### Изменения фона экрана с текущей темы

Для изменения фона приложения в `MDScreen` указываем свойство `md_bg_color` со значением `self.theme_cls.backgroundColor`

* `kv.ui`
    ```
    MDScreen:
        md_bg_color: app.theme_cls.backgroundColor
        MDButton:
            style:'outlined'
            pos_hint: {'center_x':.5,'center_y':.5}
            MDButtonText:
                text: 'Кнопка'
    ```
* Интерфейс  
    ![img_2.png](src/theming/img_2.png)

### Указание темы приложения и цветовой схемы

* `main.py`
    ```python
    from kivymd.app import MDApp
    from kivy.lang import Builder
    
    
    class TestApp(MDApp):
        def build(self):
            self.root = Builder.load_file('ui.kv')
            self.theme_cls.theme_style = 'Dark'  # Выбор темы приложения
            self.theme_cls.primary_palette = 'Blue'  # Выбор цветовой схемы
            return self.root
    
    TestApp().run()

    ```
* Интерфейс  
    ![img.png](src/theming/img.png)


### Использование иконок Material Design 3
Все иконки в `kivymd` используется со след. документации https://fonts.google.com/icons. Или скачать здесь из папки `download`.



## Макеты (Layout)

### MDBoxLayout
* `horizontal`
    * `kv.ui`
        ```
        MDScreen:
            MDBoxLayout:
                orientation: 'horizontal'
                size_hint:[1,None]
                pos_hint:{'top':1}
                MDButton:
                    style:'elevated'
                    MDButtonText:
                        text:'Кнопка 1'
                MDButton:
                    style:'elevated'
                    MDButtonText:
                        text:'Кнопка 1'
                MDButton:
                    style:'elevated'
                    MDButtonText:
                        text:'Кнопка 1'
        ```
    * Интерфейс  
        ![img.png](src/main_attr/img9.png)
      
* `vertical`
    * `kv.ui`
        ```
        MDScreen:
            MDBoxLayout:
                orientation: 'vertical'
                size_hint:[1,None]
                pos_hint:{'top':1}
                MDButton:
                    style:'elevated'
                    MDButtonText:
                        text:'Кнопка 1'
                MDButton:
                    style:'elevated'
                    MDButtonText:
                        text:'Кнопка 1'
                MDButton:
                    style:'elevated'
                    MDButtonText:
                        text:'Кнопка 1'
        ```
    * Интерфейс  
        ![img_1.png](src/main_attr/img_10.png)
* Дополнительные свойства:
    * `padding` - внутренний отступ от границ макета
    * `orientation` - расположение элементов в макете
        * `vertical`
        * `horizontal`
    * `spacing` - отступы между элементами внутри макета

### MDGridLayout
* `kv.ui`
    ```
    MDScreen:
        MDGridLayout:
            size_hint:[1,1]
            cols:3
            rows:3
            spacing: 10
            pos_hint:{'top':1}
            MDButton:
                style:'elevated'
                MDButtonText:
                    text:'Кнопка 1'
            MDButton:
                style:'elevated'
                MDButtonText:
                    text:'Кнопка 2'
            MDButton:
                style:'elevated'
                MDButtonText:
                    text:'Кнопка 3'
            MDButton:
                style:'elevated'
                MDButtonText:
                    text:'Кнопка 4'
            MDButton:
                style:'elevated'
                MDButtonText:
                    text:'Кнопка 5'
            MDButton:
                style:'elevated'
                MDButtonText:
                    text:'Кнопка 6'
            MDButton:
                style:'elevated'
                MDButtonText:
                    text:'Кнопка 7'
            MDButton:
                style:'elevated'
                MDButtonText:
                    text:'Кнопка 8'
            MDButton:
                style:'elevated'
                MDButtonText:
                    text:'Кнопка 9'
    ```
* Интерфейс  
    ![img_2.png](src/main_attr/img_11.png)

* Дополнительные свойства:
    * `padding` - внутренний отступ от границ макета
    * `orientation` - направление элементов в макете
        * `lr-tb`
        * `tb-lr`
        * `rl-tb`
        * `tb-rl`
        * `lr-bt`
        * `bt-lr`
        * `rl-bt`
        * `bt-rl`
    * `spacing` - отступы между элементами внутри макета
    * `cols` - кол-во колонок 
    * `rows` - кол-во строк

## Кнопки (Button)

* `kv.ui`
    ```
    MDScreen:
        MDButton:
            style: "elevated"
            pos_hint: {"center_x": .5, "center_y": .5}
    
            MDButtonIcon:
                icon: "plus"
    
            MDButtonText:
                text: "Elevated"
    ```
* Интерфейс  
    ![img.png](src/buttons/img.png)

### Elevated button


* `kv.ui`
    ```
    MDScreen:
        MDButton:
            style: "elevated"
            pos_hint: {"center_x": .5, "center_y": .5}
    
            MDButtonIcon:  # Если не указывать не будет иконки
                icon: "plus"
    
            MDButtonText:
                text: "Elevated"
    ```
* Интерфейс  
    ![img.png](src/buttons/img.png)




### Filled button

* `kv.ui`
    ```
    MDScreen:
        MDButton:
            style: "filled"
            pos_hint: {"center_x": .5, "center_y": .5}
            MDButtonText:
                text: "Filled"
    ```
* Интерфейс  
    ![img_1.png](src/buttons/img_1.png)

### Filled tonal button

* `kv.ui`
    ```
    MDScreen:
        MDButton:
            style: "tonal"
            pos_hint: {"center_x": .5, "center_y": .5}
            MDButtonText:
                text: "Tonal"
    ```
* Интерфейс  
    ![img_2.png](src/buttons/img_2.png)

### Outlined button

* `kv.ui`
    ```
    MDScreen:
        MDButton:
            style: "outlined"
            pos_hint: {"center_x": .5, "center_y": .5}
            MDButtonText:
                text: "Outlined"
    ```
* Интерфейс  
    ![img_3.png](src/buttons/img_3.png)

### Text button

* `kv.ui`
    ```
    MDScreen:
        MDButton:
            style: "text"
            pos_hint: {"center_x": .5, "center_y": .5}
            MDButtonText:
                text: "Text"
    ```
* Интерфейс  
    ![img_4.png](src/buttons/img_4.png)

### Icon button

* `kv.ui`
    ```
    MDScreen:
        MDIconButton:
            style: "filled"
            icon: "heart-outline"
            pos_hint: {"center_x": .5, "center_y": .5}
    ```
* Интерфейс  
    ![img_5.png](src/buttons/img_5.png)

> Icon Button поддерживает все те же стили, что и обычная кнопка

Segmented button

### Floating action button (FAB)

* `kv.ui`
    ```
    MDScreen:
        MDFabButton:
            icon: "pencil-outline"
            style: "standard"
            pos_hint: {"center_x": .5, "center_y": .5}
    ```
* Интерфейс  
    ![img_6.png](src/buttons/img_6.png)

> Fab Button имеете следующие стили `standard`, `small` и `large`

### Extended FAB

* `kv.ui`
    ```
    MDScreen:
        md_bg_color: app.theme_cls.surfaceColor
        MDExtendedFabButton:
            id: btn
            pos_hint: {"center_x": .5, "center_y": .5}
            on_press:
                self.fab_state = "expand" \
                if self.fab_state == "collapse" else "collapse"
            MDExtendedFabButtonIcon:
                icon: "pencil-outline"
            MDExtendedFabButtonText:
                text: "Compose"
    ```
* Интерфейс 
    * Обычное состояние  
        ![img_7.png](src/buttons/img_7.png)
    * После нажатия  
        ![img_8.png](src/buttons/img_8.png)

> У этой кнопки есть атрибут `fab_state` c двумя возможными значениями `collapse` (свернуть) и `expand` (развернуть)


### Customization of buttons

* `kv.ui`
    ```
    MDScreen:
        MDButton:
            style: "tonal"
            theme_width: "Custom"
            theme_height: "Custom"
            size_hint: [.5,.5]
            pos_hint: {'center_x':.5,'center_y':.5}
            MDButtonIcon:
                x: text.x - (self.width + dp(10))
                icon: "plus"
    
            MDButtonText:
                id: text
                text: "Tonal"
                pos_hint: {"center_x": .5, "center_y": .5}
    ```
* Интерфейс  
    ![img_9.png](src/buttons/img_9.png)

> Чтобы разрешить изменение у элемента свойства размера нужно выставить атрибут с приставкой `theme_` в режим `Custom`


## Текстовое поле (Text Field)

### Структура Text Field

![img.png](src/inputs/img.png)

### Текстовое поле с полной анатомией

* `kv.ui`
    ```
    MDScreen:
        md_bg_color: app.theme_cls.backgroundColor
    
        MDTextField:
            mode: "outlined"
            size_hint_x: None
            width: "240dp"
            pos_hint: {"center_x": .5, "center_y": .5}
    
            MDTextFieldLeadingIcon:
                icon: "account"
    
            MDTextFieldHintText:
                text: "Пиши здесь!"
    
            MDTextFieldHelperText:
                text: "Да здесь текст писать надо"
                mode: "persistent"
    
            MDTextFieldTrailingIcon:
                icon: "information"
    
            MDTextFieldMaxLengthText:
                max_text_length: 10
    ```
* Интерфейс  
    ![img_1.png](src/inputs/img_1.png) ![img_2.png](src/inputs/img_2.png)

### Режимы Text Filed

* `mode: "filled"`
    * `kv.ui`
        ```
        MDScreen:
            md_bg_color: app.theme_cls.backgroundColor
        
            MDTextField:
                mode: "filled"  
                size_hint_x: None
                width: "240dp"
                pos_hint: {"center_x": .5, "center_y": .5}
        
                MDTextFieldLeadingIcon:
                    icon: "account"
        
                MDTextFieldHintText:
                    text: "Пиши здесь!"
        
                MDTextFieldHelperText:
                    text: "Да здесь текст писать надо"
                    mode: "persistent"
        
                MDTextFieldTrailingIcon:
                    icon: "information"
        
                MDTextFieldMaxLengthText:
                    max_text_length: 10
        ```
    * Интерфейс  
        ![img_3.png](src/inputs/img_3.png)

* `mode: "outlined"`
    * `kv.ui`
        ```
        MDScreen:
            md_bg_color: app.theme_cls.backgroundColor
        
            MDTextField:
                mode: "outlined"  
                size_hint_x: None
                width: "240dp"
                pos_hint: {"center_x": .5, "center_y": .5}
        
                MDTextFieldLeadingIcon:
                    icon: "account"
        
                MDTextFieldHintText:
                    text: "Пиши здесь!"
        
                MDTextFieldHelperText:
                    text: "Да здесь текст писать надо"
                    mode: "persistent"
        
                MDTextFieldTrailingIcon:
                    icon: "information"
        
                MDTextFieldMaxLengthText:
                    max_text_length: 10
        ```
    * Интерфейс  
        ![img_1.png](src/inputs/img_1.png)


## Slider

* `ui.kv`
    ```
    MDSlider:
        step: 1  # Шаг
        value: 50 # Текущее значение
        min:0  # Минимальное значение
        max:100  # Максимальное значение
        orientation:'horizontal' # Ориентация слайдера
        MDSliderHandle:  # Отображение точки
        MDSliderValueLabel:  # Отображение значения
    ```
* Экран
    ![img.png](src/slider/img.png)  

Полезные атрибуты и события:
* `track_active_color` - цвет активного слайдера
* `track_active_step_point_color` - цвет точек активной части слайдера
* `track_inactive_step_point_color` - цвет точек неактивной части слайдера
* `track_inactive_color` - цвет неактивного слайдера





## Label

* `kv.ui`
    ```
    MDScreen:
        md_bg_color: app.theme_cls.backgroundColor
        MDLabel:
            text: "MDLabel"
            halign: "center"
            theme_text_color: "Custom"  # Если необходимо включаем возможность использование собтвенного цвета для текста
            text_color: "red"  # Указываем свой цвет шрифта
            font_style: "Display" # Указываем стиль
            role: "small"  #  Указываем роль
    ```
* Интерфейс  
    ![img.png](src/labels/img.png)

> Размеры label в основном зависят от стиля и роли
> ![img_1.png](src/labels/img_1.png)


## Менеджер экранов (ScreenManager)

### Основная структура

* `main.py`
    ```python
    from kivymd.app import MDApp
    from kivy.lang import Builder
    from kivymd.uix.transition.transition import MDSwapTransition
    
    
    class TestApp(MDApp):
        def build(self):
            self.root = Builder.load_file('ui.kv')
            self.theme_cls.theme_style = 'Dark'
            self.theme_cls.primary_palette = 'Blue'
            self.root.ids.sm.transition = MDSwapTransition() # Текущая анимация переключения экранов
            return self.root
    
    
    TestApp().run()

    ```

* `kv.ui`
    ```
    MDScreen:
        md_bg_color: app.theme_cls.backgroundColor
        MDScreenManager:
            id:sm
            MDScreen:
                name:'scr1'
                MDButton:
                    theme_width:'Custom'
                    theme_height:'Custom'
                    size_hint:[.5, .5]
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_press: app.root.ids.sm.current = 'scr2'
                    MDButtonText:
                        pos_hint: {"center_x": .5, "center_y": .5}
                        text: "Screen 1"
            MDScreen:
                name:'scr2'
                MDButton:
                    theme_width:'Custom'
                    theme_height:'Custom'
                    size_hint:[.5, .5]
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_press: app.root.ids.sm.current = 'scr3'
                    MDButtonText:
                        pos_hint: {"center_x": .5, "center_y": .5}
                        text: "Screen 2"
            MDScreen:
                name:'scr3'
                MDButton:
                    theme_width:'Custom'
                    theme_height:'Custom'
                    size_hint:[.5, .5]
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_press: app.root.ids.sm.current = 'scr4'
                    MDButtonText:
                        pos_hint: {"center_x": .5, "center_y": .5}
                        text: "Screen 3"
            MDScreen:
                name:'scr4'
                MDButton:
                    theme_width:'Custom'
                    theme_height:'Custom'
                    size_hint:[.5, .5]
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_press: app.root.ids.sm.current = 'scr1'
                    MDButtonText:
                        pos_hint: {"center_x": .5, "center_y": .5}
                        text: "Screen 4"

    ```
> У Screen manager есть два основных свойства:
>    * `current` - текущий экран
>    * `transition` - вид анимации   

> У самого же экрана есть атрибут `name` - название экрана


### Другие анимации

* MDSwapTransition - переход по замене, который выглядит как переход iOS при появлении нового окна на экране
    * `duration` - указываем время проигрывания анимации
* MDSlideTransition - переход слайдов сдвигом можно использовать для показа нового экрана с любого направления: слева, справа, сверху или снизу
    * `direction` - указывает направление сдвига
        * `left`
        * `right`
        * `up` 
        * `down`
  * `duration` - указываем время проигрывания анимации
* MDFadeSlideTransition - переход слайдов подтасовкой можно использовать для показа нового экрана с любого направления: слева, справа, сверху или снизу.
    * `direction` - указывает направление сдвига
        * `left`
        * `right`
        * `up`
        * `down`
    * `duration` - указываем время проигрывания анимации
* MDSharedAxisTransition - переход экрана по умолчанию в android.
    * `transition_axis` - указывает по какой оси будет происходить сдвиг с исчезновением
        * `x`
        * `y`
        * `z`
    * `duration` - указываем время проигрывания анимации


## Список и прокрутка

### Структура MDListItem (элемента списка)

![img.png](src/scrollview/img.png)

### Пример использования списков с прокруткой

* `ui.kv`
    ```
    MDScreen:
        md_bg_color: app.theme_cls.backgroundColor
        MDScrollView:
            MDBoxLayout:
                orientation:'vertical'
                adaptive_height:True
                MDListItem:
                    MDListItemLeadingIcon:
                        icon: 'plus'
                    MDListItemHeadlineText:
                        text: 'Тест заголовок'
                    MDListItemSupportingText:
                        text:'Текст подсказка'
                    MDListItemTertiaryText:
                        text:'Текст уточнение'
                    MDListItemTrailingCheckbox:
                MDListItem:
                    MDListItemLeadingIcon:
                        icon: 'plus'
                    MDListItemHeadlineText:
                        text: 'Тест заголовок'
                    MDListItemSupportingText:
                        text:'Текст подсказка'
                    MDListItemTertiaryText:
                        text:'Текст уточнение'
                    MDListItemTrailingCheckbox:
                MDListItem:
                    MDListItemLeadingIcon:
                        icon: 'plus'
                    MDListItemHeadlineText:
                        text: 'Тест заголовок'
                    MDListItemSupportingText:
                        text:'Текст подсказка'
                    MDListItemTertiaryText:
                        text:'Текст уточнение'
                    MDListItemTrailingCheckbox:
                MDListItem:
                    MDListItemLeadingIcon:
                        icon: 'plus'
                    MDListItemHeadlineText:
                        text: 'Тест заголовок'
                    MDListItemSupportingText:
                        text:'Текст подсказка'
                    MDListItemTertiaryText:
                        text:'Текст уточнение'
                    MDListItemTrailingCheckbox:

    ```

> `MDScrollView` является контейнером который может скролить свое содержимое

### Основные свойства и события ScrollView
* `on_scroll_start` - событие срабатываемся при начале прокрутки
* `on_scroll_move` - событие срабатываемся во время прокрутки
* `on_scroll_stop` - событие срабатываемся при прекращении прокрутки
* `do_scroll_x` - принимает булево значение, включение прокрутки по оси x
* `do_scroll_y` - принимает булево значение, включение прокрутки по оси y
* `bar_pos_x` - с какой стороны разместить полосу прокрутки оси x
* `bar_pos_y` - с какой стороны разместить полосу прокрутки оси y
* `bar_width` - ширина полосы прокрутки
* `hbar` - возвращает положение и размер горизонтальной полосы прокрутки
* `vbar` - возвращает положение и размер горизонтальной полосы прокрутки
* `scroll_x` - текущее значение прокрутки оси x (0 - слева, 1 - справа)
* `scroll_y` - текущее значение прокрутки оси y (0 - снизу, 1 - сверху)

## Контроль выбора SelectionControls

### MDCheckbox - элемент выбора

#### Множественный выбор

![img_2.png](src/selections/img_2.png)

* `main.py`
    ```python
    from kivymd.app import MDApp
    from kivy.lang import Builder
    
    
    class TestApp(MDApp):
        def build(self):
            self.root = Builder.load_file('ui.kv')
            self.theme_cls.theme_style = 'Dark'
            self.theme_cls.primary_palette = 'Blue'
            return self.root
    
        def on_check_box(self,checkbox, active):
            if active:
                print(checkbox.value)
                print(checkbox.group)
    
    
    TestApp().run()
    ```

* `ui.kv`
    ```
    MDScreen:
    md_bg_color: app.theme_cls.backgroundColor
    MDBoxLayout:
        orientation:'vertical'
        adaptive_size: True
        spacing: 10
        pos_hint: {'center_y':.5, 'center_x':.5}
        MDBoxLayout:
            orientation:'horizontal'
            adaptive_size:True
            MDCheckbox:
                value: '1'
                padding: [0,0,0,0]
                on_active: app.on_check_box(*args)
            MDLabel:
                text:'Тест 1'
                adaptive_width: True
        MDBoxLayout:
            orientation:'horizontal'
            adaptive_size:True
            MDCheckbox:
                value: '2'
                padding: [0,0,0,0]
                on_active: app.on_check_box(*args)
            MDLabel:
                text:'Тест 2'
                adaptive_width: True
        MDBoxLayout:
            orientation:'horizontal'
            adaptive_size:True
            MDCheckbox:
                value: '3'
                padding: [0,0,0,0]
                on_active: app.on_check_box(*args)
            MDLabel:
                text:'Тест 3'
                adaptive_width: True

    ```

> У `MDCheckBox` есть свойство `active` которое хранить булево значения текущего состояния эл-та
> (выбран/не выбран)

#### Выбор одного из нескольких

![img_1.png](src/selections/img_1.png)

* `main.py`
    ```python
    from kivymd.app import MDApp
    from kivy.lang import Builder
    
    
    class TestApp(MDApp):
        def build(self):
            self.root = Builder.load_file('ui.kv')
            self.theme_cls.theme_style = 'Dark'
            self.theme_cls.primary_palette = 'Blue'
            return self.root
    
        def on_check_box(self,checkbox, active):
            if active:
                print(checkbox.value)
                print(checkbox.group)
    
    
    TestApp().run()
    ```

* `ui.kv`
    ```
    MDScreen:
        md_bg_color: app.theme_cls.backgroundColor
        MDBoxLayout:
            orientation:'vertical'
            adaptive_size: True
            spacing: 10
            pos_hint: {'center_y':.5, 'center_x':.5}
            MDBoxLayout:
                orientation:'horizontal'
                adaptive_size:True
                MDCheckbox:
                    group: 'test'
                    value: '1'
                    padding: [0,0,0,0]
                    on_active: app.on_check_box(*args)
                MDLabel:
                    text:'Тест 1'
                    adaptive_width: True
            MDBoxLayout:
                orientation:'horizontal'
                adaptive_size:True
                MDCheckbox:
                    group: 'test'
                    value: '2'
                    padding: [0,0,0,0]
                    on_active: app.on_check_box(*args)
                MDLabel:
                    text:'Тест 2'
                    adaptive_width: True
            MDBoxLayout:
                orientation:'horizontal'
                adaptive_size:True
                MDCheckbox:
                    group: 'test'
                    value: '3'
                    padding: [0,0,0,0]
                    on_active: app.on_check_box(*args)
                MDLabel:
                    text:'Тест 3'
                    adaptive_width: True
    ```

> Если мы хотим использовать выбор одного из нескольких, то обязаны задать одинаковое имя группы
> для всех элементов перечисления


#### Родительские и подчиненные эл-ты выбора

![img.png](src/selections/img.png)

* `main.py`
    ```python
    from kivymd.app import MDApp
    from kivy.lang import Builder
    
    
    class TestApp(MDApp):
        def build(self):
            self.root = Builder.load_file('ui.kv')
            self.theme_cls.theme_style = 'Dark'
            self.theme_cls.primary_palette = 'Blue'
            return self.root
    
        def on_check_box(self,checkbox, active):
            if active:
                print(checkbox.value)
                print(checkbox.group)
    
    
    TestApp().run()
    ```

* `ui.kv`
    ```
    MDScreen:
        md_bg_color: app.theme_cls.backgroundColor
        MDBoxLayout:
            orientation:'vertical'
            adaptive_size: True
            spacing: 10
            pos_hint: {'center_y':.5, 'center_x':.5}
            MDBoxLayout:
                orientation:'horizontal'
                adaptive_size:True
                MDCheckbox:
                    group: 'root'
                    value: '0'
                    padding: [0,0,0,0]
                    on_active: app.on_check_box(*args)
                MDLabel:
                    text:'Тесты'
                    adaptive_width: True
            MDBoxLayout:
                orientation:'horizontal'
                adaptive_size:True
                MDCheckbox:
                    group: 'child'
                    value: '1'
                    padding: [20,0,0,0]
                    on_active: app.on_check_box(*args)
                MDLabel:
                    text:'Тест 1'
                    adaptive_width: True
            MDBoxLayout:
                orientation:'horizontal'
                adaptive_size:True
                MDCheckbox:
                    group: 'child'
                    value: '2'
                    padding: [20,0,0,0]
                    on_active: app.on_check_box(*args)
                MDLabel:
                    text:'Тест 2'
                    adaptive_width: True
    ```

#### Полезные атрибуты

* `checkbox_icon_normal` - иконка отображаемая во включенном состоянии (только для мн. выбора)
* `checkbox_icon_down` - иконка отображаемая в отключенном состоянии (только для мн. выбора)
* `radio_icon_normal` - иконка отображаемая во включенном состоянии (только для выбора одного из нескольких)
* `radio_icon_down` - иконка отображаемая в отключенном состоянии (только для выбора одного из нескольких)
* `color_active` - цвет иконки во включенном состоянии
* `color_inactive` - цвет иконки в отключенном состоянии 



> Чтобы создать иерархию нужно задать родительскому эл-ту группу `root`, а дочерним `child`

### MDSwitсh - переключатель

![img_3.png](src/selections/img_3.png)

* `ui.kv`
    ```
    MDScreen:
        md_bg_color: app.theme_cls.backgroundColor
        MDSwitch:
            pos_hint: {'center_y':.5, 'center_x':.5}
            on_active:
                print(1)
    ```

#### Полезные атрибуты
* `icon_active` - иконка отображаемая во включенном состоянии
* `icon_inactive` - иконка отображаемая в отключенном состоянии
* `icon_active_color` - цвет значка во включенном состоянии
* `icon_inactive_color` - цвет значка в отключенном состоянии
* `thumb_color_active` - цвет фона бегунка во включенном состоянии
* `thumb_color_inactive` - цвет фона бегунка в отключенном состоянии
* `track_color_active` - цвет фона переключателя во включенном состоянии
* `track_color_inactive` - цвет фона переключателя в отключенном состоянии


> Переключатель содержит те же события и свойства, что и эл-нт выбора

## Работа с Canvas


### Пример реализации рисования в Canvas касания

* `main.py`
    ```python
    from kivymd.app import MDApp
    from kivy.lang import Builder
    from kivy.graphics import Color, Ellipse, Line
    
    
    size_line=16
    type_edit="ellipse" # ellipse, line
    color=[0,1,0,1]
    
    
    class TestApp(MDApp):
        def build(self):
            self.root = Builder.load_file('ui.kv')
            self.config.write()  # Записать конфиг в файл
            return self.root
    
    
        def touch_down(self, element, touch):
            holst = self.root.ids.holst
            with holst.canvas:
                Color(color[0], color[1], color[2], color[3])  # Цвет создаваемого элемента
                if type_edit == "line" and holst.collide_point(touch.x + size_line / 2, touch.y + size_line / 2):
                    # Выбранный способ рисования не выходит за границы
                    Ellipse(
                        pos=[touch.x - size_line / 2, touch.y - size_line / 2],
                        size=[size_line, size_line]
                    )
                    touch.ud["line"] = Line(
                        points=[touch.x - size_line / 4, touch.y - size_line / 4],
                        width=size_line / 2
                    )
                if type_edit == "ellipse" and holst.collide_point(touch.x, touch.y):
                    # Выбранный способ рисования не выходит за границы
                    touch.ud["ellipse"] = Ellipse(
                        pos=[touch.x, touch.y],
                        size=[0, 0]
                    )
    
        def touch_up(self, element, touch):
            holst = self.root.ids.holst
            with holst.canvas:
                Color(color[0], color[1], color[2], color[3])
                if type_edit == "line" and holst.collide_point(touch.x + size_line / 2, touch.y + size_line / 2):
                    touch.ud["line"].points += [touch.x - size_line / 4, touch.y - size_line / 4]
                if type_edit == "ellipse" and holst.collide_point(touch.x, touch.y):
                    print("yes")
                    touch.ud["ellipse"].size = [touch.x - touch.ud["ellipse"].pos[0], touch.y - touch.ud["ellipse"].pos[1]]
    
    
    TestApp().run()
    ```
    > Функция `collide_point` проверяет входит ли указанные координаты в элемент

* `ui.kv`
    ```
    MDScreen:
        md_bg_color: app.theme_cls.backgroundColor
        MDWidget:
            id:holst
            pos_hint: {'center_x':.5,'center_y':.5}
            theme_bg_color:'Custom'
            md_bg_color:[1,0,0]
            size_hint_x:None
            size_hint_y:None
            theme_width: 'Custom'
            theme_height: 'Custom'
            size:[300,300]
            on_touch_down: app.touch_down(*args)
            on_touch_up: app.touch_up(*args)
    ```

## Верхний бар приложения TopAppBar

![img_3.png](src/appbar/img_3.png)  


* `ui.kv`
    ```
    MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDTopAppBar:  # Создание бара
        type: "small"  # Тип бпрп
        pos_hint: {"top": 1}

        MDTopAppBarLeadingButtonContainer:  # Левый контейнер с кнопками 
            MDActionTopAppBarButton:  # Кнопка для бара
                icon: "menu"

        MDTopAppBarTitle:  # Заголовок бара
            text: "AppBar small"  # Текст загловка
            pos_hint: {"center_x": .5}  # Центруем текст заголовка

        MDTopAppBarTrailingButtonContainer:  # Правый контейнер с кнопками
            MDActionTopAppBarButton:  # Кнопка для бара
                icon: "account-circle-outline"
    ```

Типы TopAppBar (атрибут `type`):
* `small`
    ![img.png](src/appbar/img.png)
* `medium`
    ![img_1.png](src/appbar/img_1.png)
* `large`
    ![img_2.png](src/appbar/img_2.png)
    

## Нижний бар приложения BottomAppBar



![img_4.png](src/appbar/img_4.png)


* `main.py`
    ```python
    from kivymd.app import MDApp
    from kivy.lang import Builder
    from kivymd.uix.appbar import MDActionBottomAppBarButton
    from kivymd.uix.list import *
    from faker import Faker
    
    fake = Faker('ru-RU')
    
    class TestApp(MDApp):
        def build(self):
            self.root = Builder.load_file('ui.kv')
            self.root.ids.bottom_appbar.action_items = [  # создаем кнопки управления
                MDActionBottomAppBarButton(icon='gmail')  # Добавляем кнопку управления
            ]
            for i in range(50):
                self.root.ids.cont_list.add_widget(
                    MDListItem(
                        MDListItemLeadingIcon(
                            icon='account',
                        ),
                        MDListItemHeadlineText(
                            text=fake.name(),
                        ),
                        MDListItemSupportingText(
                            text=fake.phone_number()
                        )
                    )
                )
            return self.root
    
    TestApp().run()
    ```

* `ui.kv`
    ```
    MDScreen:
        md_bg_color: app.theme_cls.backgroundColor
        ScrollView:  # Прокрутка
            id:card_list
            MDBoxLayout:  # Контейнер который прокучиваем
                id: cont_list
                orientation:'vertical'
                adaptive_height: True
        MDBottomAppBar:  # Нижний бар
            id: bottom_appbar
            scroll_cls: card_list  # Указываем эл-нт прокрутки для автоскрытия бара
            allow_hidden: True  #  Включение автоскрытия бара
            MDFabBottomAppBarButton:  # Функциональная кнопка управления 
                icon: "plus"
                theme_bg_color: "Custom"
                md_bg_color: app.theme_cls.primaryColor
                theme_icon_color: 'Custom'
                icon_color: 'white'
    ```


* Экран:  
    ![Великий скрин](src/appbar/ba.gif)

> Все кнопки управления хранятся в атрибуте action_items у BottomAppBar в виде списка кнопок MDActionBottomAppBarButton

> Обратите внимание что при скрытии BottomAppBar функциональная кнопка остается на месте. Стоит отметить что функционал автоскрытия не обязателен и вы можете его не использовать.

> Вы можете вручную скрыть/отобразить BottomAppBar используя методы hide_bar()/show_bar().


## Сборка APK

1. Проверяете наличие поддержки вашим процессором виртуализации. Включаете виртуализацию в `BIOS`.
2. Скачиваете `Ubuntu Desktop` с оф. сайта.
3. Включаете компонент `Hyper-V`:
   * открываете поиск в меню `ПУСК`;
   * ищите `Включение и отключение компонентов Windows` и открываете;
   * находите в списке `Hyper-V` и ставите ему галочку;
   * нажимаете `ОК` и ждёте окончания установки;
   * перезагружаете компьютер.
4.	Открываете `Диспетчер Hyper-V`
5.	Создаете виртуальную машину и устанавливаете на нее `Ubuntu` который скачали ранее. ([Как?](https://www.google.com/search?q=%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0+ubuntu+%D0%BD%D0%B0+hyper-v&oq=%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0+ubuntu+%D0%BD%D0%B0+hyper-v&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIICAEQABgWGB4yCAgCEAAYFhgeMgcIAxAAGO8FMgoIBBAAGIAEGKIE0gEJMTQ3MjhqMGoxqAIAsAIA&sourceid=chrome&ie=UTF-8))
6.	Открываете `Ubuntu`.
7.	Заходите в терминал и выполняете след. команду
    ```
    sudo apt update
    sudo apt install python3-pip 
    sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev cmake libffi-dev libssl-dev
    ```
8.	Скачиваете `PyCharm Community` в Магазине приложений на `Ubuntu`
9.	Создаете проект с виртуализацией под названием `Buildozer` 
10.	Открываем терминал в PyCharm и выполняете след. команды

    ```
    pip3 install buildozer
    pip3 install Cython==0.29.33
    pip3 install setuptools
    pip3 install https://github.com/kivymd/KivyMD/archive/master.zip
    ```

11.	Теперь у нас есть настроенный сборщик наших проектов.
12.	Добавляем файлы своего проекта
13. Создаем `spec` файл командой
    ```
    buildozer init
    ```
14. В `spec` файле обязательно исправляем след. параметры
    * requirements - библиотеки используемые в вашем проекте
        ```
        requirements = python3,
            kivy,
            https://github.com/kivymd/KivyMD/archive/master.zip,
            materialyoucolor,
            exceptiongroup,
            asyncgui,
            asynckivy,
            И аналогично остальные ваши библиотеки проекта  
        ```
    * osx.kivy_version - ваша версия kivy в проекте
        ```
        osx.kivy_version = 2.3.1  # Указываете свою версию
        ```
15. Запускаете сборку проекта командой:
    ```
    buildozer android debug
    ```
    > Если у вас в проекте измениться состав библиотек желательно делать очистку сборщика командой:
    >```
    > buildozer android clean
    >```
        
    


