from app import create_app


def test_chat_empty_question():

    app = create_app()

    client = app.test_client()

    response = client.post(
        "/api/chat",
        json={
            "question": ""
        }
    )

    assert response.status_code == 400
