"""
Use __main__ to specify the entry point to the application
"""
from admin_page import load_admin_page
from landing_page import load_landing_page
from subscribe_page import load_subscribe_page

if __name__ == '__main__':
    page = input('Choose the page to load: "landing", "subscribe", "admin":\n')
    print('Loading ' + page + ' page')
    if page == 'landing':
        load_landing_page()
    elif page == 'subscribe':
        load_subscribe_page()
    elif page == 'admin':
        load_admin_page()
    else:
        print('Unexpected page was requested')
