<p align="center">
  <img align="center" src="https://github.com/NafieAlhilaly/api-fatoora/blob/main/images/secret-qr-code.png" width=300/>
</p>

You can try it with simple ui @ [api-fatoora](https://api-fatoora.herokuapp.com/)
Learn more about [ZATCA's E-invoice](https://zatca.gov.sa/en/E-Invoicing/Introduction/Pages/What-is-e-invoicing.aspx) 
# api-fatoora
API to help generating QR-code for ZATCA's e-invoice known as Fatoora with any programming language
> _Disclaimer: this API is not **secure** yet, please dont post sensitive information._

---------
## how to use it 
The simplest way to get started is to send POST request with json of your data, here an example using python requests

#### Convert data to base 64
`POST /to_base64/`
```python
import requests
import json

data = {
    "seller_name": "nafie",
    "tax_number": "876554674",
    "invoice_date": "875t6554",
    "total_amount": "200",
    "tax_amount": "30"   
}

data = json.dumps(data)

response = requests.post('https://api-fatoora.herokuapp.com//to_base64', data=data)
print(response.json())
# result : {'TLV_to_base64': 'AQVuYWZpZQIJODc2NTU0Njc0Awg4NzV0NjU1NAQDMjAwBQIzMA=='}
```

#### Convert data to QR-Code
`POST /to_qrcode_image/`
```python
import requests
import json

data = {
    "seller_name": "nafie",
    "tax_number": "876554674",
    "invoice_date": "875t6554",
    "total_amount": "200",
    "tax_amount": "30"   
}

data = json.dumps(data)

response = requests.post('https://api-fatoora.herokuapp.com//to_qrcode_image', data=data)
response = response.content()
```
