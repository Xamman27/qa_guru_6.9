from selene import browser, by, be
import allure
from allure_commons.types import Severity


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Frunzelen')
@allure.description('Тест с использованием степов')
@allure.feature('Поиск issues в Github')
@allure.link('https://github.com', name='Testing')
def test_github():
    with allure.step('Open main page'):
        browser.open("https://github.com")
    with allure.step('find search input'):
        browser.element(".header-search-button").click()
    with allure.step('enter search data'):
        browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
        browser.element("#query-builder-test").press_enter()
    with allure.step('find issues tab'):
        browser.element('[id=":r8:"]').click()
    with allure.step('find issues #1'):
        browser.element(by.partial_text("#1")).should(be.visible)#Тест падает не пойму причину
