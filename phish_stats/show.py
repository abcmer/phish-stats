"""Phish Stats"""
from bs4 import BeautifulSoup

from phish_stats.phishnet_api import get_show_data


class Show():
    """Show class"""

    def __init__(self, date, data={}):
        self.date = date
        self.year = int(date.split('-')[0])
        self.month = int(date.split('-')[1])
        self.day = int(date.split('-')[2])
        self.relative_date = None
        self.data = data
        self.setlist = []
        self.total_song_count = None
        self.set1_song_count = None
        self.set2_song_count = None
        self.set3_song_count = None
        self.encore_song_count = None
        self.encore2_song_count = None
        self.country = None
        self.state = None
        self.city = None
        self.rating = None
        self.venue = None
        self.era = None
        self.song_booleans = {
            'you-enjoy-myself': 0,
            'tweezer': 0,
        }
        if data:
            self.set_attributes()

    def __repr__(self):
        """Representation of a show."""
        return self.date

    def fetch_phishnet_data(self, api_key):
        """Gets and sets phish.net api data for show."""
        if not self.data:
            self.data = get_show_data(self.date, api_key)

    def set_attributes(self):
        """Set attributes of Show"""
        if self.data.get('response', {}).get('data'):
            # Set attributes based on data
            self.parse_setlist()
            self.set_total_song_count()
            self.set_set1_song_count()
            self.set_set2_song_count()
            self.set_set3_song_count()
            self.set_encore_song_count()
            self.set_encore2_song_count()
            self.set_show_rating()
            self.set_relative_date()
            self.set_venue()
            self.set_show_location()
            self.set_song_booleans()
            self.set_era()

    def parse_setlist(self):
        """Parses setlist from raw setlist data"""
        setlist = []
        soup = BeautifulSoup(self.data["response"]["data"][0]['setlistdata'],
                             features="html.parser")

        for p_tag in soup.find_all("p"):

            setlist_tags = p_tag.contents
            for tag in setlist_tags:
                # handle Navigable Strings
                if str(type(tag)) == "<class 'bs4.element.NavigableString'>":
                    # string. Need to add special handling
                    continue

                if tag.name == "br":
                    continue

                # handle setlist notes
                elif tag.name == "sup":
                    element = {
                        "note_id": int(tag.contents[0][1:2]),
                        "element_type": "note",
                        "body": tag["title"],
                    }

                    setlist[-1]["notes"].append(element)

                elif tag["class"] == ["setlist-song"]:
                    phishnet_url = tag["href"]
                    element = {
                        "song_id": phishnet_url.split("/")[-1],
                        "element_type": "song",
                        "song_url": phishnet_url,
                        "set_label": tag.parent.span.contents[0],
                        "notes": [],
                    }

                    setlist.append(element)

        self.setlist = setlist

    def set_total_song_count(self):
        """Get total song count for the setlist."""
        self.total_song_count = len(self.setlist)

    def set_set1_song_count(self):
        """Get set 1 song count for the setlist."""
        self.set1_song_count = len(
            [song for song in self.setlist if song["set_label"] == "Set 1"])

    def set_set2_song_count(self):
        """Get set 2 song count for the setlist."""
        self.set2_song_count = len(
            [song for song in self.setlist if song["set_label"] == "Set 2"])

    def set_set3_song_count(self):
        """Get set 3 song count for the setlist."""
        self.set3_song_count = len(
            [song for song in self.setlist if song["set_label"] == "Set 3"])

    def set_encore_song_count(self):
        """Get encore song count for the setlist."""
        self.encore_song_count = len(
            [song for song in self.setlist if song["set_label"] == "Encore"])

    def set_encore2_song_count(self):
        """Get encore 2 song count for the setlist."""
        self.encore2_song_count = len(
            [song for song in self.setlist if song["set_label"] == "Encore 2"])

    def set_show_rating(self):
        """Parse show_data_json for rating."""
        self.rating = float(self.data["response"]["data"][0]["rating"])

    def set_relative_date(self):
        """Parse relative show date."""
        self.relative_date = self.data["response"]["data"][0][
            "relative_date"]

    def set_venue(self):
        """Parse venue and venueid."""
        self.venue = self.data["response"]["data"][0]["venue"]

    def set_show_location(self):
        """Set show location."""
        show_location = self.data['response']['data'][0]['location']
        self.country = show_location.split(",")[2].strip()
        self.state = show_location.split(",")[1].strip()
        self.city = show_location.split(",")[0].strip()

    def set_song_booleans(self):
        """Sets song booleans to 1 if hit songs were played."""
        setlist_song_ids = [song['song_id'] for song in self.setlist]
        for song_id in self.song_booleans:
            self.song_booleans[song_id] = 1 if song_id in setlist_song_ids else 0
    
    def set_era(self):
        """Sets era equal to 1.0, 2.0, 3.0 based on date"""
        if not self.year:
            self.era = ''
        elif self.year <= 2000:
            self.era = '1.0'
        elif self.year <= 2004:
            self.era = '2.0'
        else:
            self.era = '3.0'
