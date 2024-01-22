Задание
Ваша задача состоит в создании онлайн-платформы для управления задачами с использованием Django. Веб-приложение должно предоставлять возможность создавать задачи, назначать их исполнителям, отслеживать статус выполнения и обмениваться комментариями к задачам.

▪️ Создайте модели Task и User, которые будут содержать следующие поля:

Модель User:

- имя пользователя (CharField)

- электронная почта (EmailField)

- пароль (CharField)

Модель Task:

- название задачи (CharField)

- описание задачи (TextField)

- исполнитель (ForeignKey к модели User)

- статус выполнения (ChoiceField: "В ожидании", "В процессе", "Завершено")

- дата создания (DateTimeField)

- дата завершения (DateTimeField)

▪️ Создайте представление (view) для отображения списка всех задач на главной странице. Задачи должны быть отсортированы 
по дате создания в обратном порядке (самые новые задачи должны быть вверху).

▪️ Создайте представление (view) для создания новой задачи. На странице создания задачи пользователь должен ввести 
название, описание, исполнителя и дату завершения задачи.

▪️ Реализуйте функциональность назначения задач исполнителям. Пользователи должны иметь возможность выбирать 
исполнителя из списка зарегистрированных пользователей при создании задачи.

▪️ Создайте представление (view) для просмотра отдельной задачи. Пользователи должны иметь возможность просматривать 
детали задачи, включая описание, исполнителя, статус выполнения и комментарии к задаче.

▪️ Реализуйте функциональность обновления статуса выполнения задачи. Пользователи должны иметь возможность изменять 
статус выполнения задачи на "В процессе" и "Завершено".

▪️ Реализуйте функциональность добавления комментариев к задачам. Пользователи должны иметь возможность оставлять 
комментарии к задачам, обсуждать их и отвечать на комментарии других пользователей.

▪️ Настройте маршрутизацию (URL routing) в Django, чтобы пользователи могли получать доступ к каждому представлению 
(view) по правильному URL.

▪️ Добавьте базовую аутентификацию, чтобы только зарегистрированные пользователи могли создавать задачи, назначать 
исполнителей, изменять статус выполнения и оставлять комментарии.