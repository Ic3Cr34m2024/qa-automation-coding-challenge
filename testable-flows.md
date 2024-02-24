(Add your list of flows here)
Included in this file is a list of 7 scenarios that were taken into consideration based on the requirements specified in the instructions. These scenarios were taken into account trying to cover the acceptance criteria that Adam wanted to continue monitoring to maintain proper functioning after its improvements, below I mention the 7 scenarios and tests created in Seleium with Python in the order of reproduction:

1. 1_UIelements_happypath: This test was created to verify each element on the page to validate that they were displayed and also adding a positive scenario where the search criteria is valid and returned results.

2. 2_Verify_Results: In this scenario, it was verified that the results table would return information.

3. 3_Verify_ClickOnTheResults: In this scenario it was verified that clicking on an element in the table will redirect you to the results page in this case GitHub with some element to validate to know if it was the correct information. (this was done with specific data as an example)

4. 4_Verify_ResultswithEnter: In this scenario, it was verified as part of a requirement that when entering a search, the Enter functionality was also validated and functional.

5. 5_Verify_TypeOfDescription: In this scenario we are verifying the type of description that is being displayed for the two existing cases in which a description is displayed if it exists and in the other case where there is no description and only a (-) sign is displayed. (Likewise, a type of search criteria was chosen that would bring these two specific scenarios)

As two extra cases, two negative scenarios were taken into account to verify the behavior of the page:

6. 6_Verify_NoResults_SpecialCharacters: In this scenario it was verified that when entering special characters a warning will be thrown to the user to verify that this type of data will not be accepted

7. 7_Verify_NoResults_Emptyfield: In this scenario it was verified that by not entering data and only clicking the GO button, the message that the user does not exist was displayed.