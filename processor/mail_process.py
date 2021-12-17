import pickle
from datetime import datetime


def save_mail(data, mail_dict, counter_list):
    mail = data['mail']
    password = data['password']
    mail_dict[mail] = password
    counter_list += 1
    # save 1000 accounts
    if counter_list % 1000 == 0:
        time_now = datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(f"./store/{time_now}_1000_account.pkl", 'wb') as f:
            pickle.dump(mail_dict, f)
        # get new mail list
        mail_dict = dict()
