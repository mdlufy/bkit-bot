import pytest
from pytest_bdd import scenario, given, when, then

@scenario("catalog.feature", "Creating start menu")
def test_start_bot():
    pass

@given("The user starts the chat")
def test_creation_dialog():
    pass

@when("The start command is entered")
def test_enter_command_start():
    pass

@then("The start menu is displayed")
def test_result_menu():
    pass