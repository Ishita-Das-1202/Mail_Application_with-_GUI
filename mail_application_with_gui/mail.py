#Mail Application with GUI
import tkinter as tk
import smtplib
from tkinter import messagebox

# Function to send email
def send_email():
    sender_email = "###########"  # Enter your email here
    sender_password = "####"  # Enter your password here
   

    receiver_email = receiver_email_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", "end-1c")

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, receiver_email, message)
        server.quit()

        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Creation of  GUI
root = tk.Tk()
root.title("Mail Application")

receiver_label = tk.Label(root, text="Receiver Email:")
receiver_label.pack()
receiver_email_entry = tk.Entry(root)
receiver_email_entry.pack()

subject_label = tk.Label(root, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(root)
subject_entry.pack()

body_label = tk.Label(root, text="Body:")
body_label.pack()
body_text = tk.Text(root, height=10, width=30)
body_text.pack()

send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.pack()

root.mainloop()
