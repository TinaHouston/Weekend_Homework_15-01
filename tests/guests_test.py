import unittest

from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Sara", 20, "Genie in a Bottle")
        # self.guest_2 = Guest("Harriet", 100.00, "One Love")
        # self.guest_3 = Guest("Emily", 50.00, "What Makes You Beautiful")
        # self.guest = [self.guest_1, self.guest_2, self.guest_3]


    def test_guest_has_name(self):
        self.assertEqual("Sara", self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(20, self.guest.cash)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Genie in a Bottle", self.guest.fav_song)


    # EXTENSION
    
    def test_enough_money_for_entry(self):
        self.assertEqual(True, self.guest.entry_fee(self.guest))

    def test_play_fav_song_return_string(self):
        self.assertEqual("Woohoo!", self.guest.playback(self.guest.fav_song))

    
    # FURTHER EXTENSION

    def test_guest_pays_entry_fee(self):
        self.assertEqual(10, self.guest.pay_entry_fee(self.guest))

        