# Django-Contact-Form
Django contact form with Bootstrap 4 using Django's built-in email support, Forms API. Email submitted will be returned to the terminal.


![screenshot](https://github.com/ShannonCanTech/Django-Contact-Form/blob/master/Contact%20Form%20Screenshot.png)

### Success View
![screenshot](https://github.com/ShannonCanTech/Django-Contact-Form/blob/master/Success%20Contact%20Form.png)

### Result
![screenshot](https://github.com/ShannonCanTech/Django-Contact-Form/blob/master/Terminal%20Contact%20Form%20Result.png)

## How-to
1. Create new directory
2. Install virtial enviroment (Homebrew or Chocolately in PowerShell)
3. Install Django
4. Start the virtual enviroment
5. Create Django project with sendemail app within it
6. Migrate and run the server
7. Update settings.py, urls.py, sendemail/urls.py
8. Create a new app in sendemail called forms
9. Create ContactForm class within sendemail/forms.py
10. Create emailview and successview in sendemail/views.py
11. Create templates directory and email.html within templates
12. Add templates dir to setting.url at DIRS
13. Add django html and Bootstrap CDN to templates/email.html
14. Send first email

If issues arise, restart the server.
