import win32com.client as win32

#Cria a autenticação com outlook
outlook = win32.Dispatch('Outlook.application')

#criar emails
email = outlook.CreateItem(0)

#configurar as informações do emails
email.To = "g.quadrado@outlook.com"
email.Subject = "E-mails automatico do python"
email.HTMLBody = "Corpo do E-mails"
