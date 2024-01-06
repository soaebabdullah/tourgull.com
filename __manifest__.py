# -*- coding: utf-8 -*-
{
    'name': "Available Rental Service",

    'summary': """
        1. Rental Service
        """,

    'description': """
        1. Rental Service

        Test files:
        server/odoo/custom/as_rental/controllers/test.py
        server/odoo/custom/as_rental/templates/tmp_test.xml
    """,

    'author': "Ab Razzak",
    'website': "https://www.xsellencebdltd.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13.0.1',

    # any module necessary for this one to work correctly
    # 'depends': ['base', 'website', 'product', 'website_sale', 'portal', 'event', 'website_event', 'website_blog',
    #             'website_blog_extend', 'theme_prime'],
    'depends': ['base', 'mail', 'product', 'sale', 'dev'],
    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views_host_app.xml',
        'views/views_host_apps.xml',
        'views/views_rent_car_app.xml',
        'views/inherit_product.xml',
        'views/inherit_partner.xml',
        # 'views/inherit_setting.xml',

        'views/views_rent_car_brand.xml',
        'views/views_rent_car_type.xml',
        'views/views_rent_service_location.xml',
        'views/views_rent_model_year.xml',
        'views/views_rent_reg_year.xml',
        'views/views_rent_car_slider.xml',

        'views/views_host_property_type.xml',
        'views/views_host_place_type.xml',
        'views/views_host_ame_1.xml',
        'views/views_host_ame_2.xml',
        'views/views_host_ame_3.xml',
        'views/views_host_book.xml',
        'views/views_host_slider.xml',
        'views/views_rent_property_review.xml',
        'views/views_rent_package.xml',
        'views/views_rent_car_book.xml',
        'views/views_host_service_category.xml',
        'views/views.xml',
        'views/notification.xml',

        # security_service
        'views/security_service/security_service.xml',

        # security_service
        'views/cleaning_service/cleaning_service.xml',

        # Tourist Attraction
        'views/tourist_attraction/tourist_attraction.xml',

        # Other views
        'views/views_wishlist.xml',
        'views/views_visit.xml',
        'views/website_guest.xml',

        # Templates - Host property pages
        # 'templates/host/test_form.xml',
        'templates/host/rp_add.xml',
        'templates/host/host_templates.xml',
        'templates/host/browse_property.xml',
        'templates/host/browse_property_detail.xml',
        'templates/host/rent_host_register.xml',
        'templates/host/rent_host_register_form.xml',
        # 'templates/host/guest_add_info.xml',
        # 'templates/host/submit_a_review.xml',
        # 'templates/host/base.xml',
        'templates/host/guest_signup.xml',
        'templates/host/guest_update.xml',
        'templates/host/host_signup.xml',
        # 'templates/host/become_a_host.xml',
        # 'templates/host/host_category.xml',
        # 'templates/host/continue_as_a_guest.xml',
        'templates/host/host_login_signup_select.xml',
        'templates/host/category_selection.xml',

        # Templates - /my
        # 'templates/my/favourite.xml',
        # 'templates/my/db_host.xml',
        # 'templates/my/db_guest.xml',
        # 'templates/my/db_test.xml',
        # 'templates/my/booking_list.xml',
        # 'templates/my/portal.xml',
        # 'templates/my/portal_host.xml',
        'templates/my/db_my_account.xml',
        'templates/my/db_host_my_account.xml',

        'templates/my/db/dashboard_host.xml',
        'templates/my/db/dashboard_guest.xml',
        'templates/my/db/notifications.xml',
        'templates/my/db/message.xml',
        'templates/my/db/family_member_edit.xml',

        # Templates - Rent A Car
        # 'templates/rent_a_car/rent_a_car_base.xml',
        # 'templates/rent_a_car/rent-a-car-browse.xml',
        # 'templates/rent_a_car/rent-a-car-browse-details.xml',
        # 'templates/rent_a_car/rent_a_car_profile.xml',
        # 'templates/rent_a_car/rent_a_car_my_profile.xml',
        # 'templates/rent_a_car/tests.xml',
        # 'templates/rent_a_car/rent_a_car_registration.xml',
        # 'templates/rent_a_car/car_msg_success.xml',
        # 'templates/rent_a_car/car_msg_danger.xml',

        # security_service
        # 'templates/security_service/security_service.xml',

        # Cleaning Service
        # 'templates/cleaning_service/cleaning_service.xml',

        # Tourist Attraction
        # 'templates/tourist_attraction/tourist_attraction.xml',

        # Templates - other
        # 'templates/other/host_application_form.xml',
        # 'templates/other/car_registration.xml',
        # 'templates/other/message_success.xml',
        # 'templates/other/message_danger.xml',
        # 'templates/other/rent_car_browse.xml',
        # 'templates/other/rent_car_browse_details.xml',
        # 'templates/other/my_home.xml',
        # 'templates/other/footer_rent_property.xml',
        # 'templates/other/msg.xml',

        # Templates - inherit
        # 'templates/tour_guide/tour_guide.xml',

        # templates
        'templates/templates.xml',

        # Test
        # 'templates/tmp_test.xml',

        # New New New New New New New
        # View
        'views/base/website_menu.xml',

        # templates
        'templates/layout/as_layout.xml',
        'templates/layout/guest__layout_01.xml',
        'templates/home/home.xml',
        'templates/search.xml',
        'templates/wishlist.xml',
        'templates/tmp_01.xml',

        # Templates - Layout
        'templates/layout/rp_footer.xml',

        # Templates - Event
        'templates/event/event.xml',
        'templates/event/event_package.xml',

        # Templates - Property -> Hotel
        'templates/property/hotel.xml',
        'templates/property/property-search.xml',
        'templates/property/list-property.xml',

        # Menu
        'views/views_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
