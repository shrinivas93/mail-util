from mailer import Mailer

mailer = Mailer('smtp.gmail.com', 465)
mailer.authenticate('ssshukla1993@gmail.com', '<PASSWORD_HERE>')
mailer.send_mail(subject='Test Email', sender={
    'name': 'Shrinivas Shukla',
    'email': 'ssshukla1993@gmail.com'
},
    recipients={
        'To': ['ssshukla1993@gmail.com'],
        'Cc': ['madhurabhad@gmail.com'],
        'Bcc': ['shrinivas_shukla@persistent.co.in']
},
    body='Dear <b>X</b>,<br/>This mail is sent from python code.<br/><br/><i>HTML</i><span style="background: red; color: green; font-weight: bold;font-size: 24px; font-family: Calibri;">works like magic</span><br/><br/>Also, check out the attachment.<br/><figure> <img src="cid:shivaji_img" alt="Shivaji" style="width:100%"> <figcaption>Jai Bhawani.... Jai Shivaji...</figcaption></figure>',
    attachments=[
        {
            'name': 'attachment.txt',
            'path': 'attachment.txt'
        }
],
    inline_images=[
        {
            'name': 'shivaji.jpg',
            'path': 'shivaji.jpg',
            'cid': 'shivaji_img'
        }
]
)
