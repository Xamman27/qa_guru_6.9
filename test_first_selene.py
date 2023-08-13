from selene import browser, by, be
import allure
from allure_commons.types import Severity

@allure.tag('Web')
@allure.severity(Severity.TRIVIAL)
@allure.label('owner', 'Maksimov')
@allure.description('Тест без степов и декоратора')
@allure.feature('Поиск issues в Github')
@allure.link('https://github.com', name='Testing')
def test_github():
    browser.open("https://github.com")
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
    browser.element("#query-builder-test").press_enter()

    browser.element('[id=":r8:"]').click()

    browser.element(by.partial_text("#1")).should(be.visible)#Тест падает не пойму причину
