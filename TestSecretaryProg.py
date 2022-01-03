import pytest
from app import check_document_existence, get_doc_owner_name, remove_doc_from_shelf, append_doc_to_shelf, delete_doc
import app
import mock
import builtins

BIG_DATA = {}

existence_list = []
for doc in app.documents:
    num = doc.get('number')
    existence_list.append((num, True))
BIG_DATA['exist'] = existence_list


class TestSecretaryProg:

    @pytest.mark.parametrize('req_doc, founded_doc_bool', BIG_DATA['exist'])
    def test_check_document_existence(self, req_doc, founded_doc_bool):
        assert check_document_existence(req_doc) == founded_doc_bool

    @pytest.mark.parametrize('owner_name', ['Геннадий Покемонов'])
    def test_get_doc_owner_name(self, owner_name):
        with mock.patch.object(builtins, 'input', lambda _: '11-2'):
            assert get_doc_owner_name() == owner_name

    expected_dict = {'1': ['2207 876234', '11-2', '5455 028765'],
                     '2': ['10006'],
                     '3': ['22']
                     }

    @pytest.mark.parametrize('doc_num, shelf_num, dirs', [('22', '3', expected_dict)])
    def test_append_doc_to_shelf(self, doc_num, shelf_num, dirs):
        assert append_doc_to_shelf(doc_num, shelf_num) == dirs

    @pytest.mark.parametrize('doc_num, bool_state', [('10006', True)])
    def test_delete_doc(self, doc_num, bool_state):
        with mock.patch.object(builtins, 'input', lambda _: '10006'):
            assert delete_doc() == (doc_num, bool_state)

    @pytest.mark.parametrize('doc_num, dict_values', [('11-2', ['2207 876234', '5455 028765'])])
    def test_remove_doc_from_shelf(self, doc_num, dict_values):
        with mock.patch.object(target=app, attribute='remove_doc_from_shelf'):
            assert remove_doc_from_shelf(doc_num) == dict_values



