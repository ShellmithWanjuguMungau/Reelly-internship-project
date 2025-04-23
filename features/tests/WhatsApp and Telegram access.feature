# Created by USER at 23/04/2025
Feature: # Enter
  # Enter feature description here

  Scenario: Users can access WhatsApp and Telegram communities
    Given Open login page
    Given Enter email
    Given Enter password
    Given Click continue
    When Click on the settings option
    When Click on the support option
    When Switch to the new tab
    Then Verify the url contains api.whatsapp.com
    And Switch back to previous page
    And Click on news option
    And Verify url contains t.me
