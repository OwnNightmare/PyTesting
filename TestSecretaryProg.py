import pytest
from app import check_document_existence, get_doc_owner_name, remove_doc_from_shelf
import app
import mock
import builtins

BIG_DATA = {}

existence_list = []
for doc in app.documents:
    num = doc.get('number')
    existence_list.append((num, True))
BIG_DATA['exist'] = existence_list

# roll = []
# names = set(doc.get('name') for doc in app.documents)
# tup = tuple(frozenset(names))
# roll.append(tup)

class TestSecretaryProg:

    @pytest.mark.parametrize('req_doc, founded_doc_bool', BIG_DATA['exist'])
    def test_check_document_existence(self, req_doc, founded_doc_bool):
        assert check_document_existence(req_doc) == founded_doc_bool

    @pytest.mark.parametrize('doc_num, owner_name', [('11-2', 'Геннадий Покемонов')])
    def test_get_doc_owner_name(self, doc_num, owner_name):
        with mock.patch.object(builtins, 'input', lambda _: '11-2'):
            assert get_doc_owner_name() == owner_name

    # @pytest.mark.parametrize('users_names', roll)
    # def test_get_all_doc_owners_names(self, users_names):
    #     assert get_doc_owner_name() == users_names

    @pytest.mark.parametrize('doc_num, dict_values', [('11-2', ['2207 876234', '5455 028765'])])
    def test_remove_doc_from_shelf(self, doc_num, dict_values):
        assert remove_doc_from_shelf(doc_num) == dict_values