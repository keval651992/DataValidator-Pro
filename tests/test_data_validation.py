from clients.api_client import APIClient
from clients.db_client import DatabaseClient
from models.schemas import UserSchema
import pytest


@pytest.fixture
def api_client():
  return APIClient()


@pytest.fixture
def db_client():
  return DatabaseClient()


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_user_api_contract_and_db_state(user_id, api_client, db_client):
  #1. Fetch data from API endpoint
  raw_api_data = api_client.get_user_by_id(user_id)

  #2. Validate API response structure using Pydantic schema
  validated_user = UserSchema(**raw_api_data)
  assert validated_user.id == user_id

  #3. Fetch expected state from Database  
  db_record = db_client.get_user_record(user_id)


  #4. Compare Backend Database state against API payload
  assert validated_user.name == db_record["name"], (
      f"Name mismatch! API: {validated_user.name}, DB: {db_record['name']}"
  )
  assert validated_user.email == db_record["email"], (
      f"Email mismatch! API: {validated_user.email}, DB: {db_record['email']}"
  )
  assert validated_user.username == db_record["username"]