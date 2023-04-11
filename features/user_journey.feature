Feature: sign in and log in

  Scenario: sign in and log in
    Given a user opens the home page
    When a user clicks signup
    Then then they should be on the "Signup Page"

    When the user enters their information
      | email     | username | password | confirm_password |
      | test@test | tester   | test     | test             |
    And clicks submit
    Then then they should be on the "info Page"

    When the user enters their personal information
      | given_name | family_name | age |
      | Steve      | steven           | 72  |
    And clicks submit
    Then then they should be on the "home Page"

    When a user clicks login
    Then then they should be on the "Login Page"

    When the user enters their login information
      | username | password |
      | tester   | test     |
    And clicks submit
    Then then they should be on the "Page"
    And they should see their name "Steve"