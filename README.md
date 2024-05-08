### INF601 - Advanced Programming in Python
### Eve Wright
### Final Project


# Final Project

This project serves as a demo for a record-keeping and task management system geared toward Academic Advisors. This project also utilizes openAI’s chatGPT API to generate paragraph from user input.

## Description

Efficient Appointment Management: Advisr enables advisors to easily add an appointment record with required fields, 
cutting down on mistakes and missing information. Advisors can log in, create appointments, and document detailed notes for each interaction.

To-Do List Integration: Stay organized by using the dedicated to-do page where advisors can add and manage tasks, 
keeping all important action items in one centralized location for enhanced organization and efficiency.

AI Assistance: Complete notes more efficiently with the help of a paragraph generator, powered by openAI. 
Enter your bulleted or incomplete notes, and the paragraph generator will transform them into coherent paragraphs, saving you time and effort.

Appointment Search Functionality: Unlike existing systems, Advisr offers a search and filter feature by appointment date. 
This allows advisors to quickly locate specific appointments, improving record tracking capabilities.


## Getting Started

### Dependencies & Installing

* PIP Install instructions by running the following command in terminal:
```
-r requirements.txt
```
* Subscribe to openAI's chatGPT API and get an API key. Then, enter the API key in appts/views 
* under def generate_paragraph: https://rapidapi.com/haxednet/api/chatgpt-api8


### Executing program

* Move to project folder by running the following command in terminal:
```
cd mysite
```
* Now, run the following commands in the terminal:
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
* Create a superuser for administrator use by running following command in terminal:
```
python manage.py createsuperuser
```

## Authors

Contributors names and contact info

ex. Eve Wright


## Acknowledgments

Inspiration, code snippets, etc.
* [Generic List & Detail Views Django](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views
)
* [Django Login, Logout](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
* [Search by Date Range Django](https://www.youtube.com/watch?v=0pybB--Z7qo)
* [MDBootstrap To-Do List Styling](https://mdbootstrap.com/docs/standard/extended/to-do-list/)