from selene.support.shared import browser
from selene.support import by
from selene.support.conditions import be
import pytest


def test_github():
    browser.open("https://github.com")
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
    browser.element("#query-builder-test").press_enter()

    browser.element('[id=":r8:"]').click()

    browser.element(by.partial_text("#1")).should(be.visible)#Тест падает не пойму причину
