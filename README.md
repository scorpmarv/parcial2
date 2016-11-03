# parcial2

Clone this repository



Install virtualenv
$ [sudo] pip install virtualenv



Create enviroment
$ virtualenv env



Activate enviroment
$ source bin/activate



Install requirements
$ pip install requirements.txt



Migrate database
$ python manage.py migrate



Run server
$ python manage.py runserver 0.0.0.0:{port}



To post an invoice open the url with Postman:

http://localhost:{port}/invoices/

Mode: Post

Body -> raw:

{
  "InvoiceNumber": {id},
  "Date": "2002-05-30T09:30:10-06:00",
  "CustomerName": "Empresa SRL",
  "InvoiceTotalValue": 2000,
  "InvoiceDetail": [{
    "ArticleId": 100,
    "ArticleName": "Computer",
    "ArticlePrice": 1000
  },
  {
    "ArticleId": 150,
    "ArticleName": "Hard drive",
    "ArticlePrice": 2000
  }]
}




To check an invoice open the url with Postman:

http://localhost:{port}/invoices/{id}

Mode: Get