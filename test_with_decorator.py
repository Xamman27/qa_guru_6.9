from selene import browser, by, be
import allure
from allure_commons.types import Severity


@allure.tag('Web')
@allure.severity(Severity.TRIVIAL)
@allure.label('owner', 'Maksimov')
@allure.description('Тест c использованием декоратора')
@allure.feature('Поиск issues в Github')
@allure.link('https://github.com', name='Testing')
def test_github_with_decorator():
    open_main_page('https://github.com')
    find_search_input()
    search_repository('eroshenkoam/allure-example')
    find_issues_tab()
    find_issues()


@allure.step("Open main page")
def open_main_page(main_page):
    browser.open(main_page)


@allure.step('find search input')
def find_search_input():
    browser.element(".header-search-button").click()


@allure.step('Search{repo}')
def search_repository(repo):
    browser.element("#query-builder-test").send_keys(repo)
    browser.element("#query-builder-test").press_enter()


@allure.step('find issues tab')
def find_issues_tab():
    browser.element('[id=":r8:"]').click()


@allure.step('find issues #1')
def find_issues():
    browser.element(by.partial_text("#1")).should(be.visible)