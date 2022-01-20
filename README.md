# Todo
Todo program that was done with django. It has registration, logging and personal cabinet pages. PostgreSQL is database where all data will be saved 
# Installation
You need to download django
``` bash
pip install django
```
and you need to download repository of a program from github.
# Usage
You need to change database and insert your information in settings.py
To start you need open folder in terminal and enter
``` bash
cd ToDoApp
```
``` bash
python manage.py migrate
```
``` bash
python manage.py runserver
```
After that you need to go by link that was given by program.
# Examples
Main page or logging page:

![Снимок экрана (1440)](https://user-images.githubusercontent.com/77801087/150338360-91c2b634-b0cf-445a-8973-8eefc1ede895.png)
Personal cabinet and it has some task:

![Снимок экрана (1441)](https://user-images.githubusercontent.com/77801087/150338407-df307d3d-11c5-465e-be58-760d4998117d.png)
We can add new one:

![Снимок экрана (1442)](https://user-images.githubusercontent.com/77801087/150338428-29dc3c21-a1cb-44c0-8851-0a43dd7a3480.png)
And delete previous one:

![Снимок экрана (1443)](https://user-images.githubusercontent.com/77801087/150338437-02d83a36-0d1e-4ab6-a0f4-62e93b69efc8.png)
Let's look to the database:

![Снимок экрана (1444)](https://user-images.githubusercontent.com/77801087/150338451-2f949d18-03bd-4834-8d0f-77fa1c3cdec6.png)

It create toDo to everyone and save tasks to the table:

![image](https://user-images.githubusercontent.com/77801087/150338595-f101b35a-35b4-41cd-bf26-bd85fd30e2ea.png)

And it has data about all users:

![Снимок экрана (1446)](https://user-images.githubusercontent.com/77801087/150338876-c5ea8d28-bc59-4961-a8f0-94fd0e1629b6.png)
![Снимок экрана (1447)](https://user-images.githubusercontent.com/77801087/150338891-ae4354b7-95dc-4fb0-964f-6658e2ccae7e.png)
Let's add new one user:

![image](https://user-images.githubusercontent.com/77801087/150339273-ad7495e5-1d05-400f-8506-bae4c1867189.png)
And result in database:

![image](https://user-images.githubusercontent.com/77801087/150339386-afe34980-8bb4-4add-8349-8f66f3daacca.png)


# License
[MIT](https://choosealicense.com/licenses/mit/)
