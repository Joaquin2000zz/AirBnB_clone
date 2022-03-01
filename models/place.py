#!/usr/bin/python3
"""
Module place.py - contains the place class
"""

from models.base_model  import BaseModel

Class Place(BaseModel):
    """
    place class
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = int(0)
    number_bathrooms = int(0)
    max_guest = int(0)
    price_by_night = int(0)
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = []