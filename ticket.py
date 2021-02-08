# Sending emails without attachments using Python.
# importing the required library.
import smtplib
email = smtplib.SMTP('smtp.gmail.com', 587)
email.starttls()
email.login("rajaathota72@gmail.com", "**********")
message = "message_to_be_send"
email.sendmail("info@robokalam.com", "info@marcinsights.com", message)
email.quit()