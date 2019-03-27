from linkedin_v2 import linkedin


CONSUMER_KEY='78tmt59ip93cmb'
CONSUMER_SECRET='CBGdVjgGGYUSwx9w'
USER_TOKEN='AQXwPhRUosVe6B33fXiXECeF2AYXGIHTLcyuUaNCO4LxP3un-XLEEAkzcrEFOoz78nvRxhydjUFGV7MMsZPr9tHAnHT92jT3ExzFX91GnsIzf-94vg3iAmyhV3bJdMZcC1YAGiHuZZXQtwqqqFliGgd8kccXxk74MGDoUQLQg3-XNgQkHkQEpPlAMoW4vzvDdUWZSgD3h_twRAkUqEVhSCyJ5ZO5NXO9JhAJhhauMRc9ywMIFKYl2d5tamtUy-kG6olRHjKRUJTfnMoTSoajjDxXvVC8_5QiYUiMw-0fUaArNQ6yOEXjN_XVGzWk-4g-jqZHHK3ZKkhk7e93f8QuS2amaSXUSQ'
USER_SECRET='5183999'
RETURN_URL = 'http://localhost:8000'

authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                                          USER_TOKEN, USER_SECRET, 
                                                          RETURN_URL, linkedin.PERMISSIONS.enums.values())

application = linkedin.LinkedInApplication(authentication)

application.get_profile()
