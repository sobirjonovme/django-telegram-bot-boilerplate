JAZZMIN_SETTINGS: dict = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "HEAT Warehouse Admin",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "HEAT Warehouse",
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "HEAT Warehouse",
    # Logo to use for your site, must be present in static files, used for brand on top left
    # "site_logo": "assets/img/admin-logo.png",
    # "login_logo": "assets/img/kapital-qurilish-logo.png",
    # "login_logo_dark": "assets/img/kapital-qurilish-logo.png",
    # CSS classes that are applied to the logo above
    "site_logo_classes": "img",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    # "site_icon": "assets/img/kapital-qurilish-logo.png",
    # Welcome text on the login screen
    "welcome_sign": "Welcome to HEAT Warehouse Admin",
    # Copyright on the footer
    "copyright": "sobirjonov me",
    # The model admin to search from the search bar, search bar omitted if excluded
    # "search_model": "",
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {
            "name": "Home",
            "url": "admin:index",
            "permissions": ["auth.view_user"],
        },
        # external url that opens in a new window (Permissions can be added)
        # {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
    ],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [{"model": "users.user"}],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": False,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": [
        # "common.Region",
    ],
    "icons": {
        # account app
        "account": "fas fa-users-cog",
        "account.User": "fas fa-user-friends",
        # account app
        "defender": "fas fa-shield-alt",
        "defender.access_attempt": "fas fa-shield-alt",
        # common app
        "common": "fas fa-cubes",
        "common.Advertisement": "fas fa-ad",
        "common.Appeal": "fas fa-newspaper",
        "common.AppealStatistics": "fas fa-chart-line",
        "common.Banner": "fas fa-chalkboard",
        "common.Contact": "fas fa-phone-alt",
        "common.Department": "fas fa-building",
        "common.DirectorateMission": "fas fa-clipboard",
        "common.Footer": "fas fa-file-alt",
        "common.HomePublicInformation": "fas fa-file",
        "common.LandingPageSection": "fas fa-list-ol",
        "common.AntiCorruptionSection": "fas fa-list-ol",
        "common.Menu": "fas fa-list",
        "common.SocialNetwork": "fas fa-network-wired",
        "common.StaticPage": "fas fa-clipboard",
        "common.UseFullLinks": "fas fa-external-link-alt",
        "common.WorkingPrinciple": "fas fa-clipboard",
        "common.SearchModel": "fas fa-search",
        "common.TelegramMessageConfig": "fas fa-robot",
        # staff app
        "staff": "fas fa-users",
        "staff.Employee": "fas fa-user",
        "staff.Vacancy": "fas fa-edit",
        "staff.Candidate": "far fa-file-alt",
        # news app
        "news": "far fa-newspaper",
        "news.NewsCategory": "fas fa-bars",
        "news.News": "fas fa-newspaper",
        "news.NewsMedia": "far fa-image",
        "news.NewsViews": "far fa-eye",
        "news.Project": "far fa-building",
        "news.ProjectMedia": "far fa-image",
        # documents app
        "documents": "fas fa-file-alt",
        "documents.Document": "fas fa-file-export",
        "documents.DocumentType": "fas fa-list",
        "documents.PublicInformation": "fas fa-file-pdf",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-folder",
    "default_icon_children": "fas fa-circle",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": "assets/css/main.css",
    "custom_js": "assets/js/admin.js",
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    # "changeform_format": "vertical_tabs",
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    # Add a language dropdown into the admin
    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "litera",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}
