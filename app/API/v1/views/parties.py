from flask import jsonify, make_response, request
from app.API.v1 import v1
from app.API.v1.models.parties import Party, parties

@v1.route('/parties', methods=['GET'])
def get_parties():
  return Party.get_parties()

@v1.route('/newParty', methods=['POST'])
def new_party():
  party_data = request.get_json()
  party_id = party_data['id']
  party_name = party_data['name']
  party_address = party_data['address']
  party_image = party_data['logo']

  new_party_info = {
    "id": party_id,
    "name": party_name,
    "address": party_address,
    "logo": party_image
  }

  Party.create_party(new_party_info)
  
  return make_response(jsonify({
    "Message": "Party Info Added",
    "Status": "Ok"
  }), 201)

@v1.route('/party/<int:party_id>', methods=['GET'])
def get_party(party_id):
  for party in parties:
    if party['id'] == party_id:
      return make_response(jsonify(party))
    else:
      return None

@v1.route('/party/<int:party_id>', methods=['DELETE'])
def remove_party(party_id):
  delete_party = [party for party in parties if party['id'] == party_id]
  parties.remove(delete_party[0])
  return make_response(jsonify({
    "Meassage": "Party deleted",
    "Status": "ok"
  }), 200)
      