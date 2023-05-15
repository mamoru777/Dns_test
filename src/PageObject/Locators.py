class Locator(object):
    # logo = "header-logo"
    search_input = "presearch__input"
    search_button = "presearch__icon-search"
    Smarphones_and_photo = "//div[contains(@class, 'catalog-menu-rootmenu homepage')]/div[3]"
    Smartphones = "//div[@id='tns1-item0']/div[contains(@class, 'popular-categories__item-content')]/div[contains(@class, 'popular-categories__description')]/a[contains(@class, 'popular-categories__title')]"
    #Smartphones_and_Gadzhet = "//div[contains(@class, 'subcategory__item-container ')]/a[contains(@class, 'subcategory__item ui-link ui-link_blue')]/div[contains(@class, 'subcategory__content')]"
    #Prices = "//div[contains(@class, 'ui-checkbox-group ui-checkbox-group_list')]/label"
    Commenets = "//div[contains(@class, 'product-card-tabs__list')]/a[2]"
    Stars = "//div[contains(@class, 'star-rating')]/div[contains(@class, 'star-rating__stars')]/span[1]"
    #Dost = "input-row__container input-row__container_grey input-row__container_auto-grow"#"//div[contains(@class, 'add-opinion__block-with-vobler')]/div[contains(@class, 'input-row__container input-row__container_grey input-row__container_auto-grow')]"
    Input_button = "//div[contains(@class, 'add-opinion__block-button')]/button[contains(@class, 'button-ui button-ui_brand button-ui_big add-opinion__button')]"
    #AddComment = "//div[contains(@class, 'product-card-tabs__contents')/div[contains(@class, 'product-card-tabs__content product-card-tabs__content_default')]/div[contains(@class, 'opinions-widget')]/div[contains(@class, 'ow-header opinions-widget__header')]/div[contains(@class, 'ow-header__cols')]/div[contains(@class, 'ow-header__new-opinion')]/a[contains(@class, 'button-ui button-ui_brand ow-header__new-opinion-text-link')]"
    Izbran = "wishlist-link-counter"
    Error = "empty-search-results__container-data-header"
    Titles = "//a[contains(@class, 'catalog-product__name ui-link ui-link_black')]/span[1]"
    #Button_enter = "base-ui-button_JKH base-ui-button_medium_uIe base-ui-button_brand_avQ base-ui-button_ico-none_M-8"#"//div[contains(@class, 'user-profile__menu')]/div[contains(@class, 'user-profile__container-user-menu)']/div[contains(@class, 'user-profile__wrapper')]/div[1]/div[contains(@class, 'user-profile__guest')]/button[contains(@class, 'base-ui-button_JKH base-ui-button_medium_uIe base-ui-button_brand_avQ base-ui-button_ico-none_M-8')]"
    def getPrices(self, id):
        return "//div[contains(@class, 'ui-checkbox-group ui-checkbox-group_list')]/label[" + str(id) + "]"
    def Like(self, id):
        return "//div[contains(@class, 'catalog-products view-simple')]/div[" + str(id) + "]/div[contains(@class, 'product-buy product-buy_one-line catalog-product__buy')]/button[contains(@class, 'button-ui button-ui_white button-ui_icon wishlist-btn')]"

