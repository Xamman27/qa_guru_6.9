from selene.support.shared import browser
from selene.support import by
from selene.support.conditions import be

browser.open("https://github.com")
browser.element(".header-search-button").click()
browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
browser.element("#query-builder-test").press_enter()

browser.element('[class="Item__LiBox-sc-yeql7o-0 kUyONJ"]').click()

browser(by.partial_text("#8")).should(be.visible)