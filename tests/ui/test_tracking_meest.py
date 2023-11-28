# Project task 6. Module 28. UI testing

from modules.ui.page_object.tracking_meest import TrackingMeest
import pytest


@pytest.mark.meest
def test_tracking_meest():
    # Parcel for tracking
    parcel = "MYCV059863575PL"

    # Creating a page object
    tracking_meest = TrackingMeest()

    # We open the page https://ua.meest.com
    tracking_meest.go_to()

    # We track the shipment
    tracking_meest.tracking(parcel)

    # We check that the name of the page is what we expect
    assert tracking_meest.check_title(
        "Відстежити посилку ᐈ Meest Трекінг 【Україна】- Поштові & Транспортні послуги"
        )

    # Close the browser
    tracking_meest.close()
