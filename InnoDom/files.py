# Есть файл titanic.txt. Нужно открыть его и вывести содержимое.


with open("titanic.txt", "r", encoding="utf-8") as titanic:
    print(titanic.read())


# Из уже существующего файла titanic.txt посчитайте количество строк и выведите их.


with open("titanic.txt", "r", encoding="utf-8") as titanic:
    print(len(titanic.readlines()))


# Откройте существующий файл titanic.txt, запишите последние две             
#  строки из этого файла в новый файл some_info_about_titanic.txt


with open("titanic.txt", "r", encoding="utf-8") as  titanic, open("some_info_about_titanic.txt", "w", encoding="utf-8") as some_titanic:
    lines_titanic = titanic.readlines()
    for i in lines_titanic[-2:]:
        some_titanic.write(i)


# Пользователь вводит разные данные с клавиатуры. Если он вводит                  
# строку - записать её в файл user_response.txt. Если вводит число - пропускать его.


user_text = input("Enter your tetx: ")
with open("user_response.txt", "a") as user_respons:
    if not(user_text.isdigit()):
        user_respons.write(user_text + '\n')
    else:
        print("Your text is number")


# Считайте лог-файл 'requests.log', а затем проанализируйте его, выводя количество            
# запросов по каждому IP-адресу.

ip = set()
ip_dictionary = {}
with open("requests.log", "r") as requests:
    # for_count = requests.read()
    requests_lines = requests.readlines()
    for element in requests_lines:
        element_list = element.split(" ")
        ip.add(element_list[0])
with open("requests.log", "r") as requests:
    for_count = requests.read()
    for key in ip:
        ip_dictionary[key] = for_count.count(key)
    
print(ip_dictionary)


# Есть файл log.txt. Откройте его, найдите только строки, в которых                  
# выведены ошибки. Эти строки запишите в отдельный файл errors.txt


with open("requests.log", "r") as requests, open("errors.txt", "w") as errors:
    list_requests = requests.readlines()
    for elemen in list_requests:
        if '404' in elemen:
            errors.write(elemen)


#АААА
#AAAAAAA
# import pytube
# import io

# # Ввод URL-адреса видео
# video_url = "https://www.youtube.com/watch?v=oZzorKHnFgA"

# # Ввод пути и имени файла для сохранения
# file_path = "downloaded_video.mp4"
# try:
#     youtube = pytube.YouTube(video_url)
#     video = youtube.streams.first()

#     buffer = io.BytesIO()

#     video.stream_to_buffer(buffer)

#     with open(file_path, "wb") as file_:
#       file_.write(buffer.getbuffer())
    
#     print('Видео успешно загружено!')
# except Exception as e:
#     print({
#         "error message": "Произошла ошибка при загрузке видео",
#         "error info": f"{e}"
#     })

print()
print("Task: Open titanic.txt, output. Count lines. "
      "Write the last 2 lines to some_info_about_titanic.txt")
print()
with (open("titanic.txt", "r", encoding="utf-8") as titanic,
      open("some_info_about_titanic.txt", "w+", encoding="utf-8") as some_info):
    titanic_list = titanic.readlines()
    for line_str in titanic_list:
        print(line_str.strip())

    print(f"Lines number= {len(titanic_list)}")
    print()

    some_info.writelines(titanic_list[-2:])
    print(some_info.read())