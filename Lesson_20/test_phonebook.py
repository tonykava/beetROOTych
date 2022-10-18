from unittest import TestCase
import json
import phonebook

test_data = ('Contact №1:',
 'First name: Tony, Last name: Kava, Phone: 0959468920, City: Kiev, Country: '
 'Ukraine')


class TestPhonebook(TestCase):

    def test_create(self):
        phonebook.create(
            {'first_name': 'Tony', 'last_name': 'Kava', 'mobile': '0959468920', 'city': 'Kiev', 'country': 'Ukraine'})
        with open('data.json', 'r') as file:
            data = json.load(file)
        self.assertEqual(data, {'first_name__last_name': ['mobile', 'city', 'country'], 'Tony__Kava': ['0959468920', 'Kiev', 'Ukraine']})

    def test_search_first_name(self):
        self.assertEqual(phonebook.search_first_name('Tony'), test_data)

    def test_search_last_name(self):
        self.assertEqual(phonebook.search_last_name('Kava'), test_data)

    def test_full_name(self):
        self.assertEqual(phonebook.search_full_name('Tony', 'Kava'), test_data)

    def test_search_mobile(self):
        self.assertEqual(phonebook.search_mobile('0959468920'), test_data)

    def test_search_city(self):
        self.assertEqual(phonebook.search_city('Kiev'), test_data)

    def test_search_country(self):
        self.assertEqual(phonebook.search_country('Ukraine'), test_data)

    def test_update(self):
        phonebook.update('0959468920')
        self.assertEqual(phonebook.search_mobile('0959468920'), ('Contact №1:',
 f'First name: {phonebook.new_first_name}, Last name: {phonebook.new_last_name}, Phone: 0959468920,'
 f' City: {phonebook.new_city}, Country: {phonebook.new_country}'))

    def test_ydelete(self):
        phonebook.delete('0959468920')
        with open('data.json', 'r') as file:
            data = json.load(file)
        self.assertEqual(data, {'first_name__last_name': ['mobile', 'city', 'country']})









