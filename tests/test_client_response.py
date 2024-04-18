""" Test for the response from the server"""

from paystackease.core import PayStackResponse


def test_paystack_response():
    """Test MonnifyResponse class"""
    response = PayStackResponse(
        status_code=200,
        status=True,
        message="Success",
        data={"status": "success"},
    )
    assert response.status_code == 200
    assert response.status == True
    assert response.message == "Success"
    assert response.data == {"status": "success"}
