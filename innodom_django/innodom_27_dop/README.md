Задание 1
Создайте базовый шаблон (base.html), который будет содержать общую структуру вашего веб-сайта, включая заголовок, 
меню навигации и футер. Затем создайте дочерний шаблон (child.html), который наследует базовый шаблон и добавляет 
уникальное содержимое в блок {% block content %}. В дочернем шаблоне определите блоки для изменения заголовка 
({% block title %}) и футера ({% block footer %}).

  

Задание 2
Создайте основной шаблон (main.html), который будет содержать общие элементы для всех страниц вашего веб-сайта,
например, хедер и футер. Затем создайте дополнительный шаблон (sidebar.html), который будет содержать дополнительную
боковую панель с информацией. Включите шаблон sidebar.html в основной шаблон с помощью тега {% include 'sidebar.html' %}.
Создайте несколько дочерних шаблонов (page1.html, page2.html), которые наследуют основной шаблон и определяют уникальное
содержимое для каждой страницы. 
Убедитесь, что боковая панель из шаблона sidebar.html отображается на каждой странице вашего веб-сайта.